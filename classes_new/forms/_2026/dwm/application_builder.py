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

        if not self.is_promotion_priority:
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
                            component_type="text",
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
                title="2. Osoby upoważnione do reprezentowania wnioskodawcy, składania oświadczeń woli i zaciągania w jego imieniu zobowiązań finansowych",
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
                    ),
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
                ]
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
        pass

    def create_application_implementation_effects_data(self, number: int):
        pass

    def create_application_other_information_data(self, number: int):
        pass

    def create_application_financial_data(self, number: int):
        pass

    def create_application_statements(self, number: int):
        pass

    def create_application_attachments(self, number: int):
        pass

    def create_application_schedule_data(self, number: int):
        pass
