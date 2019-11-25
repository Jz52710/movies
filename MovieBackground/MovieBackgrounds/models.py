from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class UserAdmin(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class MovieInformation(models.Model):
    mname = models.CharField(max_length=200)
    years = models.CharField(max_length=20)
    score = models.CharField(max_length=20)
    director = models.CharField(max_length=1000)
    mold = models.CharField(max_length=200)
    act = models.CharField(max_length=1000)
    languages = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    details = models.CharField(max_length=200)
    official = models.CharField(max_length=200)

class MovieTop(models.Model):
    mname = models.CharField(max_length=200)
    years = models.CharField(max_length=20)
    score = models.CharField(max_length=20)
    director = models.CharField(max_length=1000)
    mold = models.CharField(max_length=200)
    act = models.CharField(max_length=1000)
    img = models.CharField(max_length=200)
    details = models.CharField(max_length=200)
