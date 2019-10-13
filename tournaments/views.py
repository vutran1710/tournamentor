from django.views.generic.list import ListView
from .models import LeagueTour, KnockoutTour


class LeagueTourListView(ListView):
    model = LeagueTour
    paginate_by = 100


class KnockoutTourListView(ListView):
    model = KnockoutTour
    paginate_by = 100
