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
                                    mask="share",
                                    unit="%"
                                ),
                                self.create_component(
                                    component_type="number",
                                    label="Udział starszych filmów",
                                    name="olderFilms",
                                    required=True,
                                    mask="share",
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

    def create_application_attachments(self):
        part = self.create_part(
            title="VII. Załączniki",
            short_name="VII. Załączniki",
            chapters=[
                self.create_chapter(
                    title="Obowiązkowe załączniki",
                    components=[
                        self.section.application_attachment.schedule_information()
                    ]
                ),
                self.section.application_attachment.other_attachments(),
                self.section.application_attachment.storage_of_blanks()
            ]
        )
        self.save_part(part)

    def create_application_statements(self):
        nature_of_project = [
            {
                "label": "krajowy",
                "name": "Domestic"
            },
            {
                "label": "międzynarodowy",
                "name": "International"
            },
            {
                "label": "ograniczony krąg odbiorców",
                "name": "LimitedAudience"
            },
            {
                "label": "ze względu na niską wartość komercyjną nie mogłoby się odbyć bez dofinansowania przez PISF",
                "name": "LowCommercialValue"
            },
            {
                "label": "lokalny",
                "name": "Local"
            }
        ]

        required_statements = [
            {
                "label": "Oświadczam, iż posiadam zasoby rzeczowe, finansowe i kadrowe niezbędne do realizacji zadania.",
                "name": "NecessaryResource"
            },
            {
                "label": "Oświadczam, iż nie zalegam z płatnościami na rzecz podmiotów publiczno-prawnych.",
                "name": "NotInArrears"
            },
            {
                "label": "Oświadczam, iż nie zachodzą przesłanki określone w art. 22 ust. 2 ustawy o kinematografii z dnia 30 czerwca 2005 r., które uniemożliwiają udzielenie dofinansowania.",
                "name": "ArticleTwentyTwo"
            },
            {
                "label": "W przypadku uzyskania dofinansowania, zobowiązuję się do uzupełnienia wniosku o niezbędne dokumenty w formie elektronicznej, weryfikujące dane i kwalifikowalność Wnioskodawcy (aktualny wypis z właściwego rejestru np. RIK, RIF – wystawiony nie wcześniej, niż trzy miesiące przed datą złożenia wniosku, statut, zaświadczenie o nadaniu numeru REGON, decyzję o nadaniu numeru NIP, umowę spółki cywilnej itp.), dokumenty potwierdzające uprawnienie do reprezentowania Wnioskodawcy (akt powołania, mianowania, pełnomocnictwo itp.) i dokumenty potwierdzające sposób reprezentacji (jeżeli z zapisów tych dokumentów wynika uprawnienie do reprezentowania Wnioskodawcy np. statut, umowa spółki cywilnej.",
                "name": "AllNecessaryDocuments"
            },
            {
                "label": "Oświadczenie Wnioskodawcy o braku powiązań z podmiotami sankcjonowanymi:\n\nW związku z wejściem w życie dnia 16 kwietnia 2022 roku ustawy z dnia 13 kwietnia 2022 roku o szczególnych rozwiązaniach w zakresie przeciwdziałania wspieraniu agresji na Ukrainę oraz służących ochronie bezpieczeństwa narodowego (Dz.U. z 2022 r. poz. 835) (dalej „Ustawa o przeciwdziałaniu wspieraniu agresji”), która uzupełnia pakiet wiążących Polskę środków ograniczających (sankcji) przyjętych na poziomie Unii Europejskiej oraz międzynarodowym, celem egzekwowania tychże sankcji,</br>\nWnioskodawca składa oświadczenia jak poniżej.</br>\n</br>\n§ 1</br>\n1. Beneficjent oświadcza, że, bezpośrednio lub pośrednio:</br>\na) nie wspiera agresji Federacji Rosyjskiej na Ukrainę rozpoczętą w dniu 24 lutego 2022 r.,</br>\nb) nie wspiera naruszeń praw człowieka lub represji wobec społeczeństwa obywatelskiego i opozycji demokratycznej lub których działalność stanowi inne poważne zagrożenie dla demokracji lub praworządności w Federacji Rosyjskiej lub na Białorusi,</br>\nc) nie jest bezpośrednio związany z osobami lub podmiotami, które nie spełniają kryteriów o których mowa w lit. a i b powyżej, w szczególności ze względu na powiązania o charakterze osobistym, organizacyjnym, gospodarczym lub finansowym, lub wobec których istnieje prawdopodobieństwo wykorzystania w tym celu dysponowanych przez nie takich środków finansowych, funduszy lub zasobów gospodarczych,</br>\nd) nie uchyla się od jakichkolwiek środków ograniczających (sankcji), nie narusza przepisów nakładających sankcje ani nie ułatwia innym podmiotom uchylania się od sankcji.</br>\n</br>\n2. Beneficjent oświadcza, że nie znajduje się na liście osób i podmiotów, wobec których są stosowane środki ograniczające (sankcje), o których mowa w art. 2 ustawy o przeciwdziałaniu wspieraniu agresji, a w szczególności:</br>\na) nie jest wymieniony w wykazach określonych w rozporządzeniu Rady (WE) nr 765/2006 z dnia 18 maja 2006 r. dotyczącego środków ograniczających w związku z sytuacją na Białorusi i udziałem Białorusi w agresji Rosji wobec Ukrainy (dalej jako „Rozporządzenie 765/2006”),</br>\nb) nie jest wymieniony w wykazach określonych w rozporządzeniu Rady (UE) nr 269/2014 z dnia 17 marca 2014 r. w sprawie środków ograniczających w odniesieniu do działań podważających integralność terytorialną, suwerenność i niezależność Ukrainy lub im zagrażających (dalej jako „Rozporządzenie 269/2014”),</br>\nc) wobec Beneficjenta nie została wydana decyzja w sprawie wpisu na listę osób i podmiotów, wobec których są stosowane środki w celu przeciwdziałania wspieraniu agresji Federacji Rosyjskiej na Ukrainę, z zastosowaniem środka w postaci wykluczenia z postępowania o udzielenie zamówienia publicznego lub konkursu prowadzonego na podstawie ustawy z dnia 11 września 2019 r. - Prawo zamówień publicznych,</br>\nd) Beneficjent nie jest umieszczony w wykazie cudzoziemców, których pobyt na terytorium Rzeczypospolitej Polskiej jest niepożądany, o którym mowa w art. 434 ustawy z dnia 12 grudnia 2013 r. o cudzoziemcach (dalej jako „Ustawa o cudzoziemcach”),</br>\ne) w stosunku do Beneficjenta członkiem organów, pracownikiem szczebla kierowniczego lub beneficjentem rzeczywistym, w rozumieniu ustawy z dnia 1 marca 2018 r. o przeciwdziałaniu praniu pieniędzy oraz finansowaniu terroryzmu, ani ich krewnym (przy czym na potrzeby niniejszego oświadczenia krewny, w odniesieniu do osoby fizycznej, oznacza jej małżonka, rodzeństwo, zstępnych i wstępnych) nie jest osoba znajdująca się na liście osób i podmiotów, wobec których są stosowane środki ograniczające, o której mowa w art. 2 ustawy o przeciwdziałaniu wspierania agresji, w szczególności nie znajduje się w wykazach określonych w Rozporządzeniu 765/2006, Rozporządzeniu 269/2014 lub art. 434 Ustawy o cudzoziemcach,</br>\nf) w stosunku do Beneficjenta jednostką dominującą w rozumieniu art. 3 ust. 1 pkt 37 ustawy z dnia 29 września 1994 r. o rachunkowości nie jest podmiot wymieniony w wykazach określonych w Rozporządzeniu 765/2006 i Rozporządzeniu 269/2014;</br>\ng) żaden z udziałów w kapitale zakładowym Beneficjenta nie jest własnością bezpośrednio lub pośrednio, ani nie został na nim ustanowiony zastaw ani użytkowanie na rzecz podmiotów wobec których są stosowane środki ograniczające (sankcje), o których mowa w niniejszym § 2, lub jakiegokolwiek podmiotu lub osoby, która korzysta z kapitału lub finansowania zapewnionego przez taki podmiot ani władz rosyjskich; przy czym na potrzeby niniejszego oświadczenia przez władze rosyjskie należy rozumieć Federację Rosyjską (i jej kraje związkowe), federalne i lokalne władze państwowe, państwowe jednostki organizacyjne i przedsiębiorstwa państwowe, instytucje publiczne, wszelkie spółki i podmioty bezpośrednio lub pośrednio kontrolowane przez wyżej wymienione oraz wszelkie podmioty powiązane z wyżej wymienionymi.</br>\n</br>\n3. Ponadto Beneficjent oświadcza, że nie znajduje się na liście osób i podmiotów, wobec których są stosowane środki ograniczające (sankcje) nałożone przez Organizację Narodów Zjednoczonych, państwo członkowskie Organizacji Narodów Zjednoczonych lub każdą inną organizację międzyrządową wprowadzone w związku z naruszeniem integralności terytorialnej Ukrainy i inwazją na Ukrainę (w tym również aneksją Krymu i konfliktem w regionie Donbasu) przeciwko Federacji Rosyjskiej, Białorusi, wskazanym osobom fizycznym i podmiotom.</br>\n</br>\n§ 2</br>\n1. Beneficjent przyjmuje do wiadomości, że oświadczenia Beneficjenta, o których mowa w § 1 powyżej, dotyczą środków ograniczających (sankcji), które obowiązują w dniu zawarcia Umowy i powinny pozostać prawdziwe przez cały okres obowiązywania Umowy.</br>\n2. Beneficjent zobowiązuje się monitorować swoje inwestycje, relacje biznesowe i działalność gospodarczą/zawodową w celu zapewnienia zgodności z wyżej wymienionymi oświadczeniami, przy jednoczesnym dochowaniu należytej staranności ogólnie wymaganej w relacjach biznesowych.</br>\n3. Beneficjent zobowiązuje się niezwłocznie poinformować Polski Instytut Sztuki Filmowej o każdej zmianie okoliczności, o których mowa w § 1 powyżej, które wystąpiły, powstały lub istniały przed dniem zawarcia Umowy, a których nie był świadomy, lub które wystąpiły, powstały lub zaistniały po zawarciu Umowy.</br>\n</br>\n§ 3</br>\n1. W przypadku nieprawdziwości któregokolwiek ze złożonych oświadczeń, o których mowa w § 1 powyżej, Polski Instytut Sztuki Filmowej jest uprawniony do wypowiedzenia Umowy w trybie natychmiastowym i żądania zwrotu przekazanych środków finansowych wraz z odsetkami ustawowymi za opóźnienie liczonymi od dnia przekazania środków, w terminie wskazanym przez Polski Instytut Sztuki Filmowej, jednak nie dłuższym niż 14 dni od dnia doręczenia wezwania zwrotu.</br>\n2. Bez uszczerbku dla postanowień ust. 1, w przypadku, w którym na skutek niepełnych, nierzetelnych lub nieprawdziwych oświadczeń Beneficjenta na Polski Instytut Sztuki Filmowej nałożona zostanie jakakolwiek kara administracyjna, Beneficjent zobowiązuje się do zwrotu - regresowo na wezwanie Polskiego Instytutu Sztuki Filmowej - całości pokrytych kar oraz wszelkich związanych z tym wydatków, włączając koszty postępowania sądowego, arbitrażowego, administracyjnego lub ugodowego oraz koszty pomocy prawnej.</br>",
                "name": "ApplicantsOfNoTies"
            }
        ]

        part = self.create_part(
            title="VI. Oświadczenia",
            short_name="VI. Oświadczenia",
            chapters=[
                self.create_chapter(
                    title="Oświadczenia Wnioskodawcy co do charakteru przedsięwzięcia",
                    components=[
                        *[self.create_component(
                            component_type="checkbox",
                            label=chapter["label"],
                            name=f"natureOfProject{chapter["name"]}"
                        ) for chapter in nature_of_project]
                    ]
                ),
                self.create_chapter(
                    title="Wymagane oświadczenia Wnioskodawcy",
                    components=[
                        *[self.create_component(
                            component_type="checkbox",
                            label=chapter["label"],
                            name=f"statement{chapter["name"]}",
                            required=True
                        ) for chapter in required_statements]
                    ]
                ),
                self.create_chapter(
                    title="Inne ważne informacje",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="otherImportantInformations",
                            validators=[
                                self.validator.length_validator(max_value=1800)
                            ],
                            required=True
                        )
                    ]
                )
            ]
        )

        self.save_part(part)

    def create_application_schedule(self):
        part = self.create_part(
            title="IX. Harmonogram realizacji zadania",
            short_name="IX. Harmonogram",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Nazwa przedsięwzięcia",
                            name="projectNameRepeatSchedule",
                            read_only=True,
                            required=True,
                            calculation_rules=[
                                self.calculation_rule.copy_value(
                                    from_name="applicationTaskName"
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Uwaga!<br/>Harmonogram zadania powinien uwzględniać etapy: przygotowawczy (np. poszukiwania partnerów, zaproszenie uczestników, przygotowanie promocji wydarzenia itp.), realizacji zadania (np. wykonanie i/lub wysyłka materiałów promocyjnych, pokaz filmu na festiwalu) oraz podsumowania (ewaluacja i rozliczenie zadania – ostateczna data zakończenia realizacji zadania: dzień, miesiąc i rok). <br/>W zakresie każdego z tych etapów należy określić najważniejsze działania (tzw. „kamienie milowe” zadania) i terminy ich realizacji. <br/>- Harmonogram zadania powinien uwzględniać wszystkie działania wymienione w kosztorysie zadania.<br/>- Prosimy o chronologiczne ułożenie wszystkich pozycji harmonogramu.",
                    components=[]
                ),
                self.create_chapter(
                    multiple_forms_rules={
                        "minCount": 1,
                        "maxCount": 20
                    },
                    components=[
                        self.create_chapter(
                            title="Wydarzenie",
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
                                    name="taskActionDateStart",
                                    validators=[
                                        self.validator.related_local_date_lte_validator(
                                            field_name="taskActionDateEnd",
                                            message="Termin rozpoczęcia działania musi być wcześniejszy niż termin jego zakończenia."
                                        )
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="date",
                                    label="Termin do",
                                    name="taskActionDateEnd",
                                    validators=[
                                        self.validator.related_local_date_gte_validator(
                                            field_name="taskActionDateStart",
                                            message="Termin zakończenia działania musi być późniejszy niż termin jego rozpoczęcia."
                                        )
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="textarea",
                                    label="Działanie",
                                    name="taskActionDesc",
                                    help_text="Krótki opis działania",
                                    class_list=[
                                        "table-full",
                                        "col-span-2"
                                    ],
                                    validators=[
                                        self.validator.length_validator(max_value=250)
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    class_list={
                        "main": [
                            "dates"
                        ],
                        "sub": [
                            "dates-item"
                        ]
                    },
                    components=[
                        self.create_component(
                            component_type="date",
                            label="Rozpoczęcie realizacji przedsięwzięcia",
                            name="projectCommencement",
                            read_only=True,
                            required=True,
                            calculation_rules=[
                                self.calculation_rule.first_date(
                                    field="taskActionDateStart"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="date",
                            label="Zakończenie realizacji przedsięwzięcia",
                            name="projectCompletion",
                            read_only=True,
                            required=True,
                            calculation_rules=[
                                self.calculation_rule.last_date(
                                    field="taskActionDateStart"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="date",
                            label="Termin rozliczenia z PISF",
                            name="settlementDeadline",
                            read_only=True,
                            required=True,
                            calculation_rules=[
                                self.calculation_rule.relate_to_last_date(
                                    field="projectCompletion",
                                    parameter=30
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        self.save_part(part)
