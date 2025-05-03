# cart/views.py

from django.shortcuts import render, redirect, get_object_or_404
from catalog.models import Product

CART_SESSION_ID = 'cart'

def cart_add(request, product_id):
    # Obtiene o inicializa el carrito en sesión
    cart = request.session.get(CART_SESSION_ID, {})
    cantidad = int(request.POST.get('cantidad', 1))
    # Suma la cantidad si ya existía el producto
    cart[str(product_id)] = cart.get(str(product_id), 0) + cantidad
    request.session[CART_SESSION_ID] = cart
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = request.session.get(CART_SESSION_ID, {})
    items = []
    total = 0
    for pid, qty in cart.items():
        product = get_object_or_404(Product, pk=pid)
        subtotal = product.price * qty
        items.append({
            'product': product,
            'quantity': qty,
            'subtotal': subtotal,
        })
        total += subtotal
    return render(request, 'cart/cart_detail.html', {
        'cart_items': items,
        'total': total,
    })

def cart_remove(request, product_id):
    cart = request.session.get(CART_SESSION_ID, {})
    # Elimina el producto del carrito si existe
    cart.pop(str(product_id), None)
    request.session[CART_SESSION_ID] = cart
    return redirect('cart:cart_detail')

def cart_decrement(request, product_id):
    """Resta 1 unidad del producto; si llega a 0, lo elimina."""
    cart = request.session.get(CART_SESSION_ID, {})
    if str(product_id) in cart:
        cart[str(product_id)] -= 1
        if cart[str(product_id)] < 1:
            del cart[str(product_id)]
        request.session[CART_SESSION_ID] = cart
    return redirect('cart:cart_detail')
