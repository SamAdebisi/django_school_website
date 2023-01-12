import email

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve


class CustomUserTests(TestCase):

    def test_create_user(self):
        user = get_user_model().objects.create_user(
            email='testuser@email.com',
            password='testPass1234',
        )
        self.assertEqual(user.email, 'testuser@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            email='testsuperuser@email.com',
            password='testPass1234',
        )
        self.assertEqual(user.email, 'testsuperuser@email.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class SignupPageTests(TestCase):

    email = 'newuser@email.com'
    date_of_birth = '1990-01-01'
    address = 'Home'
    bio_info = 'Software Developer'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_page(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'signup.html')
        self.assertContains(self.response, "Address")
        self.assertNotContains(self.response, "Hi there! I should not be found in there.")

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.email, self.date_of_birth,
            self.address, self.bio_info,
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].email,
                         self.email)
        self.assertEqual(get_user_model().objects.all()[0].date_of_birth,
                         self.date_of_birth)
        self.assertEqual(get_user_model().objects.all()[0].address,
                         self.address)
        self.assertEqual(get_user_model().objects.all()[0].bio_info,
                         self.bio_info)
