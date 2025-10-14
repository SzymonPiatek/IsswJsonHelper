from classes.pisf_structure.priority import Priority
from .operation import DisseminationOperation


class DisseminationPriority(DisseminationOperation, Priority):
    def __init__(self):
        super().__init__()


class FestivalsPriority(DisseminationPriority):
    PRIORITY_NAME = 'I. Festiwale filmowe'
    PRIORITY_NUM = 1

    def __init__(self):
        super().__init__()


class InitiativesPriority(DisseminationPriority):
    PRIORITY_NAME = 'II. Inicjatywy filmowe'
    PRIORITY_NUM = 2

    def __init__(self):
        super().__init__()


class LiteraturePriority(DisseminationPriority):
    PRIORITY_NAME = 'III. Literatura i czasopisma o filmie'
    PRIORITY_NUM = 3

    def __init__(self):
        super().__init__()


class ReconstructionPriority(DisseminationPriority):
    PRIORITY_NAME = 'IV. Rekonstrukcja cyfrowa'
    PRIORITY_NUM = 4

    def __init__(self):
        super().__init__()


class ResearchPriority(DisseminationPriority):
    PRIORITY_NAME = 'V. Badania rynku audiowizualnego'
    PRIORITY_NUM = 5

    def __init__(self):
        super().__init__()


class DkfPriority(DisseminationPriority):
    PRIORITY_NAME = 'VI. Działalność klubów filmowych'
    PRIORITY_NUM = 6

    def __init__(self):
        super().__init__()
