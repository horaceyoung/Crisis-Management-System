from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('map.urls', namespace='map')),
    path('callcentre/', include('callcentre.urls', namespace='callcentre')),
<<<<<<< HEAD
    path('department/', include('department.urls', namespace='department')),
    path('statustrack/', include('statusTrack.urls', namespace='statustrack')),
=======
    path('infodistribution/', include('infodistribution.urls', namespace='infodistribution')),
>>>>>>> e5d2f1c5019d4e7b33a580fdc4dc7a8cfa54dcdc
]
