from django.db import models
from django.urls import reverse


class Incident(models.Model):
    incident_time = models.CharField(max_length=100)
    incident_location = models.CharField(max_length=100)
    incident_category = models.CharField(max_length=100)
    incident_description = models.CharField(max_length=400)
    incident_status = models.BooleanField(default=False)
    incident_department = models.CharField(max_length=100, default='NULL')