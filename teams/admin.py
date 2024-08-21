from django.contrib import admin
from teams.models import Team, TeamLead,RequestToTeam, Player, ShareBonus

admin.site.register(Team)
admin.site.register(TeamLead)
admin.site.register(RequestToTeam)
admin.site.register(Player)
admin.site.register(ShareBonus)
