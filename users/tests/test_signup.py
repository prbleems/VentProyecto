from django.test import TestCase
from django.urls import reverse
from users.models import User

class CoreTests(TestCase):
    def test_something(self):
        self.assertTrue(True)
        print("CoreTests.test_something: Prueba ejecutada exitosamente")

class SignUpTests(TestCase):
    def test_signup_page_status_code(self):
        url = reverse('users:signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        print("SignUpTests.test_signup_page_status_code: Página carga correctamente")

    def test_signup_creates_user(self):
        url = reverse('users:signup')
        data = {'username': 'testuser', 'email': 'a@b.com', 'password': 'pass1234'}
        response = self.client.post(url, data, follow=True)
        self.assertTrue(User.objects.filter(username='testuser').exists())
        print("SignUpTests.test_signup_creates_user: Usuario creado exitosamente")
