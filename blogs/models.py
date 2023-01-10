import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Blog(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    title = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])


class Comment(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    comment = models.CharField(max_length=200)
    author = models.ManyToManyField(
        get_user_model(),
    )
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('comment_detail', args=[str(self.id)])
