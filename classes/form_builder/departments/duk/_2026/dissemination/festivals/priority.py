from classes.pisf_structure.priority import Priority


class FestivalsPriority(Priority):
    PRIORITY_NAME = 'I. Festiwale filmowe'
    PRIORITY_NUM = 1

    def __init__(self):
        super().__init__()
