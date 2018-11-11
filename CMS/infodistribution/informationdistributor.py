from .statusreportgenerator import StatusReportGenerator
from .socialmediaalerter import SocialMediaAlerter
from .dispatcher import Dispatcher


class InformationDistributor:
    """
    Distributes messages to the appropriate component of the subsystem
    for information distribution.
    """

    def __init__(self):
        status_report_generator = StatusReportGenerator(1800.0)
        status_report_generator.schedule_generation()
        self.observers = [Dispatcher(), SocialMediaAlerter(), status_report_generator]

    def distribute(self, message):
        """
        Distributes the given message to all observers.
        """
        for observer in self.observers:
            observer.notify(message)
