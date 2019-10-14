from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import LeagueTour, KnockoutTour


class LeagueTourListView(ListView):
    model = LeagueTour
    paginate_by = 100


class KnockoutTourListView(ListView):
    model = KnockoutTour
    paginate_by = 100


class CreateLeagueView(CreateView):
    model = LeagueTour
    fields = ['name', 'team_number']


class CreateKnockoutView(CreateView):
    model = KnockoutTour
    fields = ['name', 'team_number', 'round_number', 'knockout_legs', 'final_legs']
