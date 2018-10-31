from django.urls import path
from . import views

app_name = 'statusTrack'

urlpatterns = [
    path('', views.statusTrack, name='statusTrack'),
]
