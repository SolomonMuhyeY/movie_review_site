from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/image/', null=True, blank=True)
    hobby = models.CharField(max_length=200, null=True, blank=True)
    genre = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.user.username
