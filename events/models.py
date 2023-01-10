import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Event(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    title = models.CharField(max_length=255)
    body = models.TextField()
    location = models.CharField(max_length=150)
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    author = models.ForeignKey(
        get_user_model(),
        related_name="Announcer",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event_detail', args=[str(self.id)])
