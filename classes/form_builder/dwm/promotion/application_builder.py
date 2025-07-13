from classes.form_builder.dwm.application_builder import DWMApplicationBuilder


class PromotionApplicationBuilder(DWMApplicationBuilder):
    PRIORITY_NAME = 'I. Promocja polskiej twórczości filmowej za granicą'
    PRIORITY_NUM = 1

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.department_data_path / 'promotion'
