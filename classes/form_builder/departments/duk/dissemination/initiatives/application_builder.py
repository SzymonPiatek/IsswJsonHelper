from classes.form_builder.departments.duk.dissemination.application_builder import DisseminationApplicationBuilder
from classes.form_builder.departments.duk.application_builder import DUKApplicationBuilder
from classes.form_builder.departments.duk.application_estimate_builder import DUKApplicationEstimateBuilder
from classes.form_builder.departments.duk.dissemination.initiatives.estimate_data import estimate_sections_pt1, \
    estimate_sections_pt2, estimate_sections_pt3, estimate_sections_pt4


class InitiativesApplicationBuilder(DisseminationApplicationBuilder):
    PRIORITY_NAME = 'II. Inicjatywy filmowe'
    PRIORITY_NUM = 2
    FORM_ID = 9185

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'initiatives'

    def create_application_basic_data(self, **kwargs):
        data = {
            'projectType': {
                'options': [
                    "Organizacja przeglądów i innych wydarzeń filmowych o charakterze lokalnym",
                    "Działalność kin studyjnych i lokalnych",
                    "Działalność klubów filmowych",
                    "Organizacja kongresów, konferencji i sympozjów, mających na celu pogłębianie i upowszechnianie wiedzy o filmie",
                    "Organizacja konkursów filmowych, wystaw oraz innych wydarzeń promujących sztukę filmową",
                    "Inne działania realizujące cele Priorytetu II"
                ]
            }
        }
        DUKApplicationBuilder.create_application_basic_data(self=self, data=data)

    def create_application_project_costs(self):
        estimate_pt1 = DUKApplicationEstimateBuilder(
            estimate_sections=estimate_sections_pt1,
            after_name="Pt1"
        )
        estimate_pt2 = DUKApplicationEstimateBuilder(
            estimate_sections=estimate_sections_pt2,
            after_name="Pt2"
        )
        estimate_pt3 = DUKApplicationEstimateBuilder(
            estimate_sections=estimate_sections_pt3,
            after_name="Pt3"
        )
        estimate_pt4 = DUKApplicationEstimateBuilder(
            estimate_sections=estimate_sections_pt4,
            after_name="Pt4"
        )

        part = self.create_part(
            title="VII. Kosztorys przedsięwzięcia",
            short_name="VII. Kosztorys przedsięwzięcia",
            chapters=[
                estimate_pt1.generate_estimate_top(),
                estimate_pt1.generate_estimate_headers(),
                self.create_chapter(
                    components=[
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Organizacja przeglądów i innych wydarzeń filmowych o charakterze lokalnym"
                                    ]
                                )
                            ],
                            components=[
                                estimate_pt1.generate_estimate(),
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Działalność kin studyjnych i lokalnych"
                                    ]
                                )
                            ],
                            components=[
                                estimate_pt2.generate_estimate(),
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Działalność klubów filmowych"
                                    ]
                                )
                            ],
                            components=[
                                estimate_pt3.generate_estimate(),
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Organizacja kongresów, konferencji i sympozjów, mających na celu pogłębianie i upowszechnianie wiedzy o filmie",
                                        "Organizacja konkursów filmowych, wystaw oraz innych wydarzeń promujących sztukę filmową",
                                        "Inne działania realizujące cele Priorytetu II"
                                    ]
                                )
                            ],
                            components=[
                                estimate_pt4.generate_estimate(),
                            ]
                        )
                    ]
                ),
                estimate_pt1.generate_estimate_bottom()
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
                        self.create_chapter(
                            components=[
                                self.component.project_location()
                            ]
                        ),
                        self.create_chapter(
                            title="Rodzaj organizowanego przedsięwzięcia",
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Organizacja przeglądów i innych wydarzeń filmowych o charakterze lokalnym"
                                    ]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    name="eventTypePointOne",
                                    options=[
                                        "przegląd",
                                        "inny"
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Rodzaj organizowanego przedsięwzięcia",
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Organizacja kongresów, konferencji i sympozjów, mających na celu pogłębianie i upowszechnianie wiedzy o filmie",
                                        "Organizacja konkursów filmowych, wystaw oraz innych wydarzeń promujących sztukę filmową"
                                    ]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    name="eventTypePointsFourAndFive",
                                    options=[
                                        "konkurs",
                                        "wystawa",
                                        "kongres",
                                        "konferencja",
                                        "sympozjum",
                                        "inne"
                                    ],
                                    required=True
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Przyznane nagrody",
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="projectType",
                            values=[
                                "Organizacja kongresów, konferencji i sympozjów, mających na celu pogłębianie i upowszechnianie wiedzy o filmie",
                                "Organizacja konkursów filmowych, wystaw oraz innych wydarzeń promujących sztukę filmową"
                            ]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="textarea",
                            label="Przyznane nagrody (ile, jakie, jakie kwoty)",
                            name="awardedPrizes",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Przyznawane nagrody w ramach przedsięwzięcia (ile, jakie, jakie kwoty)",
                            name="grantedProjectAwards",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True
                        )
                    ]
                ),
                self.section.application_scope_of_project.expected_type_and_number_of_films_presented(),
                self.create_chapter(
                    title="Repertuar",
                    class_list={
                        "sub": [
                            "table-1-2-top"
                        ]
                    },
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="projectType",
                            values=[
                                "Organizacja przeglądów i innych wydarzeń filmowych o charakterze lokalnym"
                            ]
                        )
                    ],
                    components=[
                        self.create_chapter(
                            class_list={
                                "main": [
                                    "table-1-3-narrow",
                                    "grid",
                                    "grid-cols-3"
                                ],
                                "sub": [
                                    "table-1-3__col"
                                ]
                            },
                            components=[
                                self.create_component(
                                    component_type="number",
                                    label="Udział filmów z ostatnich pięciu lat",
                                    name="lastFiveYearsFilms",
                                    required=True,
                                    unit="%"
                                ),
                                self.create_component(
                                    component_type="number",
                                    label="Udział starszych filmów",
                                    name="olderFilms",
                                    required=True,
                                    unit="%"
                                ),
                                self.create_component(
                                    component_type="number",
                                    label="Łącznie",
                                    name="filmsAltogether",
                                    required=True,
                                    read_only=True,
                                    calculation_rules=[
                                        self.calculation_rule.dynamic_sum_inputs(
                                            fields=[
                                                "lastFiveYearsFilms",
                                                "olderFilms"
                                            ]
                                        )
                                    ],
                                    validators=[
                                        self.validator.exact_validator(
                                            values=[
                                                100,
                                                100.0,
                                                "100",
                                                "100.00"
                                            ],
                                            message="Suma udziałów filmów musi się równać 100%"
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Retrospektywy (twórcy, tematy, tytuły - jeśli znane)",
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="projectType",
                            values=[
                                "Organizacja przeglądów i innych wydarzeń filmowych o charakterze lokalnym"
                            ]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="textarea",
                            required=True,
                            name="retrospectives",
                            validators=[
                                self.validator.length_validator(max_value=1000),
                            ],
                        )
                    ]
                ),
                self.create_chapter(
                    title="Cel przedsięwzięcia",
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="projectType",
                            values=[
                                "Organizacja przeglądów i innych wydarzeń filmowych o charakterze lokalnym",
                                "Organizacja kongresów, konferencji i sympozjów, mających na celu pogłębianie i upowszechnianie wiedzy o filmie",
                                "Organizacja konkursów filmowych, wystaw oraz innych wydarzeń promujących sztukę filmową"
                            ]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="projectPurpose",
                            validators=[
                                self.validator.length_validator(max_value=1000),
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Wydarzenia towarzyszące (np. spotkania z twórcami, koncerty)",
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="projectType",
                            values=[
                                "Organizacja przeglądów i innych wydarzeń filmowych o charakterze lokalnym",
                                "Organizacja kongresów, konferencji i sympozjów, mających na celu pogłębianie i upowszechnianie wiedzy o filmie",
                                "Organizacja konkursów filmowych, wystaw oraz innych wydarzeń promujących sztukę filmową"
                            ]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="accompanyingEvents",
                            validators=[
                                self.validator.length_validator(max_value=1000),
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Udział specjalistów w przygotowaniu i realizacji przedsięwzięcia",
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="projectType",
                            values=[
                                "Organizacja przeglądów i innych wydarzeń filmowych o charakterze lokalnym",
                                "Organizacja kongresów, konferencji i sympozjów, mających na celu pogłębianie i upowszechnianie wiedzy o filmie",
                                "Organizacja konkursów filmowych, wystaw oraz innych wydarzeń promujących sztukę filmową"
                            ]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="participationOfSpecialist",
                            validators=[
                                self.validator.length_validator(max_value=1000),
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Promocja przedsięwzięcia",
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="projectType",
                            values=[
                                "Organizacja przeglądów i innych wydarzeń filmowych o charakterze lokalnym",
                                "Organizacja kongresów, konferencji i sympozjów, mających na celu pogłębianie i upowszechnianie wiedzy o filmie",
                                "Organizacja konkursów filmowych, wystaw oraz innych wydarzeń promujących sztukę filmową"
                            ]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="promotionOfTheProject",
                            validators=[
                                self.validator.length_validator(max_value=1000),
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Zróżnicowanie struktury i liczba uczestników",
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="projectType",
                            values=[
                                "Organizacja przeglądów i innych wydarzeń filmowych o charakterze lokalnym",
                                "Organizacja kongresów, konferencji i sympozjów, mających na celu pogłębianie i upowszechnianie wiedzy o filmie",
                                "Organizacja konkursów filmowych, wystaw oraz innych wydarzeń promujących sztukę filmową"
                            ]
                        )
                    ],
                    class_list={
                        "main": [
                            "table-1-3-narrow",
                            "grid",
                            "grid-cols-3"
                        ],
                        "sub": [
                            "table-1-3__col"
                        ]
                    },
                    components=[
                        self.create_component(
                            component_type="number",
                            label="dzieci (do 12 lat)",
                            name="kidsToTwelve"
                        ),
                        self.create_component(
                            component_type="number",
                            label="młodzież (13-18 lat)",
                            name="adolescents"
                        ),
                        self.create_component(
                            component_type="number",
                            label="dorośli (powyżej 18 lat)",
                            name="grownups"
                        )
                    ]
                ),
                self.create_chapter(
                    title="Udział w przedsięwzięciach jest",
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="projectType",
                            values=[
                                "Organizacja przeglądów i innych wydarzeń filmowych o charakterze lokalnym",
                                "Organizacja kongresów, konferencji i sympozjów, mających na celu pogłębianie i upowszechnianie wiedzy o filmie",
                                "Organizacja konkursów filmowych, wystaw oraz innych wydarzeń promujących sztukę filmową"
                            ]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="radio",
                            name="participationInVentureIs",
                            options=[
                                "bezpłatny",
                                "w większości bezpłatny",
                                "w większości płatny",
                                "płatny"
                            ],
                            required=True,
                        )
                    ]
                ),
                self.create_chapter(
                    title="Opis ogólny przedsięwzięcia (cel i zakres merytoryczny, zastosowane technologie, sposób realizacji, promocja)",
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="projectType",
                            values=[
                                "Inne działania realizujące cele Priorytetu II"
                            ]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="textarea",
                            label="Opis szczegółowy przedsięwzięcia (cel i zakres merytoryczny, zastosowane technologie, sposób realizacji, promocja)",
                            name="generalDescription",
                            validators=[
                                self.validator.length_validator(max_value=1000),
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Wartość merytoryczna przedsięwzięcia, w tym tradycja i ciągłość realizacji projektu",
                            name="substantiveValueOfProject",
                            validators=[
                                self.validator.length_validator(max_value=1000),
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Spójność i oryginalność koncepcji przedsięwzięcia, atrakcyjność przekazu dla odbiorcy",
                            name="originalityOfProject",
                            validators=[
                                self.validator.length_validator(max_value=1000),
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Zasięg przedsięwzięcia",
                            name="rangeOfProject",
                            validators=[
                                self.validator.length_validator(max_value=1000),
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Zróżnicowanie struktury odbiorców lub uczestników oraz liczba uczestników",
                            name="diversificationOfAudience",
                            validators=[
                                self.validator.length_validator(max_value=1000),
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Celowość, innowacyjność i wieloaspektowość podjętej tematyki",
                            name="purposefulnessAndInnovation",
                            validators=[
                                self.validator.length_validator(max_value=1000),
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Adekwatność planowanych działań oraz kosztów przeznaczonych na ich realizację w stosunku do przewidywanych efektów",
                            name="adequacyOfPlannedActivities",
                            validators=[
                                self.validator.length_validator(max_value=1000),
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Planowane efekty realizacji przedsięwzięcia",
                            name="plannedResultsOfProject",
                            validators=[
                                self.validator.length_validator(max_value=1000),
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Dotychczasowe doświadczenia Wnioskodawcy w działaniach będących przedmiotem przedsięwzięcia. </br><normal>Proszę o wyszczególnienie przedsięwzięć z zakresu kinematografii realizowanych przez wnioskodawcę w ostatnich 2 latach</normal>",
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="projectType",
                            values=[
                                "Organizacja przeglądów i innych wydarzeń filmowych o charakterze lokalnym",
                                "Organizacja kongresów, konferencji i sympozjów, mających na celu pogłębianie i upowszechnianie wiedzy o filmie",
                                "Organizacja konkursów filmowych, wystaw oraz innych wydarzeń promujących sztukę filmową",
                                "Inne działania realizujące cele Priorytetu II"
                            ]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="applicantsPastExperience",
                            validators=[
                                self.validator.length_validator(max_value=1000),
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Planowane efekty realizacji przedsięwzięcia",
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="projectType",
                            values=[
                                "Organizacja przeglądów i innych wydarzeń filmowych o charakterze lokalnym",
                                "Organizacja kongresów, konferencji i sympozjów, mających na celu pogłębianie i upowszechnianie wiedzy o filmie",
                                "Organizacja konkursów filmowych, wystaw oraz innych wydarzeń promujących sztukę filmową"
                            ]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="plannedEffects",
                            validators=[
                                self.validator.length_validator(max_value=300),
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Podstawowe dane liczbowe na temat bieżącej i poprzedniej edycji przedsięwzięcia",
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="projectType",
                            values=[
                                "Organizacja przeglądów i innych wydarzeń filmowych o charakterze lokalnym"
                            ]
                        )
                    ],
                    components=[
                        self.create_chapter(
                            class_list={
                                "sub": [
                                    "table-1-2-top"
                                ]
                            },
                            components=[
                                self.create_chapter(
                                    title="Liczba akredytacji",
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
                                            label="Poprzednia edycja",
                                            name="numberOfAccreditationPreviousEdition",
                                            read_only=True,
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        "numberOfAccreditationPreviousEditionPaid",
                                                        "numberOfAccreditationPreviousEditionNotPaid"
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        "numberOfAccreditationPreviousEdition"
                                                    ]
                                                ),
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        "numberOfAccreditationPreviousEditionPaid",
                                                        "numberOfAccreditationPreviousEditionNotPaid"
                                                    ]
                                                )
                                            ],
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Planowane",
                                            name="numberOfAccreditationPlanned",
                                            read_only=True,
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        "numberOfAccreditationPlannedNotPaid",
                                                        "numberOfAccreditationPlannedPaid"
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        "numberOfAccreditationPlanned"
                                                    ]
                                                ),
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        "numberOfAccreditationPlannedNotPaid",
                                                        "numberOfAccreditationPlannedPaid"
                                                    ]
                                                )
                                            ],
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Poprzednia edycja płatne",
                                            name="numberOfAccreditationPreviousEditionPaid",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Planowane płatne",
                                            name="numberOfAccreditationPlannedPaid",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Poprzednia edycja bezpłatne",
                                            name="numberOfAccreditationPreviousEditionNotPaid",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Planowane bezpłatne",
                                            name="numberOfAccreditationPlannedNotPaid",
                                            unit="szt."
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="Liczba biletów",
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
                                            label="Poprzednia edycja",
                                            name="numberOfTicketsPreviousEdition",
                                            read_only=True,
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        "numberOfTicketsPreviousEditionPaid",
                                                        "numberOfTicketsPreviousEditionNotPaid"
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        "numberOfTicketsPreviousEdition"
                                                    ]
                                                ),
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        "numberOfTicketsPreviousEditionPaid",
                                                        "numberOfTicketsPreviousEditionNotPaid"
                                                    ]
                                                )
                                            ],
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Planowane",
                                            name="numberOfTicketsPlanned",
                                            read_only=True,
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        "numberOfTicketsPlannedPaid",
                                                        "numberOfTicketsPlannedNotPaid"
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        "numberOfTicketsPlanned"
                                                    ]
                                                ),
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        "numberOfTicketsPlannedPaid",
                                                        "numberOfTicketsPlannedNotPaid"
                                                    ]
                                                )
                                            ],
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Poprzednia edycja płatne",
                                            name="numberOfTicketsPreviousEditionPaid",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Planowane płatne",
                                            name="numberOfTicketsPlannedPaid",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Poprzednia edycja bezpłatne",
                                            name="numberOfTicketsPreviousEditionNotPaid",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Planowane bezpłatne",
                                            name="numberOfTicketsPlannedNotPaid",
                                            unit="szt."
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="Liczba seansów",
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
                                            label="Poprzednia edycja",
                                            name="numberOfScreeningsPreviousEdition",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Planowane",
                                            name="numberOfScreeningsPlanned",
                                            unit="szt."
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="Liczba prezentowanych filmów",
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
                                            label="Poprzednia edycja",
                                            name="numberOfPresentedFilmsPreviousEdition",
                                            read_only=True,
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        "numberOfPresentedPolishFilmsPreviousEdition",
                                                        "numberOfForeignPresentedFilmsPreviousEdition"
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        "numberOfPresentedFilmsPreviousEdition"
                                                    ]
                                                ),
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        "numberOfPresentedPolishFilmsPreviousEdition",
                                                        "numberOfForeignPresentedFilmsPreviousEdition"
                                                    ]
                                                )
                                            ],
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Planowane",
                                            name="numberOfPresentedFilmsPlanned",
                                            read_only=True,
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        "numberOfPresentedPolishFilmsPlanned",
                                                        "numberOfForeignPresentedFilmsPlanned"
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        "numberOfPresentedFilmsPlanned"
                                                    ]
                                                ),
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        "numberOfPresentedPolishFilmsPlanned",
                                                        "numberOfForeignPresentedFilmsPlanned"
                                                    ]
                                                )
                                            ],
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Liczba filmów polskich w poprzedniej edycji",
                                            name="numberOfPresentedPolishFilmsPreviousEdition",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Liczba filmów polskich w planowanej edycji",
                                            name="numberOfPresentedPolishFilmsPlanned",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Liczba filmów zagranicznych w poprzedniej edycji",
                                            name="numberOfForeignPresentedFilmsPreviousEdition",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Liczba filmów zagranicznych w planowanej edycji",
                                            name="numberOfForeignPresentedFilmsPlanned",
                                            unit="szt."
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="Liczba nowości filmowych (z ostatnich 2 lat)",
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
                                            label="Poprzednia edycja",
                                            name="numberOfNewFilmsLastTwoYearsPreviousEdition",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Planowane",
                                            name="numberOfNewFilmsLastTwoYearsPlanned",
                                            unit="szt."
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="Liczba retrospektyw",
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
                                            label="Poprzednia edycja",
                                            name="numberOfRetrospectivesPreviousEdition",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Planowane",
                                            name="numberOfRetrospectivesPlanned",
                                            unit="szt."
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="Liczba filmów z audiodeskrypcją",
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
                                            label="Poprzednia edycja",
                                            name="audiodescriptionFilmsCountPreviousEdition",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Planowane",
                                            name="audiodescriptionFilmsCountPlaned",
                                            unit="szt."
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="Nakład materiałów promocyjnych (katalogi, plakaty)",
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
                                            label="Poprzednia edycja",
                                            name="promotionalMaterialsCountPreviousEdition",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Planowane",
                                            name="promotionalMaterialsCountPlanned",
                                            unit="szt."
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="Liczba przyznanych nagród",
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
                                            label="Poprzednia edycja",
                                            name="grantedAwardsPreviousEdition",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Planowane",
                                            name="grantedAwardsPlanned",
                                            unit="szt."
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="Liczba publikacji w mediach na temat wydarzenia",
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
                                            label="Poprzednia edycja",
                                            name="mediaPublicationCountPreviousEdition",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Planowane",
                                            name="mediaPublicationCountPlanned",
                                            unit="szt."
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="Liczba osób zaangażowanych w realizacje przedsięwzięcia",
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
                                            label="Poprzednia edycja",
                                            name="numberOfPeopleInvolvedPreviousEdition",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Planowane",
                                            name="numberOfPeopleInvolvedPlanned",
                                            unit="szt."
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="Liczba widzów",
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
                                            label="Poprzednia edycja",
                                            name="numberOfViewersPreviousEdition",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Planowane",
                                            name="numberOfViewersPlanned",
                                            unit="szt."
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="Liczba gości zagranicznych",
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
                                            label="Poprzednia edycja",
                                            name="numberOfForeignVisitorsPreviousEdition",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Planowane",
                                            name="numberOfForeignVisitorsPlanned",
                                            unit="szt."
                                        )
                                    ]
                                ),
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="projectType",
                            values=[
                                "Działalność kin studyjnych i lokalnych"
                            ]
                        )
                    ],
                    components=[
                        self.create_chapter(
                            title="Opis szczegółowy przedsięwzięcia (cel i zakres merytoryczny, zastosowane technologie, sposób realizacji, promocja)",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="detailedDescriptionOfProject",
                                    validators=[
                                        self.validator.length_validator(max_value=1000)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Lista ekspertów",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="expertsList",
                                    validators=[
                                        self.validator.length_validator(max_value=100)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Planowane wydarzenia własne (przeglądy tematyczne, biograficzne, wydanie specjalne)",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="plannedInHouseEvents",
                                    validators=[
                                        self.validator.length_validator(max_value=100)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Planowane działania promocyjne SKS",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="plannedPromotionalActivityOfSKSiL",
                                    validators=[
                                        self.validator.length_validator(max_value=1000)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Partnerzy i specjaliści zaangażowani w przedsięwzięcie",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="involvedPartnersAndSpecialist",
                                    validators=[
                                        self.validator.length_validator(max_value=1000)
                                    ],
                                    required=True
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="projectType",
                            values=[
                                "Działalność klubów filmowych"
                            ]
                        )
                    ],
                    components=[
                        self.create_chapter(
                            title="Opis przedsięwzięcia (cel i zakres merytoryczny, zastosowane technologie, zasięg przedsięwzięcia, sposób realizacji, promocja)",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="detailedDescriptionPurposeAndScope",
                                    validators=[
                                        self.validator.length_validator(max_value=1000)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Dotychczasowe doświadczenia Wnioskodawcy w działaniach będących przedmiotem przedsięwzięcia",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="applicantsPreviousExperience",
                                    validators=[
                                        self.validator.length_validator(max_value=300)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Planowany udział prelegantów, partnerów, ekspertów i specjalistów zaangażowanych w przedsięwzięcie i ich dotychczasowy dorobek w tej dziedzinie",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="plannedParticipationOfSpeakers",
                                    validators=[
                                        self.validator.length_validator(max_value=1000)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Planowany wykaz tytułów prezentowanych w ramach DKF (ze szczególnym uwzględnieniem filmów o wysokiej wartości artystycznej, w tym klasyki filmowej) i określenie częstotliwości spotkań i pokazów w DKF",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="listOfPlannedTitles",
                                    validators=[
                                        self.validator.length_validator(max_value=1000)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Liczba stałych członków klubu filmowego",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="numberOfRegularMembers",
                                    validators=[
                                        self.validator.length_validator(max_value=100)
                                    ],
                                    required=True
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Partnerzy, eksperci i specjaliści zaangażowani w przedsięwzięcie i ich dotychczasowy dorobek w tym zakresie",
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="projectType",
                            values=[
                                "Inne działania realizujące cele Priorytetu II"
                            ]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="partnersExpertsAndSpecialists",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Podstawowe dane liczbowe na temat bieżącej i poprzedniej edycji przedsięwzięcia",
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="projectType",
                            values=[
                                "Inne działania realizujące cele Priorytetu II"
                            ]
                        )
                    ],
                    components=[
                        self.create_chapter(
                            title="Liczba odbiorców wydarzenia",
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
                                    label="Poprzednia edycja",
                                    name="recipientsCountPreviousEdition",
                                    unit="os."
                                ),
                                self.create_component(
                                    component_type="number",
                                    label="Bieżąca edycja przedsięwzięcia (przewidywane wielkości)",
                                    name="recipientsCountCurrentEdition",
                                    unit="os."
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        self.save_part(part=part)
