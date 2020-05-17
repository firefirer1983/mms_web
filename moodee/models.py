from django.db import models

# Create your models here.


class Moodee(models.Model):
    username = models.CharField(max_length=64)
    phone = models.CharField(max_length=32)
    password_or_code = models.CharField(max_length=32)
    created_at = models.DateTimeField("date created")
    updated_at = models.DateTimeField("date updated")
