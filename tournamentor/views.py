from django.contrib.auth.views import LoginView as BaseLoginView
from django.views.generic import TemplateView
from .forms import UserLoginForm


class LoginView(BaseLoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    authentication_form = UserLoginForm

    def get_success_url(self):
        return self.request.GET.get('next')


class HomeView(TemplateView):
    template_name = 'index.html'
