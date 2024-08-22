from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from teams.models import TeamLead

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин',
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})  # Назначаем класс здесь
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})  # Назначаем класс здесь
    )


class RegistrationForm(UserCreationForm):

    username = forms.CharField(
        label='Логин',
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})  # Назначаем класс здесь
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})  # Назначаем класс здесь
    )
    password2 = forms.CharField(
        label='Повторить пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})  # Назначаем класс здесь
    )
    email = forms.EmailField(
        label='Email',
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control'})  # Назначаем класс здесь
    )
    user_group = forms.ModelChoiceField(
        label='Группа пользователя',
        queryset=Group.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})  # Назначаем класс здесь
    )


    # Добавляем поле выбора группы
    user_group = forms.ModelChoiceField(
        label='Группа пользователя',
        queryset=Group.objects.all(),
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'user_group', 'password1', 'password2']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']


        if commit:
            user.save()
            # Добавляем пользователя в выбранную группу
            user_group = self.cleaned_data['user_group']
            user.groups.add(user_group)

            team_lead = TeamLead()
            team_lead.name = user.username
            team_lead.user = user
            team_lead.save()

        return user
