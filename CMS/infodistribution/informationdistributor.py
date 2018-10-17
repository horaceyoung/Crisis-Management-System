from .statusreportgenerator import StatusReportGenerator
from .socialmediaalerter import SocialMediaAlerter
from .dispatcher import Dispatcher


class InformationDistributor:
    """
    Distributes messages to the appropriate component of the subsystem
    for information distribution.
    """

    def __init__(self):
        self.observers = [Dispatcher(), SocialMediaAlerter(),
                          StatusReportGenerator(1800.0)]

    def distribute(self, message):
        """
        Distributes the given message to all observers.
        """
        for observer in self.observers:
            observer.notify(message)
