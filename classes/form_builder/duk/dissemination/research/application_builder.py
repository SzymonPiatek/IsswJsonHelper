from classes.form_builder.duk.dissemination.application_builder import DisseminationApplicationBuilder


class ResearchApplicationBuilder(DisseminationApplicationBuilder):
    PRIORITY_NAME = 'V. Badania rynku audiowizualnego'

    def __init__(self):
        super().__init__()

        self.postgraduate_data_path = self.education_data_path / 'research'

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
