from classes.form_builder.duk.application_builder import DUKApplicationBuilder


class EducationApplicationBuilder(DUKApplicationBuilder):
    OPERATION_NAME = 'II. Edukacja filmowa'

    def __init__(self):
        super().__init__()

        self.education_data_path = self.duk_data_path / 'education'
