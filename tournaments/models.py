from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class BaseTourModel(models.Model):
    name = models.CharField(max_length=300, unique=True)
    team_number = models.IntegerField(validators=[MinValueValidator(2), MaxValueValidator(32)])

    class Meta:
        abstract = True


class LeagueTour(BaseTourModel):
    pass


class KnockoutTour(BaseTourModel):
    round_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(32)])
    knockout_legs = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)], default=1)
    final_legs = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)], default=1)
