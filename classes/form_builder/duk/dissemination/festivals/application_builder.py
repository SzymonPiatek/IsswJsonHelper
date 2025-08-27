from classes.form_builder.duk.dissemination.application_builder import DisseminationApplicationBuilder
from classes.form_builder.duk.application_builder import DUKApplicationBuilder
from classes.form_builder.duk.dissemination.festivals.estimate_data import estimate_sections


class FestivalsApplicationBuilder(DisseminationApplicationBuilder):
    PRIORITY_NAME = 'I. Festiwale filmowe'
    PRIORITY_NUM = 1
    FORM_ID = 9184

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'festivals'
        self.estimate_sections = estimate_sections

    def create_application_basic_data(self, **kwargs):
        data = {
            'projectType': {
                'options': [
                    "Organizacja festiwali o charakterze ogólnopolskim i międzynarodowym",
                    "Inne działania realizujące cele Priorytetu I"
                ]
            }
        }
        DUKApplicationBuilder.create_application_basic_data(self=self, data=data)
