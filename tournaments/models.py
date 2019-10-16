from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from games.models import Game


class BaseTourModel(models.Model):
    name = models.CharField(max_length=300, unique=True)
    team_number = models.IntegerField(validators=[MinValueValidator(2), MaxValueValidator(32)])
    player_per_team = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])

    class Meta:
        abstract = True


class LeagueTour(BaseTourModel):
    double_round = models.BooleanField(default=False)


class KnockoutTour(BaseTourModel):
    round_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(32)])
    knockout_legs = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)], default=2)
    final_legs = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)], default=1)


class Fixture(models.Model):
    time = models.DateTimeField(null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    tour_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    tour_id = models.PositiveIntegerField()
    tour = GenericForeignKey('tour_type', 'tour_id')
    round = models.PositiveSmallIntegerField()
