from classes.form_builder.departments.duk._2026.dissemination.application_builder import DisseminationApplicationBuilder
from .estimate_data import estimate_sections
from classes.form_builder.departments.duk._2026.application_estimate_builder import DUKApplicationEstimateBuilder
from ..priority import ResearchPriority


class ResearchApplicationBuilder(DisseminationApplicationBuilder, ResearchPriority):
    FORM_ID = 24

    def __init__(self):
        super().__init__()

        self.project_type = [
            "Badania ilościowe i jakościowe o charakterze cyklicznym, dotyczące widza kinowego oraz bilansu kompetencji.",
            "Badania rynkowe w sferze kinematografii.",
            "Przygotowanie analiz w zakresie organizacji i finansowania rynku kinematograficznego w Polsce, a także przedsięwzięć wspierających jego systemowy rozwój.",
            "Przygotowanie innowacyjnych przedsięwzięć o szczególnym znaczeniu dla rozwoju rynku audiowizualnego.",
            "Badania i analizy zjawiska piractwa w sferze kinematografii oraz wdrażanie przedsięwzięć, których celem jest zwalczanie piractwa i zapobieganie łamaniu praw autorskich.",
            "Inne działania realizujące cele Priorytetu V."
        ]

        estimate_builder = DUKApplicationEstimateBuilder(estimate_sections=estimate_sections)
        self.estimate_chapters = [
            estimate_builder.generate_estimate()
        ]

        self.source_of_financing_tickets = True

    def create_application_scope_of_project(self, number):
        pass

    def create_application_attachments(self, number):
        pass

    def create_application_schedule(self, number):
        pass
