from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

import logging

logger = logging.getLogger(__name__)


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email',)

    def send_email(self):
        logger.info(
            "Sending signup email for email=%s",
            self.cleaned_data['email'],
        )
        message = "Welcome{}".format(self.cleaned_data['email'])
        send_mail(
            "Welcome to Brown Group of Schools",
            message,
            "admin@browngroupofschools.com",
            [self.cleaned_data['email']],
            fail_silently=True,
        )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
