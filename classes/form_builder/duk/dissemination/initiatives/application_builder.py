from classes.form_builder.duk.dissemination.application_builder import DisseminationApplicationBuilder


class InitiativesApplicationBuilder(DisseminationApplicationBuilder):
    PRIORITY_NAME = 'II. Inicjatywy filmowe'
    PRIORITY_NUM = 2

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'initiatives'

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
                    "Organizacja przeglądów i innych wydarzeń filmowych o charakterze lokalnym",
                    "Działalność kin studyjnych i lokalnych",
                    "Działalność klubów filmowych",
                    "Organizacja kongresów, konferencji i sympozjów, mających na celu pogłębianie i upowszechnianie wiedzy o filmie",
                    "Organizacja konkursów filmowych, wystaw oraz innych wydarzeń promujących sztukę filmową",
                    "Inne działania realizujące cele Priorytetu II"
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
