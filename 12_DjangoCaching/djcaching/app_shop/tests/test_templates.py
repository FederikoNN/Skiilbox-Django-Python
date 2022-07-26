from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse, NoReverseMatch


class UserTestTemplates(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='TestUser')
        self.auth_client = Client()
        self.auth_client.force_login(self.user)

    def test_urls__uses_correct_template_edit_profile(self):
        templates_url_names = {
            'shop/shop_list.html': 'main',
            'users/login.html': 'login',
            'users/logout.html': 'logout',
            'users/register.html': 'register',
            'users/my_account.html': 'my_account',
        }
        for template, address in templates_url_names.items():
            with self.subTest(address=address):
                try:
                    url = reverse(address)
                except NoReverseMatch:
                    self.auth_client.force_login(self.user)
                    url = reverse(address, kwargs={'pk': self.user.id})
                response = self.auth_client.get(url)
                self.assertTemplateUsed(response, template)
