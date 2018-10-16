from django.db import models
from django.urls import reverse


class Incident(models.Model):
    caller_name = models.CharField(max_length=50)
	mobile_number = models.CharField(max_length=8)
    incident_time = models.CharField(max_length=100)
    incident_location = models.CharField(max_length=100)
    incident_category = models.CharField(max_length=100)
    incident_description = models.CharField(max_length=400)
