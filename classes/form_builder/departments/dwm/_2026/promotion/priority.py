from classes.form_builder.pisf_structure.priority import Priority


class PromotionPriority(Priority):
    PRIORITY_NAME = 'I. Promocja polskiej twórczości filmowej za granicą'
    PRIORITY_NUM = 1

    def __init__(self):
        super().__init__()
