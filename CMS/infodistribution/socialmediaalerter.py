from .informationsender import InformationSender
from callcentre.models import Incident


class SocialMediaAlerter:
    def __init__(self):
        self.messages_received = 0
        self.distro = InformationSender()
        self.phone_numbers = ['+6583980512', '+6583980512']

    def notify(self, message):
        self.messages_received += 1
        incident = Incident.objects.get(pk=message.incident_id)

        alert = "Alert: " + incident.incident_type
        alert += " in " + incident.incident_region
        alert += " at " + str(incident.incident_time)

        self.distro.send_tweet(alert)
        for number in self.phone_numbers:
            self.distro.send_sms(alert, number)
