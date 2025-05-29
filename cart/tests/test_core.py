from django.test import TestCase
from django.urls import reverse
from cart.core import Cart
from catalog.models import Category, Product

class CartCoreTests(TestCase):
    test_counter = 0 

    def setUp(self):
        self.cat = Category.objects.create(name='Dummy', slug='dummy') 
        self.p = Product.objects.create(
            category=self.cat,
            name='X',
            slug='x',
            price=10,
            stock=5
        )
        self.cart = Cart({})
    
    def tearDown(self):
        CartCoreTests.test_counter += 1
        print(f"Prueba {CartCoreTests.test_counter} ejecutada exitosamente")

    def test_add_to_cart(self):
        url = reverse('cart:cart_add', args=[self.p.id])
        response = self.client.post(url, {'quantity': 2}, follow=True)
        self.assertContains(response, 'Tu carrito')

    def test_remove_from_cart(self):
        self.client.post(reverse('cart:cart_add', args=[self.p.id]), {'quantity': 1})
        response = self.client.post(reverse('cart:cart_remove', args=[self.p.id]), follow=True)
        self.assertNotContains(response, 'X')
