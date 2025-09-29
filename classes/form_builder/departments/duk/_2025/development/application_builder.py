from classes.form_builder.departments.duk._2025.application_builder import DUKApplicationBuilder2025


class DevelopmentApplicationBuilder(DUKApplicationBuilder2025):
    OPERATION_NAME = 'IV. Rozwój kin'
    OPERATION_NUM = "iv"

    def __init__(self):
        super().__init__()

        self.program_data_path = self.department_data_path / 'development'

    def create_application_scope_of_project(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'scope_of_the_project.json')
        self.save_part(part)
