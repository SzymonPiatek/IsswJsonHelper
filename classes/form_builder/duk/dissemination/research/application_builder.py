from classes.form_builder.duk.dissemination.application_builder import DisseminationApplicationBuilder
from classes.form_builder.duk.application_builder import DUKApplicationBuilder


class ResearchApplicationBuilder(DisseminationApplicationBuilder):
    PRIORITY_NAME = 'V. Badania rynku audiowizualnego'
    PRIORITY_NUM = 5
    FORM_ID = 2600

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'research'

    def create_application_basic_data(self, **kwargs):
        data = {
            'projectType': {
                'options': [
                    "Badania ilościowe i jakościowe o charakterze cyklicznym, dotyczące widza kinowego oraz bilansu kompetencji",
                    "Badania rynkowe w sferze kinematografii",
                    "Przygotowanie analiz w zakresie organizacji i finansowania rynku kinematograficznego w Polsce, a także przedsięwzięć wspierających jego systemowy rozwój",
                    "Przygotowanie innowacyjnych przedsięwzięć o szczególnym znaczeniu dla rozwoju rynku audiowizualnego",
                    "Badania i analizy zjawiska piractwa w sferze kinematografii oraz wdrażanie przedsięwzięć, których celem jest zwalczanie piractwa i zapobieganie łamaniu praw autorskich",
                    "Inne działania realizujące cele Priorytetu V"
                ]
            }
        }
        DUKApplicationBuilder.create_application_basic_data(self=self, data=data)
