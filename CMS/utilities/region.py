from enum import Enum


class Region(Enum):
    SW = "South West"
    NW = "North West"
    CS = "Central Singapore"
    SE = "South East"
    NE = "North East"

    @staticmethod
    def from_str(label):
        for region in Region:
            if label == str(region):
                return region
