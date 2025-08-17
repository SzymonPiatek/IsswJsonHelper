from classes.form_builder.duk.dissemination.application_builder import DisseminationApplicationBuilder
from classes.form_builder.duk.application_builder import DUKApplicationBuilder


class InitiativesApplicationBuilder(DisseminationApplicationBuilder):
    PRIORITY_NAME = 'II. Inicjatywy filmowe'
    PRIORITY_NUM = 2
    FORM_ID = 2597

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'initiatives'

    def create_application_basic_data(self, **kwargs):
        data = {
            'projectType': {
                'options': [
                    "Organizacja przeglądów i innych wydarzeń filmowych o charakterze lokalnym",
                    "Działalność kin studyjnych i lokalnych",
                    "Działalność klubów filmowych",
                    "Organizacja kongresów, konferencji i sympozjów, mających na celu pogłębianie i upowszechnianie wiedzy o filmie",
                    "Organizacja konkursów filmowych, wystaw oraz innych wydarzeń promujących sztukę filmową",
                    "Inne działania realizujące cele Priorytetu II"
                ]
            }
        }
        DUKApplicationBuilder.create_application_basic_data(self=self, data=data)
