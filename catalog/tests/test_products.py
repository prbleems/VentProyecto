from django.test import TestCase
from django.urls import reverse
from catalog.models import Product

class CoreTests(TestCase):
    def test_something(self):
        self.assertTrue(True)
        print("CoreTests.test_something: Prueba ejecutada exitosamente")

class ProductTests(TestCase):
    def test_product_list(self):
        response = self.client.get(reverse('catalog:product_list'))
        self.assertEqual(response.status_code, 200)
        print("ProductTests.test_product_list: Lista de productos cargada correctamente")

    def test_product_detail_404(self):
        response = self.client.get(reverse('catalog:product_detail', args=[999]))
        self.assertEqual(response.status_code, 404)
        print("ProductTests.test_product_detail_404: Producto no encontrado correctamente (404)")
