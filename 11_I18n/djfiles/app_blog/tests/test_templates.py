from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse, NoReverseMatch
from ..models import Post


class PostTestTemplates(TestCase):
    def setUp(self):
        self.client = Client()
        self.post = Post.objects.create(title='test post',
                                        description='test text...')
        self.user = User.objects.create_user(username='TestUser')
        self.auth_client = Client()
        self.auth_client.force_login(self.user)

    def test_urls__uses_correct_template_edit_profile(self):
        templates_url_names = {
            'djfiles/posts_list.html': 'main',
            'djfiles/post_single_page.html': 'post',
            'djfiles/post_creation_page.html': 'post_creation',
            'djfiles/upload_posts_file.html': 'upload',
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
