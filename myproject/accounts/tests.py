from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, resolve
from django.test import TestCase
from .views import signup


class SignupTest(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_singup_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def signup_url_resovles_signup_view(self):
        view = resolve('/signup/')
        self.assertEqual(view.func, signup)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, UserCreationForm)