import logging

from teams.models import Team, TeamLead, Player, RequestToTeam, ProcessStatus

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from .forms import TeamForm, TeamleadMoneyForm, TransferMoneyForm
from django.contrib import messages
from django.db.models import Max, Min

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


#-------CRUD-----
@login_required
def team_update(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('myteams')
    else:
        form = TeamForm(instance=team)
    return render(request, 'team_update.html', {'form': form})

@login_required
def team_delete(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        team.delete()
        return redirect('myteams')
    return render(request, 'team_confirm_delete.html', {'team': team})

@login_required
def add_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)

        if form.is_valid():
            form.save(user=request.user)
            return redirect('myteams')  # Перенаправление на главную страницу после добавления команды
    else:
        form = TeamForm()
    return render(request, 'team_add.html', {'form': form})

#----баллы----
@login_required
def mybonus_view(request):

    if not request.user.groups.filter(name='TeamLead').exists():
        return redirect('home')

    teamlead = TeamLead.objects.get(user_id=request.user)

    if request.method == 'POST':
        if 'update_money' in request.POST:
            # Обработка изменения количества денег
            form = TeamleadMoneyForm(request.POST, instance=teamlead)
            if form.is_valid():
                form.save()
                messages.success(request, "Баланс успешно обновлен.")
                return redirect('mybonus')
        elif 'transfer_money' in request.POST:
            # Обработка перевода денег
            transfer_form = TransferMoneyForm(request.POST)
            if transfer_form.is_valid():
                recipient = transfer_form.cleaned_data['recipient']
                amount = transfer_form.cleaned_data['amount']

                if teamlead.money >= amount:
                    teamlead.money -= amount
                    recipient.money += amount
                    teamlead.save()
                    recipient.save()
                    messages.success(request, f"Успешно переведено {amount} баллов {recipient.name}.")
                else:
                    messages.error(request, "Недостаточно средств для перевода.")
                return redirect('mybonus')
    else:
        form = TeamleadMoneyForm(instance=teamlead)
        transfer_form = TransferMoneyForm()

    return render(request, 'mybonus.html', {
        'form': form,
        'transfer_form': transfer_form,
        'teamlead': teamlead
    })


def player_info(request):
    teams = Team.objects.all()  # Получаем все команды
    return render(request, 'playerinfo.html', {'teams': teams})


@login_required
def apply_to_team(request, team_id):
    if request.method == 'POST':

        team = Team.objects.get(pk=team_id)
        current_player = Player.objects.get(user=request.user)
        count_on_team_players = RequestToTeam.objects.select_related('player').filter(team=team).count()

        req = RequestToTeam()
        req.team = team
        req.player = current_player

        remove_candidates = None
        if( count_on_team_players > 5 ):
            remove_candidates = (RequestToTeam.objects.select_related('player')
                                 .filter(team=team, player__stamina__lt=current_player.stamina)
                                 .order_by('player__stamina')).first()

            if(remove_candidates):
                remove_candidates.delete()

                req.status_id = ProcessStatus.approved
            else:
                req.status_id = ProcessStatus.denied
        else:
            req.status_id = ProcessStatus.approved

        req.save()


        return redirect('player_info')
