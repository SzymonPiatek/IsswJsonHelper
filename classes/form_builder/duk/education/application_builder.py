from classes.form_builder.duk.application_builder import DUKApplicationBuilder


class EducationApplicationBuilder(DUKApplicationBuilder):
    OPERATION_NAME = 'II. Edukacja filmowa'
    OPERATION_NUM = 2

    def __init__(self):
        super().__init__()

        self.program_data_path = self.department_data_path / 'education'
