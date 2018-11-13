from django.http import Http404
#from django.http import HttpResponse
from callcentre.models import Incident
#from django.template import loader
from django.shortcuts import render

from django.shortcuts import render
from django import forms
from callcentre.models import Incident
from .models import ContactForm3
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from utilities.message import Message
from utilities.incidentstatus import IncidentStatus
from infodistribution.informationdistributor import InformationDistributor

from django.views.generic import TemplateView
from flask import Flask
from flask import request

def index(request):
    all_unsolved_incidents = Incident.objects.exclude(incident_status='Resolved').order_by('incident_time')
    return render(request, 'statustrack/statusCreation_home.html', {'all_unsolved_incidents' : all_unsolved_incidents})
#    all_unsolved_incidents = Incident.objects.all()
    #template = loader.get_template('statustrack/statusCreation_home.html')

    #html = ''
    #for incident in all_unsolved_incidents:
    #    url = '/statusCreation/' + str(incident.id) +'/'
    #html +='<a href="' + url + '">' + incident.incident_status + '</a><br>'
    #return HttpResponse(template.render(context, request))




def detail(request, incident_id):
    try:
        incident = Incident.objects.get(id=incident_id)
        form = ContactForm3(request.POST)
        if request.method == 'POST':
            if form.is_valid():

                incident = Incident.objects.get(id=incident_id)
                incident.incident_status = form.cleaned_data['incident_status']
                incident.save()

                message = Message(incident.id, IncidentStatus.from_str(incident.incident_status))
                info_dist = InformationDistributor.get_instance()
                info_dist.distribute(message)

                context = {'form': form, 'incident': incident}
                return render(request, 'statustrack/detail.html', context)
        else:
            form = ContactForm3()
            context =  {'form': form, 'incident': incident}
            return render(request, 'statustrack/detail.html', context)

    except Incident.DoesNotExist:
        raise Http404("Incident does not exist")




def statusTrack(request):
    if request.method == 'GET':
        form = ContactForm3(request.GET)
        if form.is_valid():
            # print("The form is valid\n\n\n\n")
            incident = Incident.objects.get(id=5)
            incident.incident_status = form.cleaned_data['incident_status']
            incident.save()

            message = Message(incident.id, IncidentStatus.from_str(incident.incident_status))
            info_dist = InformationDistributor.get_instance()
            info_dist.distribute(message)

            # print("A new incident is saved\n\n\n\n")
            return render_to_response('statustrack/statustrack_home.html',{'form':form},RequestContext(request))
        else:
            form=ContactForm3()
            return render_to_response('statustrack/statustrack_home.html',{'form':form},RequestContext(request))