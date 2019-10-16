from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from django.contrib.auth.models import User


SECRET_REGEX = "^[A-Za-z0-9]{6}"
PASSWORD_REG = "^[A-Za-z0-9]{8}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    secret = models.CharField(max_length=20, validators=[RegexValidator(SECRET_REGEX)], unique=True)


class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.SmallIntegerField(default=0, validators=[MinValueValidator(0)])
