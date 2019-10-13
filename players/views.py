from django.views.generic.list import ListView
from .models import Player


class PlayerListView(ListView):
    model = Player
    paginate_by = 100
