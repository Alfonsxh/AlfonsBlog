from django.urls import reverse, resolve
from django.test import TestCase
from .views import signup


class SignupTest(TestCase):
    def test_singup_status_code(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def signup_url_resovles_signup_view(self):
        view = resolve('/signup/')
        self.assertEqual(view.func, signup)
