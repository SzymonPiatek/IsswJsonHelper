from classes.form_builder.dwm.application_builder import DWMApplicationBuilder


class DWMApplicationBuilder2025(DWMApplicationBuilder):
    DEPARTMENT_NAME = 'DWM'
    OPERATION_NAME = 'V. Promocja polskiej twórczości filmowej za granicą'
    OPERATION_NUM = 5
    YEAR = 2025

    def __init__(self):
        super().__init__()
