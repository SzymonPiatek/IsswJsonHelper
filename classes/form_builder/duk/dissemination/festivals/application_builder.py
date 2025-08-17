from classes.form_builder.duk.dissemination.application_builder import DisseminationApplicationBuilder
from classes.form_builder.duk.application_builder import DUKApplicationBuilder


class FestivalsApplicationBuilder(DisseminationApplicationBuilder):
    PRIORITY_NAME = 'I. Festiwale filmowe'
    PRIORITY_NUM = 1
    FORM_ID = 2596

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'festivals'

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
