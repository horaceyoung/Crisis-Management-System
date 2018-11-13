from django.db import models
from django import forms
import sys, os 
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect


sys.path.append(os.path.abspath(os.path.join('..', 'callcentre')))

from callcentre.models import Incident

class ContactForm2(forms.ModelForm):
    class Meta:
        model=Incident                   
        fields=('caller_name','mobile_number','incident_location','incident_region','incident_category','incident_type','incident_description')
