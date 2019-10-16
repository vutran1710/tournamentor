from django.db import transaction
from django.dispatch import receiver
from django.db.models.signals import post_save
from games.models import Team, Game
from players.models import Player
from .models import LeagueTour, KnockoutTour, Fixture


@receiver(post_save, sender=LeagueTour)
def create_league_tour(sender, instance, created, **kwargs):
    if not created:
        return

    with transaction.atomic():
        """Round-robin Tournaments Algorithm
        - Create the neccessary Teams
        - Apply the round-robin algorithm to create required Fixtures
        """
        number_of_teams = instance.team_number
        player_per_team = instance.player_per_team
        all_teams = []

        for idx in range(number_of_teams):

            def _player_name(play_id):
                name = "LT{league_id}-T{team_id}-Player_{play_id}".format(
                    league_id=instance.id,
                    team_id=idx,
                    play_id=play_id)
                return name

            players = [Player.objects.create(name=_player_name(playid)) for playid in range(player_per_team)]
            team = Team.objects.create(
                player_a=players[0],
                player_b=players[1],
                player_c=players[2],
                player_d=players[3],
            )

            all_teams.append(team)

        """
        Refer to https://en.wikipedia.org/wiki/Round-robin_tournament#Scheduling_algorithm
        """
        # number_of_games = number_of_teams / 2 * (number_of_teams - 1)


@receiver(post_save, sender=KnockoutTour)
def create_knockout_tour(sender, instance, created, **kwargs):
    if not created:
        return
    pass
