from classes_new.form_builder.form_builder import ApplicationFormBuilder
from classes_new.form_components.section.dwm.section import DWMSection


class DWMDepartmentApplicationFormBuilder(ApplicationFormBuilder):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.parts = [
            self.create_application_metadata,
            self.create_application_name_data,
            self.create_application_applicant_data,
            self.create_application_applicant_achievements_data,
            self.create_application_description_of_the_project_data,
            self.create_application_logo_data,
            self.create_application_implementation_effects_data,
            self.create_application_other_information_data,
            self.create_application_financial_data,
            self.create_application_statements,
            self.create_application_attachments,
            self.create_application_schedule_data
        ]

        self.section = DWMSection()

        self.requested_support_type: list[str] = []
        self.is_promotion_priority: bool = False
        self.grantee_vat_declaration: list[str] = []

    def create_application_metadata(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Metadane wniosku",
            chapters=[
                self.create_chapter(
                    title="1. Program",
                    components=[
                        self.create_component(
                            component_type="text",
                            name="programName",
                            read_only=True,
                            value=str(self.priority.operation_program)
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Priorytet",
                    components=[
                        self.create_component(
                            component_type="text",
                            name="priorityName",
                            read_only=True,
                            value=str(self.priority)
                        )
                    ]
                ),

            ]
        )

        if self.is_promotion_priority:
            chapters = [
                self.create_chapter(
                    title="3. Rodzaj przedsięwzięcia określony w programie operacyjnym",
                    components=[
                        self.create_component(
                            component_type="radio",
                            options=self.requested_support_type,
                            name="requestedSupportType",
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="4. Przedsięwzięcie dotyczy organizacji promocyjnych kampanii lub stoisk na międzynarodowych targach, festiwalach oraz innych wydarzeniach branżowych z udziałem polskich twórców filmowych, związanych z polską twórczością filmową zakwalifikowaną do:",
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="requestedSupportType",
                            values=[
                                "Organizowanie promocyjnych kampanii lub stoisk na międzynarodowych targach, festiwalach oraz innych wydarzeniach branżowych z udziałem polskich twórców filmowych, związanych z polską twórczością filmową zgodnie z ust. 2 pkt 1"
                            ]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="radio",
                            label="Rodzaj przedsięwzięcia - wyszczególnienie",
                            name="requestedSupportTypePkt1",
                            options=[
                                "międzynarodowych festiwali filmowych zaliczonych przez FIAPF do kategorii konkursowych festiwali filmów fabularnych",
                                "oficjalnej selekcji festiwali filmowych w Toronto, Telluride oraz konkursów międzynarodowych na festiwalach filmowych: Sundance, Busan, IDFA, HotDocs, Annecy, Visions du Réel, CPH:DOX",
                                "ubiegania się o prestiżowe międzynarodowe nagrody filmowe, tj. Nagrody Amerykańskiej Akademii Wiedzy i Sztuki Filmowej – Oscar, Złote Globy, Nagrody Brytyjskiej Akademii Filmowej – BAFTA, Nagrody Emmy oraz Nagrody European Film Awards"
                            ]
                        )
                    ]
                )
            ]

            for chapter in chapters:
                part["chapters"].append(chapter)
        else:
            part["chapters"].append(
                self.create_chapter(
                    title="3. Czy przedsięwzięcie jest związane z udziałem w targach branżowych, pitchingach lub prezentacjach Work in Progress?",
                    components=[
                        self.create_component(
                            component_type="radio",
                            name="wasRelatedToParticipation",
                            options=[
                                "Tak",
                                "Nie"
                            ],
                            required=True
                        )
                    ]
                )
            )

        self.save_part(part)

    def create_application_name_data(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Nazwa przedsięwzięcia, którego dotyczy wniosek",
            short_name=f"{self.helpers.int_to_roman(number)}. Nazwa przedsięwzięcia",
            chapters=[
                self.create_chapter(
                    title="1. Nazwa przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="applicationTaskName",
                            required=True,
                            validators=[
                                self.validator.length_validator(max_value=600)
                            ],
                            placeholder="Nazwa przedsięwzięcia"
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Nazwa i termin docelowego wydarzenia",
                    components=[
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
                                            component_type="text",
                                            label="Nazwa wydarzenia",
                                            name="eventName",
                                            required=True,
                                            class_list=[
                                                "table-full",
                                                "col-span-2"
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="date",
                                            label="Termin od",
                                            name="eventDateStart",
                                            required=True,
                                            validators=[
                                                self.validator.related_local_date_lte_validator(
                                                    field_name="eventDateEnd",
                                                    message="Data początkowa nie może być późniejsza niż data końcowa."
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="date",
                                            label="Termin do",
                                            name="eventDateEnd",
                                            required=True,
                                            validators=[
                                                self.validator.related_local_date_gte_validator(
                                                    field_name="eventDateStart",
                                                    message="Data końcowa nie może być wcześniejsza niż data początkowa."
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="3. Miasto i kraj, w którym odbywa sie wydarzenie",
                    components=[
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 1,
                                "maxCount": 20
                            },
                            components=[
                                self.create_chapter(
                                    title="Lokalizacja",
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
                                            component_type="country",
                                            label="Kraj",
                                            name="eventCountry",
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Miasto",
                                            name="eventLocation",
                                            required=True
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="4. Forma udziału Wnioskodawcy w wydarzeniu",
                    components=[
                        self.create_component(
                            component_type="radio",
                            options=[
                                "online",
                                "stacjonarnie/hybrydowo"
                            ],
                            name="eventParticipationType",
                            required=True
                        )
                    ]
                )
            ]
        )
        if self.is_promotion_priority:
            chapters = [
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="requestedSupportType",
                            values=[
                                "Organizowanie promocyjnych kampanii lub stoisk na międzynarodowych targach, festiwalach oraz innych wydarzeniach branżowych z udziałem polskich twórców filmowych, związanych z polską twórczością filmową zgodnie z ust. 2 pkt 1",
                                "Organizowanie promocyjnych kampanii lub stoisk na międzynarodowych targach, festiwalach oraz innych wydarzeniach branżowych z udziałem polskich twórców filmowych, związanych z polską twórczością filmową zgodnie z ust. 2 pkt 2"
                            ]
                        )
                    ],
                    components=[
                        self.create_chapter(
                            title="5. Projekt/film, z którym Wnioskodawca bierze udział w wydarzeniu",
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
                                    component_type="text",
                                    label="Tytuł filmu",
                                    name="eventMovieTitle",
                                    required=True,
                                    class_list=[
                                        "table-full"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Imię i nazwisko reżysera",
                                    name="eventMovieDirector",
                                    required=True,
                                    class_list=[
                                        "table-full"
                                    ]
                                ),
                                self.create_component(
                                    component_type="number",
                                    label="Metraż filmu w minutach",
                                    name="eventMovieDuration",
                                    required=True
                                ),
                                self.create_component(
                                    component_type="select",
                                    label="Rodzaj filmu",
                                    name="movieType",
                                    options=[
                                        "fabularny",
                                        "dokumentalny",
                                        "animowany"
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Sekcja na festiwalu",
                                    name="eventEventSession",
                                    help_text="Podaj sekcję na festiwalu, w której odbędzie się prezentacja filmu.",
                                    required=True,
                                    class_list=[
                                        "table-full"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Rodzaj premiery",
                                    name="eventMoviePremiereType",
                                    required=True
                                ),
                                self.create_component(
                                    component_type="number",
                                    label="Rok produkcji",
                                    name="movieProdYear",
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="6. Czy projekt/film został wsparty przez PISF?",
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="radio",
                                            name="wasMovieProjectSupportedByPisfPkt12",
                                            options=[
                                                "Tak",
                                                "Nie"
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
                                            field_name=f"wasMovieProjectSupportedByPisfPkt12",
                                            values=[
                                                "Tak"
                                            ]
                                        )
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            label="Program operacyjny",
                                            name=f"movieProjectSupportedByPisfProgramPkt12",
                                            required=True,
                                            class_list=[
                                                "col-span-2",
                                                "table-full"
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Priorytet",
                                            name=f"movieProjectSupportedByPisfPriorityPkt12",
                                            required=True,
                                            class_list=[
                                                "col-span-2",
                                                "table-full"
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Rok przyznania dofinansowania",
                                            name=f"movieProjectSupportedPisfYearPkt12",
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Kwota dofinansowania",
                                            name=f"movieProjectSupportedPisfAmountPkt12",
                                            unit="PLN",
                                            required=True
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
                            field_name="requestedSupportType",
                            values=[
                                "Organizowanie albo współorganizowanie poza granicami Polski wydarzeń promujących dorobek polskich twórców filmowych oraz polską twórczość filmową, w tym przeglądów, retrospektyw, wystaw, konferencji zgodnie z ust. 2 pkt 3",
                                "Organizowanie albo współorganizowanie w Polsce wizyt, spotkań zagranicznych inwestorów, producentów i twórców filmowych, które służą rozwojowi koprodukcji, usług filmowych oraz dystrybucji polskiej twórczości filmowej za granicą zgodnie z ust. 2 pkt 4",
                                "Organizowanie albo współorganizowanie z partnerami zagranicznymi wydarzeń dla przedstawicieli branży filmowej w formie szkoleń, warsztatów, prezentacji zgodnie z ust. 2 pkt 5"
                            ]
                        )
                    ],
                    components=[
                        self.create_chapter(
                            title="5. Czy poprzednia edycja wydarzenia zostałą wsparta przez PISF?",
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="radio",
                                            name="wasMovieProjectSupportedByPisfPkt345",
                                            options=[
                                                "Tak",
                                                "Nie"
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
                                    field_name="wasMovieProjectSupportedByPisfPkt345",
                                    values=[
                                        "Tak"
                                    ]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Kwota dofinansowania",
                                    name="eventPrevSupportedPisfAmount",
                                    required=True,
                                    unit="PLN"
                                )
                            ]
                        )
                    ]
                )
            ]
        else:
            chapters = [
                self.create_chapter(
                    title="5. Czy wniosek jest składany przynajmniej 30 dni przed rozpoczęciem wydarzenia?",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    name="isApplicationSubmittedEarly",
                                    options=[
                                        "Tak",
                                        "Nie"
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="isApplicationSubmittedEarly",
                                    values=[
                                        "Nie"
                                    ]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    label="Proszę o wskazanie powodów (zgodnie z trybem naboru i wyboru wniosków dla Priorytetu II: Stypendia zagraniczne, ust. 1 pkt 4). Brak wskazania uzasadnionych przyczyn opóźnienia może skutkować formalnym odrzuceniem wniosku",
                                    validators=[
                                        self.validator.length_validator(max_value=500)
                                    ],
                                    name="lateApplicationExplanation"
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="6. Główny cel udziały Wnioskodawcy w wydarzeniu",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    name="participationGoal",
                                    options=[
                                        "Festiwal",
                                        "Market",
                                        "Co-production market/pitching",
                                        "Warsztaty/szkolenia",
                                        "Inne wydarzenie branżowe"
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="participationGoal",
                                    values=[
                                        "Inne wydarzenie branżowe"
                                    ]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    label="Jakie?",
                                    name="otherEventDesc",
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
                    title="7. Projekt/film, z którym Wnioskodawca bierze udział w wydarzeniu",
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
                            component_type="text",
                            label="Tytuł filmu",
                            name="eventMovieTitle",
                            required=True,
                            class_list=[
                                "table-full"
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Imię i nazwisko reżysera",
                            name="eventMovieDirector",
                            required=True,
                            class_list=[
                                "table-full"
                            ]
                        ),
                        self.create_component(
                            component_type="number",
                            label="Metraż filmu w minutach",
                            name="eventMovieDuration",
                            required=True
                        ),
                        self.create_component(
                            component_type="select",
                            label="Rodzaj filmu",
                            name="movieType",
                            options=[
                                "fabularny",
                                "dokumentalny",
                                "animowany"
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Sekcja na festiwalu",
                            name="eventEventSession",
                            help_text="Podaj sekcję na festiwalu, w której odbędzie się prezentacja filmu.",
                            required=True,
                            class_list=[
                                "table-full"
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Rodzaj premiery",
                            name="eventMoviePremiereType",
                            required=True
                        ),
                        self.create_component(
                            component_type="number",
                            label="Rok produkcji",
                            name="movieProdYear",
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="8. Czy projekt/film został wsparty przez PISF?",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    name="wasMovieProjectSupportedByPisf",
                                    options=[
                                        "Tak",
                                        "Nie"
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
                                    field_name="wasMovieProjectSupportedByPisf",
                                    values=[
                                        "Tak"
                                    ]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="Program operacyjny",
                                    name="movieProjectSupportedByPisfProgram",
                                    required=True,
                                    class_list=[
                                        "col-span-2",
                                        "table-full"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Priorytet",
                                    name="movieProjectSupportedByPisfPriority",
                                    required=True,
                                    class_list=[
                                        "col-span-2",
                                        "table-full"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Rok przyznania dofinansowania",
                                    name="movieProjectSupportedPisfYear",
                                    required=True
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Kwota dofinansowania",
                                    name="movieProjectSupportedPisfAmount",
                                    unit="PLN",
                                    required=True
                                )
                            ]
                        )
                    ]
                )
            ]

        for chapter in chapters:
            part["chapters"].append(chapter)

        self.save_part(part=part)

    def create_application_applicant_data(self, number: int):
        chapters = [
            self.create_chapter(
                title=f"1. {'Pełna nazwa Wnioskodawcy (firma)' if self.is_promotion_priority else 'Imię i nazwisko Wnioskodawcy'}",
                components=[
                    self.create_component(
                        component_type="text",
                        name="applicantName",
                        required=True,
                        placeholder='Pełna nazwa Wnioskodawcy (firma)' if self.is_promotion_priority else 'Imię i nazwisko Wnioskodawcy'
                    )
                ]
            ),
            self.create_chapter(
                title="2. Osoby upoważnione do reprezentowania Wnioskodawcy, składania oświadczeń woli i zaciągania w jego imieniu zobowiązań finansowych",
                components=[
                    self.create_chapter(
                        multiple_forms_rules={
                            "minCount": 1,
                            "maxCount": 8
                        },
                        class_list={
                            "sub": [
                                "table-1-2-top"
                            ]
                        },
                        components=[
                            self.create_chapter(
                                title="Osoba upoważniona do reprezentowania Wnioskodawcy",
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
                                        component_type="text",
                                        label="Imię",
                                        name="eligiblePersonFirstName",
                                        required=True
                                    ),
                                    self.create_component(
                                        component_type="text",
                                        label="Nazwisko",
                                        name="eligiblePersonLastName",
                                        required=True
                                    ),
                                    self.create_component(
                                        component_type="text",
                                        label="Email",
                                        name="eligiblePersonEmail",
                                        required=True,
                                        validators=[
                                            self.validator.email_validator()
                                        ]
                                    ),
                                    self.create_component(
                                        component_type="text",
                                        label="Numer telefonu",
                                        name="eligiblePersonPhoneNum",
                                        required=True,
                                        mask="phoneNumber",
                                        validators=[
                                            self.validator.phone_number_validator()
                                        ]
                                    ),
                                    self.create_component(
                                        component_type="text",
                                        label="Stanowisko zgodnie z reprezentacją/ załączonym upoważnieniem",
                                        name="eligiblePersonPosition",
                                        required=True,
                                        class_list=[
                                            "table-full"
                                        ]
                                    )
                                ]
                            )
                        ]
                    )
                ]
            ) if self.is_promotion_priority else self.create_chapter(
                title="2. Funkcja pełniona przy projekcie",
                components=[
                    self.create_chapter(
                        components=[
                            self.create_component(
                                component_type="select",
                                name="applicantRole",
                                options=[
                                    "reżyser",
                                    "producent",
                                    "producent liniowy",
                                    "dystrybutor",
                                    "agent sprzedaży",
                                    "operator",
                                    "scenarzysta",
                                    "scenograf",
                                    "aktor/aktorka",
                                    "kompozytor",
                                    "montażysta",
                                    "kierownik produkcji",
                                    "inna"
                                ],
                                required=True,
                                placeholder="Funkcja pełniona przy projekcie"
                            )
                        ]
                    ),
                    self.create_chapter(
                        visibility_rules=[
                            self.visibility_rule.depends_on_value(
                                field_name="applicantRole",
                                values=[
                                    "inna"
                                ]
                            )
                        ],
                        components=[
                            self.create_component(
                                component_type="text",
                                label="Nazwa pełnionej funkcji przy projekcie",
                                name="applicantRoleOther",
                                required=True
                            )
                        ]
                    )
                ]
            ),
            self.create_chapter(
                title="3. Osoba odpowiedzialna za przygotowanie wniosku i kontakty z PISF",
                class_list={
                    "sub": [
                        "table-1-2-top"
                    ]
                },
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
                                component_type="text",
                                label="Imię",
                                name="authPersonFirstName",
                                required=True
                            ),
                            self.create_component(
                                component_type="text",
                                label="Nazwisko",
                                name="authPersonLastName",
                                required=True
                            ),
                            self.create_component(
                                component_type="text",
                                label="Numer telefonu stacjonarnego",
                                name="authPersonPhoneNum",
                                mask="landline",
                                required=True
                            ),
                            self.create_component(
                                component_type="text",
                                label="Numer telefonu komórkowego",
                                name="authPersonMobileNum",
                                mask="phoneNumber",
                                required=True,
                                validators=[
                                    self.validator.phone_number_validator()
                                ]
                            ),
                            self.create_component(
                                component_type="text",
                                label="Email kontaktowy",
                                name="authPersonEmail",
                                required=True,
                                validators=[
                                    self.validator.email_validator()
                                ],
                                class_list=[
                                    "col-span-2"
                                ]
                            )
                        ]
                    )
                ]
            ),
            self.section.create_full_address_section(
                name="applicant",
                who='Wnioskodawcy',
                number=4,
                main_poland=True,
                main_foreign=True,
                contact_poland=True,
                contact_foreign=True,
                is_local=False
            )
        ]

        if not self.is_promotion_priority:
            chapters.append(
                self.create_chapter(
                    title="5. Numery identyfikacyjne",
                    components=[
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="applicantResidence",
                                    values=[
                                        "w Polsce"
                                    ]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="Numer PESEL",
                                    name="applicantPesel",
                                    required=True,
                                    validators=[
                                        self.validator.pesel_validator()
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Właściwy urząd skarbowy",
                                    name="applicantTaxOffice",
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="applicantResidence",
                                    values=[
                                        "za granicą"
                                    ]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="Numer PESEL",
                                    name="applicantForeignPesel",
                                    required=True,
                                    validators=[
                                        self.validator.pesel_validator()
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Właściwy urząd skarbowy",
                                    name="applicantForeignTaxOffice",
                                    required=True
                                )
                            ]
                        )
                    ]
                )
            )

        chapters.extend(
            [
                self.section.applicant_bank_data(
                    number=5 if self.is_promotion_priority else 6,
                    poland=True,
                    foreign=True
                ),
                self.section.pisf_transfer_currency(
                    number=6 if self.is_promotion_priority else 7
                )
            ]
        )

        if self.is_promotion_priority:
            chapters.extend(
                [
                    self.section.applicant_legal_information(
                        number=7
                    ),
                    self.section.applicant_statistical_data(
                        number=8
                    )
                ]
            )

        chapters.append(
            self.create_chapter(
                components=[
                    self.create_component(
                        component_type="radio",
                        label=f"W przypadku otrzymania {'dofinansowania' if self.is_promotion_priority else 'stypendium'} od PISF proszę o przygotowanie umowy:",
                        name="contractPreparationIfReceivingFunding",
                        options=[
                            "w formie papierowej (do podpisu odręcznego)",
                            "w formie elektronicznej (do podpisu kwalifikowanym podpisem elektronycznym)"
                        ],
                        required=True
                    ),
                    self.create_component(
                        component_type="header",
                        value="<a target='_blank' rel='noopener noreferrer' href='https://biznes.gov.pl/pl/portal/0075' style='font-weight: bold; text-decoration: underline;'>Informacja na temat kwalifikowanych podpisów elektronicznych.</a>",
                        name="contractPreparationIfReceivingFundingSignatureInfo"
                    ),
                    self.create_component(
                        component_type="header",
                        value="Uwaga! W przypadku zmiany formy podpisania umowy Instytut może odstąpić od zawarcia umowy.",
                        name="contractPreparationIfReceivingFundingInfo"
                    )
                ]
            )
        )

        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Informacje o Wnioskodawcy",
            chapters=chapters
        )

        self.save_part(part=part)

    def create_application_applicant_achievements_data(self, number: int):
        pass

    def create_application_description_of_the_project_data(self, number: int):
        pass

    def create_application_logo_data(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Wskazanie sposobu wykorzystania logotypu PISF / Informacja o dofinansowaniu ze środków PISF w kampanii promocyjnej",
            short_name=f"{self.helpers.int_to_roman(number)}. Logotyp PISF",
            chapters=[
                self.create_chapter(
                    title="Opis wykorzystania logotypu lub informacji o dofinansowaniu",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="applicantLogotypePromotionDesc",
                            validators=[
                                self.validator.length_validator(max_value=20000)
                            ],
                            required=True,
                            help_text="Opisz w jaki sposób wykorzystasz logotyp PISF i/lub zamieścisz informację o dofinansowaniu ze środków PISF."
                        )
                    ]
                )
            ]
        )
        self.save_part(part=part)

    def create_application_implementation_effects_data(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Planowane efekty realizacji przedsięwzięcia",
            short_name=f"{self.helpers.int_to_roman(number)}. Efekty realizacji",
            chapters=[
                self.create_chapter(
                    title="Planowane efekty",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="applicantPlannedTaskEffects",
                            validators=[
                                self.validator.length_validator(max_value=20000)
                            ],
                            help_text=f"Opisz planowane efekty wykonania przedsięwzięcia. Należy podać konkretny efekt np. nawiązanie innej współpracy, zaproszenie na inny festiwal, itp. Po zakończeniu przedsięwzięcia {'Beneficjent' if self.is_promotion_priority else 'Stypendysta'} jest zobowiązany przedstawić w raporcie efekty przedsięwzięcia.",
                            required=True
                        )
                    ]
                )
            ]
        )
        self.save_part(part=part)

    def create_application_other_information_data(self, number: int):
        pass

    def create_application_financial_data(self, number: int):
        financing_source_chapters = [
            {
                "section_title": "Koszty akredytacji",
                "cost_title": "Koszty akredytacji",
                "name": "accreditation"
            },
            {
                "section_title": "Koszty noclegu",
                "cost_title": "Koszty noclegu",
                "name": "accommodation"
            },
            {
                "section_title": "Koszty transportu",
                "cost_title": "Koszty transportu",
                "name": "trasportation"
            },
            {
                "section_title": "Koszty uczesnictwa w warsztatach (jeśli dotyczy)",
                "cost_title": "Koszty uczestnictwa",
                "name": "participation"
            }
        ]

        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Koszty planowanego przedsięwzięcia",
            short_name=f"{self.helpers.int_to_roman(number)}. Koszty przedsięwzięcia",
            class_list=[
                "full-width-grid"
            ],
            chapters=[
                self.create_chapter(
                    title="Nazwa przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="applicationTaskNameRepeat",
                            calculation_rules=[
                                self.calculation_rule.copy_value(from_name="applicationTaskName")
                            ],
                            read_only=True,
                            placeholder="Nazwa przedsięwzięcia"
                        )
                    ]
                ),
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="radio",
                            name="granteeVatDeclaration",
                            required=True,
                            options=self.grantee_vat_declaration
                        )
                    ]
                ),
                self.create_chapter(
                    title="<normal>Uwaga! W przypadku braku automatycznego przeliczenia wartości finansowych prosimy o użycie przycisku „Przelicz i waliduj”, który znajduje się w prawym, dolnym rogu ekranu. Wymusi to dokonanie niezbędnych przeliczeń oraz podświetli nieuzupełnione pola formularza.</normal>"
                ),
                self.create_chapter(
                    components=[
                        self.create_chapter(
                            title="1. Koszty wg źródeł finansowania",
                            class_list={
                                "main": [
                                    "table-6-top"
                                ],
                                "sub": [
                                    "table-6-top__col"
                                ]
                            },
                            components=[
                                self.create_chapter(
                                    title=chapter["section_title"],
                                    class_list={
                                        "main": [
                                            "table-6",
                                            "grid",
                                            "grid-cols-2"
                                        ],
                                        "sub": [
                                            "table-6__col"
                                        ]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="textarea",
                                            label="Rodzaj kosztów",
                                            value=chapter["cost_title"],
                                            name=f"{chapter["name"]}Costs",
                                            read_only=True
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Koszt całkowity",
                                            name=f"{chapter["name"]}CostTotal",
                                            read_only=True,
                                            unit="PLN",
                                            calculation_rules=[
                                                self.calculation_rule.sum_inputs(
                                                    fields=[
                                                        f"{chapter["name"]}CostRequestPisf",
                                                        f"{chapter["name"]}CostOwnFunds",
                                                        f"{chapter["name"]}CostPartnersSponsors",
                                                        f"{chapter["name"]}CostOtherSources"
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        f"{chapter["name"]}CostRequestPisf",
                                                        f"{chapter["name"]}CostOwnFunds",
                                                        f"{chapter["name"]}CostPartnersSponsors",
                                                        f"{chapter["name"]}CostOtherSources"
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Wniosek o dotację PISF",
                                            name=f"{chapter["name"]}CostRequestPisf",
                                            unit="PLN"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Środki własne",
                                            name=f"{chapter["name"]}CostOwnFunds",
                                            unit="PLN"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Środki innych partnerów/sponsorów",
                                            name=f"{chapter["name"]}CostPartnersSponsors",
                                            unit="PLN"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Pozostałe źródła publiczne",
                                            name=f"{chapter["name"]}CostOtherSources",
                                            unit="PLN"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Udział wnioskowanej dotacji PISF we wskazanym rodzaju kosztów",
                                            name=f"{chapter["name"]}CostRequestPisfShare",
                                            unit="%",
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field=f"{chapter["name"]}CostRequestPisf",
                                                    divisor_field=f"{chapter["name"]}CostTotal"
                                                )
                                            ],
                                            read_only=True
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Udział środków własnych we wskazanym rodzaju kosztów",
                                            name=f"{chapter["name"]}CostOwnFundsShare",
                                            unit="%",
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field=f"{chapter["name"]}CostOwnFunds",
                                                    divisor_field=f"{chapter["name"]}CostTotal"
                                                )
                                            ],
                                            read_only=True
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Udział środków od partnerów/sponsorów we wskazanym rodzaju kosztów",
                                            name=f"{chapter["name"]}CostPartnersSponsorsShare",
                                            unit="%",
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field=f"{chapter["name"]}CostPartnersSponsors",
                                                    divisor_field=f"{chapter["name"]}CostTotal"
                                                )
                                            ],
                                            read_only=True
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Udział innych środków publicznych we wskazanym rodzaju kosztów",
                                            name=f"{chapter["name"]}CostOtherSourcesShare",
                                            unit="%",
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field=f"{chapter["name"]}CostOtherSources",
                                                    divisor_field=f"{chapter["name"]}CostTotal"
                                                )
                                            ],
                                            read_only=True
                                        )
                                    ]
                                ) for chapter in financing_source_chapters
                            ]
                        ),
                        self.create_chapter(
                            title="Źródła finansowania łącznie",
                            class_list={
                                "main": [
                                    "table-6-top"
                                ],
                                "sub": [
                                    "table-6-top__col"
                                ]
                            },
                            components=[
                                self.create_chapter(
                                    class_list={
                                        "main": [
                                            "table-6",
                                            "grid",
                                            "grid-cols-2"
                                        ],
                                        "sub": [
                                            "table-6__col"
                                        ]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Koszt całkowity",
                                            name="costTotalSum",
                                            read_only=True,
                                            unit="PLN",
                                            class_list=[
                                                "col-span-2"
                                            ],
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        f"{chapter["name"]}CostTotal" for chapter in financing_source_chapters
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        f"{chapter["name"]}CostTotal" for chapter in financing_source_chapters
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Wniosek o dotację PISF",
                                            name="costRequestPisfSum",
                                            read_only=True,
                                            unit="PLN",
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        f"{chapter["name"]}CostRequestPisf" for chapter in financing_source_chapters
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        f"{chapter["name"]}CostRequestPisf" for chapter in financing_source_chapters
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Środki własne",
                                            name="costOwnFundsSum",
                                            read_only=True,
                                            unit="PLN",
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        f"{chapter["name"]}CostOwnFunds" for chapter in financing_source_chapters
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        f"{chapter["name"]}CostOwnFunds" for chapter in financing_source_chapters
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Środki innych partnerów/sponsorów",
                                            name="costPartnersSponsorsSum",
                                            read_only=True,
                                            unit="PLN",
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        f"{chapter["name"]}CostPartnersSponsors" for chapter in financing_source_chapters
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        f"{chapter["name"]}CostPartnersSponsors" for chapter in financing_source_chapters
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Pozostałe źródła publiczne",
                                            name="costOtherSourcesSum",
                                            read_only=True,
                                            unit="PLN",
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        f"{chapter["name"]}CostOtherSources" for chapter in financing_source_chapters
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        f"{chapter["name"]}CostOtherSources" for chapter in financing_source_chapters
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    class_list={
                                        "main": [
                                            "table-6",
                                            "grid",
                                            "grid-cols-2"
                                        ],
                                        "sub": [
                                            "table-6__col"
                                        ]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Udział wnioskowanej dotacji PISF w kosztach razem",
                                            name="costRequestPisfSumShare",
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field="costRequestPisfSum",
                                                    divisor_field="costTotalSum"
                                                )
                                            ],
                                            read_only=True,
                                            validators=[
                                                self.validator.range_validator(
                                                    max_value=90,
                                                    message="Przekroczono maksymalny limit dofinansowania, który dla wybranego przedsięwzięcia wynosi: 90%. Wymagana będzie zgoda dyrektora PISF."
                                                )
                                            ],
                                            unit="%"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Udział środków własnych w kosztach razem",
                                            name="costOwnFundsSumShare",
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field="costOwnFundsSum",
                                                    divisor_field="costTotalSum"
                                                )
                                            ],
                                            read_only=True,
                                            validators=[
                                                self.validator.range_validator(
                                                    min_value=10,
                                                    message="Minimalny wkład własny Wnioskodawcy powinien wynosić 10% całości budżetu przedsięwzięcia."
                                                )
                                            ],
                                            unit="%"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Udział środków innych partnerów/sponsorów w kosztach razem",
                                            name="costPartnersSponsorsSumShare",
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field="costPartnersSponsorsSum",
                                                    divisor_field="costTotalSum"
                                                )
                                            ],
                                            read_only=True,
                                            unit="%",
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Udział innych środków publicznych w kosztach razem",
                                            name="costOtherSourcesSumShare",
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field="costOtherSourcesSum",
                                                    divisor_field="costTotalSum"
                                                )
                                            ],
                                            read_only=True,
                                            unit="%",
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    class_list={
                                        "main": [
                                            "table-6",
                                            "grid",
                                            "grid-cols-2"
                                        ],
                                        "sub": [
                                            "table-6__col"
                                        ]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Udział dotacji PISF oraz innych środków publicznych w kosztach razem",
                                            name="costPisfPublicShareInTotal",
                                            calculation_rules=[
                                                self.calculation_rule.sum_inputs(
                                                    fields=[
                                                        "costRequestPisfSumShare",
                                                        "costOtherSourcesSumShare"
                                                    ]
                                                )
                                            ],
                                            read_only=True,
                                            unit="%",
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        "costRequestPisfSumShare",
                                                        "costOtherSourcesSumShare"
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Udział środków własnych oraz środków innych partnerów/sponsorów w kosztach razem",
                                            name="costOwnPartnersSponsorsShareInTotal",
                                            calculation_rules=[
                                                self.calculation_rule.sum_inputs(
                                                    fields=[
                                                        "costOwnFundsSumShare",
                                                        "costPartnersSponsorsSumShare"
                                                    ]
                                                )
                                            ],
                                            read_only=True,
                                            unit="%",
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        "costOwnFundsSumShare",
                                                        "costPartnersSponsorsSumShare"
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ) if not self.is_promotion_priority else self.create_chapter(
                    components=[
                        self.create_chapter(
                            title="1. Koszty wg źródeł finansowania",
                            class_list={
                                "main": [
                                    "table-6-top",
                                ],
                                "sub": [
                                    "table-6-top__col",
                                ]
                            },
                            components=[
                                self.create_chapter(
                                    multiple_forms_rules={
                                        "minCount": 1,
                                        "maxCount": 20
                                    },
                                    components=[
                                        self.create_chapter(
                                            title="Koszt",
                                            class_list={
                                                "main": [
                                                    "table-6",
                                                    "grid",
                                                    "grid-cols-2",
                                                ],
                                                "sub": [
                                                    "table-6__col",
                                                ]
                                            },
                                            components=[
                                                self.create_component(
                                                    component_type="textarea",
                                                    label="Rodzaj kosztów",
                                                    name="costType",
                                                    validators=[
                                                        self.validator.length_validator(max_value=200)
                                                    ],
                                                    class_list=[
                                                        "col-span-2"
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Koszt całkowity",
                                                    name="costTotal",
                                                    read_only=True,
                                                    unit="PLN",
                                                    calculation_rules=[
                                                        self.calculation_rule.local_sum(
                                                            fields=[
                                                                "costRequestPisf",
                                                                "costOwnFunds",
                                                                "costPartnersSponsors",
                                                                "costOtherSources"
                                                            ]
                                                        )
                                                    ],
                                                    validators=[
                                                        self.validator.related_local_sum_validator(
                                                            field_names=[
                                                                "costRequestPisf",
                                                                "costOwnFunds",
                                                                "costPartnersSponsors",
                                                                "costOtherSources"
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Wniosek o dotację PISF",
                                                    name="costRequestPisf",
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Środki własne",
                                                    name="costOwnFunds",
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Środki innych partnerów/sponsorów",
                                                    name="costPartnersSponsors",
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Pozostałe źródła publiczne",
                                                    name="costOtherSources",
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Udział wnioskowanej dotacji PISF we wskazanym rodzaju kosztów",
                                                    name="costRequestPisfShare",
                                                    unit="%",
                                                    calculation_rules=[
                                                        self.calculation_rule.local_share_calculator(
                                                            dividend_field="costRequestPisf",
                                                            divisor_field="costTotal"
                                                        )
                                                    ],
                                                    read_only=True
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Udział środków własnych we wskazanym rodzaju kosztów",
                                                    name="costOwnFundsShare",
                                                    unit="%",
                                                    calculation_rules=[
                                                        self.calculation_rule.local_share_calculator(
                                                            dividend_field="costOwnFunds",
                                                            divisor_field="costTotal"
                                                        )
                                                    ],
                                                    read_only=True
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Udział środków od partnerów/sponsorów we wskazanym rodzaju kosztów",
                                                    name="costPartnersSponsorsShare",
                                                    unit="%",
                                                    calculation_rules=[
                                                        self.calculation_rule.local_share_calculator(
                                                            dividend_field="costPartnersSponsors",
                                                            divisor_field="costTotal"
                                                        )
                                                    ],
                                                    read_only=True
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Udział innych środków publicznych we wskazanym rodzaju kosztów",
                                                    name="costOtherSourcesShare",
                                                    unit="%",
                                                    calculation_rules=[
                                                        self.calculation_rule.local_share_calculator(
                                                            dividend_field="costOtherSources",
                                                            divisor_field="costTotal"
                                                        )
                                                    ],
                                                    read_only=True
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Źródła finansowania łącznie",
                            class_list={
                                "main": [
                                    "table-6-top"
                                ],
                                "sub": [
                                    "table-6-top__col"
                                ]
                            },
                            components=[
                                self.create_chapter(
                                    class_list={
                                        "main": [
                                            "table-6",
                                            "grid",
                                            "grid-cols-2"
                                        ],
                                        "sub": [
                                            "table-6__col"
                                        ]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Koszt całkowity",
                                            name="costTotalSum",
                                            read_only=True,
                                            unit="PLN",
                                            class_list=[
                                                "col-span-2"
                                            ],
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        "costTotal"
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        "costTotal"
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Wniosek o dotację PISF",
                                            name="costRequestPisfSum",
                                            read_only=True,
                                            unit="PLN",
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        "costRequestPisf"
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        "costRequestPisf"
                                                    ]
                                                ),
                                                self.validator.related_condition_ratio_validator(
                                                    field_name="costTotalSum",
                                                    conditions=[
                                                        {
                                                            "field_name": "requestedSupportType",
                                                            "value": "Organizowanie promocyjnych kampanii lub stoisk na międzynarodowych targach, festiwalach oraz innych wydarzeniach branżowych z udziałem polskich twórców filmowych, związanych z polską twórczością filmową zgodnie z ust. 2 pkt 1",
                                                            "max_ratio": 90,
                                                        },
                                                        {
                                                            "field_name": "requestedSupportType",
                                                            "value": "Organizowanie promocyjnych kampanii lub stoisk na międzynarodowych targach, festiwalach oraz innych wydarzeniach branżowych z udziałem polskich twórców filmowych, związanych z polską twórczością filmową zgodnie z ust. 2 pkt 2",
                                                            "max_ratio": 70
                                                        },
                                                        {
                                                            "field_name": "requestedSupportType",
                                                            "value": "Organizowanie albo współorganizowanie poza granicami Polski wydarzeń promujących dorobek polskich twórców filmowych oraz polską twórczość filmową, w tym przeglądów, retrospektyw, wystaw, konferencji zgodnie z ust. 2 pkt 3",
                                                            "max_ratio": 70
                                                        },
                                                        {
                                                            "field_name": "requestedSupportType",
                                                            "value": "Organizowanie albo współorganizowanie w Polsce wizyt, spotkań zagranicznych inwestorów, producentów i twórców filmowych, które służą rozwojowi koprodukcji, usług filmowych oraz dystrybucji polskiej twórczości filmowej za granicą zgodnie z ust. 2 pkt 4",
                                                            "max_ratio": 50
                                                        },
                                                        {
                                                            "field_name": "requestedSupportType",
                                                            "value": "Organizowanie albo współorganizowanie z partnerami zagranicznymi wydarzeń dla przedstawicieli branży filmowej w formie szkoleń, warsztatów, prezentacji zgodnie z ust. 2 pkt 5",
                                                            "max_ratio": 50
                                                        }
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Środki własne",
                                            name="costOwnFundsSum",
                                            read_only=True,
                                            unit="PLN",
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        "costOwnFunds"
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        "costOwnFunds"
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Środki innych partnerów/sponsorów",
                                            name="costPartnersSponsorsSum",
                                            read_only=True,
                                            unit="PLN",
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        "costPartnersSponsors"
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        "costPartnersSponsors"
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Pozostałe źródła publiczne",
                                            name="costOtherSourcesSum",
                                            read_only=True,
                                            unit="PLN",
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        "costOtherSources"
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        "costOtherSources"
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    class_list={
                                        "main": [
                                            "table-6",
                                            "grid",
                                            "grid-cols-2"
                                        ],
                                        "sub": [
                                            "table-6__col"
                                        ]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Udział wnioskowanej dotacji PISF w kosztach razem",
                                            name="costRequestPisfSumShare",
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field="costRequestPisfSum",
                                                    divisor_field="costTotalSum"
                                                )
                                            ],
                                            read_only=True,
                                            validators=[
                                                self.validator.related_condition_range_validator(
                                                    conditions=[
                                                        {
                                                            "field_name": "requestedSupportType",
                                                            "value": "Organizowanie promocyjnych kampanii lub stoisk na międzynarodowych targach, festiwalach oraz innych wydarzeniach branżowych z udziałem polskich twórców filmowych, związanych z polską twórczością filmową zgodnie z ust. 2 pkt 1",
                                                            "max_range": 90,
                                                            "message": "Przekroczono maksymalny limit dofinansowania, który dla wybranego przedsięwzięcia wynosi: 90%. Wymagana będzie zgoda dyrektora PISF."
                                                        },
                                                        {
                                                            "field_name": "requestedSupportType",
                                                            "value": "Organizowanie promocyjnych kampanii lub stoisk na międzynarodowych targach, festiwalach oraz innych wydarzeniach branżowych z udziałem polskich twórców filmowych, związanych z polską twórczością filmową zgodnie z ust. 2 pkt 2",
                                                            "max_range": 70,
                                                            "message": "Przekroczono maksymalny limit dofinansowania, który dla wybranego przedsięwzięcia wynosi: 70%. Wymagana będzie zgoda dyrektora PISF."
                                                        },
                                                        {
                                                            "field_name": "requestedSupportType",
                                                            "value": "Organizowanie albo współorganizowanie poza granicami Polski wydarzeń promujących dorobek polskich twórców filmowych oraz polską twórczość filmową, w tym przeglądów, retrospektyw, wystaw, konferencji zgodnie z ust. 2 pkt 3",
                                                            "max_range": 70,
                                                            "message": "Przekroczono maksymalny limit dofinansowania, który dla wybranego przedsięwzięcia wynosi: 70%. Wymagana będzie zgoda dyrektora PISF."
                                                        },
                                                        {
                                                            "field_name": "requestedSupportType",
                                                            "value": "Organizowanie albo współorganizowanie w Polsce wizyt, spotkań zagranicznych inwestorów, producentów i twórców filmowych, które służą rozwojowi koprodukcji, usług filmowych oraz dystrybucji polskiej twórczości filmowej za granicą zgodnie z ust. 2 pkt 4",
                                                            "max_range": 50,
                                                            "message": "Przekroczono maksymalny limit dofinansowania, który dla wybranego przedsięwzięcia wynosi: 50%. Wymagana będzie zgoda dyrektora PISF."
                                                        },
                                                        {
                                                            "field_name": "requestedSupportType",
                                                            "value": "Organizowanie albo współorganizowanie z partnerami zagranicznymi wydarzeń dla przedstawicieli branży filmowej w formie szkoleń, warsztatów, prezentacji zgodnie z ust. 2 pkt 5",
                                                            "max_range": 50,
                                                            "message": "Przekroczono maksymalny limit dofinansowania, który dla wybranego przedsięwzięcia wynosi: 50%. Wymagana będzie zgoda dyrektora PISF."
                                                        }
                                                    ]
                                                )
                                            ],
                                            unit="%"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Udział środków własnych w kosztach razem",
                                            name="costOwnFundsSumShare",
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field="costOwnFundsSum",
                                                    divisor_field="costTotalSum"
                                                )
                                            ],
                                            read_only=True,
                                            validators=[
                                                self.validator.range_validator(
                                                    min_value=10,
                                                    message="Minimalny wkład własny Wnioskodawcy powinien wynosić 10% całości budżetu przedsięwzięcia."
                                                )
                                            ],
                                            unit="%"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Udział środków innych partnerów/sponsorów w kosztach razem",
                                            name="costPartnersSponsorsSumShare",
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field="costPartnersSponsors",
                                                    divisor_field="costTotalSum"
                                                )
                                            ],
                                            read_only=True,
                                            unit="%"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Udział innych środków publicznych w kosztach razem",
                                            name="costOtherSourcesSumShare",
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field="costOtherSourcesSum",
                                                    divisor_field="costTotalSum"
                                                )
                                            ],
                                            read_only=True,
                                            unit="%"
                                        )
                                    ]
                                )
                            ]
                        ),
                    ]
                ),
                self.create_chapter(
                    title="2. Środki innych partnerów/sponsorów (wyłącznie udokumentowane deklaracjami i listami intencyjnymi)",
                    class_list={
                        "main": [
                            "table-2-top"
                        ]
                    },
                    components=[
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 1,
                                "maxCount": 20
                            },
                            class_list={
                                "main": [
                                    "table-2-multiple"
                                ]
                            },
                            components=[
                                self.create_chapter(
                                    title="Podmiot finansujący",
                                    class_list={
                                        "main": [
                                            "table-2",
                                            "grid",
                                            "grid-cols-2"
                                        ],
                                        "sub": [
                                            "table-2__col"
                                        ]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="textarea",
                                            label="Nazwa podmiotu finansującego",
                                            name="otherPartnersSponsorsName",
                                            class_list=[
                                                "table-2__col--textarea"
                                            ],
                                            validators=[
                                                self.validator.length_validator(max_value=200)
                                            ],
                                            help_text="Beneficjent powinien wpisać pełną nazwę podmiotu współfinansującego ze wskazaniem formy organizacyjno-prawnej."
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Kwota",
                                            name="otherPartnersSponsorsAmount",
                                            class_list=[
                                                "table-2__col--text"
                                            ],
                                            unit="PLN"
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Razem",
                            class_list={
                                "main": [
                                    "summary"
                                ]
                            },
                            components=[
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    name="otherPartnersSponsorsAmountSum",
                                    read_only=True,
                                    calculation_rules=[
                                        self.calculation_rule.dynamic_sum_inputs(
                                            fields=[
                                                "otherPartnersSponsorsAmount"
                                            ]
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_sum_validator(
                                            field_names=[
                                                "otherPartnersSponsorsAmount"
                                            ]
                                        ),
                                        self.validator.related_sum_validator(
                                            field_names=[
                                                "costPartnersSponsorsSum"
                                            ]
                                        )
                                    ],
                                    unit="PLN"
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="3. Pozostałe źródła publiczne (wyłącznie udokumentowane deklaracjami i listami intencyjnymi)",
                    class_list={
                        "main": [
                            "table-2-top"
                        ]
                    },
                    components=[
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 1,
                                "maxCount": 20
                            },
                            class_list={
                                "main": [
                                    "table-2-multiple"
                                ]
                            },
                            components=[
                                self.create_chapter(
                                    title="Podmiot publiczny",
                                    class_list={
                                        "main": [
                                            "table-2",
                                            "grid",
                                            "grid-cols-2"
                                        ],
                                        "sub": [
                                            "table-2__col"
                                        ]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="textarea",
                                            label="Nazwa podmiotu publicznego",
                                            name="otherSourcesName",
                                            class_list=[
                                                "table-2__col--textarea"
                                            ],
                                            validators=[
                                                self.validator.length_validator(max_value=200)
                                            ],
                                            help_text="Beneficjent powinien wpisać pełną nazwę podmiotu współfinansującego ze wskazaniem formy organizacyjno-prawnej."
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Kwota",
                                            name="otherSourcesAmount",
                                            class_list=[
                                                "table-2__col--text"
                                            ],
                                            unit="PLN"
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Razem",
                            class_list={
                                "main": [
                                    "summary"
                                ]
                            },
                            components=[
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    name="otherSourcesAmountSum",
                                    read_only=True,
                                    calculation_rules=[
                                        self.calculation_rule.dynamic_sum_inputs(
                                            fields=[
                                                "otherSourcesAmount"
                                            ]
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_sum_validator(
                                            field_names=[
                                                "otherSourcesAmount"
                                            ]
                                        ),
                                        self.validator.related_sum_validator(
                                            field_names=[
                                                "costOtherSourcesSum"
                                            ]
                                        )
                                    ],
                                    unit="PLN"
                                )
                            ]
                        )
                    ]
                )
            ]
        )

        if not self.is_promotion_priority:
            part["chapters"].extend([
                self.create_chapter(
                    title="4. Dodatkowe wyjaśnienia",
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Czy któryś z kosztów został zapewniony przez organizatora wydarzenia?",
                            name="isCostsCoveredByEventOrganizer"
                        )
                    ]
                ),
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="isCostsCoveredByEventOrganizer",
                            values=[
                                True
                            ]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="textarea",
                            label="Dodatkowe wyjaśnienia",
                            name="CostsCoveredByEventOrganizerInfo",
                            placeholder="Akredytacja/nocleg/transport została zapewniona przez organizatora wydarzenia."
                        )
                    ]
                )
            ])

        self.save_part(part=part)

    def create_application_statements(self, number: int):
        pass

    def create_application_attachments(self, number: int):
        pass

    def create_application_schedule_data(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Harmonogram realizacji przedsięwzięcia",
            short_name=f"{self.helpers.int_to_roman(number)}. Harmonogram",
            chapters=[
                self.create_chapter(
                    title="Nazwa przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="applicationTaskNameRepeatCopy",
                            calculation_rules=[
                                self.calculation_rule.copy_value(from_name="applicationTaskName")
                            ],
                            read_only=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="<normal>Uwaga!</br></br>-Harmonogram przedsięwzięcia powinien uwzględniać etapy: przygotowawczy (np. poszukiwania partnerów, zaproszenie uczestników, przygotowanie promocji wydarzenia itp.), realizacji przedsięwzięcia (np. wykonanie i/lub wysyłka materiałów promocyjnych, pokaz filmu na festiwalu) oraz podsumowania (ewaluacja i rozliczenie przedsięwzięcia - ostateczna data zakończenia realizacji przedsięwzięcia: dzień, miesiąc i rok). W zakresie każdego z tych etapów należy określić najwazniejsze działania (tzw. \"kamienie milowe\" przedsięwzięcia) i terminy ich realizacji.</br>- Harmonogram przedsięwzięcia powinien uwzględniać wszystkie działania wymienione w kosztorysie przedsięwzięcia i mieć charakter ciągły (brak przerw między kolejnymi pozycjami harmonogramu).</br>- Prosimy o chronologiczne ułożenie wszystkich pozycji harmonogramu.</br></br>Wymagane jest uwzględnienie przynajmniej 3 etapów realizacji przedsięwzięcia.",
                ) if self.is_promotion_priority else self.create_chapter(
                    title="<normal>Uwaga!</br></br>-Harmonogram przedsięwzięcia powinien uwzględniać wszystkie działania wymienione w kosztorysie przedsięwzięcia z wyraźnie wyodrębnioną pozycją dotyczącą pobytu na wydarzeniu.</br>- Harmonogram powinien mieć charakter ciągły (brak przerw między kolejnymi pozycjami harmonogramu) w przypadku wydarzeń niezwiązanych z warsztatami.</br>- Prosimy o chronologiczne ułożenie wszystkich pozycji harmonogramu.</br></br>Wymagane jest uwzględnienie przynajmniej 3 etapów realizacji przedsięwzięcia.",
                ),
                self.create_chapter(
                    multiple_forms_rules={
                        "minCount": 3,
                        "maxCount": 20
                    },
                    components=[
                        self.create_chapter(
                            title="Etap",
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
                                    name=f"taskActionDateStart",
                                    required=True,
                                    validators=[
                                        self.validator.related_local_date_lte_validator(
                                            field_name="taskActionDateEnd",
                                            message="Data początkowa musi być wcześniejsza od daty końcowej"
                                        )
                                    ]
                                ),
                                self.create_component(
                                    component_type="date",
                                    label="Termin do",
                                    name=f"taskActionDateEnd",
                                    required=True,
                                    validators=[
                                        self.validator.related_local_date_gte_validator(
                                            field_name="taskActionDateStart",
                                            message="Data końcowa musi być późniejsza od daty początkowej"
                                        )
                                    ]
                                ),
                                self.create_component(
                                    component_type="textarea",
                                    label="Działanie",
                                    name=f"taskActionDesc",
                                    help_text="Krótki opis działania",
                                    validators=[
                                        self.validator.length_validator(max_value=500)
                                    ],
                                    required=True,
                                    class_list=[
                                        "table-full",
                                        "col-span-2"
                                    ]
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
                            component_type="date",
                            label="Zakończenie realizacji przedsięwzięcia",
                            name="taskActionCompletionDate",
                            read_only=True,
                            calculation_rules=[
                                self.calculation_rule.last_date(field="taskActionDateEnd")
                            ],
                            validators=[
                                self.validator.related_last_date_validator(
                                    field_name="taskActionDateEnd"
                                )
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="date",
                            label="Maksymalny termin złożenia raportu końcowego do PISF",
                            name="taskActionSettlingDate",
                            read_only=True,
                            calculation_rules=[
                                self.calculation_rule.relate_to_last_date(
                                    field="taskActionDateEnd",
                                    parameter=30
                                )
                            ],
                            required=True
                        )
                    ]
                )
            ]
        )
        self.save_part(part=part)
