from django.urls import path
from . import views
from .views import myteams_view

urlpatterns = [
    path('myteams/', myteams_view, name='myteams'),
    path('', views.home_view, name='home'),  # URL для главной страницы
    path('add-team/', views.add_team, name='add_team'),
]
