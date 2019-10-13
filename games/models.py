from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from djchoices import DjangoChoices, ChoiceItem
from players.models import Player
from clubs.models import Club


class Team(models.Model):
    player_a = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_a')
    player_b = models.ForeignKey(Player, on_delete=models.SET_NULL, related_name='player_b', null=True)
    player_c = models.ForeignKey(Player, on_delete=models.SET_NULL, related_name='player_c', null=True)
    player_d = models.ForeignKey(Player, on_delete=models.SET_NULL, related_name='player_d', null=True)


class Game(models.Model):

    class TieType(DjangoChoices):
        single = ChoiceItem('Single-legged')
        twotie = ChoiceItem('Two-legged')

    home_team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='home_team')
    home_club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, related_name='home_club')
    home_result = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], null=True)

    away_team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='away_team')
    away_club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, related_name='away_club')
    away_result = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], null=True)
    time = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    tie_type = models.CharField(max_length=30, choices=TieType.choices, default=TieType.single)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    tournament = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'tournament')
