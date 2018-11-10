from django.db import models
from django import forms
from callcentre.models import Incident
import sys
import os

sys.path.append(os.path.abspath(os.path.join('..', 'callcentre')))


class ContactForm2(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ('caller_name', 'mobile_number', 'incident_location',
                  'incident_region', 'incident_type', 'incident_category')
