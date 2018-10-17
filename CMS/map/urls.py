from django.urls import path
from map.views import LocationFormView
from . import views

app_name = 'map'

urlpatterns = [
    path('', LocationFormView.as_view(), name='map_home'),
]