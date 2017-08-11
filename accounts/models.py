# accounts/models.py
from django.conf import settings
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models

# 우선적으로 마이그레이션을 해야 한다.
class Profile(AbstractUser):

    # phone_number = models.CharField(max_length=20)
    realname = models.CharField(max_length=50)
    student_number = models.CharField(max_length=20)
    class_name = models.CharField(max_length=20)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'realname', 'student_number', 'class_name']

    def __str__(self):
        return self.realname