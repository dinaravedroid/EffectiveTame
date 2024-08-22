from django import forms
from .models import Team, TeamLead
from django import forms

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']  # Поля, которые будут отображаться в форме


    def save(self, commit=True, user=None):
        instance = super(TeamForm, self).save(commit=False)
        if user:
            instance.creator = user
        if commit:
            instance.save()
        return instance

class TeamleadMoneyForm(forms.ModelForm):
    class Meta:
        model = TeamLead
        fields = ['money']


class TransferMoneyForm(forms.Form):
    recipient = forms.ModelChoiceField(queryset=TeamLead.objects.all(), label="Получатель")
    amount = forms.FloatField(min_value=0.01, label="Сумма перевода")
