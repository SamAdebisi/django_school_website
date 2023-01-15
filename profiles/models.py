import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Profile(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    tutor = models.OneToOneField(
        get_user_model(),
        related_name="Profile",
        on_delete=models.CASCADE,
    )
    email = models.EmailField(max_length=220)
    facebook_link = models.CharField(max_length=220)
    twitter_link = models.CharField(max_length=220)
    linkedin_link = models.CharField(max_length=220)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)

    class Meta:
        permissions = [
            ('profile_status', "Can edit the profile"),
        ]

    def __str__(self):
        return self.tutor.objects.all().first_name

    def get_absolute_url(self):
        return reverse('profile_detail', args=[str(self.id)])
