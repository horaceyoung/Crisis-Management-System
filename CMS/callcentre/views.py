from django.shortcuts import render
from .models import Incident


def callcentre_home(request):
    all_unsolved_incidents = Incident.objects.exclude(incident_status='Resolved').order_by('incident_time')
    context = {'all_unsolved_incidents' : all_unsolved_incidents }
    return render(request, 'callcentre/callcentre_home.html', context)

def callcentre_history(request):
    incident_history = Incident.objects.filter(incident_status='Resolved')
    context = {'incident_history' : incident_history }
    return render(request, 'callcentre/callcentre_history.html', context)

#def status_track(request):
#    status_track = Incident.objects.filter(id)
#    context = {'status_track' : status_track}
#    return render(request, 'statustrack/statustrack_home.html',context)