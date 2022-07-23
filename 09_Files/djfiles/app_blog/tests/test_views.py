from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Post, Gallery
from django.core.files.uploadedfile import SimpleUploadedFile

NUMBER_OF_POSTS = 12


class TestPostsView(TestCase):
    @classmethod
    def setUpTestData(cls):
        for post_index in range(NUMBER_OF_POSTS):
            Post.objects.create(
                title=f'Post # {post_index}',
                description=f'Test text {post_index}'
            )

    def test_posts_number_posts_view(self):
        response = self.client.get(reverse('main'))
        self.assertTrue(len(response.context['posts_list']) == NUMBER_OF_POSTS)


class TestCreatePostView(TestCase):
    @classmethod
    def setUpTestData(cls):
        for post_index in range(NUMBER_OF_POSTS):
            Post.objects.create(
                title=f'Post # 1',
                description=f'Test text 1'
            )

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='TestUser')
        self.auth_client = Client()
        self.auth_client.force_login(self.user)

    def test_create_post(self):
        posts_count = Post.objects.count()
        image_count = Gallery.objects.count()
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x02\x00'
            b'\x01\x00\x80\x00\x00\x00\x00\x00'
            b'\xFF\xFF\xFF\x21\xF9\x04\x00\x00'
            b'\x00\x00\x00\x2C\x00\x00\x00\x00'
            b'\x02\x00\x01\x00\x00\x02\x02\x0C'
            b'\x0A\x00\x3B'
        )
        uploaded = SimpleUploadedFile(
            name='small.gif',
            content=small_gif,
            content_type='image/gif'
        )
        data = {
            'title': 'Test title',
            'description': 'Test text...',
            'images': uploaded,
        }
        url = reverse('post_creation')
        response = self.auth_client.post(url, data=data, follow=True)
        self.assertEqual(Post.objects.count(), posts_count + 1)
        self.assertEqual(Gallery.objects.count(), image_count + 1)
        self.assertRedirects(response, reverse('main'))
