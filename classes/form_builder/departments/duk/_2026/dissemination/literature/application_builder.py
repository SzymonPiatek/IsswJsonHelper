from classes.form_builder.departments.duk._2026.dissemination.application_builder import DisseminationApplicationBuilder
from .estimate_data import estimate_sections
from classes.form_builder.departments.duk._2026.application_estimate_builder import DUKApplicationEstimateBuilder
from ..priority import LiteraturePriority


class LiteratureApplicationBuilder(DisseminationApplicationBuilder, LiteraturePriority):
    FORM_ID = 22

    def __init__(self):
        super().__init__()

        self.project_type = [
            "Publikacja opracowań naukowych, książek, czasopism z dziedziny kinematografii, w formatach takich jak: książka drukowana, e-book, audiobook, książka dla niewidomych i słabowidzących.",
            "Publikacja opracowań naukowych, książel, czasopism z dziedziny kinematografii, w formatach takich jak: albumy.",
            "Publikacja opracowań naukowych, książel, czasopism z dziedziny kinematografii, w formatach takich jak: publikacje popularno-naukowe.",
            "Publikacja opracowań naukowych, książel, czasopism z dziedziny kinematografii, w formatach takich jak: czasopisma - w ramach Priorytetu III można finansować wyłącznie czasopisma funkcjonujące na rynku wydawniczym lub w formie publikacji elektronicznej.",
            "Działalność portali, serwisów, baz z zakresu wiedzy o filmie.",
            "Inne działanie realizujące cele Priorytetu III."
        ]

        estimate_builder = DUKApplicationEstimateBuilder(estimate_sections=estimate_sections)
        self.estimate_chapters = [
            estimate_builder.generate_estimate()
        ]

    def create_application_scope_of_project(self, number):
        pass

    def create_application_attachments(self, number):
        pass

    def create_application_schedule(self, number):
        pass
