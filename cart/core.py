# cart/core.py

from django.conf import settings
from catalog.models import Product

CART_SESSION_ID = getattr(settings, 'CART_SESSION_ID', 'cart')

class Cart:
    def __init__(self, request_or_session):
        # if they passed a request, grab .session; if they passed a dict, use it
        if hasattr(request_or_session, 'session'):
            self.session = request_or_session.session
        else:
            self.session = request_or_session

        cart = self.session.get(CART_SESSION_ID)
        if cart is None:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, qty=1):
        pid = str(product.id)
        self.cart[pid] = self.cart.get(pid, 0) + qty
        self.session.modified = True

    def remove(self, product):
        pid = str(product.id)
        if pid in self.cart:
            del self.cart[pid]
            self.session.modified = True
