from enum import Enum, auto


class IncidentType(Enum):
    EMERGENCY_AMBULANCE = "Emergency Ambulance"
    RESCUE_AND_EVACUATION = "Rescue & Evacuation"
    FIRE_FIGHTING = "Fire Fighting"
    GAS_LEAK_CONTROL = "Gas Leak Control"