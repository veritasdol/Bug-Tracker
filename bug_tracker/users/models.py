from django.contrib.auth.models import AbstractUser
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('tester', 'Tester'),
        ('developer', 'Developer'),
        ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='tester')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True, related_name='users')

    def __str__(self):
        return f'{self.username} ({self.role})'
    