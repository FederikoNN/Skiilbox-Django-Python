from http import HTTPStatus
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Post


class PostTestUrls(TestCase):
    def setUp(self):
        self.client = Client()
        self.post = Post.objects.create(title='test post',
                                        description='test text...')
        self.user = User.objects.create_user(username='TestUser')
        self.auth_client = Client()
        self.auth_client.force_login(self.user)

    def test_is_ok_page_main(self):
        url = reverse('main')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_is_ok_page_single_post(self):
        url = reverse('post', kwargs={'pk': self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_is_ok_page_new_post_create_for_authenticated_user(self):
        url = reverse('post_creation')
        response = self.auth_client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_is_ok_page_new_post_create_for_anonymous_user(self):
        url = reverse('post_creation')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_post_creation_redirect_for_anonymous_user_on_login(self):
        url = reverse('post_creation')
        response = self.client.get(url, follow=True)
        self.assertRedirects(response, (f'/login/?next=/post_creation_page/'))

    def test_is_ok_page_post_single_page(self):
        url = reverse('post', kwargs={'pk': self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_is_ok_page_upload_posts_file_for_authenticated_user(self):
        url = reverse('upload')
        response = self.auth_client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_is_ok_page_upload_posts_file_for_anonymous_user(self):
        url = reverse('upload')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_upload_posts_file_redirect_for_anonymous_user_on_login(self):
        url = reverse('upload')
        response = self.client.get(url, follow=True)
        self.assertRedirects(response, (f'/login/?next=/upload_posts_file/'))

