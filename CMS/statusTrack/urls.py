from django.urls import path
from . import views

app_name = 'statustrack'

urlpatterns = [
    path('', views.statustrack_home, name='statustrack_home'),
]