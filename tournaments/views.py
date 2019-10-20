from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import LeagueTour, KnockoutTour
from .calculations import create_league_tour


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

    @transaction.atomic
    def form_valid(self, form):
        league_data = form.cleaned_data
        league, teams, games, fixtures = create_league_tour(LeagueTour.objects.create(**league_data))
        return HttpResponseRedirect(reverse_lazy('league-detail-view', args=[league.id]))

    def get_success_url(self):
        return reverse_lazy('league-detail-view', args=(self.object.id,))


class CreateKnockoutView(LoginRequiredMixin, CreateView):
    model = KnockoutTour
    fields = ['name', 'team_number', 'round_number', 'knockout_legs', 'final_legs']
