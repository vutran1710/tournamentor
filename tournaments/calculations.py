from games.models import Team, Game
from players.models import Player
from .models import Fixture
from .algorimths import round_robin_scheduler


def create_league_tour(league_instance):
    """Round-robin Tournaments Algorithm
    - Create the neccessary Teams
    - Apply the round-robin algorithm to create required Fixtures
    """
    number_of_teams = league_instance.team_number
    player_per_team = league_instance.player_per_team
    teams = []

    for idx in range(number_of_teams):

        def _player_name(play_id):
            name = "LT{league_id}-T{team_id}-Player_{play_id}".format(
                league_id=league_instance.id,
                team_id=idx,
                play_id=play_id)
            return name

        players = [Player.objects.create(name=_player_name(playid)) for playid in range(player_per_team)]
        team = Team(player_a=players[0])
        team.player_b = players[1] if len(players) > 2 else None
        team.player_c = players[2] if len(players) > 3 else None
        team.player_d = players[3] if len(players) == 4 else None
        team.save()

        teams.append(team)

    games = []
    fixtures = []

    def create_game_and_fixture(match, round):
        home_team = match[0]
        away_team = match[1]
        game = Game.objects.create(home_team=home_team, away_team=away_team)
        games.append(game)
        fixture = Fixture.objects.create(game=game, tour=league_instance, round=round+1)
        fixtures.append(fixture)

    round_robin_scheduler(teams, create_game_and_fixture)

    return league_instance, teams, games, fixtures
