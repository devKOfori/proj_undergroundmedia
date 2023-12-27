from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.conf import settings
# Create your models here.

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('Email', max_length=255, unique=True)
    date_of_birth = models.DateField('Date of Birth', blank=True, null=True)
    phone_number = models.CharField('Phone Number', max_length=255, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def  __str__(self):
        return self.email

    objects = CustomUserManager()

class Artist(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    stage_name = models.CharField('Stage Name', max_length=255)
    twitter_profile = models.URLField('X Profile', blank=True)
    instagram_profile = models.URLField('Instagram Profile', blank=True)
    facebook_profile = models.URLField('Facebook Profile', blank=True)

    def __str__(self):
        return self.stage_name
    
class Writer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

