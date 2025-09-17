from classes.form_builder.dwm.application_builder import DWMApplicationBuilder


class DWMApplicationBuilder2026(DWMApplicationBuilder):
    DEPARTMENT_NAME = 'DWM'
    OPERATION_NAME = 'V. Promocja polskiej twórczości filmowej za granicą'
    OPERATION_NUM = 5
    YEAR = 2026

    def __init__(self):
        super().__init__()
