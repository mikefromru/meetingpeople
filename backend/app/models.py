from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def upload_path(instance, username):
    return f'images/{instance}/{username}'

class CustomUser(AbstractUser):
    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    email = models.EmailField(max_length=100, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    avatar = models.ImageField(upload_to=upload_path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        photo = Image.open(self.avatar.path)
        watermark = Image.open('app/icon.png') 
        width, height = photo.size
        transparent = Image.new('RGBA', (width, height), (0,0,0,0))
        transparent.paste(photo, (0,0))
        transparent.paste(watermark, mask=watermark)
        transparent.show()
        transparent.save(self.avatar.path)

    def __str__(self):
        return self.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

