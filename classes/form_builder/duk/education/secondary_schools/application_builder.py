from classes.form_builder.duk.education.application_builder import EducationApplicationBuilder


class SecondarySchoolsApplicationBuilder(EducationApplicationBuilder):
    PRIORITY_NAME = 'II. Edukacja w szkołach średnich i zawodowych'

    def __init__(self):
        super().__init__()

        self.postgraduate_data_path = self.education_data_path / 'professional_training'

    def generate(self):
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
        # V. Oświadczenia
        # VI. Załączniki
        # VII. Kosztorys przedsięwzięcia
        # VIII. Harmonogram

        self.save_output()
