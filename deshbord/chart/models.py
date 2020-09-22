from django.db import models

# Create your models here.

class City(models.Model):
    name = models.IntegerField(null=True, blank=True)
    population = models.IntegerField(null=True, blank=True)
    male = models.IntegerField(null=True, blank=True)
    female = models.IntegerField(null=True, blank=True)
    other = models.IntegerField(null=True, blank=True)


