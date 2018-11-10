from .informationsender import InformationSender
from callcentre.models import Incident



class Dispatcher:

    """
    Checks if it should be sent to SCDF or Singapore Power and dispatches the reformed information via SMS

    Author: Austin Tarango
    """

    def __init__(self):
        self.messages_received = 0
        self.distro = InformationSender()
        self.singapore_power_phone = '+6583980512'
        self.SCDF_phone = '+6584149952'
        self.receiver = ""

    def notify(self, message):
        self.messages_received += 1
        incident = Incident.objects.get(pk=message.incident_id)
        self.generate_sms(incident)

    def generate_sms(self, incident):
        #Reform information to be read sequntally by importance in the SMS for emergancy responders
        sms = "Alert: "
        sms += incident.incident_category + " in or around "
        sms += incident.incident_location + ". Reported at "
        sms += str(incident.incident_time)[:16] + " "
        sms += "Details: " + str(incident.incident_description)

        #Checks if it is a Singapore Power or SCFD incident
        if incident.incident_category == "Gas Leak Control":
            self.receiver = "SP"
            self.distro.send_sms("Singapore Power " + sms, self.singapore_power_phone)

        else:
            self.receiver = "SCDF"
            self.distro.send_sms("SCDF " + sms, self.SCDF_phone)