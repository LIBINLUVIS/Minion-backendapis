from django.db import models

# Create your models here.


class ThresholdValue(models.Model):
    value=models.FloatField()
    