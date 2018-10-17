from django.test import TestCase
from .informationdistributor import InformationDistributor
from .statusreportgenerator import StatusReportGenerator, KeyIndicators
from callcentre.models import Incident
from utilities.message import Message
from utilities.incidentstatus import IncidentStatus
from utilities.incidenttype import IncidentType
from utilities.region import Region
from datetime import datetime


class InformationDistributorTest(TestCase):
    def setUp(self):
        incident1 = Incident(incident_time=datetime.now(),
                             incident_region=Region.CS,
                             incident_category=IncidentType.GAS_LEAK_CONTROL,
                             incident_status=IncidentStatus.NEW)
        incident1.save()
        self.message = Message(incident1.id, incident1.incident_status)

    def test_message_receivement(self):
        infodist = InformationDistributor()
        infodist.distribute(self.message)

        for observer in infodist.observers:
            self.assertEqual(1, observer.messages_received, 'Component should have received exactly 1 message')


class KeyIndicatorsTest(TestCase):
    def setUp(self):
        incident1 = Incident(incident_time=datetime.now(),
                             incident_region=Region.CS,
                             incident_category=IncidentType.GAS_LEAK_CONTROL,
                             incident_status=IncidentStatus.NEW)
        incident1.save()
        message1 = Message(incident1.id, incident1.incident_status)
        print(message1.incident_status)