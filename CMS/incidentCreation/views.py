from django.shortcuts import render
from django import forms
from .models import Incident, ContactForm2
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext

def incidentCreation(request):
	if request.method=='POST':
		form=ContactForm2(request.POST)

		if form.is_valid():
			caller_name = form.cleaned_data['caller_name']
			mobile_number = form.cleaned_data['mobile_number']
			incident_time = form.cleaned_data['incident_time']
			incident_location = form.cleaned_data['incident_location']
			incident_category = form.cleaned_data['incident_category']
			ContactForm2.objects.create(caller_name = request.POST.get('caller_name'),
							mobile_number = request.POST.get('mobile_number'),
							incident_time = request.POST.get('incident_time'),
							incident_location = request.POST.get('incident_location'),
							incident_category = request.POST.get('incident_category'))
 
			return render_to_response('callcentre/incidentCreation.html',{'form':form},RequestContext(request)) 
	else:
		form=ContactForm2()

	return render_to_response('callcentre/incidentCreation.html',{'form':form},RequestContext(request))