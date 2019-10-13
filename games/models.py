from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from djchoices import DjangoChoices, ChoiceItem
from players.models import Player
from clubs.models import Club


class Tournament(models.Model):

    class TourType(DjangoChoices):
        knockout = ChoiceItem('Knockout')
        league = ChoiceItem('League')

    name = models.CharField(max_length=300)
    type = models.CharField(max_length=20, choices=TourType.choices)
    team_number = models.IntegerField(validators=[MinValueValidator(2), MaxValueValidator(32)])
    round_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(32)])
    knockout_legs = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)], default=1)
    final_legs = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)], default=1)


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
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True)
    tie_type = models.CharField(max_length=30, choices=TieType.choices, default=TieType.single)


class TwoLeggedTie(models.Model):
    first_leg = models.OneToOneField(Game, on_delete=models.CASCADE, related_name='first_leg', unique=True)
    second_leg = models.OneToOneField(Game, on_delete=models.CASCADE, related_name='second_leg', unique=True)
