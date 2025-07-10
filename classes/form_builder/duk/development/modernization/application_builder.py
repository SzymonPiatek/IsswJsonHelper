from classes.form_builder.duk.development.application_builder import DevelopmentApplicationBuilder


class ModernizationApplicationBuilder(DevelopmentApplicationBuilder):
    PRIORITY_NAME = 'I. Modernizacja kin'

    def __init__(self):
        super().__init__()

        self.postgraduate_data_path = self.education_data_path / 'modernization'

    def generate(self):
        self.create_application_base()

        # Metadane wniosku
        self.create_application_metadata()

        # I. Dane podstawowe
        self.create_application_basic_data(data={
            'projectType': {
                'options': [
                    "Współfinansowanie zakupu i modernizacji wyposażenia do prowadzenia lub rozpoczęcia działalności kinowej, w tym sprzętu umożliwiającego odbiór filmów przez osoby ze szczególnymi potrzebami",
                    "Inne działania realizujące cele Priorytetu I"
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
