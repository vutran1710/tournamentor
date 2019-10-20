from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from players.models import Player
from clubs.models import Club


class Team(models.Model):
    name = models.CharField(max_length=100, null=True)
    player_a = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_a')
    player_b = models.ForeignKey(Player, on_delete=models.SET_NULL, related_name='player_b', null=True)
    player_c = models.ForeignKey(Player, on_delete=models.SET_NULL, related_name='player_c', null=True)
    player_d = models.ForeignKey(Player, on_delete=models.SET_NULL, related_name='player_d', null=True)
    tour_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    tour_id = models.PositiveIntegerField(null=True)
    tour = GenericForeignKey('tour_type', 'tour_id')


class Game(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='home_team')
    home_club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, related_name='home_club')
    home_result = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], null=True)

    away_team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='away_team')
    away_club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, related_name='away_club')
    away_result = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], null=True)
