from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('map.urls', namespace='map')),
    path('callcentre/', include('callcentre.urls', namespace='callcentre')),
    path('statustrack/', include('statusTrack.urls', namespace='statustrack')),
    path('incidentCreation/', include('incidentCreation.urls', namespace='incidentCreation')),
]
