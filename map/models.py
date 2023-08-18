from django.db import models


# Create your models here.
class Marker(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    name = models.CharField(null =True, max_length=120)
    description = models.CharField(max_length=120)
    type = models.CharField(null =True, max_length=120)
