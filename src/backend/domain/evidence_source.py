from enum import Enum


class EvidenceSource(str, Enum):
    """
    Represents where a piece of evidence originated.
    """

    CITIZEN = "citizen"
    INSPECTOR = "inspector"
    DRONE = "drone"
    SATELLITE = "satellite"
    SYSTEM = "system"