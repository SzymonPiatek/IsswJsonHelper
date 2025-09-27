from classes.pisf_structure.priority import Priority


class ForeignScholarshipPriority(Priority):
    PRIORITY_NAME = 'II. Stypendia zagraniczne'
    PRIORITY_NUM = 2

    def __init__(self):
        super().__init__()
