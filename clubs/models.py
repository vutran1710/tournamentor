from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Club(models.Model):
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=300)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
