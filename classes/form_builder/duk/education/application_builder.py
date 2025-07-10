from classes.form_builder.duk.application_builder import DUKApplicationBuilder


class EducationApplicationBuilder(DUKApplicationBuilder):
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


