from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('map.urls', namespace='map')),
    path('callcentre/', include('callcentre.urls', namespace='callcentre')),
<<<<<<< HEAD
    path('department/', include('department.urls', namespace='department')),
    path('statustrack/', include('statusTrack.urls', namespace='statustrack')),
    path('infodistribution/', include('infodistribution.urls', namespace='infodistribution')),
]
=======
    # path('department/', include('department.urls', namespace='department')),
    path('statustrack/', include('statusTrack.urls', namespace='statustrack')),
    path('infodistribution/', include('infodistribution.urls', namespace='infodistribution')),
]
>>>>>>> e1a117cd58a5e32619dfefd31599f1712a0a7f8e
