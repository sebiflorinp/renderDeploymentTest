from django.db import models

# Create your models here.


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    initials = models.CharField(max_length=10)
