from .statusreportgenerator import StatusReportGenerator
from .socialmediaalerter import SocialMediaAlerter
from .dispatcher import Dispatcher

class InformationDistributor:
    """
    Distributes messages to the appropriate component of the subsystem
    for information distribution.

    Implemented using the Singleton pattern, only instantiating a single object.

    Author: Emil Luusua
    """

    instance = None

    @staticmethod
    def get_instance():
        """
        Method used to access the single instantiated InformationDistributor.
        """
        if InformationDistributor.instance is None:
            InformationDistributor()
        return InformationDistributor.instance

    def __init__(self):
        if InformationDistributor.instance is not None:
            raise Exception('Singleton class instantiated multiple times.')
        else:
            InformationDistributor.instance = self

        status_report_generator = StatusReportGenerator(1800.0)
        status_report_generator.schedule_generation()
        self.observers = [Dispatcher(), SocialMediaAlerter(), status_report_generator]

    def distribute(self, message):
        """
        Distributes the given message to all observers.
        """
        for observer in self.observers:
            observer.notify(message)
