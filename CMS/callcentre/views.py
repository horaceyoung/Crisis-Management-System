from django.shortcuts import render
from .models import Incident
from django.http import HttpResponse


def callcentre_home(request):
    all_unsolved_incidents = Incident.objects.exclude(incident_status='Resolved').order_by('incident_time')
    context = {'all_unsolved_incidents' : all_unsolved_incidents }
    #    html=''
    #    for incident in all_unsolved_incidents:
    #        url = '/callcentre/' + str(incident.id) +'/'
    #        html +='<a href="' + url + '">' + incident.incident_status + '</a><br>'
    #        return HttpResponse(html)
    return render(request, 'callcentre/callcentre_home.html', context)

def callcentre_history(request):
    incident_history = Incident.objects.filter(incident_status='Resolved')
    context = {'incident_history' : incident_history }
    return render(request, 'callcentre/callcentre_history.html', context)

#def detail(request, incident_id):
#    return HttpResponse("<h1>Details for incident id:"+str(incident_id)+"</h1>")
