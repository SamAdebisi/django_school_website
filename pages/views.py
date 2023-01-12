from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(TemplateView):
    template_name = 'home.html'


class HomeOnlineView(TemplateView):
    template_name = 'home_online.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'


class FaqsPageView(TemplateView):
    template_name = 'faq_list.html'


class PortfolioPageView(TemplateView):
    template_name = 'portfolio.html'


class MembershipPageView(LoginRequiredMixin, TemplateView):
    template_name = 'membership.html'
    login_url = 'account_login'
