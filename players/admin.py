from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import Player
from .forms import CustomAdminLoginForm


class CustomLoginAdminSite(AdminSite):
    login_form = CustomAdminLoginForm


admin_site = CustomLoginAdminSite()
admin.site.register(Player)
