from classes.form_builder.duk.education.application_builder import EducationApplicationBuilder
from classes.form_builder.duk.application_builder import DUKApplicationBuilder


class PostgraduateSchoolsApplicationBuilder(EducationApplicationBuilder):
    PRIORITY_NAME = 'I. Szkoły wyższe i podyplomowe'
    PRIORITY_NUM = 1

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'postgraduate_schools'

    def create_application_basic_data(self, **kwargs):
        data = {
            'projectType': {
                'options': [
                    "programy edukacyjne wchodzące w skład edukacji ciągłej",
                    "realizacja szkolnych i pozaszkolnych filmów krótko- i średniometrażowych",
                    "kształcenie zawodowe i podnoszenie kompetencji poprzez organizację studiów podyplomowych",
                    "inne działania realizujące cele Priorytetu I"
                ]
            }
        }
        DUKApplicationBuilder.create_application_basic_data(self=self, data=data)
