from classes.form_builder.duk.education.application_builder import EducationApplicationBuilder
from classes.form_builder.duk.application_builder import DUKApplicationBuilder


class SecondarySchoolsApplicationBuilder(EducationApplicationBuilder):
    PRIORITY_NAME = 'II. Edukacja w szkołach średnich i zawodowych'
    PRIORITY_NUM = 2
    FORM_ID = 9181

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'professional_training'

    def create_application_basic_data(self, data: dict):
        data = {
            'projectType': {
                'options': [
                    "programy edukacyjne wchodzące w skład edukacji ciągłej",
                    "kształcenie w kierunku zdobycia zawodów związanych z potrzebami współczesnego rynku audiowizualnego",
                    "inne działania realizujące cele Priorytetu II",
                ]
            }
        }
        DUKApplicationBuilder.create_application_basic_data(self=self, data=data)
