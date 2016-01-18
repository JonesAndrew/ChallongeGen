from django.db import models

class Player(models.Model):
    mu = models.DecimalField(max_digits=52, decimal_places=48)
    sigma = models.DecimalField(max_digits=52, decimal_places=48)
    name = models.CharField(max_length=24,unique=True)

# Create your models here.
