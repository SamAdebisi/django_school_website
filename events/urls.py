from django.urls import path
from .views import (
    EventListView, EventDetailView,
    EventCreateView, EventUpdateView, EventDeleteView
)

urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),
    path('<uuid:pk>', EventDetailView.as_view(), name='event_detail'),
    path('event_create/', EventCreateView.as_view(), name='event_create'),
    path('event_delete/', EventDeleteView.as_view(), name='event_delete'),
    path('event_update/', EventUpdateView.as_view(), name='event_update'),
]
