from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class HomeOnlineView(TemplateView):
    template_name = 'home_online.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'
