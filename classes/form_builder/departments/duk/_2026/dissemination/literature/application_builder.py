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

    def create_application_scope_of_project(self, number):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Zakres przedsięwzięcia i jego charakterystyka",
            short_name=f"{self.helpers.int_to_roman(number)}. Zakres przedsięwziecia",
            chapters=[
                self.create_chapter(
                    title="1. Zakres przedsięwzięcia i jego charakterystyka",
                    components=[
                        self.create_chapter(
                            title="Opis przedsięwzięcia",
                            help_text="Cel i zakres merytoryczny przedsięwzięcia",
                            components=[
                                self.create_component(
                                    name="generalProjectDescription",
                                    component_type="textarea",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=3000
                                        )
                                    ],
                                    required=True,
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Potencjał popularyzatorski",
                            help_text="Innowacyjność w zakresie treści, znaczenie projektu w upowszechnianiu wiedzy o kinematografii.",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="popularizationPotential",
                                    validators=[
                                        self.validator.length_validator(max_value=1000)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Koncepcja opracowania",
                            help_text="Formy publikacji, sposób realizacji, zastosowane technologie graficzne i edytorskie.",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="conceptOfStudy",
                                    validators=[
                                        self.validator.length_validator(max_value=1000)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Analiza zapotrzebowania rynku na realizację przedsięwzięcia",
                            help_text="Grupa docelowa oraz zastosowanie praktyczne.",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="marketAnalysisForProjectImplementation",
                                    validators=[
                                        self.validator.length_validator(max_value=1000)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Doświadczenie wnioskodawcy i kompetencje zespołu",
                            help_text="Udział specjalistów i ekspertów w realizację przedsięwzięcia.",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="applicantAndTeamExperience",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=3000
                                        )
                                    ],
                                    required=True
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Strategia promocyjna",
                            help_text="Działania promocyjne wspierające upowszechnienie przedsięwzięcia.",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="promotionalStrategy",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=3000
                                        )
                                    ],
                                    required=True
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Dostępność przedsięwzięcia",
                            help_text="Działania podejmowane na rzecz osób ze szczególnymi potrzebami oraz wspierania inkluzywności.",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="projectAccessibility",
                                    validators=[
                                        self.validator.length_validator(max_value=1000)
                                    ],
                                    required=True,
                                ),
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Podstawowe dane liczbowe i planowane wskaźniki",
                    components=[
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Publikacja opracowań naukowych, książek (w formie papierowej, e-book, audiobook, książka dla niewidomych i słabowidzących), albumów, czasopism z dziedziny kinematografii funkcjonujących na rynku wydawniczym (również w formie publikacji elektronicznej).",
                                    ]
                                )
                            ],
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
                            components=[
                                self.create_component(
                                    component_type="number",
                                    label="Przewidywany nakład",
                                    name="expectedCirculation",
                                    unit="szt."
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Planowane wpływy ze sprzedaży",
                                    name="plannedSalesRevenues",
                                    unit="PLN"
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Działalność portali, serwisów, baz z zakresu wiedzy o filmie.",
                                    ]
                                )
                            ],
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="number",
                                            label="Przewidywany liczba odwiedzin (sesji) miesięcznie",
                                            name="estimatedNumberOfVisitsMonthly",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="radio",
                                            label="Dostęp dla użytkowników jest",
                                            name="accessForUsersType",
                                            options=[
                                                "Bezpłatny", "Płatny"
                                            ],
                                            required=True
                                        ),
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="accessForUsersType",
                                            values=[
                                                "Płatny"
                                            ]
                                        )
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Planowane miesięczne wpływy ze sprzedaży",
                                            name="plannedSalesRevenuesMonthly",
                                            unit="PLN"
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        self.save_part(part)

