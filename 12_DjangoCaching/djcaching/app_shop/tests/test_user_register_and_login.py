from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class UserTestTemplates(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_user(self):
        data = {
            'username': 'TestUser', 'password': '112233gjk'
        }
        User.objects.create_user(**data)
        url = reverse('login')
        response = self.client.post(url, data, follow=True)
        self.assertTrue(response.context['user'].is_active)

    def test_register_user(self):
        data = {
            'username': 'TestUser',
            'phone': 123,
            'password1': '112233gjk',
            'password2': '112233gjk',
        }
        url = reverse('register')
        self.client.post(url, data)
        try:
            user = User.objects.get(username=data['username'])
        except Exception:
            user = None
        self.assertIsInstance(user, User)
