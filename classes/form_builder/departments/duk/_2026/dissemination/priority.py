from classes.pisf_structure.priority import Priority


class FestivalsPriority(Priority):
    PRIORITY_NAME = 'I. Festiwale filmowe'
    PRIORITY_NUM = 1

    def __init__(self):
        super().__init__()


class InitiativesPriority(Priority):
    PRIORITY_NAME = 'II. Inicjatywy filmowe'
    PRIORITY_NUM = 2

    def __init__(self):
        super().__init__()


class LiteraturePriority(Priority):
    PRIORITY_NAME = 'III. Literatura i czasopisma o filmie'
    PRIORITY_NUM = 3

    def __init__(self):
        super().__init__()


class ReconstructionPriority(Priority):
    PRIORITY_NAME = 'IV. Rekonstrukcja cyfrowa'
    PRIORITY_NUM = 4

    def __init__(self):
        super().__init__()


class ResearchPriority(Priority):
    PRIORITY_NAME = 'V. Badania rynku audiowizualnego'
    PRIORITY_NUM = 5

    def __init__(self):
        super().__init__()


class DkfPriority(Priority):
    PRIORITY_NAME = 'VI. Działalność dyskusyjnych klubów filmowych'
    PRIORITY_NUM = 6

    def __init__(self):
        super().__init__()
