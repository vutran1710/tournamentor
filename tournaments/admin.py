from django.contrib import admin
from .models import LeagueTour, KnockoutTour, Fixture


admin.site.register(LeagueTour)
admin.site.register(KnockoutTour)
admin.site.register(Fixture)
