from django.db import models
from django.urls import reverse
from utilities.incidentstatus import IncidentStatus
from utilities.incidenttype import IncidentType
from utilities.region import Region
from django.utils import timezone

REGION_CHOICES = [
    ("North West","North West"),
    ("Central Singapore","Central Singapore"),
    ("South East","South East"),
    ("North East","North East"),
]
CATEGORY_CHOICES = [    # Note square brackets.
    ("Emergency Ambulance", "Emergency Ambulance"), 
    ("Rescue and Evacuation", "Rescue and Evacuation"),
    ("Fire Fighting", "Fire Fighting"),
    ("Gas Leak Control", "Gas Leak Control"),        
]

TYPE_CHOICES = [
    ("--------Emergency Situations--------", "--------Emergency Situations--------"),
    ("----Natural Hazards----", "----Natural Hazards----"),
    ("Fire", "Fire"),
    ("Haze", "Haze"),
    ("Tsunami", "Tsunami"),
    ("Typhoon", "Typhoon"),
    ("Earthquake", "Earthquake"),
    ("Earthquake Aftershocks", "Earthquake Aftershocks"),
    ("----Epidemic----", "----Epidemic----"),
    ("Dengue", "Dengue"),
    ("HIV/AIDS", "HIV/AIDS"),
    ("Bird-flu", "Bird-flu"),
    ("Zika", "Zika"),
    ("----Traffic Accidents----","----Traffic Accidents----"),
    ("Single Car Accidents","Single Car Accidents"),
    ("Two Car Collisions","Two Car Collisions"),
    ("Multiple Vehicle Pile-up","Multiple Vehicle Pile-up"),
    ("----Incidents within Crowded Areas----", "----Incidents within Crowded Areas----"),
    ("Terrorist Attacks","Terrorist Attacks"),
    ("Mass Shooting","Mass Shooting"),
    ("Other Useful Information", "Other Useful Information"),
    ("Weather", "Weather"),
    ("Civil Defense Shelters", "Civil Defense Shelters"),
]

STATUS_UPDATE = [
    ("New", "New"),
    ("Planned", "Planned"),
    ("In Progress", "In Progress"),
    ("Resolved", "Resolved"),
]

class Incident(models.Model):
    caller_name = models.CharField(max_length=50, default='NULL',blank=True)
    mobile_number = models.CharField(max_length=8, default='NULL',blank=True)
    incident_time = models.DateTimeField(default=timezone.now)
    incident_location = models.CharField(max_length=100, default='NULL',blank=True)
    incident_department = models.CharField(max_length=100, default='NULL')
    incident_region = models.CharField(max_length=100, default='NULL')
    incident_category = models.CharField(max_length=100, default='NULL')
    incident_type = models.CharField(max_length=100, default='NULL')
    incident_status = models.CharField(max_length=100, choices=STATUS_UPDATE, default='New')
#   incident_status = models.CharField(max_length=100, choices=[(tag, tag.value) for tag in IncidentStatus], default='New')
    incident_description = models.CharField(max_length=200, default='NULL',blank=True)


