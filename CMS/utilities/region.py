from enum import Enum


class Region(Enum):
    """
    Enum for the different reqions that an incident can occur in.

    Author: Emil Luusua
    """
    SW = "South West"
    NW = "North West"
    CS = "Central Singapore"
    SE = "South East"
    NE = "North East"

    @staticmethod
    def from_str(label):
        for region in Region:
            if label == region.value:
                return region
