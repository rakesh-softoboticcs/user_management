from django.core.validators import validate_email
from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=20, default="")
    last_name = models.CharField(max_length=20, default="")
    user_name = models.CharField(max_length=5, default="", unique=True)
    email = models.EmailField(max_length=100, unique=True)
    # mobile = models.IntegerField(max_length=10)
    password = models.CharField(
        max_length=20, default="",)
    confirm_password = models.CharField(
        max_length=20, default="",)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Posts(models.Model):
    post = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
