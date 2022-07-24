from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Profile
# from django.core.files.uploadedfile import SimpleUploadedFile


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
        self.assertEqual(Profile.objects.count(), 1)
        self.assertIsInstance(user, User)


class UserTestEditProfileView(TestCase):
    @classmethod
    def setUpTestData(cls):
        data = {
            'username': 'TestUser',
            'first_name': 'TestFirst',
            'last_name': 'TestLast',
            'password': '112233gjk',
        }
        user = User.objects.create(**data)
        Profile.objects.create(phone=123, city='Paris',
                               about_user='All about me...', user=user)

    def setUp(self):
        self.user = User.objects.get(username='TestUser')
        self.auth_client = Client()
        self.auth_client.force_login(self.user)

    def test_edit_profile_user(self):
        data_new = {
            'first_name': 'TestFirst New',
            'last_name': 'TestLast New',
            'about_user': 'One more about me...',
        }
        url = reverse('edit_profile', kwargs={'pk': self.user.id})
        self.auth_client.post(url, data=data_new, follow=True)
        self.assertTrue(User.objects.filter(first_name=data_new['first_name'],
                                            last_name=data_new[
                                                'last_name']).exists())
        self.assertTrue(
            Profile.objects.filter(about_user=data_new['about_user']).exists())
