from classes.form_builder.departments.duk._2026.dissemination.application_builder import DisseminationApplicationBuilder
from classes.form_builder.departments.duk._2026.dissemination.priority import DkfPriority
from .estimate_data import estimate_sections
from classes.form_builder.departments.duk._2026.estimate.application_estimate_builder import DUKApplicationEstimateBuilder


class DkfApplicationBuilder(DisseminationApplicationBuilder, DkfPriority):
    FORM_ID = 25

    def __init__(self):
        super().__init__()

        # Variables
        self.project_type = [
            "Działalność dyskusyjnych klubów filmowych."
        ]
        self.source_of_financing_tickets = True
        self.is_dkf = True

        # Estimate
        estimate_builder = DUKApplicationEstimateBuilder(estimate_sections=estimate_sections)
        self.estimate_chapters = [
            estimate_builder.generate_estimate()
        ]
