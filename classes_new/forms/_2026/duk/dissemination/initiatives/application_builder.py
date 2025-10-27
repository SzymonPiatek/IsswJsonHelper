from classes_new.forms._2026.duk.dissemination.application_builder import \
    DisseminationOperationalProgramApplicationFormBuilder
from classes_new.forms._2026.duk.pisf_structure import InitiativesPriority
from .estimate_data import estimate_sections_pt124, estimate_sections_pt3
from classes.form_builder.departments.duk._2026.estimate.application_estimate_builder import DUKApplicationEstimateBuilder


class InitiativesPriorityApplicationFormBuilder(DisseminationOperationalProgramApplicationFormBuilder):
    def __init__(self):
        super().__init__(
            priority=InitiativesPriority()
        )

        self.form_id = self.set_ids(
            local_id=20,
            uat_id=None
        )

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
            title=f"{self.helpers.int_to_roman(number)}. Zakres przedsięwzięcia i jego charakterystyka",
            short_name=f"{self.helpers.int_to_roman(number)}. Zakres przedsięwzięcia",
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
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Organizacja przeglądów, konkursów, wystaw i innych wydarzeń filmowych promujących sztukę filmową.",
                                    ]
                                )
                            ],
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
                        )
                    ]
                ),
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
                        ),
                        self.create_chapter(
                            title="2. Zakres przedsięwzięcia i jego charakterystyka",
                            components=[
                                self.create_chapter(
                                    title="Idea i charakter przedsięwzięcia",
                                    components=[
                                        self.create_component(
                                            component_type="textarea",
                                            name="characterAndGoalsOfProject",
                                            validators=[
                                                self.validator.length_validator(max_value=2000)
                                            ],
                                            required=True
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="Program przedsięwzięcia",
                                    components=[
                                        self.create_component(
                                            component_type="textarea",
                                            name="projectProgram",
                                            validators=[
                                                self.validator.length_validator(max_value=5000)
                                            ],
                                            required=True,
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="Wydarzenia towarzyszące",
                                    help_text="Np. spotkania z twórcami, warsztaty, retrospektywy, prelekcje",
                                    components=[
                                        self.create_component(
                                            component_type="textarea",
                                            name="accompanyingEvents",
                                            validators=[
                                                self.validator.length_validator(max_value=5000)
                                            ],
                                            required=True,
                                        ),
                                    ]
                                ),
                                self.create_chapter(
                                    title="Promocja przedsięwzięcia",
                                    components=[
                                        self.create_component(
                                            component_type="textarea",
                                            name="projectPromotion",
                                            validators=[
                                                self.validator.length_validator(max_value=1500)
                                            ],
                                            required=True,
                                        ),
                                    ]
                                ),
                                self.create_chapter(
                                    title="Dostępność przedsięwzięcia",
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
                                ),
                                self.create_chapter(
                                    title="Odbiorcy i uczestnicy",
                                    components=[
                                        self.create_component(
                                            component_type="textarea",
                                            name="audienceProfile",
                                            validators=[
                                                self.validator.length_validator(max_value=1000)
                                            ],
                                            required=True,
                                        ),
                                    ]
                                ),
                                self.create_chapter(
                                    title="Planowane efekty realizacji przedsięwzięcia",
                                    components=[
                                        self.create_component(
                                            component_type="textarea",
                                            name="plannedEffects",
                                            validators=[
                                                self.validator.length_validator(max_value=1000)
                                            ],
                                            required=True,
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="Doświadczenie wnioskodawcy i kompetencje zespołu",
                                    components=[
                                        self.create_component(
                                            component_type="textarea",
                                            name="applicantExperienceAndTeamCompetences",
                                            validators=[
                                                self.validator.length_validator(max_value=1500)
                                            ],
                                            required=True,
                                        ),
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
                                                "Organizacja przeglądów, konkursów, wystaw i innych wydarzeń filmowych promujących sztukę filmową.",
                                            ]
                                        ),
                                    ],
                                    components=[
                                        self.create_chapter(
                                            visibility_rules=[
                                                self.visibility_rule.depends_on_value(
                                                    field_name="undertakingForm",
                                                    values=[
                                                        "Przegląd"
                                                    ]
                                                ),
                                            ],
                                            components=[
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
                                                    components=[
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Filmy polskie i koprodukcje",
                                                            name="polishFilmsAndCoproductionsPt1",
                                                            unit="szt."
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Filmy zagraniczne",
                                                            name="foreignFilmsPt1",
                                                            unit="szt."
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Filmy z audiodeskrypcją",
                                                            name="filmsWithAudioDescriptionPt1",
                                                            unit="szt."
                                                        ),
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
                                                    components=[
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Szacowana liczba widzów",
                                                            name="estimatedNumberOfViewersPt1",
                                                            unit="osoby"
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Ogólna liczba seansów",
                                                            name="totalNumberOfSeasonsPt1",
                                                            unit="szt."
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Liczba płatnych akredytacji",
                                                            name="numberOfPaidAccreditationsPt1",
                                                            unit="szt."
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Liczba bezpłatnych akredytacji",
                                                            name="numberOfFreeAccreditationsPt1",
                                                            unit="szt."
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_chapter(
                                            visibility_rules=[
                                                self.visibility_rule.depends_on_value(
                                                    field_name="undertakingForm",
                                                    values=[
                                                        "Wystawa"
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
                                                    label="Liczba prezentowanych prac/obiektów",
                                                    name="numberOfPresentedObjectsPt1",
                                                    unit="szt."
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Liczba twórców, instytucji lub partnerów, których prace/obiekty są prezentowane",
                                                    name="numberOfPresentedInstitutionsOrPartnersPt1",
                                                    unit="szt."
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Szacowana liczba zwiedzających",
                                                    name="estimatedNumberOfVisitorsPt1",
                                                    unit="szt."
                                                )
                                            ]
                                        ),
                                        self.create_chapter(
                                            visibility_rules=[
                                                self.visibility_rule.depends_on_value(
                                                    field_name="undertakingForm",
                                                    values=[
                                                        "Przegląd",
                                                        "Wystawa"
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
                                                    label="Liczba płatnych biletów",
                                                    name="numberOfPaidTicketsPt1",
                                                    unit="szt."
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Liczba bezpłatnych biletów",
                                                    name="numberOfFreeTicketsPt1",
                                                    unit="szt."
                                                )
                                            ]
                                        ),
                                        self.create_chapter(
                                            visibility_rules=[
                                                self.visibility_rule.depends_on_value(
                                                    field_name="undertakingForm",
                                                    values=[
                                                        "Konkurs"
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
                                                    label="Liczba nadesłanych prac",
                                                    name="numberOfSubmittedWorks",
                                                    unit="szt."
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Liczba uczestników",
                                                    name="numberOfParticipantsPt1",
                                                    unit="szt."
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Liczba przyznawanych nagród finansowych",
                                                    name="numberOfFinancialPrizesAwardedPt1",
                                                    unit="szt."
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
                                                "Organizacja kongresów, konferencji, sympozjów i inne działania edukacyjne pogłębiające wiedzę o filmie.",
                                            ]
                                        ),
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
                                            label="Szacowana liczba uczestników",
                                            name="estimatedNumberOfParticipantsPt2",
                                            unit="osoby"
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Liczba paneli, wykładów, warsztatów",
                                            name="numberOfPanelsPt2",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Liczba prelegentów i ekspertów biorących udział",
                                            name="numberOfSpeakersAndExpertsPt2",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Liczba płatnych akredytacji",
                                            name="numberOfPaidAccreditationsPt2",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Liczba bezpłatnych akredytacji",
                                            name="numberOfFreeAccreditationsPt2",
                                            unit="szt."
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="projectType",
                                            values=[
                                                "Inne działania realizujące cele Priorytetu II."
                                            ]
                                        ),
                                    ],
                                    components=[
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
                                            components=[
                                                self.create_component(
                                                    component_type="number",
                                                    label="Filmy polskie i koprodukcje",
                                                    name="polishFilmsAndCoproductionsPt4",
                                                    unit="szt."
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Filmy zagraniczne",
                                                    name="foreignFilmsPt4",
                                                    unit="szt."
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Filmy z audiodeskrypcją",
                                                    name="filmsWithAudioDescriptionPt4",
                                                    unit="szt."
                                                ),
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
                                            components=[
                                                self.create_component(
                                                    component_type="number",
                                                    label="Szacowana liczba widzów",
                                                    name="estimatedNumberOfViewersPt4",
                                                    unit="osoby"
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Ogólna liczba seansów",
                                                    name="totalNumberOfSeasonsPt4",
                                                    unit="szt."
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Liczba płatnych akredytacji",
                                                    name="numberOfPaidAccreditationsPt4",
                                                    unit="szt."
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Liczba bezpłatnych akredytacji",
                                                    name="numberOfFreeAccreditationsPt4",
                                                    unit="szt."
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Liczba płatnych biletów",
                                                    name="numberOfPaidTicketsPt4",
                                                    unit="szt."
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Liczba bezpłatnych biletów",
                                                    name="numberOfFreeTicketsPt4",
                                                    unit="szt."
                                                )
                                            ]
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
                                    components=[
                                        self.create_component(
                                            component_type="number",
                                            label="Zakres zastosowanych udogodnień zwiększających dostępność wydarzenia",
                                            name="rangeOfFacilitiesUsedToIncreaseEventAccessibility",
                                            required=True,
                                            unit="%"
                                        )
                                    ]
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
                                "Działalność Sieci Kin Studyjnych."
                            ]
                        )
                    ],
                    components=[
                        self.create_chapter(
                            title="Liczba zrzeszonych kin",
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
                                    name="affiliatedCinemasNumber",
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Zakres i kluczowe obszary programu Sieci Kin Studyjnych",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="scopeofArthouseCinemaNetworkProgram",
                                    validators=[
                                        self.validator.length_validator(max_value=5000)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Realizowane projekty filmowe",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="filmProjectsInProgress",
                                    validators=[
                                        self.validator.length_validator(max_value=5000)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Organizowane wydarzenia branżowe",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="organizedIndustryEvents",
                                    validators=[
                                        self.validator.length_validator(max_value=5000)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Działania na rzecz profesjonalizacji i reprezentacji zrzeszonych kin",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="activitiesForProfessionalizationAndRepresentation",
                                    validators=[
                                        self.validator.length_validator(max_value=5000)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Działania promocyjne Sieci Kin Studyjnych",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="promotionalActivitiesOfArthouseCinemaNetwork",
                                    validators=[
                                        self.validator.length_validator(max_value=5000)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Działania na rzecz dostępnych seansów i wydarzeń",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="actionsForAccessibleScreeningsAndEvents",
                                    validators=[
                                        self.validator.length_validator(max_value=5000)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Doświadczenie wnioskodawcy i kompetencje zespołu",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="applicantExperienceAndTeamCompetencesDsks",
                                    validators=[
                                        self.validator.length_validator(max_value=5000)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Planowane efekty realizowanych działań",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="plannedEffectsOfImplementedActivitiesDsks",
                                    validators=[
                                        self.validator.length_validator(max_value=5000)
                                    ],
                                    required=True
                                )
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
