from django.views.generic import (
    ListView, DetailView,
    CreateView, DeleteView, UpdateView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionDenied

from .models import Event


class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'event_list'


class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'events/event_detail.html'


class EventCreateView(CreateView):
    model = Event
    template_name = 'events/event_create.html'
    fields = ('title', 'body', 'location', 'date',
              'time_start', 'date_end')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events/event_delete.html'
    success_url = reverse_lazy('events/event_list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class EventUpdateView(UpdateView):
    model = Event
    fields = ('title', 'body', 'location', 'date',
              'time_start', 'time_end')
    template_name = 'events/event_update.html'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return self.dispatch(request, *args, **kwargs)
