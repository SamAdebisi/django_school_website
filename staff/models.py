from django.db import models
from django.contrib.auth import get_user_model


class Staff(get_user_model()):

    subject = models.CharField(max_length=150, null=True, blank=True)
    admin_role = models.CharField(max_length=150, null=True, blank=True)
    date_joined_sch = models.DateField()
    is_staff = True

    class Meta:
        verbose_name = 'tutor'
        verbose_name_plural = 'tutors'

    def __str__(self):
        return f"{self.subject} Tutor"
