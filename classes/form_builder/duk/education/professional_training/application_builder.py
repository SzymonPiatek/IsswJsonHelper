from classes.form_builder.duk.education.application_builder import EducationApplicationBuilder
from classes.form_builder.duk.application_builder import DUKApplicationBuilder


class ProfessionalTrainingApplicationBuilder(EducationApplicationBuilder):
    PRIORITY_NAME = 'III. Edukacja i kształcenie profesjonalne'
    PRIORITY_NUM = 3
    FORM_ID = 2594

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'professional_training'

    def create_application_basic_data(self, **kwargs):
        data = {
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
        }
        DUKApplicationBuilder.create_application_basic_data(self=self, data=data)
