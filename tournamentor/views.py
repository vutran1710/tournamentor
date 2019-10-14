from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Home view
    """
    template_name = 'index.html'
