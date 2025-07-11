from classes.form_builder.dpf.application_builder import DPFApplicationBuilder


class FamilyFilmApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'VII. Produkcja filmów kina familijnego'
    PRIORITY_NUM = 7

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.department_data_path / 'family_film'

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
