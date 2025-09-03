from classes.form_builder.duk.dissemination.application_builder import DisseminationApplicationBuilder
from classes.form_builder.duk.application_builder import DUKApplicationBuilder
from classes.form_builder.duk.dissemination.festivals.estimate_data import estimate_sections


class FestivalsApplicationBuilder(DisseminationApplicationBuilder):
    PRIORITY_NAME = 'I. Festiwale filmowe'
    PRIORITY_NUM = 1
    FORM_ID = 9184

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'festivals'
        self.estimate_sections = estimate_sections

    def create_application_basic_data(self, **kwargs):
        data = {
            'projectType': {
                'options': [
                    "Organizacja festiwali o charakterze ogólnopolskim i międzynarodowym",
                    "Inne działania realizujące cele Priorytetu I"
                ]
            }
        }
        DUKApplicationBuilder.create_application_basic_data(self=self, data=data)

    def create_application_scope_of_project(self):
        expected_films_chapters = [
            {
                "name": "feature",
                "label": "Film fabularny"
            },
            {
                "name": "documentary",
                "label": "Film dokumentalny"
            },
            {
                "name": "animated",
                "label": "animowany"
            },
            {
                "name": "experimental",
                "label": "Film eksperymentalny"
            },
            {
                "name": "other",
                "label": "Inny (jakie?)",
                "isOther": True
            }
        ]

        part = self.create_part(
            title="III. Zakres przedsięwzięcia i jego charakterystyka",
            short_name="III. Zakres przedsięwięcia",
            chapters=[
                self.create_chapter(
                    title="1. Termin i miejsce odbywania się zasadniczej części festiwalu",
                    components=[
                        self.create_chapter(
                            class_list=[
                              "grid",
                              "grid-cols-2"
                            ],
                            components=[
                                self.component.project_location(),
                                self.create_component(
                                    component_type="text",
                                    label="Miejsca lub obiekty, w których odbędą się projekcje lub wydarzenia",
                                    name="projectPlacesObjects",
                                    validators=[
                                        self.validator.length_validator(max_value=100)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
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
                                        "Organizacja festiwali o charakterze ogólnopolskim i międzynarodowym",
                                    ]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="date",
                                    label="Termin od (otwacie festiwalu)",
                                    name="projectOpeningDatePointOne",
                                    required=True,
                                    validators=[
                                        self.validator.related_local_date_lte_validator(
                                            field_name="projectClosingDatePointOne",
                                            message="Data otwarcia festiwalu nie może być późniejsza od daty jego zamknięcia."
                                        )
                                    ]
                                ),
                                self.create_component(
                                    component_type="date",
                                    label="Termin do (zamknięcie festiwalu)",
                                    name="projectClosingDatePointOne",
                                    required=True,
                                    validators=[
                                        self.validator.related_local_date_gte_validator(
                                            field_name="projectOpeningDatePointOne",
                                            message="Data zamknięcia festiwalu nie może być wcześniejsza od daty jego otwarcia."
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Rodzaj i przewidywana liczba prezentowanych filmów, przykładowe tytuły (jeśli są już znane)",
                    components=[
                        *[self.create_chapter(
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="checkbox",
                                            label=chapter["label"],
                                            name=f"{chapter["name"]}Film"
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name=f"{chapter["name"]}Film",
                                            values=[True]
                                        )
                                    ],
                                    class_list=[
                                        "grid",
                                        "grid-cols-3"
                                    ],
                                    components=[
                                        *(
                                            [
                                                self.create_component(
                                                    component_type="text",
                                                    label="Jakie?",
                                                    name=f"{chapter['name']}FilmKind",
                                                    validators=[
                                                        self.validator.length_validator(max_value=100),
                                                        self.validator.related_required_if_equal_validator(
                                                            field_name=f"{chapter['name']}Film",
                                                            value=True
                                                        )
                                                    ],
                                                    class_list=["col-span-3"],
                                                    required=True
                                                )
                                            ] if chapter.get("isOther", False) else []
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Liczba",
                                            name=f"{chapter["name"]}FilmCount",
                                            required=True,
                                            validators=[
                                                self.validator.related_required_if_equal_validator(
                                                    field_name=f"{chapter["name"]}Film",
                                                    value=True
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="textarea",
                                            label="Tytuły",
                                            name=f"{chapter["name"]}FilmTitles",
                                            validators=[
                                                self.validator.length_validator(max_value=200)
                                            ],
                                            required=True,
                                            class_list=[
                                                "col-star-2",
                                                "col-end-4"
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ) for chapter in expected_films_chapters]
                    ]
                ),
                self.create_chapter(
                    title="3. Repertuar",
                    class_list={
                        "sub": [
                            "table-1-2-top"
                        ]
                    },
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
                    title="4. Retrospektywy (twórcy, tematy, tytuły - jeśli znane)",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            required=True,
                            name="retrospectives",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="5. Przyznawane nagrody w ramach przedsięwzięcia (ile, jakie, jakie kwoty)",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            label="Przyznawane nagrody w ramach przedsięwzięcia (ile, jakie, jakie kwoty)",
                            name="grantedProjectAwards",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="6. Cel przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            required=True,
                            name="projectPurpose",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="7. Zakres i wartość merytoryczna, w tym - celowość, innowacyjność i wieloaspektowość podjętej tematyki oraz sposób realizacji przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="scopeAndValueOfContent",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="8. Wydarzenia towarzyszące (np. spotkania z twórcami, koncerty)",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="accompanyingEvents",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="9. Udział specjalistów w przygotowaniu i realizacji przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="participationOfSpecialist",
                            validators=[
                                self.validator.length_validator(max_value=500)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="10. Promocja wydarzenia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="promotionOfTheProject",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="11. Zróżnicowanie struktury i liczba uczestników",
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
                    title="12. Udział w przedsięwzięciach jest",
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
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="13. Dotychczasowe doświadczenia Wnioskodawcy w działaniach będących przedmiotem przedsięwzięcia. </br><normal>Proszę o wyszczególnienie przedsięwzięć z zakresu kinematografii realizowanych przez wnioskodawcę w ostatnich 2 latach</normal>",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="applicantsPastExperience",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="14. Planowane efekty realizacji przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="plannedEffects",
                            validators=[
                                self.validator.length_validator(max_value=300)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="15. Podstawowe dane liczbowe na temat bieżącej i poprzedniej edycji przedsięwzięcia",
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
                            ]
                        )
                    ]
                )
            ]
        )
        self.save_part(part)
