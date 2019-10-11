from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Club


class ClubListView(ListView):
    model = Club
    paginate_by = 100
