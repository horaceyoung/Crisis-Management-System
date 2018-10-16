from django.shortcuts import render
from .models import Incident


def callcentre_home(request):
    all_incidents = Incident.objects.exclude(incident_status='RESOLVED')
    context = {'all_incidents' : all_incidents }
    return render(request, 'callcentre/callcentre_home.html', context)
