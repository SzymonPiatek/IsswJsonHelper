from classes.form_builder.dpf.application_builder import DPFApplicationBuilder


class FamilyFilmApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'VII. Produkcja filmów kina familijnego'
    PRIORITY_NUM = 7

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.department_data_path / 'family_film'
