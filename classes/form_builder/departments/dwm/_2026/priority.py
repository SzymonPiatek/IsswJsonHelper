from classes.pisf_structure.priority import Priority


class PromotionPriority(Priority):
    PRIORITY_NAME = 'I. Promocja polskiej twórczości filmowej za granicą'
    PRIORITY_NUM = 1

    def __init__(self):
        super().__init__()


class ForeignScholarshipPriority(Priority):
    PRIORITY_NAME = 'II. Stypendia zagraniczne'
    PRIORITY_NUM = 2

    def __init__(self):
        super().__init__()
