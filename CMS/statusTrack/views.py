from django.shortcuts import render
from django import forms
from callcentre.models import Incident
<<<<<<< HEAD
from .models import ContactForm3
=======
from .models import ContactForm3, ContactForm4
from utilities.message import Message
from utilities.incidentstatus import IncidentStatus
from infodistribution.informationdistributor import InformationDistributor
>>>>>>> b4f52dd7ced4e6542d6820ae2ba9ab7dcec714e9
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.views.generic import TemplateView
from statusTrack.forms import StatusForm
from flask import Flask
from flask import request



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
			return render_to_response('statustrack/statustrack_home.html', {'form': form}, RequestContext(request))
		else:
			form=ContactForm3()
			return render_to_response('statustrack/statustrack_home.html', {'form': form}, RequestContext(request))
