from django.db import models
from django.urls import reverse
from utilities.incidentstatus import IncidentStatus
from utilities.incidenttype import IncidentType
from utilities.region import Region
from django.utils import timezone


CATEGORY_CHOICES = [    # Note square brackets.
    ("Emergency Ambulance", "Emergency Ambulance"), 
    ("Rescue & Evacuation", "Rescue & Evacuation"),
    ("Fire Fighting", "Fire Fighting"),
    ("Gas Leak Control", "Gas Leak Control"),        
]

class Incident(models.Model):
    caller_name = models.CharField(max_length=50, default='NULL')
    mobile_number = models.CharField(max_length=8, default='NULL')
    incident_time = models.DateTimeField(default=timezone.now)
    incident_location = models.CharField(max_length=100, default='NULL')
    incident_department = models.CharField(max_length=100, default='NULL')
    incident_region = models.CharField(max_length=100, choices=[(tag, tag.value) for tag in Region], default='NULL')
    incident_category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='NULL')
    incident_status = models.CharField(max_length=100, choices=[(tag, tag.value) for tag in IncidentStatus], default='NULL')
    incident_description = models.CharField(max_length=400, default='NULL')
