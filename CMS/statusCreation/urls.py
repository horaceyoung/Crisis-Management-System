from django.conf.urls import url
from statusCreation import views
from django.urls import path

app_name='statusCreation'

urlpatterns = [

    url(r'^$', views.index, name='index'),

    url(r'^(?P<incident_id>[0-9]+)/$', views.detail, name='detail'),

#    url(r'^(?P<incident_id>[0-9]+)/$', views.statusTrack, name='statustrack'),


#    url(r'^(?P<incident_id>[0-9]+)/updated/$', views.update, name='update'),

]