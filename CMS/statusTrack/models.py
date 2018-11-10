from django.db import models
from django import forms
import sys, os


sys.path.append(os.path.abspath(os.path.join('..', 'callcentre')))

from callcentre.models import Incident

class ContactForm3(forms.ModelForm):
    class Meta:
        model=Incident
        fields=('incident_status',)


