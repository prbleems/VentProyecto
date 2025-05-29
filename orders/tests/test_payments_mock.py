import requests
from django.test import SimpleTestCase

class PaymentMockTests(SimpleTestCase):
    def setUp(self):
        self.url_ok       = 'https://run.mocky.io/v3/76d146ab-2638-4a81-94ee-5bda203342a6'
        self.url_declined = 'https://run.mocky.io/v3/4fdbf2e3-0b50-4123-b539-4e5a9252fb66'
        self.url_down     = 'https://run.mocky.io/v3/b8d1855e-7b81-45c2-841e-2433e44ce515'

    def test_payment_authorized(self):
        resp = requests.get(self.url_ok)
        self.assertEqual(resp.status_code, 200, "El status code no es 200 en pago autorizado")
        data = resp.json()
        print("Respuesta JSON test_payment_authorized:", data)
        self.assertEqual(data['status'], 'AUTHORIZED', "El estado no es AUTHORIZED")
        print("test_payment_authorized: Pago autorizado correctamente")

    def test_payment_declined(self):
        resp = requests.get(self.url_declined)
        self.assertEqual(resp.status_code, 200, "El status code no es 200 en pago rechazado")
        data = resp.json()
        print("Respuesta JSON test_payment_declined:", data)
        self.assertEqual(data['status'], 'DECLINED', "El estado no es DECLINED")
        print("test_payment_declined: Pago rechazado correctamente")

    def test_payment_service_unavailable(self):
        resp = requests.get(self.url_down)
        self.assertEqual(resp.status_code, 503, "El status code no es 503 en servicio no disponible")
        print(f"Respuesta status code test_payment_service_unavailable: {resp.status_code}")
        print("test_payment_service_unavailable: Servicio no disponible correctamente detectado (503)")
