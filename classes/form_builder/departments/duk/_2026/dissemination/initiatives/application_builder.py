from classes.form_builder.departments.duk._2026.dissemination.application_builder import DisseminationApplicationBuilder
from .estimate_data import estimate_sections_pt124, estimate_sections_pt3
from classes.form_builder.departments.duk._2026.estimate.application_estimate_builder import DUKApplicationEstimateBuilder
from classes.form_builder.departments.duk._2026.dissemination.priority import InitiativesPriority
from classes.helpers import int_to_roman


class InitiativesApplicationBuilder(DisseminationApplicationBuilder, InitiativesPriority):
    FORM_ID = 21

    def __init__(self):
        super().__init__()

        # Variables
        self.project_type = [
            "Organizacja przeglądów, konkursów, wystaw i innych wydarzeń filmowych promujących sztukę filmową.",
            "Organizacja kongresów, konferencji, sympozjów i inne działania edukacyjne pogłębiające wiedzę o filmie.",
            "Działalność Sieci Kin Studyjnych.",
            "Inne działania realizujące cele Priorytetu II."
        ]
        self.source_of_financing_tickets = True

        # Estimate
        estimate_builder_pt124 = DUKApplicationEstimateBuilder(
            estimate_sections=estimate_sections_pt124,
            after_name="pt124"
        )
        estimate_builder_pt3 = DUKApplicationEstimateBuilder(
            estimate_sections=estimate_sections_pt3,
            after_name="pt3"
        )
        self.estimate_chapters = [
            self.create_chapter(
                visibility_rules=[
                    self.visibility_rule.depends_on_value(
                        field_name="projectType",
                        values=[
                            "Organizacja przeglądów, konkursów, wystaw i innych wydarzeń filmowych promujących sztukę filmową.",
                            "Organizacja kongresów, konferencji, sympozjów i inne działania edukacyjne pogłębiające wiedzę o filmie.",
                            "Inne działania realizujące cele Priorytetu II."
                        ]
                    )
                ],
                components=[
                    estimate_builder_pt124.generate_estimate(),
                ]
            ),
            self.create_chapter(
                visibility_rules=[
                    self.visibility_rule.depends_on_value(
                        field_name="projectType",
                        values=[
                            "Działalność Sieci Kin Studyjnych."
                        ]
                    )
                ],
                components=[
                    estimate_builder_pt3.generate_estimate(),
                ]
            )
        ]

    def create_application_scope_of_project(self, number):
        part = self.create_part(
            title=f"{int_to_roman(number)}. Zakres przedsięwzięcia i jego charakterystyka",
            short_name=f"{int_to_roman(number)}. Zakres przedsięwzięcia",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_chapter(
                            title="Nazwa przedsięwzięcia",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="applicationTaskNameRepeatPage4",
                                    read_only=True,
                                    calculation_rules=[
                                        self.calculation_rule.copy_value(
                                            from_name="applicationTaskName"
                                        )
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Forma przedsięwzięcia",
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    name="undertakingForm",
                                    required=True,
                                    options=[
                                        "Przegląd",
                                        "Wystawa",
                                        "Konkurs"
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="1. Termin i miejsce realizacji przedsięwzięcia",
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
                                    component_type="date",
                                    label="Termin od",
                                    name="projectOpeningDatePointOne",
                                    validators=[
                                        self.validator.related_date_lte_validator(
                                            field_name="projectClosingDatePointOne",
                                        )
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="date",
                                    label="Termin do",
                                    name="projectClosingDatePointOne",
                                    validators=[
                                        self.validator.related_date_gte_validator(
                                            field_name="projectOpeningDatePointOne",
                                        )
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Miejscowość",
                                    name="projectCity",
                                    validators=[
                                        self.validator.length_validator(max_value=100)
                                    ],
                                    required=True,
                                    class_list=[
                                        "table-full"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Miejsce realizacji przedsięwzięcia",
                                    name="projectPlacesObjects",
                                    required=True,
                                    validators=[
                                        self.validator.length_validator(max_value=100)
                                    ],
                                    class_list=[
                                        "table-full"
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Zakres przedsięwzięcia i jego charakterystyka",
                    components=[
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Organizacja przeglądów, konkursów, wystaw i innych wydarzeń filmowych promujących sztukę filmową."
                                    ]
                                )
                            ],
                            components=[]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Organizacja kongresów, konferencji, sympozjów i inne działania edukacyjne pogłębiające wiedzę o filmie."
                                    ]
                                )
                            ],
                            components=[]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Działalność Sieci Kin Studyjnych."
                                    ]
                                )
                            ],
                            components=[]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Inne działania realizujące cele Priorytetu II."
                                    ]
                                )
                            ],
                            components=[]
                        )
                    ]
                ),
                self.create_chapter(
                    title="3. Podstawowe dane liczbowe i wskaźniki",
                    components=[
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Organizacja przeglądów, konkursów, wystaw i innych wydarzeń filmowych promujących sztukę filmową."
                                    ]
                                )
                            ],
                            components=[]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Organizacja kongresów, konferencji, sympozjów i inne działania edukacyjne pogłębiające wiedzę o filmie."
                                    ]
                                )
                            ],
                            components=[]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Działalność Sieci Kin Studyjnych."
                                    ]
                                )
                            ],
                            components=[]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Inne działania realizujące cele Priorytetu II."
                                    ]
                                )
                            ],
                            components=[]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Czy przedsięwzięcie, na które składany jest wniosek jest powiązane z innymi przedsięwzięciami, o dofinansowanie których ubiega się Wnioskodawca w bieżącym roku z innych programów operacyjnych PISF? Jeżeli tak, proszę podać nazwę przedsięwzięcia, program oraz wnioskowaną kwotę dofinansowania",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    name="wasSubmittedBefore",
                                    options=["Tak", "Nie"],
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="wasSubmittedBefore",
                                    values=["Tak"])
                            ],
                            multiple_forms_rules={"minCount": 1, "maxCount": 20},
                            components=[
                                self.create_chapter(
                                    class_list=["grid", "grid-cols-3"],
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            label="Nazwa przedsięwzięcia",
                                            name="otherProjectName"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Program operacyjny",
                                            name="programmeName"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Wnioskowana kwota",
                                            name="otherProjectFundingAmount",
                                            unit="PLN",
                                            mask="fund"
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
