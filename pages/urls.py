from django.urls import path

from .views import (
    HomePageView, HomeOnlineView,
    AboutPageView, ContactPageView,
    FaqsPageView, PortfolioPageView,
    MembershipPageView,
)

urlpatterns = [
    path('home_online/', HomeOnlineView.as_view(), name='home_online'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('faqs/', FaqsPageView.as_view(), name='faqs'),
    path('portfolio/', PortfolioPageView.as_view(), name='portfolio'),
    path('membership/', MembershipPageView.as_view(), name='membership'),
    path('', HomePageView.as_view(), name='home'),
]
