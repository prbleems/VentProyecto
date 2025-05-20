import requests
from django.test import SimpleTestCase

class PaymentMockTests(SimpleTestCase):
    def setUp(self):
        #  mocky.io
        self.url_ok      = 'https://run.mocky.io/v3/76d146ab-2638-4a81-94ee-5bda203342a6'
        self.url_declined= 'https://run.mocky.io/v3/4fdbf2e3-0b50-4123-b539-4e5a9252fb66'
        self.url_down    = 'https://run.mocky.io/v3/b8d1855e-7b81-45c2-841e-2433e44ce515'

    def test_payment_authorized(self):
        resp = requests.get(self.url_ok)
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data['status'], 'AUTHORIZED')

    def test_payment_declined(self):
        resp = requests.get(self.url_declined)
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data['status'], 'DECLINED')

    def test_payment_service_unavailable(self):
        resp = requests.get(self.url_down)
        self.assertEqual(resp.status_code, 503)
