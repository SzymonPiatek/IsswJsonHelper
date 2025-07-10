from classes.form_builder.duk.development.application_builder import DevelopmentApplicationBuilder


class ModernizationApplicationBuilder(DevelopmentApplicationBuilder):
    PRIORITY_NAME = 'I. Modernizacja kin'

    def __init__(self):
        super().__init__()

        self.postgraduate_data_path = self.education_data_path / 'modernization'

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
