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
        part = self.create_part(
            title="III. Zakres przedsięwzięcia i jego charakterystyka",
            short_name="III. Zakres przedsięwięcia",
            chapters=[
                self.create_chapter(
                    title="Miejsce realizacji i rodzaj organizowanego przedsięwzięcia",
                    components=[
                        self.component.project_location()
                    ]
                ),
                self.create_chapter(
                    title="Cel i zakres merytoryczny przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="projectGoalAndScope",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Innowacyjność w zakresie treści i formy publikacji",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="projectInnovativeness",
                            validators=[
                                self.validator.length_validator(max_value=400)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Sposób realizacji, zastosowane technologie graficzne i edytorskie",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="projectExecution",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Planowane efekty realizacji przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="projectOutcomes",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Dotychczasowe doświadczenia Wnioskodawcy w działaniach będących przedmiotem przedsięwzięcia. </br><normal>Proszę o wyszczególnienie przedsięwzięć z zakresu kinematografii realizowanych przez Wnioskodawcę w ostatnich 2 latach, o budżecie przekraczającym 50 000 zł</normal>",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="granteeExperience",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Partnerzy, eksperci i specjaliści zaangażowani w przedsięwzięcie i ich dotychczasowy dorobek w tym zakresie (z wyszczególnieniem stopni i tytułów naukowych oraz afiliacji instytucjonalnych)",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="projectCooperators",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Podstawowe dane liczbowe na temat przedsięwzięcia",
                    class_list={
                        "main": [
                            "table-1-2",
                            "grid",
                            "grid-cols-2"
                        ],
                        "sub": [
                            "table-1-2__col"
                        ]
                    },
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
                        self.create_component(
                            component_type="number",
                            label="Przewidywany nakład",
                            name="plannedCirculationAmount",
                            unit="szt."
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="Planowane wpływy ze sprzedaży",
                            name="plannedSalesIncome",
                            unit="PLN"
                        )
                    ]
                )
            ]
        )
        self.save_part(part=part)
