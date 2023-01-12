from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import (
    HomePageView, HomeOnlineView, AboutPageView, ContactPageView,
    FaqsPageView, PortfolioPageView, MembershipPageView,
)


class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'home.html')
        self.assertContains(self.response, "Brown")
        self.assertNotContains(self.response, "Hi there! I should not be found there!")

    def test_homepage_url_resolves(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


class HomeOnlineTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home_online')
        self.response = self.client.get(url)

    def test_home_online(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'home_online.html')
        self.assertContains(self.response, 'Online')
        self.assertNotContains(self.response, 'Hi there! I should not be found in there!')

    def test_home_online_view(self):
        view = resolve('/home_online/')
        self.assertEqual(
            view.func.__name__,
            HomeOnlineView.as_view().__name__
        )


class AboutPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_about_page(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'about.html')
        self.assertContains(self.response, "About")
        self.assertNotContains(self.response, "Hi there! I should not be found in there!")

    def test_about_page_view(self):
        view = resolve('/about/')
        self.assertEqual(view.func.__name__,
                         AboutPageView.as_view().__name__)


class ContactPageViewTests(SimpleTestCase):

    def setUp(self):
        url = reverse('contact')
        self.response = self.client.get(url)

    def test_contact_page(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'contact.html')
        self.assertContains(self.response, "Contact")
        self.assertNotContains(self.response, "Hi there! I should not be found in there.")

    def test_contact_page_view(self):
        view = resolve('/contact/')
        self.assertEqual(
            view.func.__name__, ContactPageView.as_view().__name__
        )


class FaqsPageViewTests(SimpleTestCase):

    def setUp(self):
        url = reverse('faqs')
        self.response = self.client.get(url)

    def test_faqs_page(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'faq_list.html')
        self.assertContains(self.response, "FAQ's")
        self.assertNotContains(self.response, "Hi there! I should not be found in there.")

    def test_faqs_page_view(self):
        view = resolve('/faqs/')
        self.assertEqual(
            view.func.__name__, FaqsPageView.as_view().__name__
        )


class PortfolioPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('portfolio')
        self.response = self.client.get(url)

    def test_portfolio_page(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'portfolio.html')
        self.assertContains(self.response, "Portfolio")
        self.assertNotContains(self.response, "Hi there! I should not be found in there.")

    def test_portfolio_page_view(self):
        view = resolve('/portfolio/')
        self.assertEqual(
            view.func.__name__, PortfolioPageView.as_view().__name__
        )


class MembershipPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('membership')
        self.response = self.client.get(url)

    def test_membership_page(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "membership.html")
        self.assertContains(self.response, "Membership")
        self.assertNotContains(self.response, "Hi there! I should not be found in there.")

    def test_membership_page_view(self):
        view = resolve('/membership/')
        self.assertEqual(
            view.func.__name__, MembershipPageView.as_view().__name__
        )
