from django.urls import path
from . import views
from .views import myteams_view, mybonus_view

urlpatterns = [
    path('myteams/', myteams_view, name='myteams'),
    path('', views.home_view, name='home'),  # URL для главной страницы
    path('add-team/', views.add_team, name='add_team'),
    path('update/<int:pk>/', views.team_update, name='team_update'),
    path('delete/<int:pk>/', views.team_delete, name='team_delete'),
    path('mybonus/', mybonus_view, name='mybonus')
]
