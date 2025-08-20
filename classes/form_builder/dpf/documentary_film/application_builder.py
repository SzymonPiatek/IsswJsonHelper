from classes.form_builder.dpf.application_builder import DPFApplicationBuilder


class DocumentaryFilmApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'IV. Produkcja filmów dokumentalnych'
    PRIORITY_NUM = 4
    FORM_ID = 9197

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.department_data_path / 'documentary_film'
