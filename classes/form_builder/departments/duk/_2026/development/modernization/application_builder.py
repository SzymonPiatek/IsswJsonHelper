from classes.form_builder.departments.duk._2026.development.application_builder import DevelopmentApplicationBuilder
from classes.form_builder.departments.duk._2026.development.priority import ModernizationPriority
from classes.form_builder.departments.duk._2026.estimate.application_estimate_builder import DUKApplicationEstimateBuilder
from .estimate_data import estimate_sections


class ModernizationApplicationBuilder(DevelopmentApplicationBuilder, ModernizationPriority):
    FORM_ID = 26

    def __init__(self):
        super().__init__()

        self.project_type = [
            "Współfinansowanie zakupu i modernizacji wyposażenia do prowadzenia lub rozpoczęcia działalności kinowej, w tym sprzętu umożliwiającego odbiór filmów przez osoby ze szczególnymi potrzebami."
        ]

        estimate_builder = DUKApplicationEstimateBuilder(estimate_sections=estimate_sections)
        self.estimate_chapters = [
            estimate_builder.generate_estimate()
        ]
