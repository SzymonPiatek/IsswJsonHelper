from classes.form_builder.duk.application_builder import DUKApplicationBuilder


class DevelopmentApplicationBuilder(DUKApplicationBuilder):
    OPERATION_NAME = 'IV. Rozwój kin'

    def __init__(self):
        super().__init__()

        self.dissemination_data_path = self.duk_data_path / 'development'
