import utilities.IncidentStatus
from . import statusreportgenerator as srg


class InformationDistributor:
    def __init__(self):
        # Only incidents with the status NEW shall be dispatched
        self.new_incident_observers = []

        self.incident_status_observers = [srg.StatusReportGenerator]

    def register_observer(self, observer, only_new_incidents):
        if only_new_incidents:
            self.new_incident_observers.append(observer)
        else:
            self.incident_status_observers.append(observer)

    def notify_observers(self, message):
        if message.incident_status == utilities.IncidentStatus.NEW:
            for observer in self.new_incident_observers:
                observer.notify(message)

        for observer in self.incident_status_observers:
            observer.notify(message)