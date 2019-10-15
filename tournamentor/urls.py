"""tournamentor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from players.admin import admin_site
from django.urls import path
from clubs.views import ClubListView
from players.views import (
    PlayerListView,
    SignupView,
    SigupSuccessView,
)
from tournaments.views import (
    LeagueTourListView,
    KnockoutTourListView,
    CreateLeagueView,
    CreateKnockoutView,
)
from .views import (
    HomeView,
    LoginView,
)

urlpatterns = [
    path('admin/', admin_site.urls),
    path('clubs', ClubListView.as_view(), name='club-list'),
    path('players', PlayerListView.as_view(), name='player-list'),
    path('leagues', LeagueTourListView.as_view(), name='league-tour-list'),
    path('knockout', KnockoutTourListView.as_view(), name='knockout-tour-list'),
    path('new-league', CreateLeagueView.as_view(), name='create-league-form'),
    path('new-knockout', CreateKnockoutView.as_view(), name='create-knockout-form'),
    path('login', LoginView.as_view(), name='login-view'),
    path('signup', SignupView.as_view(), name='signup-view'),
    path('signup-success', SigupSuccessView.as_view(), name='signup-success'),
    path('', HomeView.as_view(), name='home-view'),
]
