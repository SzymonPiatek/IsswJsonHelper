from classes.form_builder.duk.education.application_builder import EducationApplicationBuilder


class SecondarySchoolsApplicationBuilder(EducationApplicationBuilder):
    PRIORITY_NAME = 'II. Edukacja w szkołach średnich i zawodowych'
    PRIORITY_NUM = 2

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'professional_training'

    def generate(self):
        self.create_application_base()

        # Metadane wniosku
        self.create_application_metadata()

        # I. Dane podstawowe
        self.create_application_basic_data(data={
            'projectType': {
                'options': [
                    "programy edukacyjne wchodzące w skład edukacji ciągłej",
                    "kształcenie w kierunku zdobycia zawodów związanych z potrzebami współczesnego rynku audiowizualnego",
                    "inne działania realizujące cele Priorytetu II",
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
