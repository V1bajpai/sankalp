from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(verbose_name='email address',max_length=255, unique=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    country_code = models.CharField(max_length=6)
    phone = models.CharField(max_length=14, unique=True)
    gender = models.CharField(max_length=10)

    objects = models.Manager()

    def __str__(self):
        return self.email

class SignupValidationToken(models.Model):
    token = models.CharField(blank=False, max_length=55)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sign_up_validation_token', null=True, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.user.name
