from django.urls import path

from .views import (
    HomePageView, HomeOnlineView, AboutPageView, ContactPageView
)

urlpatterns = [
    path('home_online/', HomeOnlineView.as_view(), name='home_online'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('', HomePageView.as_view(), name='home'),
]
