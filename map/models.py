from django.db import models


# Create your models here.
class Marker(models.Model):
    lat = models.IntegerField()
    lng = models.IntegerField()
    name = models.CharField(null =True, max_length=120)
    description = models.CharField(max_length=120)
    type = models.CharField(null =True, max_length=120)
