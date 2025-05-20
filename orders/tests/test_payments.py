from django.test import TestCase, override_settings
from django.urls import reverse

class CoreTests(TestCase):
    def test_something(self):
        self.assertTrue(True)


class PaymentTests(TestCase):
    @override_settings(TRANSBANK_COMMERCE_CODE=None)
    def test_payment_endpoint_unavailable(self):
        url = reverse('orders:payment')  # ajusta según tu URL
        response = self.client.post(url, {'order_id':123})
        self.assertEqual(response.status_code, 503)  # suponiendo que devuelves 503
