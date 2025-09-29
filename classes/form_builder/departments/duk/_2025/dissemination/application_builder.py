from classes.form_builder.departments.duk.application_builder import DUKApplicationBuilder


class DisseminationApplicationBuilder(DUKApplicationBuilder):
    OPERATION_NAME = 'III. Upowszechnianie kultury filmowej'
    OPERATION_NUM = "iii"

    def __init__(self):
        super().__init__()
