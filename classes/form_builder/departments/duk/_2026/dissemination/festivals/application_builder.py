from classes.form_builder.departments.duk._2026.dissemination.application_builder import DisseminationApplicationBuilder
from classes.form_builder.departments.duk._2026.dissemination.priority import FestivalsPriority


class FestivalsApplicationBuilder(DisseminationApplicationBuilder, FestivalsPriority):
    FORM_ID = 9184

    def __init__(self):
        super().__init__()

    def create_application_basic_data(self):
        part = self.create_part(
            title="II. Dane podstawowe",
            short_name="II. Dane podstawowe",
            chapters=[
                self.create_chapter(
                    title="1. Nazwa przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="applicationTaskName",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Rodzaj przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="radio",
                            name="projectType",
                            options=["Organizacja festiwali filmowych o charakterze ogólnopolskim lub międzynarodowym, będących wydarzeniami cyklicznymi, obejmujących szeroki program filmowy, sekcje konkursowe oceniane przez jury oraz wydarzenia towarzyszące, takie jak spotkania z twórcami, panele dyskusyjne czy warsztaty."]
                        )
                    ]
                ),
                self.create_chapter(
                    title="3. Poprzednia edycja przedsięwzięcia",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    label="Czy poprzednia edycja przedsięwzięcia została dofinansowana przez PISF?",
                                    name="previousApplicationForProject",
                                    options=[
                                        "Tak", "Nie"
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="previousApplicationForProject",
                                    values=[
                                        "Tak"
                                    ]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="text",
                                    name="fiveDigitNumberOfApplication",
                                    label="Numer wniosku dotyczący poprzedniej edycji przedsięwzięcia",
                                    validators=[
                                        self.validator.related_required_if_equal_validator(
                                            field_name="previousApplicationForProject",
                                            value="Tak"
                                        )
                                    ],
                                    required=True
                                )
                            ]
                        )
                    ]
                )
            ]
        )

        self.save_part(part)

    def create_application_scope_of_project(self):
        part = self.create_part(
            title="IV. Zakres przedsięwzięcia",
            short_name="IV. Zakres przedsięwzięcia",
            chapters=[
                self.create_chapter(
                    title="Zakres i charakterystyka przedsięwzięcia",
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
                            label="Termin od (otwarcie festiwalu)",
                            name="projectOpeningDatePointOne",
                            validators=[
                                self.validator.related_date_lte_validator(
                                    field_name="projectClosingDatePointOne",
                                    message="Data otwarcia festiwalu nie może być późniejsza niż data zamknięcia festiwalu."
                                )
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="date",
                            label="Termin do (zamknięcie festiwalu)",
                            name="projectClosingDatePointOne",
                            validators=[
                                self.validator.related_date_gte_validator(
                                    field_name="projectOpeningDatePointOne",
                                    message="Data zamknięcia festiwalu nie może być wcześniejszy niż data otwarcia festiwalu."
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
                            label="Miejsce realizacji projekcji i wydarzeń",
                            name="projectPlacesObjects",
                            validators=[
                                self.validator.length_validator(max_value=100)
                            ],
                            required=True,
                            class_list=[
                                "table-full"
                            ]
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
                    title="Przyznawane nagrody w ramach przedsięwzięcia (ile, jakie, jakie kwoty)",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            label="Przyznawane nagrody w ramach przedsięwzięcia (ile, jakie, jakie kwoty)",
                            name="grantedProjectAwards",
                            validators=[
                                self.validator.length_validator(max_value=500)
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Cel przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            required=True,
                            name="projectPurpose",
                            validators=[
                                self.validator.length_validator(max_value=200)
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Zakres i wartość merytoryczna, w tym - celowość, innowacyjność i wieloaspektowość podjętej tematyki oraz sposób realizacji przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="scopeAndValueOfContent",
                            validators=[
                                self.validator.length_validator(max_value=500)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Wydarzenia towarzyszące (np. spotkania z twórcami, koncerty)",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="accompanyingEvents",
                            validators=[
                                self.validator.length_validator(max_value=500)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Udział specjalistów w przygotowaniu i realizacji przedsięwzięcia",
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
                    title="Promocja wydarzenia",
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
                    title="Dostępność wydarzenia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="eventAvailability",
                            label="Działania podejmowane na rzecz osób ze szczególnymi potrzebami oraz wspierania inkluzywności.",
                            validators=[
                                self.validator.length_validator(max_value=500)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Zróżnicowanie struktury i liczba uczestników",
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
                    title="Dotychczasowe doświadczenia Wnioskodawcy w działaniach będących przedmiotem przedsięwzięcia. </br><normal>Proszę o wyszczególnienie przedsięwzięć z zakresu kinematografii realizowanych przez wnioskodawcę w ostatnich 2 latach</normal>",
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
                    title="Planowane efekty realizacji przedsięwzięcia",
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
                    title="Podstawowe dane liczbowe na temat bieżącej i poprzedniej edycji przedsięwzięcia",
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
