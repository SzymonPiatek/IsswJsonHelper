from classes.form_builder.departments.duk._2025.application_builder import DUKApplicationBuilder2025


class DisseminationApplicationBuilder(DUKApplicationBuilder2025):
    OPERATION_NAME = 'III. Upowszechnianie kultury filmowej'
    OPERATION_NUM = "iii"

    def __init__(self):
        super().__init__()
