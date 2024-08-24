from django.contrib import admin
from teams.models import Team, TeamLead,RequestToTeam, Player
from django.utils.html import format_html

class RequestToTeamViewAdmin(admin.ModelAdmin):
    list_display = ['player','teams']

    def teams(self, instance):
        return format_html(
            '<a href="/admin/teams/team/{}/change/">{}</div>',
            instance.team.id,
            instance.team.name,  # Or whatever you want to put here
        )

admin.site.register(RequestToTeam, RequestToTeamViewAdmin)

admin.site.register(Team)
admin.site.register(TeamLead)
admin.site.register(Player)
