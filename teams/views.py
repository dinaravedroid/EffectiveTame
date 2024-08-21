from django.shortcuts import render

from teams.models import Team, TeamLead

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from .forms import TeamForm

# Create your views here.



def home_view(request):
    user = request.user

    user_is_player = user.groups.filter(name='Player').exists()
    user_is_lead = user.groups.filter(name='TeamLead').exists()

    return render(request, 'home.html',dict(user_is_player=user_is_player,user_is_lead=user_is_lead))


@login_required
def myteams_view(request):

    teams = Team.objects.filter(creator=request.user) # Получаем все статьи
    return render(request, "team_list.html", {"teams":teams})



def add_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)

        if form.is_valid():
            form.save(user=request.user)
            return redirect('myteams')  # Перенаправление на главную страницу после добавления команды
    else:
        form = TeamForm()
    return render(request, 'team_add.html', {'form': form})