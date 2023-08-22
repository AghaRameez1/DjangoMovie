from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
import random
import string
# Create your models here.
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


class Users(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    otp = models.IntegerField(default=0)
    access_token = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username.username


@receiver(pre_save, sender=Users)
def access_token_generator(sender, instance, **kwargs):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(5))
    print("Random string of length", 5, "is:", result_str)
    instance.access_token = result_str
