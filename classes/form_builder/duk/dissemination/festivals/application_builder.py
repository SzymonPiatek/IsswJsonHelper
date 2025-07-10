from classes.form_builder.duk.dissemination.application_builder import DisseminationApplicationBuilder


class FestivalsApplicationBuilder(DisseminationApplicationBuilder):
    PRIORITY_NAME = 'I. Festiwale filmowe'

    def __init__(self):
        super().__init__()

        self.festivals_data_path = self.education_data_path / 'festivals'

    def generate(self):
        self.create_application_base()

        # Metadane wniosku
        self.create_application_metadata()

        # I. Dane podstawowe
        self.create_application_basic_data(data={
            'projectType': {
                'options': [
                    "Organizacja festiwali o charakterze ogólnopolskim i międzynarodowym",
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
        self.create_application_attachments()

        # VII. Kosztorys przedsięwzięcia

        # VIII. Harmonogram
        self.create_application_schedule()

        self.save_output()
