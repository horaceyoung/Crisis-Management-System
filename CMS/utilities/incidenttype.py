from enum import Enum


class IncidentType(Enum):
    EMERGENCY_AMBULANCE = "Emergency Ambulance"
    RESCUE_AND_EVACUATION = "Rescue & Evacuation"
    FIRE_FIGHTING = "Fire Fighting"
    GAS_LEAK_CONTROL = "Gas Leak Control"

    @staticmethod
    def from_str(label):
        for incident_type in IncidentType:
            if label == str(incident_type.value):
                return incident_type
