from classes.form_builder.duk.application_builder import DUKApplicationBuilder


class DisseminationApplicationBuilder(DUKApplicationBuilder):
    OPERATION_NAME = 'III. Upowszechnianie kultury filmowej'

    def __init__(self):
        super().__init__()

        self.dissemination_data_path = self.duk_data_path / 'dissemination'
