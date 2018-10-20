from .informationsender import InformationSender
from utilities.incidenttype import IncidentType
from utilities.incidentstatus import IncidentStatus
from utilities.region import Region
from callcentre.models import Incident


class Dispatcher:
    def __init__(self):
        self.messages_received = 0
        self.distro = InformationSender()
        self.singapore_power_phone = "1234567"
        self.SCDF_phone = "7654321"

    def notify(self, message):
        self.messages_received += 1
        incident = Incident.objects.get(pk=message.incident_id)
        # organise message to be fit for sms
        self.generate_sms(incident)

    def generate_sms(self, incident):
        sms = "Test sms"

        if incident.incident_category == "Gas Leak Control":
            self.distro.send_sms(sms, self.singapore_power_phone)
        else:
            self.distro.send_sms(sms, self.SCDF_phone)