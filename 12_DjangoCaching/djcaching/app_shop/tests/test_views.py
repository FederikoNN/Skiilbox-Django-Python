from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from django.apps import apps


class UserTestSignUpView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_user_signup(self):
        data = {
            'username': 'TestUser',
            'first_name': 'TestFirst',
            'last_name': 'TestLast',
            'phone': 123,
            'city': 'Paris',
            'about_user': 'All about me...',
            'password1': '112233gjk',
            'password2': '112233gjk',
        }
        url = reverse('register')
        self.client.post(url, data)
        try:
            user = User.objects.get(username=data['username'])
        except Exception:
            user = None
        balance = apps.get_model('app_shop', 'Balance')
        self.assertEqual(balance.objects.count(), 1)
        self.assertIsInstance(user, User)
