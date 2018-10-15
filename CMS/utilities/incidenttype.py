from enum import Enum, auto


class IncidentType(Enum):
    EMERGENCY_AMBULANCE = auto()
    RESCUE_AND_EVACUATION = auto()
    FIRE_FIGHTING = auto()
    GAS_LEAK_CONTROL = auto()