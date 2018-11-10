class Message:
    """
    Message to be sent when an incident is created or its status is updated.

    Author: Emil Luusua
    """
    def __init__(self, id, status):
        self.incident_id = id
        self.incident_status = status