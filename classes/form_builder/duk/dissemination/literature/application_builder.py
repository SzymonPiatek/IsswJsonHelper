from classes.form_builder.duk.dissemination.application_builder import DisseminationApplicationBuilder


class LiteratueApplicationBuilder(DisseminationApplicationBuilder):
    PRIORITY_NAME = 'III. Literatura i czasopisma o filmie'
    PRIORITY_NUM = 3

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'literature'

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
                    "Publikacja opracowań naukowych, książek, czasopism z dziedziny kinematografii, w formatach takich jak: książka drukowana, e-book, audiobook, książka dla niewidomych i słabowidzących",
                    "Publikacja opracowań naukowych, książek, czasopism z dziedziny kinematografii, w formatach takich jak: albumy",
                    "Publikacja opracowań naukowych, książek, czasopism z dziedziny kinematografii, w formatach takich jak: publikacje popularno-naukowe",
                    "Publikacja opracowań naukowych, książek, czasopism z dziedziny kinematografii, w formatach takich jak: czasopisma - w ramach Priorytetu III można finansować wyłącznie czasopisma funkcjonujące na rynku wydawniczym lub w formie publikacji elektronicznej",
                    "Działalność portali, serwisów, baz z zakresu wiedzy o filmie",
                    "Inne działania realizujące cele Priorytetu III"
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
