from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = 'login.html'


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
