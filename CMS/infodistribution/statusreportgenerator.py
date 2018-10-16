from .messageDistro import distributeMessage
from utilities.incidenttype import IncidentType
from utilities.incidentstatus import IncidentStatus
from utilities.region import Region
from callcentre.models import Incident
from threading import Timer
from datetime import datetime


class StatusReportGenerator:
    def __init__(self, interval):
        self.distro = distributeMessage()
        self.interval = interval
        self.prime_minister_address = 'lee.hsien.loong@gmail.com'
        self.prev_key_indicators = KeyIndicators()
        self.key_indicators = KeyIndicators()

        Timer(interval, self.generate_report).start()  # Schedule first report

    def notify(self, message):
        incident = Incident.objects.get(pk=message.incident_id)
        if message.incident_status == IncidentStatus.NEW:
            self.key_indicators.reported_incidents[incident.incident_category] += 1
        elif message.incident_status == IncidentStatus.RESOLVED:
            self.key_indicators.total_resolution_time +=\
                datetime.now() - incident.incident_time
            self.key_indicators.resolved_incidents += 1

    def generate_report(self):
        # Schedule next report
        Timer(self.interval, self.generate_report).start()

        title = 'Incident Status Report ' + str(datetime.now())
        report = 'Number of reported incidents of type\n'
        report += self.key_indicators.reported_incidents_by_type()
        report += self.key_indicators.ongoing_incidents() + '\n'
        report += self.key_indicators.mean_resolution_time() + '\n'
        report += self.key_indicators.trending_incident_type(self.prev_key_indicators) + '\n'
        report += self.key_indicators.trending_region(self.prev_key_indicators)

        self.distro.sendEmail(title, report, self.prime_minister_address)

        # Reset statistics
        self.prev_key_indicators = self.key_indicators
        self.key_indicators = KeyIndicators()


class KeyIndicators:
    def __init__(self):
        self.reported_incidents = {key: 0 for key in IncidentType}
        self.affected_regions = {key: 0 for key in Region}
        self.resolved_incidents = 0
        self.total_resolution_time = 0.0

    def reported_incidents_by_type(self):
        res = ''
        for tag in IncidentType:
            res += '\t- ' + tag.value + ': ' + self.key_indicators.reported_incidents[tag] + '.\n'

    def ongoing_incidents(self):
        ongoing = sum(self.reported_incidents.values()) - self.resolved_incidents
        return 'Number of incidents which are still ongoing: ' + ongoing + '.'

    def mean_resolution_time(self):
        mtr = self.total_resolution_time / self.resolved_incidents
        return 'Mean time of incident resolution: ' + str(mtr) + '.'

    def trending_incident_type(self, prev):
        increase, type = self.__largest_derivative(self.reported_incidents, prev.reported_incidents, IncidentType)
        if increase == 0:
            return 'The number of reported incidents is not increasing in any category.'
        else:
            return 'The number of reported incidents in the ' + type.value + ' category are increasing the fastest.'

    def trending_region(self, prev):
        increase, region = self.__largest_derivative(self.affected_regions, prev.affected_regions, Region)
        if increase == 0:
            return 'The number of reported incidents is not increasing in any region.'
        else:
            return 'The number of reported incidents in the ' + region.value + ' region are increasing the fastest.'

    @staticmethod
    def __largest_derivative(dict1, dict2, keys):
        best_derivative = 0
        best_key = None
        for key in keys:
            if dict2[key] - dict1[key] > best_derivative:
                best_derivative = dict2[key] - dict1[key]
                best_key = key

        return best_derivative, best_key
