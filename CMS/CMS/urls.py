from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('map.urls', namespace='map')),
    path('callcentre/', include('callcentre.urls', namespace='callcentre')),
    path('department/', include('department.urls', namespace='department')),
    path('statustrack/', include('statusTrack.urls', namespace='statustrack')),
    path('infodistribution/', include('infodistribution.urls', namespace='infodistribution')),
    path('incidentCreation/', include('incidentCreation.urls', namespace='incidentCreation')),
]
