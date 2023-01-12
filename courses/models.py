import uuid

from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Course(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(max_length=200, verbose_name='Course')
    description = models.CharField(max_length=255)
    details = models.TextField()
    curriculum = models.TextField()
    track = models.CharField(max_length=220)
    cross_price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(max_digits=6, decimal_places=0)
    cover = models.ImageField(upload_to='covers/', blank=True)

    class Meta:
        permissions = [
            ('special_status', 'Can do all course CRUD'),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('course_list', kwargs={'pk': str(self.pk)})


class Instructor(models.Model):
    tutor = models.ManyToManyField(
        get_user_model(),
        verbose_name='Tutor',
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE,
        related_name='Instructor',
    )
    role = models.CharField(max_length=120)
    body = models.CharField(max_length=255)

    class Meta:
        permissions = [
            ('tutor_status', 'Can do all instructor CRUD'),
        ]

    def __str__(self):
        return self.tutor

    def get_absolute_url(self):
        return reverse('course_detail', args=[str(self.id)])
