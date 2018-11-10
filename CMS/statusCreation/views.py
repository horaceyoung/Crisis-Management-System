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

from django.views.generic import TemplateView
from statusTrack.forms import StatusForm
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
        if request.method == 'GET':
            form = ContactForm3(request.GET)
            if form.is_valid():
                incident = Incident.objects.get(id=incident_id)
                incident.incident_status = form.cleaned_data['incident_status']
                incident.save()
                return render_to_response('statustrack/detail.html', {'form': form, 'incident': incident}, RequestContext(request))
            else:
                form = ContactForm3()
                return render_to_response('statustrack/detail.html', {'form': form, 'incident': incident}, RequestContext(request))


    except Incident.DoesNotExist:
        raise Http404("Incident does not exist")
    return render(request, 'statustrack/detail.html', {'incident': incident, 'form': form})
#    return HttpResponse("<h2>Details for incident id: " + str(incident_id) + "</h2>")



def statusTrack(request,incident_id):
	if request.method == 'GET':
		form = ContactForm3(request.GET)
		if form.is_valid():
			# print("The form is valid\n\n\n\n")
			incident = Incident.objects.get(id=incident_id)
			incident.incident_status = form.cleaned_data['incident_status']
			incident.save()
			# print("A new incident is saved\n\n\n\n")
			return render_to_response('statustrack/statustrack_home.html',{'form':form},RequestContext(request))
		else:
			form=ContactForm3()
			return render_to_response('statustrack/statustrack_home.html',{'form':form},RequestContext(request))



