from classes.form_builder.duk.dissemination.application_builder import DisseminationApplicationBuilder


class ReconstructionApplicationBuilder(DisseminationApplicationBuilder):
    PRIORITY_NAME = 'IV. Rekonstrukcja cyfrowa'

    def __init__(self):
        super().__init__()

        self.reconstruction_data_path = self.education_data_path / 'reconstruction'

    def generate(self):
        # Metadane wniosku
        self.create_application_metadata()

        # I. Dane podstawowe
        # II. Dane wnioskodawcy
        # III. Zakres przedsięwzięcia
        # IV. Źródła finansowania
        # V. Oświadczenia
        # VI. Załączniki
        # VII. Kosztorys przedsięwzięcia
        # VIII. Harmonogram

        self.save_output()
