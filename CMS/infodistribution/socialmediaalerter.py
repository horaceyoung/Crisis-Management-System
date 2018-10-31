from .informationsender import InformationSender
from callcentre.models import Incident


class SocialMediaAlerter:
    def __init__(self):
        self.messages_received = 0
        self.distro = InformationSender()
        self.phone_numbers = ['+6583980512', '+6583980512']

    def notify(self, message):
        self.messages_received += 1
<<<<<<< HEAD
        alert = "Alert: " + Incident.incident_type
        alert += " in " + Incident.incident_region
        alert += " at " + Incident.incident_time
=======
        alert = "Alert: " + str(Incident.incident_type)
        alert += " in " + str(Incident.incident_region)
        alert += " at " + str(Incident.incident_time)
>>>>>>> master
        self.distro.send_tweet(alert)
        for number in self.phone_numbers:
            self.distro.send_sms(alert, number)
