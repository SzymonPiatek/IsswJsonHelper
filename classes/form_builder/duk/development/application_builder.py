from classes.form_builder.duk.application_builder import DUKApplicationBuilder


class DevelopmentApplicationBuilder(DUKApplicationBuilder):
    OPERATION_NAME = 'IV. Rozwój kin'
    OPERATION_NUM = 4

    def __init__(self):
        super().__init__()

        self.program_data_path = self.department_data_path / 'development'
