from classes.pisf_structure import Priority
from .operation import DevelopmentOperation


class DevelopmentPriority(DevelopmentOperation, Priority):
    def __init__(self):
        super().__init__()


class ModernizationPriority(DevelopmentPriority):
    PRIORITY_NAME = "I. Modernizacja kin"
    PRIORITY_NUM = 1

    def __init__(self):
        super().__init__()


class DigitalizationPriority(DevelopmentPriority):
    PRIORITY_NAME = "II. Cyfryzacja kin"
    PRIORITY_NUM = 2
