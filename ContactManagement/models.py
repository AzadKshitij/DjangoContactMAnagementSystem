from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Contact(models.Model):
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=200, default=None)
    number = models.IntegerField()
    dateAdded = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'pk': self.pk})
