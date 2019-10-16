from django.contrib.admin import AdminSite
from .models import Player, Profile
from .forms import CustomAdminLoginForm


class CustomLoginAdminSite(AdminSite):
    login_form = CustomAdminLoginForm


admin_site = CustomLoginAdminSite()
admin_site.register(Profile)
admin_site.register(Player)
