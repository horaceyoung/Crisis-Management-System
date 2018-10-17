from .messageDistro import distributeMessage
from utilities.incidenttype import IncidentType
from utilities.incidentstatus import IncidentStatus
from utilities.region import Region
from callcentre.models import Incident

class Dispatcher:
    def __init__(self):
        self.distro = distributeMessage()
        self.prev_key_indicators = KeyIndicators()
        self.key_indicators = KeyIndicators()
        self.singapore_power_phone = "1234567"
        self.SCDF_phone = "7654321"
    
    def notify(self, message):
        incident = Incident.objects.get(pk=message.incident_id)
        # organise message to be fit for sms
        self.distro.sendSMS(message)

    def generatre_SMS(self):
    sms = "Test sms"

    if self.key_indicators.reported_incidents_by_type() == "Gas Leak Control"
        self.distro.sendSMS(sms,singapore_power_phone)
    elif
        self.distro.sendSMS(sms,SCDF_phone)

