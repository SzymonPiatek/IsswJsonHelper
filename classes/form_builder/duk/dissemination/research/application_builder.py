from classes.form_builder.duk.dissemination.application_builder import DisseminationApplicationBuilder


class ResearchApplicationBuilder(DisseminationApplicationBuilder):
    PRIORITY_NAME = 'V. Badania rynku audiowizualnego'
    PRIORITY_NUM = 5

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'research'

    def create_application_scope_of_project(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'scope_of_the_project.json')
        self.save_part(part)

    def generate(self):
        self.create_application_base()

        # Metadane wniosku
        self.create_application_metadata()

        # I. Dane podstawowe
        self.create_application_basic_data(data={
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
        })

        # II. Dane wnioskodawcy
        self.create_application_applicant_data()

        # III. Zakres przedsięwzięcia
        self.create_application_scope_of_project()

        # IV. Źródła finansowania
        self.create_application_sources_of_financing()

        # V. Oświadczenia
        self.create_application_statements()

        # VI. Załączniki
        self.create_application_attachments()

        # VII. Kosztorys przedsięwzięcia
        self.create_application_project_costs()

        # VIII. Harmonogram
        self.create_application_schedule()

        self.save_output()
