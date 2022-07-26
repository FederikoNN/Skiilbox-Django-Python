from http import HTTPStatus
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class UserTestCaseUrls(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='TestUser')
        self.auth_client = Client()
        self.auth_client.force_login(self.user)

    def test_is_ok_page_login(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_is_ok_page_logout(self):
        url = reverse('logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_is_ok_page_main(self):
        url = reverse('main')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_is_ok_page_register(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_is_ok_page_edit_profile_for_authenticated_user(self):
        url = reverse('my_account', kwargs={'pk': self.user.id})
        response = self.auth_client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_edit_profile_redirect_for_anonymous_user(self):
        url = reverse('my_account', kwargs={'pk': self.user.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_edit_profile_redirect_for_anonymous_user_on_login(self):
        url = reverse('my_account', kwargs={'pk': self.user.id})
        response = self.client.get(url)
        self.assertRedirects(response,
                             (f'/login/?next=/{self.user.id}/my_account/'))
