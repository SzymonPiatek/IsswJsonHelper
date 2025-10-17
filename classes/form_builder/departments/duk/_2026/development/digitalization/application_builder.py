from classes.form_builder.departments.duk._2026.development.application_builder import DevelopmentApplicationBuilder
from classes.form_builder.departments.duk._2026.development.priority import DigitalizationPriority
from classes.form_builder.departments.duk.application_estimate_builder import DUKApplicationEstimateBuilder
from .estimate_data import estimate_sections


class DigitalizationApplicationBuilder(DevelopmentApplicationBuilder, DigitalizationPriority):
    FORM_ID = 27

    def __init__(self):
        super().__init__()

        self.project_type = [
            "Współfinansowanie zakupu sprzętu do projekcji cyfrowych o minimalnej rozdzielczości 2K w standardzie DCI."
        ]

        estimate_builder = DUKApplicationEstimateBuilder(estimate_sections=estimate_sections)
        self.estimate_chapters = [
            estimate_builder.generate_estimate()
        ]
