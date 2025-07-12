from classes.form_builder.dpf.application_builder import DPFApplicationBuilder


class CoproductionFilmApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'VI. Produkcja koprodukcji mniejszościowych'
    PRIORITY_NUM = 6

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.department_data_path / 'coproduction_film'

    def generate(self):
        self.create_application_base()

        # Metadane wniosku
        self.create_application_metadata(task_type='Produkcja filmowa')

        # I. Dane podstawowe
        # II. Dane wnioskodawcy
        # III. Informacje
        # IV. Termin realizacji
        # V. Dane finansowe
        # VI. Dane dodatkowe
        # VII. Załączniki
        # VIII. Oświadczenia

        self.save_output()
