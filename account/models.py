from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    GENDERS = [
        ('MALE','male'),
        ('FEMALE','female'),
    ]
    phone_number = models.CharField(max_length=150, unique=True)
    username = models.CharField(max_length=150, unique=True, null=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    gender = models.CharField(max_length=6, choices=GENDERS, null=True, default='')
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'username']

    @property
    def get_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name:
            return f'{self.first_name}'
        elif self.last_name:
            return f'{self.last_name}'
        else:
            return f'{self.phone_number}'

