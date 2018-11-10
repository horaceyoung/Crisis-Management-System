from django.shortcuts import render
from django import forms
from .models import Incident, ContactForm2
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from utilities.message import Message
from utilities.incidentstatus import IncidentStatus
from infodistribution.informationdistributor import InformationDistributor


def incidentCreation(request):
    if request.method == 'GET':
        form = ContactForm2(request.GET)
        if form.is_valid():
            # print("The form is valid\n\n\n\n")
            incident = Incident()
            incident.caller_name = form.cleaned_data['caller_name']
            incident.mobile_number = form.cleaned_data['mobile_number']
            incident.incident_location = form.cleaned_data['incident_location']
            incident.incident_category = form.cleaned_data['incident_category']
            incident.incident_type = form.cleaned_data['incident_type']
            incident.incident_region = form.cleaned_data['incident_region']
            incident.incident_status = IncidentStatus.NEW.value
            incident.save()

            message = Message(incident.id, IncidentStatus.NEW)
            info_dist = InformationDistributor.get_instance()
            info_dist.distribute(message)

            # print("A new incident is saved\n\n\n\n")
            return render_to_response('callcentre/incidentCreation.html', {'form': form}, RequestContext(request))
        else:
            form = ContactForm2()
            return render_to_response('callcentre/incidentCreation.html', {'form': form}, RequestContext(request))
