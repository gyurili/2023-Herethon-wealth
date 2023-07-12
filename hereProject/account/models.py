from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#이메일, 비밀번호, 닉네임

class CustomUser(AbstractUser):
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=20)
    nickname=models.CharField(max_length = 20)

    groups = models.ManyToManyField('auth.Group', related_name='custom_users')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_users')
