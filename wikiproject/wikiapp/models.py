from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone


class PostModel(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=9999999)
    image = models.ImageField(null=True, blank=True, upload_to='media')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    userTableForeignKey = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class RelatedModel(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=300)
    image = models.ImageField(null=True, blank=True, upload_to='media')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
