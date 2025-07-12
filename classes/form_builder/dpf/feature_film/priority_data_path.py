from classes.form_builder.dpf.application_builder import DPFApplicationBuilder


class FeatureFilmApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'III. Produkcja filmów fabularnych'
    PRIORITY_NUM = 3

    def __init__(self):
        super().__init__()

        self.feature_data_path = self.department_data_path / 'feature_film'

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
