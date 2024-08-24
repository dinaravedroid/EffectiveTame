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
    max_members = models.PositiveIntegerField(default=5)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команда"

class Player(models.Model):
    name = models.CharField(max_length=100, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    stamina = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} '

    class Meta:
        verbose_name = "Игрок"
        verbose_name_plural = "Игрок"


class ProcessStatus:
    in_process = 'in_process' # В процессе
    approved = 'approved' # Завершена
    denied = 'denied' # Отклонена

class RequestToTeam(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='team_members')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    status_id = models.CharField(default='', max_length=100)

    def __str__(self):
        return f'{self.player} -> {self.team}'

    class Meta:
        verbose_name = "Заявка в команду"
        verbose_name_plural = "Заявка в команду"





