from django.shortcuts import render
from django import forms
from callcentre.models import Incident
from .models import ContactForm3, ContactForm4
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.views.generic import TemplateView
from statusTrack.forms import StatusForm
from flask import Flask
from flask import request

def getid(request):
	if request.method == 'post':
		form = ContactForm4(request.post)
		idget = request.form['id']

def statusTrack(request):
	if request.method == 'GET':
		form = ContactForm3(request.GET)
		if form.is_valid():
			# print("The form is valid\n\n\n\n")
			incident = Incident.objects.get(id=idget)
			incident.incident_status = form.cleaned_data['incident_status']
			incident.save()
			# print("A new incident is saved\n\n\n\n")
			return render_to_response('statustrack/statustrack_home.html',{'form':form},RequestContext(request))
		else:
			form=ContactForm3()
			return render_to_response('statustrack/statustrack_home.html',{'form':form},RequestContext(request))
