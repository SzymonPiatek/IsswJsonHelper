from classes.form_builder.dpf.application_builder import DPFApplicationBuilder


class ScreenplayScholarshipApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'I. Stypendia scenariuszowe'

    def __init__(self):
        super().__init__()

        self.screenplay_data_path = self.dpf_data_path / 'screenplay_scholarship'

    def generate(self):
        # Metadane wniosku
        self.create_application_metadata(task_type='Stypendium scenariuszowe')

        # I. Dane podstawowe
        # II. Dane wnioskodawcy
        # III. Informacje
        # IV. Termin realizacji
        # V. Dane finansowe
        # VI. Dane dodatkowe
        # VII. Załączniki
        # VIII. Oświadczenia

        self.save_output()
