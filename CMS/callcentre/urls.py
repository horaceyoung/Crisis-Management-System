from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'callcentre'

urlpatterns = [
    path('', views.callcentre_home, name='callcentre_home'),
    path('history/', views.callcentre_history, name='callcentre_history'),

#    url(r'^(?P<incident_id>[0-9]+)/$', views.detail, name='detail'),
]