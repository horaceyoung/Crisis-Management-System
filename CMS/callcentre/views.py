from django.shortcuts import render
from django import forms
from .models import Incident, ContactForm2
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect

IncidentType = CATEGORY_CHOICES = [    # Note square brackets.
    ("Emergency Ambulance", "Emergency Ambulance"), 
    ("Rescue & Evacuation", "Rescue & Evacuation"),
    ("Fire Fighting", "Fire Fighting"),
    ("Gas Leak Control", "Gas Leak Control"),        
]

def incidentCreation(request):
	print("A new page is shown\n\n\n\n")
	print(request.method)
	if request.method=='GET':
		form = ContactForm2(request.GET)											
		print(form.is_valid())
		print(form.errors)
		if form.is_valid():
			print("The form is valid\n\n\n\n")
			#if(form.cleaned_data['caller_name'])==None:
				#return render_to_response('callcentre/incidentCreation.html',{'form':form},RequestContext(request))
			incident = Incident()
			incident.caller_name = form.cleaned_data['caller_name']
			incident.mobile_number = form.cleaned_data['mobile_number']
			incident.location = form.cleaned_data['incident_location']
			incident.incident_category = form.cleaned_data['incident_category']
			incident.save()
			print("A new incident is saved\n\n\n\n")
			return render_to_response('callcentre/incidentCreation.html',{'form':form},RequestContext(request))
		else:
		#print("test")
			form=ContactForm2()
			return render_to_response('callcentre/incidentCreation.html',{'form':form},RequestContext(request))
