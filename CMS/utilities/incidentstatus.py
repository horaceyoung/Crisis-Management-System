from enum import Enum

class IncidentStatus(Enum):
    # The incident has just been reported.
    NEW = 1

    # A plan to handle the incident has been constructed.
    PLANNED = 2

    # The incident work has started.
    IN_PROGRESS = 3

    # The incident has been resolved.
    RESOLVED = 4