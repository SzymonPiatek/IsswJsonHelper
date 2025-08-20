from classes.form_builder.duk.dissemination.application_builder import DisseminationApplicationBuilder
from classes.form_builder.duk.application_builder import DUKApplicationBuilder


class LiteratueApplicationBuilder(DisseminationApplicationBuilder):
    PRIORITY_NAME = 'III. Literatura i czasopisma o filmie'
    PRIORITY_NUM = 3
    FORM_ID = 9186

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'literature'

    def create_application_basic_data(self, **kwargs):
        data = {
            'projectType': {
                'options': [
                    "Publikacja opracowań naukowych, książek, czasopism z dziedziny kinematografii, w formatach takich jak: książka drukowana, e-book, audiobook, książka dla niewidomych i słabowidzących",
                    "Publikacja opracowań naukowych, książek, czasopism z dziedziny kinematografii, w formatach takich jak: albumy",
                    "Publikacja opracowań naukowych, książek, czasopism z dziedziny kinematografii, w formatach takich jak: publikacje popularno-naukowe",
                    "Publikacja opracowań naukowych, książek, czasopism z dziedziny kinematografii, w formatach takich jak: czasopisma - w ramach Priorytetu III można finansować wyłącznie czasopisma funkcjonujące na rynku wydawniczym lub w formie publikacji elektronicznej",
                    "Działalność portali, serwisów, baz z zakresu wiedzy o filmie",
                    "Inne działania realizujące cele Priorytetu III"
                ]
            }
        }
        DUKApplicationBuilder.create_application_basic_data(self=self, data=data)
