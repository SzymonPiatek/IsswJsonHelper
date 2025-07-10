from classes.form_builder.duk.education.application_builder import EducationApplicationBuilder


class ProfessionalTrainingApplicationBuilder(EducationApplicationBuilder):
    PRIORITY_NAME = 'III. Edukacja i kształcenie profesjonalne'

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
                    "kształcenie zawodowe i podnoszenie kompetencji poprzez organizację szkoleń zawodowych, warsztatów, kursów i innych przedsięwzięć lub programów długoterminowych",
                    "edukacja dotycząca historii filmu polskiego i światowego, estetyki filmowej i środków wyrazu oraz społecznych funkcji filmu",
                    "projekty edukacyjne dla przedstawicieli wszystkich grup zawodowych, pracujących na potrzeby polskiej kinematografii",
                    "organizacja kursów nauki języków obcych dla przedstawicieli zawodów filmowych",
                    "inne działania realizujące cele Priorytetu V",
                    "inne działania realizujące cele Priorytetu III",
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
