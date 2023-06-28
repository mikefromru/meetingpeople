from django.db import models
from django.contrib.auth.models import User


def upload_path(instance, user):
    return f'images/{instance}/{user}'

class Profile(models.Model):
    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    avatar = models.ImageField(upload_to=upload_path, blank=True, null=True)

    def __str__(self):
        return self.user.username




