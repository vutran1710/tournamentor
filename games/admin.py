from players.admin import admin_site
from .models import (
    Team,
    Game
)


admin_site.register(Team)
admin_site.register(Game)
