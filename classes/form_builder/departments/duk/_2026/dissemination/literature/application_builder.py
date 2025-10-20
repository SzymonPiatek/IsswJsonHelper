from classes.form_builder.departments.duk._2026.dissemination.application_builder import DisseminationApplicationBuilder
from .estimate_data import estimate_sections
from classes.form_builder.departments.duk._2026.estimate.application_estimate_builder import DUKApplicationEstimateBuilder
from ..priority import LiteraturePriority


class LiteratureApplicationBuilder(DisseminationApplicationBuilder, LiteraturePriority):
    FORM_ID = 22

    def __init__(self):
        super().__init__()

        self.project_type = [
            "Publikacja opracowań naukowych, książek (w formie papierowej, e-book, audiobook, książka dla niewidomych i słabowidzących), albumów, czasopism z dziedziny kinematografii funkcjonujących na rynku wydawniczym (również w formie publikacji elektronicznej).",
            "Działalność portali, serwisów, baz z zakresu wiedzy o filmie.",
        ]

        estimate_builder = DUKApplicationEstimateBuilder(estimate_sections=estimate_sections)
        self.estimate_chapters = [
            estimate_builder.generate_estimate()
        ]

        self.source_of_financing_tickets = True
