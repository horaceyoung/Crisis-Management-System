from django.urls import path
from . import views

app_name = 'incidentCreation'

urlpatterns = [
    path('', views.incidentCreation, name='incidentCreation'),
]