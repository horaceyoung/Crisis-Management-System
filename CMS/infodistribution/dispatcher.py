from .informationsender import InformationSender
from callcentre.models import Incident


class Dispatcher:
    def __init__(self):
        self.messages_received = 0
        self.distro = InformationSender()
        self.singapore_power_phone = '+6583980512'
        self.SCDF_phone = '+6583980512'

    def notify(self, message):
        self.messages_received += 1
        incident = Incident.objects.get(pk=message.incident_id)
        self.generate_sms(incident)

    def generate_sms(self, incident):
        sms = "Alert: "
        sms += str(Incident.incident_type) + " in or around "
        sms += str(Incident.incident_location) + ". Reported at "
        sms += str(Incident.incident_time) + "."
        sms += "Details: " + str(Incident.incident_description)
        if incident.incident_category == "Gas Leak Control":
            self.distro.send_sms("Singapore Power " + sms, self.singapore_power_phone)
        else:
            self.distro.send_sms("SCDF " + sms, self.SCDF_phone)