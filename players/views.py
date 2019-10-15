from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Player


class PlayerListView(ListView):
    model = Player
    paginate_by = 100


class SignupView(CreateView):
    model = User
    fields = ['email']
    template_name = 'signup.html'

    def get_success_url(self):
        return reverse('signup-success', kwargs={"secret": self.object.profile.secret, "test": "ahihi"})


class SigupSuccessView(TemplateView):
    template_name = 'success-signup.html'
