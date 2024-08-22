from django.db import models
import datetime
from django.contrib.auth.models import User
from django import forms
import logging

class TeamLead(models.Model):
    name = models.CharField(max_length=100)
    money = models.FloatField(default=0.0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaduser', null=True, blank=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Тимлид"
        verbose_name_plural = "Тимлид"


class Team(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teams', null=True, blank=True)




    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команда"



class Player(models.Model):
    name = models.CharField(max_length=100)
    stamina = models.IntegerField(default=0)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='participants')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Игрок"
        verbose_name_plural = "Игрок"


class RequestToTeam(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='applications')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='applications')

    def __str__(self):
        return f'{self.player.name} -> {self.team.name}'

    class Meta:
        verbose_name = "Заявка в команду"
        verbose_name_plural = "Заявка в команду"

class ProcessStatus:
    in_process = 0 # В процессе
    done = 1 # Завершена
    error = 2 # Отклонена

class ShareBonus(models.Model):
    from_user = models.ForeignKey(TeamLead, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(TeamLead, on_delete=models.CASCADE, related_name='to_user')
    status = models.IntegerField(default=ProcessStatus.in_process)
    create_dt = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f'{self.from_user.name} -> {self.to_user.name}'

    class Meta:
        verbose_name = "Поделиться баллами"
        verbose_name_plural = "Поделиться баллами"