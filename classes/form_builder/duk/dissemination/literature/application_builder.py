from classes.form_builder.duk.dissemination.application_builder import DisseminationApplicationBuilder
from classes.form_builder.duk.application_builder import DUKApplicationBuilder
from classes.form_builder.duk.dissemination.literature.estimate_data import estimate_sections_pt1234, estimate_sections_pt5, estimate_sections_pt6
from classes.form_builder.duk.application_estimate_builder import DUKApplicationEstimateBuilder


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

    def create_application_project_costs(self):
        estimate_pt1234 = DUKApplicationEstimateBuilder(
            estimate_sections=estimate_sections_pt1234,
            after_name="Pt1234"
        )
        estimate_pt5 = DUKApplicationEstimateBuilder(
            estimate_sections=estimate_sections_pt5,
            after_name="Pt5"
        )
        estimate_pt6 = DUKApplicationEstimateBuilder(
            estimate_sections=estimate_sections_pt6,
            after_name="Pt6"
        )

        part = self.create_part(
            title="VII. Kosztorys przedsięwzięcia",
            short_name="VII. Kosztorys przedsięwzięcia",
            chapters=[
                estimate_pt1234.generate_estimate_top(),
                estimate_pt1234.generate_estimate_headers(),
                self.create_chapter(
                    components=[
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Publikacja opracowań naukowych, książek, czasopism z dziedziny kinematografii, w formatach takich jak: książka drukowana, e-book, audiobook, książka dla niewidomych i słabowidzących",
                                        "Publikacja opracowań naukowych, książek, czasopism z dziedziny kinematografii, w formatach takich jak: albumy",
                                        "Publikacja opracowań naukowych, książek, czasopism z dziedziny kinematografii, w formatach takich jak: publikacje popularno-naukowe",
                                        "Publikacja opracowań naukowych, książek, czasopism z dziedziny kinematografii, w formatach takich jak: czasopisma - w ramach Priorytetu III można finansować wyłącznie czasopisma funkcjonujące na rynku wydawniczym lub w formie publikacji elektronicznej"
                                    ]
                                )
                            ],
                            components=[
                                estimate_pt1234.generate_estimate(),
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Działalność portali, serwisów, baz z zakresu wiedzy o filmie"
                                    ]
                                )
                            ],
                            components=[
                                estimate_pt5.generate_estimate()
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Inne działania realizujące cele Priorytetu III"
                                    ]
                                )
                            ],
                            components=[
                                estimate_pt6.generate_estimate()
                            ]
                        )
                    ]
                ),
                estimate_pt1234.generate_estimate_bottom()
            ]
        )

        self.save_part(part=part)

    def create_application_scope_of_project(self):
        pass
