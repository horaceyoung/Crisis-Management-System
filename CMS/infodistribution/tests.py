from django.test import TestCase
from .informationdistributor import InformationDistributor
from .statusreportgenerator import StatusReportGenerator, KeyIndicators
from callcentre.models import Incident
from utilities.message import Message
from utilities.incidentstatus import IncidentStatus
from utilities.incidenttype import IncidentType
from utilities.region import Region
from django.utils import timezone


class InformationDistributorTest(TestCase):
    def setUp(self):
        incident1 = Incident(incident_time=timezone.now(),
                             incident_region=Region.CS,
                             incident_category=IncidentType.GAS_LEAK_CONTROL.value,
                             incident_status=IncidentStatus.NEW)
        incident1.save()
        self.message = Message(incident1.id, incident1.incident_status)

    def test_messages_received(self):
        """Tests that all observers receive the passed message."""
        infodist = InformationDistributor()
        infodist.distribute(self.message)

        for observer in infodist.observers:
            self.assertEqual(observer.messages_received, 1, 'Observers should have received exactly 1 message')


class KeyIndicatorsTest(TestCase):
    def setUp(self):
        self.prev_key_indicators = KeyIndicators()
        self.key_indicators = KeyIndicators()

        # One of each incident type was previously reported
        for incident_type in IncidentType:
            self.prev_key_indicators.reported_incidents[incident_type] = 1
        # Three of the incidents were reported in CS, one in NW
        self.prev_key_indicators.affected_regions[Region.CS] = 3
        self.prev_key_indicators.affected_regions[Region.NW] = 1

        # Six fire fighting incidents are now reported
        self.key_indicators.reported_incidents[IncidentType.FIRE_FIGHTING] = 6
        # => Fire fighting is trending

        # Two incidents are resolved
        self.key_indicators.number_of_resolved_incidents = 2
        # => Eight incidents are ongoing
        self.key_indicators.number_of_ongoing_incidents = 8

        # First one in 20 minutes
        self.key_indicators.total_resolution_time += 20.0
        # Second one in 10 minutes
        self.key_indicators.total_resolution_time += 10.0
        # => Mean resolution time is 15 minutes

        # Four of the incidents are reported in CS, two in NE
        self.key_indicators.affected_regions[Region.CS] = 4
        self.key_indicators.affected_regions[Region.NE] = 2
        # => NE is trending

    def test_reported_incidents_by_type(self):
        """Tests that the output of reported_incidents_by_type is correct."""
        expected_outputs = ['Number of reported incidents of type',
                            '\t- Fire Fighting: 6.',
                            '\t- Emergency Ambulance: 0.',
                            '\t- Rescue & Evacuation: 0.',
                            '\t- Gas Leak Control: 0.']
        actual_outputs = self.key_indicators.reported_incidents_by_type().split('\n')

        for output in expected_outputs:
            self.assertTrue(output in actual_outputs, 'Unexpected output generated for reported incidents by type.')

    def test_ongoing_incidents(self):
        """Tests that the output of ongoing_incidents is correct."""
        expected_output = 'Number of incidents which are still ongoing: 8.'
        actual_output = self.key_indicators.ongoing_incidents()
        self.assertEqual(actual_output, expected_output, 'Unexpected output generated for number of ongoing incidents.')

    def test_mean_resolution_time(self):
        """Tests that the output of mean_resolution_time is correct."""
        expected_output = 'Mean time of incident resolution: 15.0 minutes.'
        actual_output = self.key_indicators.mean_resolution_time()
        self.assertEqual(actual_output, expected_output, 'Unexpected output generated for mean resolution time.')

    def trending_incident_type(self):
        """Tests that the output of trending_incident_type is correct."""
        expected_output = 'The number of reported incidents in the Fire Fighting category are increasing the fastest.'
        actual_output = self.key_indicators.trending_incident_type()
        self.assertEqual(actual_output, expected_output, 'Unexpected output generated for trending incident type.')

    def trending_region(self):
        """Tests that the output of trending_region is correct."""
        expected_output = 'The number of reported incidents in the North East region are increasing the fastest.'
        actual_output = self.key_indicators.trending_region()
        self.assertEqual(actual_output, expected_output, 'Unexpected output generated for trending region.')


class StatusReportGeneratorTest(TestCase):
    def setUp(self):
        self.incident_type = IncidentType.GAS_LEAK_CONTROL
        self.region = Region.CS
        incident1 = Incident(incident_time=timezone.now(),
                             incident_region=self.region,
                             incident_category=self.incident_type.value,
                             incident_status=IncidentStatus.NEW)
        incident1.save()
        self.message_new = Message(incident1.id, incident1.incident_status)
        self.message_resolved = Message(incident1.id, IncidentStatus.RESOLVED)

    def test_notify(self):
        """Tests that the correct statistics are updated on notification."""
        generator = StatusReportGenerator(1800)

        generator.notify(self.message_new)
        for key in IncidentType:
            if key == self.incident_type:
                self.assertEqual(generator.key_indicators.reported_incidents[key], 1,
                                 'Incidents of reported type was not updated.')
            else:
                self.assertEqual(generator.key_indicators.reported_incidents[key], 0,
                                 'Incident of incorrect type was updated.')
        for key in Region:
            if key == self.region:
                self.assertEqual(generator.key_indicators.affected_regions[key], 1,
                                 'Incidents in reported region was not updated.')
            else:
                self.assertEqual(generator.key_indicators.affected_regions[key], 0,
                                 'Incidents in incorrect region was updated.')
        self.assertEqual(generator.key_indicators.number_of_resolved_incidents, 0,
                         'Resolved incidents was incorrectly updated.')
        self.assertEqual(generator.key_indicators.total_resolution_time, 0.0,
                         'Resolution time was incorrectly updated.')

        generator.notify(self.message_resolved)
        self.assertEqual(generator.key_indicators.number_of_resolved_incidents, 1,
                         'Resolved incidents was not updated.')
        self.assertGreater(generator.key_indicators.total_resolution_time, 0.0,
                           'Resolution time was not updated.')

    def test_key_indicator_reset(self):
        """Tests whether KeyIndicator objects are reset correctly after report generation."""
        generator = StatusReportGenerator(1800)
        current_indicators = generator.key_indicators
        generator.notify(self.message_new)
        generator.generate_report()

        self.assertEqual(generator.prev_key_indicators, current_indicators,
                         'Previous key indicators were not updated correctly upon status report generation.')

        self.assertEqual(generator.key_indicators.reported_incidents[self.incident_type], 0,
                         'Current key indicators were not reset correctly upon status report generation.')
        self.assertEqual(generator.key_indicators.affected_regions[self.region], 0,
                         'Current key indicators were not reset correctly upon status report generation.')

    def test_status_report_generation(self):
        """Tests that a status report has been generated and that its length is correct."""
        keeper = StatusReportKeeper()
        generator = StatusReportGenerator(1800)
        generator.distributor = keeper
        generator.generate_report()
        report = keeper.report
        self.assertNotEquals(report, '' 'No status report was generated.')

        # 4 incident types, 2 other key indicators, 2 trends
        number_of_lines = 4 + 2 + 2
        self.assertEqual(report.count('\n'), number_of_lines, 'The generated status report has incorrect length.')


class StatusReportKeeper:
    def __init__(self):
        self.report = ''

    def send_email(self, _, report, __):
        self.report = report
