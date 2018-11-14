from django.shortcuts import render
from django import forms
from .models import Incident, ContactForm2
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from utilities.message import Message
from utilities.incidentstatus import IncidentStatus
from infodistribution.informationdistributor import InformationDistributor

def incidentCreation(request):
	if request.method=='GET':
		form = ContactForm2(request.GET)
		# form is valid
		if form.is_valid():
			incident = Incident()
			incident.caller_name = form.cleaned_data['caller_name']
			incident.mobile_number = form.cleaned_data['mobile_number']
			incident.incident_location = form.cleaned_data['incident_location']
			incident.incident_region = form.cleaned_data['incident_region']
			incident.incident_category = form.cleaned_data['incident_category']
			incident.incident_type = form.cleaned_data['incident_type']
			incident.incident_description = form.cleaned_data['incident_description']


			if incident.incident_category=='Emergency Ambulance':
				incident.incident_department = 'Singapore Civil Defence Force'
			if incident.incident_category=='Rescue and Evacuation':
				incident.incident_department = 'Singapore Civil Defence Force'
			if incident.incident_category=='Fire Fighting':
				incident.incident_department = 'Singapore Civil Defence Force'
			if incident.incident_category=='Gas Leak Control':
				incident.incident_department = 'Singapore Power'
				
			incident.save()

			message = Message(incident.id, IncidentStatus.NEW)
			info_dist = InformationDistributor.get_instance()
			info_dist.distribute(message)

			# print("A new incident is saved\n\n\n\n")
			# print(incident.errors.as_json())
			# return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
			# return render_to_response('/callcentre/',{'form':form},RequestContext(request))
			return HttpResponseRedirect('/callcentre/')
		else:
			form=ContactForm2()
			return render_to_response('callcentre/incidentCreation.html',{'form':form},RequestContext(request))
