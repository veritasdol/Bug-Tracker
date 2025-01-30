from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('tester', 'Tester'),
        ('developer', 'Developer'),
        ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='tester')

    def __str__(self):
        return f'{self.username} ({self.role})'
    