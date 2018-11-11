from .informationsender import InformationSender
from callcentre.models import Incident
from utilities.region import Region
from utilities.incidentstatus import IncidentStatus




class SocialMediaAlerter:
    def __init__(self):
        self.sentTo = ''
        self.messages_received = 0
        self.distro = InformationSender()
        self.phone_numbers = {Region.SW:['+6583980512'], Region.NW:['+6584149952'],Region.CS:['+6583980512','+6584149952'],Region.SE:['+6584149952'],Region.NE:['+6583980512','+6584149952']}

    def notify(self, message):
        self.messages_received += 1
        incident = Incident.objects.get(pk=message.incident_id)
        region = Region.from_str(incident.incident_region)
        status = IncidentStatus.from_str(incident.incident_status)

        if status == IncidentStatus.NEW:
            alert = "Alert: " + incident.incident_type
            alert += " in " + region.value
            alert += " at " + str(incident.incident_time)[:16]

            self.distro.send_tweet(alert)

            if (region in list(self.phone_numbers.keys())):
                numberList = list(self.phone_numbers[region])
                self.sentTo = region
                for number in numberList:
                 self.distro.send_sms(alert, number)
            else:
                print("No Region")

        elif status == IncidentStatus.IN_PROGRESS:
            alert = "Emergency services have arrived. " + incident.incident_type
            alert += " in " + region.value
            alert += " at " + str(incident.incident_time)[:16]

            self.distro.send_tweet(alert)

            if (region in list(self.phone_numbers.keys())):
                numberList = list(self.phone_numbers[region])
                self.sentTo = region
                for number in numberList:
                 self.distro.send_sms(alert, number)
            else:
                print("No Region")
        elif status == IncidentStatus.RESOLVED:
            alert = incident.incident_type + " has been resolved."
            alert += " in " + region.value
            alert += " at " + str(incident.incident_time)[:16]

            self.distro.send_tweet(alert)

            if (region in list(self.phone_numbers.keys())):
                numberList = list(self.phone_numbers[region])
                self.sentTo = region
                for number in numberList:
                    self.distro.send_sms(alert, number)
            else:
                print("No Region")
