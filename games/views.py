from django.views.generic.list import ListView
from .models import (
    Tournament,
    Team,
    Game
)


class TournamentListView(ListView):
    model = Tournament
    paginate_by = 50


class TeamListView(ListView):
    model = Team
    paginate_by = 50


class GameListView(ListView):
    model = Game
    paginate_by = 50
