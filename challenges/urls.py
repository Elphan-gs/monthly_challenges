from django.urls import path
from . import views

app_name = 'challenges'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:month>', views.monthly_challenges_number, name="monthly_challenges_number"),
    path('<str:month>', views.monthly_challenges, name="monthly_challenges"),
]
