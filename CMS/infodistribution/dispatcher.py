from .messageDistro import distributeMessage
from utilities.incidenttype import IncidentType
from utilities.incidentstatus import IncidentStatus
from utilities.region import Region
from callcentre.models import Incident

class Dispatcher:
    def __init__(self):
        self.distro = distributeMessage()
        self.singapore_power_phone = "1234567"
        self.SCDF_phone = "7654321"
        self.sms = "test sms"
    
    def notify(self, message):
        incident = Incident.objects.get(pk=message.incident_id)
        if IncidentType == "Gas Leak Control":
            self.distro.sendSMS(self.sms, self.singapore_power_phone)
        else:
            self.distro.sendSMS(self.sms, self.SCDF_phone)



