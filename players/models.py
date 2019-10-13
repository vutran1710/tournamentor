from django.db import models


class Player(models.Model):
    name = models.TextField(unique=True)
    position = models.CharField(max_length=300)
    strength = models.TextField()
    weakness = models.TextField()
    stats = models.TextField()
