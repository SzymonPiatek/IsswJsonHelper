from classes.form_builder.duk.application_builder import DUKApplicationBuilder2025


class EducationApplicationBuilder2025(DUKApplicationBuilder2025):
    OPERATION_NAME = 'II. Edukacja filmowa'

class PostgraduateSchoolsApplicationBuilder2025(EducationApplicationBuilder2025):
    PRIORITY_NAME = 'I. Szkoły wyższe i podyplomowe'

class PostgraduateSchoolsApplicationBuilder2025Session01(PostgraduateSchoolsApplicationBuilder2025):
    SESSION = 'I'

    def generate(self):
        self.create_application_base()
        self.create_application_metadata()
        self.create_application_basic_data(data={
            'projectType': {
                'options': [
                    "programy edukacyjne wchodzące w skład edukacji ciągłej",
                    "realizacja szkolnych i pozaszkolnych filmów krótko- i średniometrażowych",
                    "kształcenie zawodowe i podnoszenie kompetencji poprzez organizację studiów podyplomowych",
                    "inne działania realizujące cele Priorytetu I"
                ]
            }
        })
        self.save_output()
