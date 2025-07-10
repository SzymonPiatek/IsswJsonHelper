from classes.form_builder.duk.dissemination.application_builder import DisseminationApplicationBuilder


class DocumentaryDistributionApplicationBuilder(DisseminationApplicationBuilder):
    PRIORITY_NAME = 'VI. Dystrybucja filmów dokumentalnych'

    def __init__(self):
        super().__init__()

        self.documentary_data_path = self.education_data_path / 'documentary_distribution'

    def generate(self):
        self.create_application_base()

        # Metadane wniosku
        self.create_application_metadata()

        # I. Dane podstawowe
        self.create_application_basic_data(data={
            'projectType': {
                'options': [
                    "Dystrybucja kinowa pełnometrażowych filmów dokumentalnych na terenie Polski"
                ]
            }
        })

        # II. Dane wnioskodawcy
        self.create_application_applicant_data()

        # III. Zakres przedsięwzięcia

        # IV. Źródła finansowania
        self.create_application_sources_of_financing()

        # V. Oświadczenia
        self.create_application_statements()

        # VI. Załączniki

        # VII. Kosztorys przedsięwzięcia

        # VIII. Harmonogram
        self.create_application_schedule()

        self.save_output()
