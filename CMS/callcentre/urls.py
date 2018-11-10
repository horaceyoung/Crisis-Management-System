from django.urls import path
from . import views

app_name = 'callcentre'

urlpatterns = [
    path('', views.callcentre_home, name='callcentre_home'),
    path('history/', views.callcentre_history, name='callcentre_history'),
]