from django import forms
from .models import Team

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