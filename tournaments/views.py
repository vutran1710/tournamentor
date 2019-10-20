from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from games.models import Team
from .models import LeagueTour, KnockoutTour, Fixture
from .calculations import create_league_tour


class LeagueTourListView(ListView):
    model = LeagueTour
    paginate_by = 100


class LeagueTourDetailView(DetailView):
    model = LeagueTour
    context_object_name = 'league'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        league = context['league']
        tour_type = ContentType.objects.get_for_model(LeagueTour)
        fixtures = Fixture.objects.filter(tour_type=tour_type, tour_id=league.id)
        teams = Team.objects.filter(tour_type=tour_type, tour_id=league.id)
        context['fixtures'] = fixtures
        context['teams'] = teams
        return context


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
