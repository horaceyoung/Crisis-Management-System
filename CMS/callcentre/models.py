from django.db import models
from django.urls import reverse
from utilities.incidentstatus import IncidentStatus
from utilities.incidenttype import IncidentType
from utilities.region import Region


class Incident(models.Model):
    incident_time = models.DateTimeField()
    incident_location = models.CharField(max_length=100)
    incident_region = models.CharField(max_length=100, choices=[(tag, tag.value) for tag in Region])
    incident_category = models.CharField(max_length=100, choices=[(tag, tag.value) for tag in IncidentType])
    incident_status = models.CharField(max_length=100, choices=[(tag, tag.value) for tag in IncidentStatus])
    incident_description = models.CharField(max_length=400)