from django.test import TestCase
from django.urls import reverse
from catalog.models import Category, Product

class PaymentTests(TestCase):
    def setUp(self):
        self.cat = Category.objects.create(name='Dummy', slug='dummy')
        self.prod = Product.objects.create(category=self.cat, name='Prod1', slug='prod1', price=1000)

    def test_checkout_redirects_to_webpay(self):
        session = self.client.session
        session['cart'] = {str(self.prod.id): 2}
        session.save()
        response = self.client.post(reverse('orders:order_checkout'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('token_ws=', response.url)
        print("PaymentTests.test_checkout_redirects_to_webpay: Redirección a Webpay exitosa")

    def test_finish_without_token(self):
        response = self.client.get(reverse('orders:order_finish'))
        self.assertEqual(response.status_code, 302)
        print("PaymentTests.test_finish_without_token: Redirección por falta de token_ws correcta")
