from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import LeagueTour, KnockoutTour


class LeagueTourListView(ListView):
    model = LeagueTour
    paginate_by = 100


class LeagueTourDetailView(DetailView):
    model = LeagueTour
    context_object_name = 'league'


class KnockoutTourListView(ListView):
    model = KnockoutTour
    paginate_by = 100


class CreateLeagueView(LoginRequiredMixin, CreateView):
    model = LeagueTour
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('league-detail-view', args=(self.object.id,))


class CreateKnockoutView(LoginRequiredMixin, CreateView):
    model = KnockoutTour
    fields = ['name', 'team_number', 'round_number', 'knockout_legs', 'final_legs']
