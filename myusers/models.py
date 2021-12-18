from django.db import models

# Create your models here.
from django.contrib.auth.admin import UserAdmin

class User(UserAdmin):
    username = models.CharField(null=True),
    email = models.EmailField(null=True),
    phone = models.IntegerField(null=True),
    password = models.TextField(null=True),

    def __str__(self):
        return self.username





