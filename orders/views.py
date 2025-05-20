import uuid
from django.shortcuts      import render, redirect, get_object_or_404
from django.http          import HttpResponse
from django.views.decorators.http import require_http_methods
from django.conf           import settings
from transbank.webpay.webpay_plus.transaction import Transaction
from cart.views            import CART_SESSION_ID
from catalog.models        import Product
from .models               import Order, OrderItem

def order_checkout(request):
    if request.method == 'GET':
        return HttpResponse(status=503)

    cart = request.session.get(CART_SESSION_ID, {})
    if not cart:
        return redirect('catalog:product_list')

    amount = sum(
        int(Product.objects.get(pk=pid).price) * qty
        for pid, qty in cart.items()
    )

    # Genera buy_order de máximo 26 caracteres
    tmp = uuid.uuid4().hex  # 32 hex chars
    buy_order = tmp[:26]
    session_id = str(request.user.id or 'anon')

    # Crea la sesión de pago
    tx = Transaction()
    response = tx.create(
        buy_order=buy_order,
        session_id=session_id,
        amount=amount,
        return_url=request.build_absolute_uri('/orders/finish/')
    )

    # Guarda en sesión
    request.session['tbk_order']       = buy_order
    request.session['tbk_cart_amount'] = amount

    # Redirige a Webpay
    url   = response['url']
    token = response.get('token_ws') or response.get('token')
    return redirect(f"{url}?token_ws={token}")


def order_finish(request):
    token = request.GET.get('token_ws')
    if not token:
        return redirect('catalog:product_list')

    # Confirma la transacción
    tx     = Transaction()
    result = tx.commit(token)

    # Si no fue autorizada
    if result.get('status') != 'AUTHORIZED':
        return render(request, 'orders/order_failed.html', {'result': result})

    # Persiste el pedido en la DB
    buy_order = request.session.pop('tbk_order')
    amount    = request.session.pop('tbk_cart_amount')
    cart      = request.session.pop(CART_SESSION_ID, {})

    order = Order.objects.create(
        user=request.user,
        total=amount / 100,
        paid=True
    )
    for pid, qty in cart.items():
        prod = get_object_or_404(Product, pk=pid)
        OrderItem.objects.create(
            order=order,
            product=prod,
            price=prod.price,
            quantity=qty
        )

    return render(request, 'orders/order_success.html', {
        'order': order,
        'tbk':   result
    })

def payment(request):
    """
    Punto de entrada para probar la indisponibilidad del endpoint de pago.
    Siempre devuelve 503, sin importar el método.
    """
    return HttpResponse(status=503)