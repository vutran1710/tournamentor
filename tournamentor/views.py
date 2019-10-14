from django.shortcuts import render
from django.views import View


class HomeView(View):
    """Home view
    """
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
