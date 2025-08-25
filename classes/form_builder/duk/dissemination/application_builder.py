from classes.form_builder.duk.application_builder import DUKApplicationBuilder


class DisseminationApplicationBuilder(DUKApplicationBuilder):
    OPERATION_NAME = 'III. Upowszechnianie kultury filmowej'
    OPERATION_NUM = 3

    def __init__(self):
        super().__init__()

        self.program_data_path = self.department_data_path / 'dissemination'

    def create_application_scope_of_project(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'scope_of_the_project.json')
        self.save_part(part)
