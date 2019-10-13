from django.views.generic.list import ListView
from .models import (
    Team,
    Game
)


class TeamListView(ListView):
    model = Team
    paginate_by = 50


class GameListView(ListView):
    model = Game
    paginate_by = 50
