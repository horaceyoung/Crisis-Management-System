from enum import Enum


class IncidentStatus(Enum):
    # The incident has just been reported.
    NEW = "New"

    # A plan to handle the incident has been constructed.
    PLANNED = "Planned"

    # The incident work has started.
    IN_PROGRESS = "In Progress"

    # The incident has been resolved.
    RESOLVED = "Resolved"

    @staticmethod
    def from_str(label):
        for incident_status in IncidentStatus:
            if label == str(incident_status):
                return incident_status
