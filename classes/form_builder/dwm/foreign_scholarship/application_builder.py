from classes.form_builder.dwm.application_builder import DWMApplicationBuilder


class ForeignScholarshipApplicationBuilder(DWMApplicationBuilder):
    PRIORITY_NAME = 'II. Stypendia zagraniczne'
    PRIORITY_NUM = 2
    FORM_ID = 9193

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.department_data_path / 'foreign_scholarship'

    def create_application_metadata(self):
        part = self.create_part(
            title="I. Metadane wniosku",
            short_name="I. Metadane wniosku",
            chapters=[
                self.create_chapter(
                    title="1. Program",
                    components=[
                        self.create_component(
                            component_type="text",
                            name="programName",
                            read_only=True,
                            value=self.operation_name
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
                            value=self.priority_name
                        )
                    ]
                ),
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
            ]
        )
        self.save_part(part=part)

    def create_application_name_data(self):
        part = self.create_part(
            title="II. Nazwa przedsięwzięcia, którego dotyczy wniosek",
            short_name="II. Nazwa przedsięwzięcia",
            chapters=[
                self.create_chapter(
                    title="1. Nazwa przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="applicationTaskName",
                            required=True,
                            validators=[
                                {
                                    "name": "LengthValidator",
                                    "kwargs": {
                                        "max": 601
                                    },
                                    "validationMsg": "Maksymalna ilość znaków nie może przekroczyć 600."
                                }
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Nazwa i termin docelowego wydarzenia",
                    is_multiple_forms=True,
                    multiple_forms_rules={
                        "minCount": 1,
                        "maxCount": 20
                    },
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            label="Nazwa wydarzenia",
                                            name="eventName",
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
                                    components=[
                                        self.create_component(
                                            component_type="date",
                                            label="Termin od",
                                            name="eventDateStart",
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="date",
                                            label="Termin do",
                                            name="eventDateEnd",
                                            required=True,
                                            validators=[
                                                {
                                                    "name": "RelatedDateGTEValidator",
                                                    "kwargs": {
                                                        "field_name": "eventDateEnd"
                                                    },
                                                    "validationMsg": "Data końcowa nie może być wcześniejsza niż data początkowa."
                                                },
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
                    is_multiple_forms=True,
                    multiple_forms_rules={
                        "minCount": 1,
                        "maxCount": 20
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
                ),
                self.create_chapter(
                    title="4. Forma udziału wnioskodawcy w wydarzeniu",
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
                ),
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
                                {
                                    "name": "dependsOnValue",
                                    "kwargs": {
                                        "fieldName": "isApplicationSubmittedEarly",
                                        "values": [
                                            "Nie"
                                        ]
                                    }
                                }
                            ],
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    label="Proszę o wskazanie powodów (zgodnie z trybem naboru i wyboru wniosków dla Priorytetu II: Stypendia zagraniczne, ust. 1 pkt 4). Brak wskazania uzasadnionych przyczyn opóźnienia może skutkować formalnym odrzuceniem wniosku",
                                    validators=[
                                        {
                                            "name": "LengthValidator",
                                            "kwargs": {
                                                "max": 501
                                            },
                                            "validationMsg": "Maksymalna ilość znaków nie może przekroczyć 500."
                                        }
                                    ],
                                    name="lateApplicationExplanation"
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="6. Główny cel udziały wnioskodawcy w wydarzeniu",
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
                                {
                                    "name": "dependsOnValue",
                                    "kwargs": {
                                        "fieldName": "participationGoal",
                                        "values": [
                                            "Inne wydarzenie branżowe"
                                        ]
                                    }
                                }
                            ],
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    label="Jakie?",
                                    name="otherEventDesc",
                                    validators=[
                                        {
                                            "name": "LengthValidator",
                                            "kwargs": {
                                                "max": 101
                                            },
                                            "validationMsg": "Maksymalna ilość znaków nie może przekroczyć 100."
                                        }
                                    ],
                                    required=True
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="7. Projekt/film z którym wnioskodawca bierze udział w wydarzeniu",
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
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Imię i nazwisko reżysera",
                            name="eventMovieDirector",
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Metraż filmu w minutach",
                            name="eventMovieDuration",
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
                            required=True
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
                                {
                                    "name": "dependsOnValue",
                                    "kwargs": {
                                        "fieldName": "wasMovieProjectSupportedByPisf",
                                        "values": [
                                            "Tak"
                                        ]
                                    }
                                }
                            ],
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="Program operacyjny",
                                    name="movieProjectSupportedByPisfProgram",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "wasMovieProjectSupportedByPisf",
                                                "value": "Tak"
                                            }
                                        }
                                    ],
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
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "wasMovieProjectSupportedByPisf",
                                                "value": "Tak"
                                            }
                                        }
                                    ],
                                    class_list=[
                                        "col-span-2",
                                        "table-full"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Rok przyznania dofinansowania",
                                    name="movieProjectSupportedPisfYear",
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "wasMovieProjectSupportedByPisf",
                                                "value": "Tak"
                                            }
                                        }
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Kwota dofinansowania",
                                    name="movieProjectSupportedPisfAmount",
                                    value=0,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "wasMovieProjectSupportedByPisf",
                                                "value": "Tak"
                                            }
                                        }
                                    ],
                                    unit="PLN",
                                    required=True
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        self.save_part(part=part)

    def create_application_applicant_data(self):
        part = self.create_part(
            title="III. Informacje o wnioskodawcy",
            short_name="III. Informacje o wnioskodawcy",
            chapters=[
                self.create_chapter(
                    title="1. Imie i nazwisko wnioskodawcy",
                    components=[
                        self.create_component(
                            component_type="text",
                            name="applicantFullname",
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
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
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                {
                                    "name": "dependsOnValue",
                                    "kwargs": {
                                        "fieldName": "applicantRole",
                                        "values": [
                                            "inna"
                                        ]
                                    }
                                }
                            ],
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="Nazwa pełnionej funkcji przy projekcie",
                                    name="applicantRoleOther",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantRole",
                                                "value": "inna"
                                            }
                                        }
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="3. Osoba odpowiedzialna za przygotowanie wniosku i kontakty z PISF",
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
                            label="Numer telefonu",
                            mask="phoneNumber",
                            name="authPersonPhoneNum",
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Numer telefonu komórkowego",
                            mask="phoneNumber",
                            name="authPersonMobileNum",
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Email kontaktowy",
                            name="authPersonEmail",
                            required=True,
                            validators=[
                                {
                                    "name": "EmailValidator",
                                    "validationMsg": "Podaj prawidłowy adres email."
                                },
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="4. Adres i dane wnioskodawcy",
                    components=[
                        self.create_chapter(
                            title="4a. Adres zamieszkania",
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    name="applicantResidence",
                                    options=[
                                        "w Polsce",
                                        "za granicą"
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                {
                                    "name": "dependsOnValue",
                                    "kwargs": {
                                        "fieldName": "applicantResidence",
                                        "values": [
                                            "w Polsce"
                                        ]
                                    }
                                }
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
                                    component_type="select",
                                    label="Województwo",
                                    name="applicantVoivodeship",
                                    options=[
                                        "dolnośląskie",
                                        "kujawsko-pomorskie",
                                        "lubelskie",
                                        "lubuskie",
                                        "łódzkie",
                                        "małopolskie",
                                        "mazowieckie",
                                        "opolskie",
                                        "podkarpackie",
                                        "podlaskie",
                                        "pomorskie",
                                        "śląskie",
                                        "świętokrzyskie",
                                        "warmińsko-mazurskie",
                                        "wielkopolskie",
                                        "zachodniopomorskie"
                                    ],
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantResidence",
                                                "value": "w Polsce"
                                            }
                                        },
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Powiat",
                                    name="applicantCounty",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantResidence",
                                                "value": "w Polsce"
                                            }
                                        },
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Gmina",
                                    name="applicantMunicipality",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantResidence",
                                                "value": "w Polsce"
                                            }
                                        }
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Identyfikator gminy (Kod JST)",
                                    name="applicantJst",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantResidence",
                                                "value": "w Polsce"
                                            }
                                        }
                                    ],
                                    help_text="Kod JST gminy można znaleźć w wyszukiwarce pod adresem https://eteryt.stat.gov.pl/"
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Miejscowość",
                                    name="applicationLocation",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantResidence",
                                                "value": "w Polsce"
                                            }
                                        },
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Ulica",
                                    name="applicantStreet",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantResidence",
                                                "value": "w Polsce"
                                            }
                                        },
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Numer domu",
                                    name="applicantHouseNum",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantResidence",
                                                "value": "w Polsce"
                                            }
                                        },
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Numer lokalu",
                                    name="applicantApartmentNum"
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Kod pocztowy",
                                    name="applicantZipCode",
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantContactResidence",
                                                "value": "w Polsce"
                                            }
                                        }
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Poczta",
                                    name="applicantPostOffice"
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="phoneNumber",
                                    label="Numer telefonu",
                                    name="applicantPhoneNum"
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Email kontaktowy",
                                    name="applicantEmail",
                                    validators=[
                                        {
                                            "name": "EmailValidator",
                                            "validationMsg": "Podaj prawidłowy adres email."
                                        },
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                {
                                    "name": "dependsOnValue",
                                    "kwargs": {
                                        "fieldName": "applicantResidence",
                                        "values": [
                                            "za granicą"
                                        ]
                                    }
                                }
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
                                    component_type="text",
                                    label="Kraj",
                                    name="applicantCountry",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantResidence",
                                                "value": "za granicą"
                                            }
                                        },
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Miejscowość",
                                    name="applicationForeignLocation",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantResidence",
                                                "value": "za granicą"
                                            }
                                        },
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Ulica",
                                    name="applicantForeignStreet",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantResidence",
                                                "value": "za granicą"
                                            }
                                        },
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Numer domu",
                                    name="applicantForeignHouseNum",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantResidence",
                                                "value": "za granicą"
                                            }
                                        },
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Numer lokalu",
                                    name="applicantForeignApartmentNum"
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Kod pocztowy",
                                    name="applicantForeignZipCode",
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantResidence",
                                                "value": "za granicą"
                                            }
                                        }
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Poczta",
                                    name="applicantForeignPostOffice"
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="phoneNumber",
                                    label="Numer telefonu",
                                    name="applicantForeignPhoneNum"
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Email kontaktowy",
                                    name="applicantForeignEmail",
                                    validators=[
                                        {
                                            "name": "EmailValidator",
                                            "validationMsg": "Podaj prawidłowy adres email."
                                        },
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Należy zaznaczyć jeśli adres korespondencyjny jest inny",
                            name="applicantHasDifferentContactAddress"
                        )
                    ]
                ),
                self.create_chapter(
                    visibility_rules=[
                        {
                            "name": "dependsOnValue",
                            "kwargs": {
                                "fieldName": "applicantHasDifferentContactAddress",
                                "values": [
                                    True
                                ]
                            }
                        }
                    ],
                    components=[
                        self.create_chapter(
                            title="4b. Adres korespondencyjny",
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    name="applicantContactResidence",
                                    options=[
                                        "w Polsce",
                                        "za granicą"
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                {
                                    "name": "dependsOnValue",
                                    "kwargs": {
                                        "fieldName": "applicantContactResidence",
                                        "values": [
                                            "w Polsce"
                                        ]
                                    }
                                }
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
                                    component_type="select",
                                    label="Województwo",
                                    name="applicantContactVoivodeship",
                                    options=[
                                        "dolnośląskie",
                                        "kujawsko-pomorskie",
                                        "lubelskie",
                                        "lubuskie",
                                        "łódzkie",
                                        "małopolskie",
                                        "mazowieckie",
                                        "opolskie",
                                        "podkarpackie",
                                        "podlaskie",
                                        "pomorskie",
                                        "śląskie",
                                        "świętokrzyskie",
                                        "warmińsko-mazurskie",
                                        "wielkopolskie",
                                        "zachodniopomorskie"
                                    ],
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantContactResidence",
                                                "value": "w Polsce"
                                            }
                                        },
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Powiat",
                                    name="applicantContactCounty",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantContactResidence",
                                                "value": "w Polsce"
                                            }
                                        },
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Gmina",
                                    name="applicantContactMunicipality",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantContactResidence",
                                                "value": "w Polsce"
                                            }
                                        }
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Identyfikator gminy (Kod JST)",
                                    name="applicantContactJst",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantContactResidence",
                                                "value": "w Polsce"
                                            }
                                        }
                                    ],
                                    help_text="Kod JST gminy można znaleźć w wyszukiwarce pod adresem https://eteryt.stat.gov.pl/"
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Miejscowość",
                                    name="applicationContactLocation",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantContactResidence",
                                                "value": "w Polsce"
                                            }
                                        },
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Ulica",
                                    name="applicantContactStreet",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantContactResidence",
                                                "value": "w Polsce"
                                            }
                                        },
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Numer domu",
                                    name="applicantContactHouseNum",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantContactResidence",
                                                "value": "w Polsce"
                                            }
                                        },
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Numer lokalu",
                                    name="applicantContactApartmentNum"
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Kod pocztowy",
                                    name="applicantContactZipCode",
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantContactResidence",
                                                "value": "w Polsce"
                                            }
                                        }
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Poczta",
                                    name="applicantContactPostOffice"
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="phoneNumber",
                                    label="Numer telefonu",
                                    name="applicantContactPhoneNum"
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Email kontaktowy",
                                    name="applicantContactEmail",
                                    validators=[
                                        {
                                            "name": "EmailValidator",
                                            "validationMsg": "Podaj prawidłowy adres email."
                                        },
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                {
                                    "name": "dependsOnValue",
                                    "kwargs": {
                                        "fieldName": "applicantContactResidence",
                                        "values": [
                                            "za granicą"
                                        ]
                                    }
                                }
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
                                    component_type="text",
                                    label="Kraj",
                                    name="applicantContactCountry",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantContactResidence",
                                                "value": "za granicą"
                                            }
                                        },
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Miejscowość",
                                    name="applicationContactForeignLocation",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantContactResidence",
                                                "value": "za granicą"
                                            }
                                        },
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Ulica",
                                    name="applicantContactForeignStreet",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantContactResidence",
                                                "value": "za granicą"
                                            }
                                        },
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Numer domu",
                                    name="applicantContactForeignHouseNum",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantContactResidence",
                                                "value": "za granicą"
                                            }
                                        },
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Numer lokalu",
                                    name="applicantContactForeignApartmentNum"
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Kod pocztowy",
                                    name="applicantContactForeignZipCode",
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantContactResidence",
                                                "value": "za granicą"
                                            }
                                        }
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Poczta",
                                    name="applicantContactForeignPostOffice"
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="phoneNumber",
                                    label="Numer telefonu",
                                    name="applicantContactForeignPhoneNum"
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Email kontaktowy",
                                    name="applicantContactForeignEmail",
                                    validators=[
                                        {
                                            "name": "EmailValidator",
                                            "validationMsg": "Podaj prawidłowy adres email."
                                        },
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="4c. Numery identyfikacyjne",
                    components=[
                        self.create_chapter(
                            visibility_rules=[
                                {
                                    "name": "dependsOnValue",
                                    "kwargs": {
                                        "fieldName": "applicantResidence",
                                        "values": [
                                            "w Polsce"
                                        ]
                                    }
                                }
                            ],
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="Numer PESEL",
                                    name="applicantPesel",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "PeselValidator"
                                        },
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Właściwy urząd skarbowy",
                                    name="applicantTaxOffice",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantResidence",
                                                "value": "w Polsce"
                                            }
                                        }
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                {
                                    "name": "dependsOnValue",
                                    "kwargs": {
                                        "fieldName": "applicantResidence",
                                        "values": [
                                            "za granicą"
                                        ]
                                    }
                                }
                            ],
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="Numer PESEL",
                                    name="applicantForeignPesel",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "PeselValidator"
                                        },
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Właściwy urząd skarbowy",
                                    name="applicantForeignTaxOffice",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantResidence",
                                                "value": "za granicą"
                                            }
                                        }
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="5. Nazwa i numer rachunku bankowego",
                    components=[
                        self.create_chapter(
                            visibility_rules=[
                                {
                                    "name": "dependsOnValue",
                                    "kwargs": {
                                        "fieldName": "applicantResidence",
                                        "values": [
                                            "w Polsce"
                                        ]
                                    }
                                }
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
                                    component_type="text",
                                    label="Nazwa banku",
                                    name="applicantBank",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantResidence",
                                                "value": "w Polsce"
                                            }
                                        }
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Numer konta bankowego",
                                    mask="bankAccount",
                                    name="applicantBankAccountNum",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "LengthValidator",
                                            "kwargs": {
                                                "min": 26,
                                                "max": 27
                                            },
                                            "validationMsg": "Numer konta bankowego musi liczyć 26 cyfr."
                                        },
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantResidence",
                                                "value": "w Polsce"
                                            }
                                        }
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                {
                                    "name": "dependsOnValue",
                                    "kwargs": {
                                        "fieldName": "applicantResidence",
                                        "values": [
                                            "za granicą"
                                        ]
                                    }
                                }
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
                                    component_type="text",
                                    label="Nazwa banku",
                                    name="applicantForeignBank",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantResidence",
                                                "value": "za granicą"
                                            }
                                        }
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Numer IBAN",
                                    name="applicantIban",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "IBANValidator"
                                        },
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantResidence",
                                                "value": "za granicą"
                                            }
                                        }
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Kod SWIFT banku",
                                    name="applicantForeignBankSwift",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "SwiftValidator"
                                        },
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantResidence",
                                                "value": "za granicą"
                                            }
                                        }
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        self.save_part(part=part)

    def create_application_applicant_achievements_data(self):
        part = self.create_part(
            title="IV. Dotychczasowy dorobek i doświadczenie wnioskodawcy w dziedzinie, której wniosek dotyczy",
            short_name="IV. Dorobek wnioskodawcy",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="textarea",
                            label="CV wnioskodawcy (należy podać filmografię z informacją o pełnionej funkcji w projekcie oraz ew. nagrody filmu lub/i nagrody dla wnioskodawcy)",
                            name="applicantCv",
                            validators=[
                                {
                                    "name": "LengthValidator",
                                    "kwargs": {
                                        "max": 10001
                                    },
                                    "validationMsg": "Maksymalna ilość znaków nie może przekroczyć 10000."
                                },
                            ],
                            required=True
                        )
                    ]
                )
            ]
        )
        self.save_part(part=part)
