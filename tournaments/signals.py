from django.db import transaction
from django.dispatch import receiver
from django.db.models.signals import post_save
from games.models import Team, Game
from players.models import Player
from .models import LeagueTour, KnockoutTour, Fixture
from algorimths import round_robin_scheduler


@receiver(post_save, sender=LeagueTour)
def create_league_tour(sender, instance, created, **kwargs):
    if not created:
        return
    try:
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
                team = Team(player_a=players[0])
                team.player_b = players[1] if len(players) > 2 else None
                team.player_c = players[2] if len(players) > 3 else None
                team.player_d = players[3] if len(players) == 4 else None
                team.save()

                all_teams.append(team)

            def create_game_and_fixture(match, round):
                home_team = match[0]
                away_team = match[1]
                game = Game.objects.create(home_team=home_team, away_team=away_team)
                Fixture.objects.create(game=game, tour=instance, round=round)

            round_robin_scheduler(all_teams, create_game_and_fixture)

    except Exception as err:
        print('Error creating')
        print(err)
        print('=============')


@receiver(post_save, sender=KnockoutTour)
def create_knockout_tour(sender, instance, created, **kwargs):
    if not created:
        return
    pass
