from classes.form_builder.dwm.application_builder import DWMApplicationBuilder


class PromotionApplicationBuilder(DWMApplicationBuilder):
    PRIORITY_NAME = 'I. Promocja polskiej twórczości filmowej za granicą'
    PRIORITY_NUM = 1
    FORM_ID = 9192

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.department_data_path / 'promotion'

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
                    title="3. Rodzaj przedsięwzięcia określony w programie operacyjnym",
                    components=[
                        self.create_component(
                            component_type="radio",
                            options=[
                                "Organizowanie promocyjnych kampanii lub stoisk na międzynarodowych targach, festiwalach oraz innych wydarzeniach branżowych z udziałem polskich twórców filmowych, związanych z polską twórczością filmową zgodnie z ust. 2 pkt 1",
                                "Organizowanie promocyjnych kampanii lub stoisk na międzynarodowych targach, festiwalach oraz innych wydarzeniach branżowych z udziałem polskich twórców filmowych, związanych z polską twórczością filmową zgodnie z ust. 2 pkt 2",
                                "Organizowanie albo współorganizowanie poza granicami Polski wydarzeń promujących dorobek polskich twórców filmowych oraz polską twórczość filmową, w tym przeglądów, retrospektyw, wystaw, konferencji zgodnie z ust. 2 pkt 3",
                                "Organizowanie albo współorganizowanie w Polsce wizyt, spotkań zagranicznych inwestorów, producentów i twórców filmowych, które służą rozwojowi koprodukcji, usług filmowych oraz dystrybucji polskiej twórczości filmowej za granicą zgodnie z ust. 2 pkt 4",
                                "Organizowanie albo współorganizowanie z partnerami zagranicznymi wydarzeń dla przedstawicieli branży filmowej w formie szkoleń, warsztatów, prezentacji zgodnie z ust. 2 pkt 5"
                            ],
                            name="requestedSupportType"
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
                    visibility_rules=[
                        {
                            "name": "dependsOnValue",
                            "kwargs": {
                                "fieldName": "requestedSupportType",
                                "values": [
                                    "Organizowanie promocyjnych kampanii lub stoisk na międzynarodowych targach, festiwalach oraz innych wydarzeniach branżowych z udziałem polskich twórców filmowych, związanych z polską twórczością filmową zgodnie z ust. 2 pkt 1",
                                    "Organizowanie promocyjnych kampanii lub stoisk na międzynarodowych targach, festiwalach oraz innych wydarzeniach branżowych z udziałem polskich twórców filmowych, związanych z polską twórczością filmową zgodnie z ust. 2 pkt 2"
                                ]
                            }
                        }
                    ],
                    components=[
                        self.create_chapter(
                            title="5. Projekt/film, z którym wnioskodawca bierze udział w wydarzeniu",
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
                ),
                self.create_chapter(
                    visibility_rules=[
                        {
                            "name": "dependsOnValue",
                            "kwargs": {
                                "fieldName": "requestedSupportType",
                                "values": [
                                    "Organizowanie albo współorganizowanie poza granicami Polski wydarzeń promujących dorobek polskich twórców filmowych oraz polską twórczość filmową, w tym przeglądów, retrospektyw, wystaw, konferencji zgodnie z ust. 2 pkt 3",
                                    "Organizowanie albo współorganizowanie w Polsce wizyt, spotkań zagranicznych inwestorów, producentów i twórców filmowych, które służą rozwojowi koprodukcji, usług filmowych oraz dystrybucji polskiej twórczości filmowej za granicą zgodnie z ust. 2 pkt 4",
                                    "Organizowanie albo współorganizowanie z partnerami zagranicznymi wydarzeń dla przedstawicieli branży filmowej w formie szkoleń, warsztatów, prezentacji zgodnie z ust. 2 pkt 5"
                                ]
                            }
                        }
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
                                {
                                    "name": "dependsOnValue",
                                    "kwargs": {
                                        "fieldName": "wasMovieProjectSupportedByPisfPkt345",
                                        "values": [
                                            "Tak"
                                        ]
                                    }
                                }
                            ],
                            components=[
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Kwota dofinansowania",
                                    name="eventPrevSupportedPisfAmount",
                                    required=True,
                                    value=0,
                                    unit="PLN",
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "wasMovieProjectSupportedByPisfPkt345",
                                                "value": "Tak"
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

    def create_application_applicant_data(self):
        part = self.create_part(
            title="III. Informacje o wnioskodawcy",
            short_name="III. Informacje o wnioskodawcy",
            chapters=[
                self.create_chapter(
                    title="1. Pełna nazwa wnioskodawcy (firma)",
                    components=[
                        self.create_component(
                            component_type="text",
                            name="applicantName",
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Osoby upoważnione do reprezentowania wnioskodawcy, składania oświadczeń woli i zaciągania w jego imieniu zobowiązań finansowych",
                    is_multiple_forms=True,
                    multiple_forms_rules={
                        "minCount": 1,
                        "maxCount": 8
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
                                    label="Stanowisko zgodnie z reprezentacją/załączonym upoważnieniem",
                                    name="eligiblePersonPosition",
                                    required=True
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
                            title="4a. Adres siedziby",
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
                        self.create_chapter(
                            title="4c. Dane identyfikacyjne firmy",
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
                                    label="Numer NIP",
                                    name="applicantNip",
                                    validators=[
                                        {
                                            "name": "LengthValidator",
                                            "kwargs": {
                                                "min": 9,
                                                "max": 11
                                            },
                                            "validationMsg": "Niepoprawny numer NIP"
                                        },
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantResidence",
                                                "value": "w Polsce"
                                            }
                                        }
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Numer REGON",
                                    name="applicantRegon",
                                    validators=[
                                        {
                                            "name": "RegonValidator",
                                            "validationMsg": "Niepoprawny numer REGON"
                                        },
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantResidence",
                                                "value": "w Polsce"
                                            }
                                        }
                                    ],
                                    required=True
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
                ),
                self.create_chapter(
                    title="6. Waluta, z której dotacja PISF ma zostać przelana na w/w konto",
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
                            label="Waluta",
                            name="applicantCurrency",
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Waluta rozliczenia",
                            name="applicantCurrencySettlement",
                            read_only=True,
                            value="PLN"
                        )
                    ]
                ),
                self.create_chapter(
                    title="7. Informacje prawne",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="select",
                                    label="Forma organizacyjno-prawna",
                                    name="orgAndLegalStructure",
                                    options=[
                                        "Spółka z ograniczoną odpowiedzialnością",
                                        "Spółka akcyjna",
                                        "Spółka jawna",
                                        "Spółka komandytowa",
                                        "Spółka komandytowo-akcyjna",
                                        "Osoba fizyczna prowadząca działalność gospodarczą",
                                        "Spółka cywilna",
                                        "Fundacja",
                                        "Stowarzyszenie",
                                        "Instytucja kultury",
                                        "Instytucja filmowa",
                                        "Publiczna szkoła lub uczelnia artystyczna",
                                        "Niepubliczna szkoła lub uczelnia artystyczna",
                                        "Kościół lub związek wyznaniowy",
                                        "Jednostka samorządu terytorialnego",
                                        "Placówka dyplomatyczna",
                                        "Instytut Polski",
                                        "Inna (np. spółka w organizacji)"
                                    ],
                                    required=True,
                                    help_text="Wybierz formę organizacyjno-prawną wnioskodawcy."
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
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    label="Kod PKD zgodny z charakterem przedsięwzięcia, na realizację którego przeznaczona będzie pomoc z sektora kinematografii (uwzględniony w dokumencie rejestrowym, np. KRS, w dziale: przedmiot działalności, upoważniający do składania wniosku w danym programie operacyjnym)",
                                    name="applicantPkd",
                                    options=[
                                        "59.11 – Działalność związana z produkcją filmów, nagrań wideo i programów telewizyjnych",
                                        "59.12 - Działalność postprodukcyjna związana z filmami, nagraniami wideo i programami telewizyjnymi",
                                        "59.13 - Działalność związana z dystrybucją filmów, nagrań wideo i programów telewizyjnych",
                                        "59.14 - Działalność związana z projekcją filmów",
                                        "59.20 - Działalność w zakresie nagrań dźwiękowych i muzycznych"
                                    ],
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantResidence",
                                                "value": "w Polsce"
                                            }
                                        },
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Numer właściwego rejestru",
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
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="select",
                                            label="Typ rejestru",
                                            name="registrationType",
                                            options=[
                                                "KRS",
                                                "Ewidencja działalności gospodarczej",
                                                "Rejestr Instytucji Filmowych",
                                                "Rejestr Instytucji Kultury",
                                                "Inny"
                                            ],
                                            help_text="Wskaż rejestr, w którym Wnioskodawca został zarejestrowany.",
                                            required=True
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            label="Numer rejestru",
                                            name="registrationNumber",
                                            required=True
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        {
                                            "name": "dependsOnValue",
                                            "kwargs": {
                                                "fieldName": "registrationType",
                                                "values": [
                                                    "Inny"
                                                ]
                                            }
                                        }
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            label="Nazwa rejestru",
                                            name="registrationName",
                                            required=True,
                                            help_text="Podaj nazwę rejestru, w którym Wnioskodawca został zarejestrowany.",
                                            validators=[
                                                {
                                                    "name": "RelatedRequiredIfEqualValidator",
                                                    "kwargs": {
                                                        "field_name": "registrationType",
                                                        "value": "Inny"
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
                                                "fieldName": "registrationType",
                                                "values": [
                                                    "Ewidencja działalności gospodarczej",
                                                    "Rejestr Instytucji Filmowych",
                                                    "Rejestr Instytucji Kultury",
                                                    "Inny"
                                                ]
                                            }
                                        }
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            label="Prowadzony przez",
                                            name="registrationAuthority",
                                            required=True,
                                            help_text="Podaj nazwę podmiotu, który odpowiada za prowadzenie wskazanego rejestru."
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="8. Dane statystyczne",
                    components=[
                        self.create_chapter(
                            title="Przypisanie formy prawnej beneficjenta dla potrzeb statystycznych PUP",
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    label="Forma prawna",
                                    name="legalFormStats",
                                    options=[
                                        "przedsiębiorstwo państwowe",
                                        "jednoosobowa spółka Skarbu Państwa",
                                        "jednoosobowa spółka jednostki samorządu terytorialnego, w rozumieniu przepisów o gospodarce komunalnej",
                                        "spółka akcyjna albo spółka z o.o., jeżeli Skarb Państwa albo jednostka samorządu terytorialnego albo przedsiębiorstwo państwowe albo jednoosobowa spółka Skarbu Państwa mają wobec nich uprawnienia jak przedsiębiorca dominujący w rozumieniu przepisów o ochronie konkurencji i konsumentów",
                                        "jednostka sektora finansów publicznych w rozumieniu przepisów ustawy z dnia 27 sierpnia 2009 r. o finansach publicznych (Dz. U. z 2013 r. poz. 885, z późn. zm.)",
                                        "pozostali, którzy nie mieszczą się w klasyfikacji 1.A, 1.B, 1.C ani 1.D"
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Kod formy prawnej",
                                    name="legalFormCode",
                                    read_only=True,
                                    calculation_rules=[
                                        {
                                            "name": "assignValue",
                                            "kwargs": {
                                                "options": [
                                                    {
                                                        "fieldName": "legalFormStats",
                                                        "value": "przedsiębiorstwo państwowe",
                                                        "inputValue": "1.A"
                                                    },
                                                    {
                                                        "fieldName": "legalFormStats",
                                                        "value": "jednoosobowa spółka Skarbu Państwa",
                                                        "inputValue": "1.B"
                                                    },
                                                    {
                                                        "fieldName": "legalFormStats",
                                                        "value": "jednoosobowa spółka jednostki samorządu terytorialnego, w rozumieniu przepisów o gospodarce komunalnej",
                                                        "inputValue": "1.C"
                                                    },
                                                    {
                                                        "fieldName": "legalFormStats",
                                                        "value": "spółka akcyjna albo spółka z o.o., jeżeli Skarb Państwa albo jednostka samorządu terytorialnego albo przedsiębiorstwo państwowe albo jednoosobowa spółka Skarbu Państwa mają wobec nich uprawnienia jak przedsiębiorca dominujący w rozumieniu przepisów o ochronie konkurencji i konsumentów",
                                                        "inputValue": "1.D"
                                                    },
                                                    {
                                                        "fieldName": "legalFormStats",
                                                        "value": "jednostka sektora finansów publicznych w rozumieniu przepisów ustawy z dnia 27 sierpnia 2009 r. o finansach publicznych (Dz. U. z 2013 r. poz. 885, z późn. zm.)",
                                                        "inputValue": "1.E"
                                                    },
                                                    {
                                                        "fieldName": "legalFormStats",
                                                        "value": "pozostali, którzy nie mieszczą się w klasyfikacji 1.A, 1.B, 1.C ani 1.D",
                                                        "inputValue": "2"
                                                    }
                                                ]
                                            }
                                        }
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Określenie wielkości wnioskodawcy dla potrzeb statystycznych PUP",
                            components=[
                                self.create_component(
                                    component_type="select",
                                    label="Wielkość wnioskodawcy",
                                    name="applicantSize",
                                    options=[
                                        "mikroprzedsiębiorca (zatrudnia mniej niż 10 pracowników, a roczny obrót i/lub całkowity bilans roczny nie przekracza 2 milionów EUR)",
                                        "mały przedsiębiorca (zatrudnia mniej niż 50 pracowników, a roczny obrót i/lub całkowity bilans roczny nie przekracza 10 milionów EUR)",
                                        "średni przedsiębiorca (zatrudnia mniej niż 250 pracowników, a roczny obrót i/lub całkowity bilans roczny nie przekracza 50 milionów EUR)",
                                        "inny przedsiębiorca"
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Kod wielkości wnioskodawcy",
                                    name="applicantSizeCode",
                                    read_only=True,
                                    calculation_rules=[
                                        {
                                            "name": "assignValue",
                                            "kwargs": {
                                                "options": [
                                                    {
                                                        "fieldName": "applicantSize",
                                                        "value": "mikroprzedsiębiorca (zatrudnia mniej niż 10 pracowników, a roczny obrót i/lub całkowity bilans roczny nie przekracza 2 milionów EUR)",
                                                        "inputValue": "0"
                                                    },
                                                    {
                                                        "fieldName": "applicantSize",
                                                        "value": "mały przedsiębiorca (zatrudnia mniej niż 50 pracowników, a roczny obrót i/lub całkowity bilans roczny nie przekracza 10 milionów EUR)",
                                                        "inputValue": "1"
                                                    },
                                                    {
                                                        "fieldName": "applicantSize",
                                                        "value": "średni przedsiębiorca (zatrudnia mniej niż 250 pracowników, a roczny obrót i/lub całkowity bilans roczny nie przekracza 50 milionów EUR)",
                                                        "inputValue": "2"
                                                    },
                                                    {
                                                        "fieldName": "applicantSize",
                                                        "value": "inny przedsiębiorca",
                                                        "inputValue": "3"
                                                    }
                                                ]
                                            }
                                        }
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Sposób wykorzystania dofinansowania oraz rodzaj jednostki, której przekazywane są środki",
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="select",
                                            label="Cel dofinansowania",
                                            name="applicationGrantUsage",
                                            options=[
                                                "Wnioskowane dofinansowanie zostanie wykorzystane na realizację przedsięwzięć bieżących",
                                                "Wnioskowane dofinansowanie zostanie wykorzystane na finansowanie lub dofinansowanie kosztów realizacji inwestycji i zakupów inwestycyjnych"
                                            ],
                                            required=True
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="select",
                                            label="Rodzaj jednostki",
                                            name="applicationGrantUsageTargetEntity",
                                            options=[
                                                "Dla jednostek zaliczanych do sektora finansów publicznych wymienionych w art. 9 Ustawy o finansach publicznych",
                                                "Dla jednostek niezaliczanych do sektora finansów publicznych"
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
                                                "fieldName": "applicationGrantUsageTargetEntity",
                                                "values": [
                                                    "Dla jednostek zaliczanych do sektora finansów publicznych wymienionych w art. 9 Ustawy o finansach publicznych"
                                                ]
                                            }
                                        }
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="select",
                                            label="Rodzaj podmiotu",
                                            name="applicationGrantUsageTargetEntityType",
                                            options=[
                                                "Organy władzy publicznej, w tym organy administracji rządowej, organy kontroli państwowej i ochrony prawa oraz sądy i trybunały",
                                                "Jednostki samorządu terytorialnego oraz ich związki",
                                                "Jednostki budżetowe",
                                                "Samorządowe zakłady budżetowe",
                                                "Agencje wykonawcze",
                                                "Instytucja gospodarki budżetowej",
                                                "Państwowe fundusze celowe",
                                                "Zakład Ubezpieczeń Społecznych i zarządzane przez niego fundusze oraz Kasa Rolniczego Ubezpieczenia społecznego i fundusze zarządzane przez Prezesa Kasy Rolniczego Ubezpieczenia Społecznego",
                                                "Narodowy Fundusz Zdrowia",
                                                "Samodzielna publiczne zakłady opieki zdrowotnej",
                                                "Uczelnie publiczne",
                                                "Polska Akademia Nauk i tworzone przez nią jednostki organizacyjne",
                                                "Państwowe samorządowe instytucje kultury oraz państwowe instytucje filmowe",
                                                "Inne państwowe lub samorządowe osoby prawne utworzone na podstawie odrębnych ustaw w celu wykonywania przedsięwzięć publicznych, z wyłączeniem przedsiębiorstw, instytutów badawczych, banku w I spółek prawa handlowego"
                                            ],
                                            required=True
                                        )
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
                    title="1. Przy wnioskodawca realizował już przedsięwzięćie w dziedzienie, której wniosek dotyczy?",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    label="Doświadczenie wnioskodawcy",
                                    name="applicantHasAccomplishedSimilarTasks",
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
                                        "fieldName": "applicantHasAccomplishedSimilarTasks",
                                        "values": [
                                            "Tak"
                                        ]
                                    }
                                }
                            ],
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    label="Opis przedsięwzięć podjętych w przeszłości",
                                    name="applicantPrevTasksDesc",
                                    help_text="Podaj daty i krótki opis przedsięwzięć podjętych w przeszłości (z uwzględnieniem ich miejsca, zasięgu i partnerów).",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "applicantHasAccomplishedSimilarTasks",
                                                "value": "Tak"
                                            }
                                        }
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Wskazanie innych przedsięwzięć z zakresu kinematografii, podejmowanych w przeszłości (z uwzględnieniem ich miejsca, zasięgu i partnerów)",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            label="Opis innych przedsięwzięć podjętych w przeszłości",
                            name="applicantOtherPrevTasks",
                            validators=[
                                {
                                    "name": "LengthValidator",
                                    "kwargs": {
                                        "max": 10000
                                    },
                                    "validationMsg": "Maksymalna ilość znaków nie może przekroczyć 10000."
                                },
                            ],
                            help_text="Podaj opis innych przedsięwzięć z zakresu kinematografii, podejmowanych w przeszłości (z uwzględnieniem ich miejsca, zasięgu i partnerów).",
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    visibility_rules=[
                        {
                            "name": "dependsOnValue",
                            "kwargs": {
                                "fieldName": "requestedSupportType",
                                "values": [
                                    "Organizowanie promocyjnych kampanii lub stoisk na międzynarodowych targach, festiwalach oraz innych wydarzeniach branżowych z udziałem polskich twórców filmowych, związanych z polską twórczością filmową zgodnie z ust. 2 pkt 1",
                                    "Organizowanie promocyjnych kampanii lub stoisk na międzynarodowych targach, festiwalach oraz innych wydarzeniach branżowych z udziałem polskich twórców filmowych, związanych z polską twórczością filmową zgodnie z ust. 2 pkt 2"
                                ]
                            }
                        }
                    ],
                    components=[
                        self.create_component(
                            component_type="textarea",
                            label="Opis innych przedsięwzięc podjętych w przeszłości",
                            name="applicantDirectorCv",
                            validators=[
                                {
                                    "name": "LengthValidator",
                                    "kwargs": {
                                        "max": 10000
                                    },
                                    "validationMsg": "Maksymalna ilość znaków nie może przekroczyć 10000."
                                },
                                {
                                    "name": "RelatedRequiredIfEqualValidator",
                                    "kwargs": {
                                        "field_name": "requestedSupportType",
                                        "value": "Organizowanie promocyjnych kampanii lub stoisk na międzynarodowych targach, festiwalach oraz innych wydarzeniach branżowych z udziałem polskich twórców filmowych, związanych z polską twórczością filmową zgodnie z ust. 2 pkt 1",
                                    }
                                },
                                {
                                    "name": "RelatedRequiredIfEqualValidator",
                                    "kwargs": {
                                        "field_name": "requestedSupportType",
                                        "value": "Organizowanie promocyjnych kampanii lub stoisk na międzynarodowych targach, festiwalach oraz innych wydarzeniach branżowych z udziałem polskich twórców filmowych, związanych z polską twórczością filmową zgodnie z ust. 2 pkt 2"
                                    }
                                }
                            ],
                            required=True
                        )
                    ]
                )
            ]
        )
        self.save_part(part=part)
