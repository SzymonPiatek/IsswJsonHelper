from classes.pisf_structure.priority import Priority
from .operation import EducationOperation


class EducationPriority(EducationOperation, Priority):
    def __init__(self):
        super().__init__()


class HigherSchoolsPriority(EducationPriority):
    PRIORITY_NAME = "I. Szkoły wyższe"
    PRIORITY_NUM = 1

    def __init__(self):
        super().__init__()


class SecondarySchoolsPriority(EducationPriority):
    PRIORITY_NAME = "II. Szkoły średnie i zawodowe"
    PRIORITY_NUM = 2

    def __init__(self):
        super().__init__()


class ProfessionalTrainingPriority(EducationPriority):
    PRIORITY_NAME = "III. Edukacja profesjonalna i doskonalenie zawodowe"
    PRIORITY_NUM = 3

    def __init__(self):
        super().__init__()


class AudiencePriority(EducationPriority):
    PRIORITY_NAME = "IV. Edukacja widowni filmowej"
    PRIORITY_NUM = 4

    def __init__(self):
        super().__init__()
