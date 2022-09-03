from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    gender_choices = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('N', 'None')
    )

    gender = models.CharField(blank=True, choices=gender_choices, max_length=1, null=True)
    phone_number = models.CharField(blank=True, default='', max_length=11, null=True)

