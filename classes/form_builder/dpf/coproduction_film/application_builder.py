from classes.form_builder.dpf.application_builder import DPFApplicationBuilder


class CoproductionFilmApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'VI. Produkcja koprodukcji mniejszościowych'
    PRIORITY_NUM = 6

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.department_data_path / 'coproduction_film'
