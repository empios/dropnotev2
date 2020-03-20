from django.test import TestCase

from .models import Post
from .views import post_new
from django.contrib.auth.models import User
from django.test.client import Client
from .forms import *


class SetupClass(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('foo', 'myemail@test.com', 'bar123!!!')


class RegisterFormTest(TestCase):

    # Valid Form Data
    def test_RegisterForm_valid(self):
        form = RegisterForm(data=dict(username="foo", email="myemail@test.com", password1="bar123!!!",
                                      password2="bar123!!!"))
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_RegisterForm_invalid(self):
        form = RegisterForm(data={'username': "", 'email': "", 'password1': "", 'password2': ""})
        self.assertFalse(form.is_valid())


class PostFormTest(TestCase):

    # Valid Form Data
    def test_PostForm_valid(self):
        form = PostForm(data={'title': "title", 'text': "text"})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_PostForm_invalid(self):
        form = PostForm(data={'title': "", 'text': ""})
        self.assertFalse(form.is_valid())


class UserViewsTest(SetupClass):

    def test_home_view(self):
        user_login = self.client.login(username="foo", password="bar123!!!")
        self.assertTrue(user_login)
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)