from classes.form_builder.departments.duk._2026.dissemination.application_builder import DisseminationApplicationBuilder
from classes.form_builder.departments.duk._2026.dissemination.priority import DkfPriority
from .estimate_data import estimate_sections
from classes.form_builder.departments.duk._2026.application_estimate_builder import DUKApplicationEstimateBuilder


class DkfApplicationBuilder(DisseminationApplicationBuilder, DkfPriority):
    FORM_ID = 25

    def __init__(self):
        super().__init__()

        self.project_type = [
            "Działalność dyskusyjnych klubów filmowych."
        ]

        estimate_builder = DUKApplicationEstimateBuilder(estimate_sections=estimate_sections)
        self.estimate_chapters = [
            estimate_builder.generate_estimate()
        ]

        self.source_of_financing_tickets = True
