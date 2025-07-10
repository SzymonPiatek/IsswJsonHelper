from classes.form_builder.duk.application_builder import DUKApplicationBuilder2025


class EducationApplicationBuilder2025(DUKApplicationBuilder2025):
    OPERATION_NAME = 'II. Edukacja filmowa'

    def __init__(self):
        super().__init__()

        self.education_data_path = self.duk_data_path / 'education'

    def create_application_statements(self):
        part = self.load_json(path=self.education_data_path / 'pages' / 'statements.json')
        self.save_part(part)

    def create_application_basic_data(self, data):
        part = self.load_json(path=self.education_data_path / 'pages' / 'application_basic_data.json')
        values = {
            "programNamePartTwo": self.operation_name,
            "priorityNamePartTwo": self.priority_name,
            "projectType": {
                "options": data["projectType"]["options"]
            }
        }
        final_part = self.replace_placeholders(part, values)
        self.save_part(final_part)


class PostgraduateSchoolsApplicationBuilder2025(EducationApplicationBuilder2025):
    PRIORITY_NAME = 'I. Szkoły wyższe i podyplomowe'

    def __init__(self):
        super().__init__()

        self.postgraduate_data_path = self.education_data_path / 'postgraduateSchools'

    def create_application_scope_of_project(self):
        part = self.load_json(path=self.postgraduate_data_path / 'pages' / 'scope_of_the_project.json')
        self.save_part(part)


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
        self.create_application_applicant_data()
        self.create_application_scope_of_project()
        self.create_application_sources_of_financing()
        self.create_application_statements()
        self.save_output()
