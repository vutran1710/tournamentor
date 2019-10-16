from players.admin import admin_site
from .models import LeagueTour, KnockoutTour, Fixture


admin_site.register(LeagueTour)
admin_site.register(KnockoutTour)
admin_site.register(Fixture)
