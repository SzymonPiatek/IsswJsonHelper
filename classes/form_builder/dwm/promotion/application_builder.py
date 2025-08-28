from classes.form_builder.dwm.application_builder import DWMApplicationBuilder


class PromotionApplicationBuilder(DWMApplicationBuilder):
    PRIORITY_NAME = 'I. Promocja polskiej twórczości filmowej za granicą'
    PRIORITY_NUM = 1
    FORM_ID = 9192

    def __init__(self):
        super().__init__()

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
                                self.validator.length_validator(max_value=600)
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Nazwa i termin docelowego wydarzenia",
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
                                                    "name": "RelatedDateGTEself.validator",
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
                                            validators=[
                                                {
                                                    "name": "RelatedRequiredIfEqualself.validator",
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
                                                    "name": "RelatedRequiredIfEqualself.validator",
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
                                                    "name": "RelatedRequiredIfEqualself.validator",
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
                                                    "name": "RelatedRequiredIfEqualself.validator",
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
                                    value=0,
                                    unit="PLN",
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualself.validator",
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
                self.dwm_section.applicant_name(number="1"),
                self.dwm_section.eligible_person_data(number="2"),
                self.dwm_section.responsible_person_data(number="3"),
                self.dwm_section.applicant_address(number="4", main_poland=True, contact_poland=True, main_foreign=True, contact_foreign=True),
                self.dwm_section.applicant_bank_data(number="5", poland=True, foreign=True),
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
                self.dwm_section.applicant_legal_information(number="7"),
                self.dwm_section.applicant_statistical_data(number="8")
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
                                self.visibility_rule.depends_on_value(
                                    field_name="applicantHasAccomplishedSimilarTasks",
                                    values=[
                                        "Tak"
                                    ]
                                )
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
                                            "name": "RelatedRequiredIfEqualself.validator",
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
                                self.validator.length_validator(max_value=10000)
                            ],
                            help_text="Podaj opis innych przedsięwzięć z zakresu kinematografii, podejmowanych w przeszłości (z uwzględnieniem ich miejsca, zasięgu i partnerów).",
                            required=True
                        )
                    ]
                ),
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
                        self.create_component(
                            component_type="textarea",
                            label="Opis innych przedsięwzięc podjętych w przeszłości",
                            name="applicantDirectorCv",
                            validators=[
                                self.validator.length_validator(max_value=10000),
                                {
                                    "name": "RelatedRequiredIfEqualself.validator",
                                    "kwargs": {
                                        "field_name": "requestedSupportType",
                                        "value": "Organizowanie promocyjnych kampanii lub stoisk na międzynarodowych targach, festiwalach oraz innych wydarzeniach branżowych z udziałem polskich twórców filmowych, związanych z polską twórczością filmową zgodnie z ust. 2 pkt 1",
                                    }
                                },
                                {
                                    "name": "RelatedRequiredIfEqualself.validator",
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

    def create_application_description_of_the_project_data(self):
        part = self.create_part(
            title="V. Opis zaplanowanego przedsięwzięcia",
            short_name="V. Opis przedsięwzięcia",
            chapters=[
                self.create_chapter(
                    components=[
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
                                self.create_component(
                                    component_type="textarea",
                                    label="Należy podać opis, charakter wydarzenia oraz cel uczestnictwa wnioskodawcy",
                                    name="plannedTaskDesc",
                                    validators=[
                                        self.validator.length_validator(max_value=20000)
                                    ],
                                    help_text="Podaj opis innych przedsięwzięć z zakresu kinematografii, podejmowanych w przeszłości (z uwzględnieniem ich miejsca, zasięgu i partnerów).",
                                    required=True
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
                                    title="1. Plan, opis, charakter oraz cel wydarzenia",
                                    components=[
                                        self.create_component(
                                            component_type="textarea",
                                            name="plannedTaskDesc345",
                                            validators=[
                                                self.validator.length_validator(max_value=20000)
                                            ],
                                            help_text="Podaj opis innych przedsięwzięć z zakresu kinematografii, podejmowanych w przeszłości (z uwzględnieniem ich miejsca, zasięgu i partnerów).",
                                            required=True
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="2. Lista filmów planowanych do prezentacji podczas wydarzenia",
                                    components=[
                                        self.create_component(
                                            component_type="textarea",
                                            name="movieListToShow",
                                            validators=[
                                                self.validator.length_validator(max_value=20000)
                                            ],
                                            required=True
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="3. Lista gości wydarzenia z zaznaczeniem kraju pochodzenia",
                                    components=[
                                        self.create_component(
                                            component_type="textarea",
                                            name="questList",
                                            validators=[
                                                self.validator.length_validator(max_value=20000)
                                            ],
                                            help_text="Podaj listę gości wydarzenia z zaznaczeniem kraju pochodzenia",
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

    def create_application_other_information_data(self):
        part = self.create_part(
            title="VIII. Inne informacje",
            short_name="VIII. Inne informacje",
            chapters=[
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
                        self.create_component(
                            component_type="textarea",
                            label="1. Synposis filmu / opis projektu",
                            name="movieProjectDesc",
                            validators=[
                                self.validator.length_validator(max_value=20000)
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="2. Link do filmu",
                            name="movieLink",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="3. Potwierdzony udział partnerów w projekcie (wyłącznie udokumentowany deklaracjami i listami intencyjnymi)",
                            name="partnersParticipationConfirm",
                            validators=[
                                self.validator.length_validator(max_value=20000)
                            ],
                            required=True,
                            help_text="Opisz udział partnerów w projekcie."
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="4. Plan promocji (z uwzględnieniem kampanii reklamowych w prasie branżowej/mediach społecznościowych/obsługa PR)",
                            name="promotionPlan",
                            validators=[
                                self.validator.length_validator(max_value=20000)
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="5. Festiwale, warsztaty, pitchingi w których film/projekt dotychczas wziął udział",
                            name="previouesEventsMoviePromotion",
                            validators=[
                                self.validator.length_validator(max_value=20000)
                            ],
                            required=True,
                            help_text="Opisz festiwale, warsztaty. pitchingi lub inne wydarzenia, w którym film wziął już udział."
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
                        self.create_component(
                            component_type="textarea",
                            label="1. Potwierdzony udział partnerów w projekcie (wyłącznie udokumentowany deklaracjami i listami intencyjnymi)",
                            name="partnersParticipationConfirm345",
                            validators=[
                                self.validator.length_validator(max_value=20000)
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="2. Plan promocji (z uwzględnieniem kampanii reklamowych w prasie branżowej/mediach społecznościowych/obsługa PR)",
                            name="promotionPlan345",
                            validators=[
                                self.validator.length_validator(max_value=20000)
                            ],
                            required=True
                        )
                    ]
                )
            ]
        )
        self.save_part(part=part)

    def create_application_financial_data(self):
        part = self.create_part(
            title="IX. Koszty planowanego przedsięwzięcia",
            short_name="IX. Koszty przedsięwzięcia",
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
                            read_only=True
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
                            multiple_forms_rules={
                                "minCount": 1,
                                "maxCount": 20
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
                                            component_type="number",
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
                                            component_type="number",
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
                                            component_type="number",
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
                                            component_type="number",
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
                                            "table-6"
                                        ],
                                        "sub": [
                                            "table-6__col"
                                        ]
                                    },
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
                                            component_type="number",
                                            label="Udział wnioskodawnej dotacji PISF w kosztach razem",
                                            name="costRequestPisfSumShare1",
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
                                            component_type="number",
                                            label="Udział środków własnych w kosztach razem",
                                            name="costOwnFundsSumShare1",
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
                                                    message="Minimalny wkład własny wnioskodawcy powinien wynosić 10% całości budżetu przedsięwzięcia."
                                                )
                                            ],
                                            unit="%"
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Udział środków od partnerów/sponsorów w kosztach razem",
                                            name="costPartnersSponsorsSumShare1",
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
                                            component_type="number",
                                            label="Udział innych środków publicznych w kosztach razem",
                                            name="costOtherSourcesSumShare1",
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
                                ),
                                self.create_chapter(
                                    class_list={
                                        "main": [
                                            "table-6"
                                        ],
                                        "sub": [
                                            "table-6__col"
                                        ]
                                    },
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="requestedSupportType",
                                            values=[
                                                "Organizowanie promocyjnych kampanii lub stoisk na międzynarodowych targach, festiwalach oraz innych wydarzeniach branżowych z udziałem polskich twórców filmowych, związanych z polską twórczością filmową zgodnie z ust. 2 pkt 2",
                                                "Organizowanie albo współorganizowanie poza granicami Polski wydarzeń promujących dorobek polskich twórców filmowych oraz polską twórczość filmową, w tym przeglądów, retrospektyw, wystaw, konferencji zgodnie z ust. 2 pkt 3"
                                            ]
                                        )
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="number",
                                            label="Udział wnioskodawnej dotacji PISF w kosztach razem",
                                            name="costRequestPisfSumShare23",
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field="costRequestPisfSum",
                                                    divisor_field="costTotalSum"
                                                )
                                            ],
                                            read_only=True,
                                            validators=[
                                                self.validator.range_validator(
                                                    max_value=70,
                                                    message="Przekroczono maksymalny limit dofinansowania, który dla wybranego przedsięwzięcia wynosi: 70%. Wymagana będzie zgoda dyrektora PISF."
                                                )
                                            ],
                                            unit="%"
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Udział środków własnych w kosztach razem",
                                            name="costOwnFundsSumShare23",
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
                                                    message="Minimalny wkład własny wnioskodawcy powinien wynosić 10% całości budżetu przedsięwzięcia."
                                                )
                                            ],
                                            unit="%"
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Udział środków od partnerów/sponsorów w kosztach razem",
                                            name="costPartnersSponsorsSumShare23",
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
                                            component_type="number",
                                            label="Udział innych środków publicznych w kosztach razem",
                                            name="costOtherSourcesSumShare23",
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
                                ),
                                self.create_chapter(
                                    class_list={
                                        "main": [
                                            "table-6"
                                        ],
                                        "sub": [
                                            "table-6__col"
                                        ]
                                    },
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="requestedSupportType",
                                            values=[
                                                "Organizowanie albo współorganizowanie w Polsce wizyt, spotkań zagranicznych inwestorów, producentów i twórców filmowych, które służą rozwojowi koprodukcji, usług filmowych oraz dystrybucji polskiej twórczości filmowej za granicą zgodnie z ust. 2 pkt 4",
                                                "Organizowanie albo współorganizowanie z partnerami zagranicznymi wydarzeń dla przedstawicieli branży filmowej w formie szkoleń, warsztatów, prezentacji zgodnie z ust. 2 pkt 5"
                                            ]
                                        )
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="number",
                                            label="Udział wnioskodawnej dotacji PISF w kosztach razem",
                                            name="costRequestPisfSumShare45",
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field="costRequestPisfSum",
                                                    divisor_field="costTotalSum"
                                                )
                                            ],
                                            read_only=True,
                                            validators=[
                                                self.validator.range_validator(
                                                    max_value=50,
                                                    message="Przekroczono maksymalny limit dofinansowania, który dla wybranego przedsięwzięcia wynosi: 50%. Wymagana będzie zgoda dyrektora PISF."
                                                )
                                            ],
                                            unit="%"
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Udział środków własnych w kosztach razem",
                                            name="costOwnFundsSumShare45",
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
                                                    message="Minimalny wkład własny wnioskodawcy powinien wynosić 10% całości budżetu przedsięwzięcia."
                                                )
                                            ],
                                            unit="%"
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Udział środków od partnerów/sponsorów w kosztach razem",
                                            name="costPartnersSponsorsSumShare45",
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
                                            component_type="number",
                                            label="Udział innych środków publicznych w kosztach razem",
                                            name="costOtherSourcesSumShare45",
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
                                            ]
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
                                            ]
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
        self.save_part(part=part)

    def create_application_statements(self):
        part = self.create_part(
            title="X. Oświadczenia wnioskodawcy",
            short_name="X. Oświadczenia",
            chapters=[
                self.create_chapter(
                    title="1. Oświadczam, że przesięwzięcie ma charakter (można podać kilka):",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="checkbox",
                                    label="nie dotyczy",
                                    name="statementTaskNotApplicable"
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="statementTaskNotApplicable",
                                    values=[
                                        False
                                    ]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="checkbox",
                                    label="krajowy",
                                    name="statementTaskIsCountrywide"
                                ),
                                self.create_component(
                                    component_type="checkbox",
                                    label="międzynarodowy",
                                    name="statementTaskIsInternational"
                                ),
                                self.create_component(
                                    component_type="checkbox",
                                    label="lokalny",
                                    name="statementTaskIsLocal"
                                ),
                                self.create_component(
                                    component_type="checkbox",
                                    label="regionalny",
                                    name="statementTaskIsRegional"
                                ),
                                self.create_component(
                                    component_type="checkbox",
                                    label="ograniczonego kręgu odbiorców",
                                    name="statementTaskHasLimitedAudience"
                                ),
                                self.create_component(
                                    component_type="checkbox",
                                    label="ze względu na niską wartość komercyjną nie mogłoby się odbyć bez dofinansowania przez PISF",
                                    name="statementTaskHasLowCommercialValue"
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="2. Oświadczam, iż posiadam zasoby rzeczowe, finansowe i kadrowe niezbędne do realizacji przedsięwzięcia.",
                            required=True,
                            name="statementHaveSufficientResources"
                        ),
                        self.create_component(
                            component_type="checkbox",
                            label="3. Oświadczam, iż nie zalegam z płatnościami na rzecz podmiotów publiczno-prawnych.",
                            required=True,
                            name="statementNoPublicLiabilities"
                        ),
                        self.create_component(
                            component_type="checkbox",
                            label="4. Oświadczam, iż nie zachodzą przesłanki określone w art. 22 ust. 2 Ustawy u kinematografii, które uniemożliwiają udzielenie dofinansowania przez Polski Instytut Sztuki Filmowej.",
                            required=True,
                            name="statementEligibleForFunding"
                        ),
                        self.create_component(
                            component_type="checkbox",
                            label="5. Oświadczam, iż spełniam warunki do otrzymania dofinansowania określone w Ustawie o kinematografii, Rozporządzeniu Ministra Kultury w sprawie udzielenia przez PISF dofinansowania przedsięwzięć z zakresu kinematografii oraz Programie Operacyjnym V - Promocja polskiej twórczości filmowej za granicą",
                            required=True,
                            name="statementMeetConditions"
                        ),
                        self.create_component(
                            component_type="checkbox",
                            label="6. Oświadczam, że zapoznałem się z treścią i zasadami dofinansowania w ramach <a href='https://pisf.pl/wp-content/uploads/2024/12/Programy-Operacyjne-PISF-na-rok-2025.pdf' target=\"_blank\">V Programu Operacyjnego, Priorytet I: Promocja polskiej twórczości filmowej za granicą Polskiego Instytutu Sztuki Filmowej na rok 2025</a>",
                            required=True,
                            name="statementDeclareRead"
                        ),
                        self.create_component(
                            component_type="checkbox",
                            label="7. W przypadku uzyskania dofinansowania, zobowiązuję się do doręczenia do PISF aktualnego wypisu z właściwego rejestru (w zależności od formy prawnej: KRS – wystawionego nie wcześniej, niż trzy miesiące przed datą złożenia; RIK; RIF; zaświadczenia o wpisie do ewidencji działalności gospodarczej; lub innego), zaświadczenia o nadaniu numeru REGON, decyzji o nadaniu numeru NIP oraz umowy spółki cywilnej (jeśli dotyczy).",
                            required=True,
                            name="statementDeliverPromise"
                        ),
                        self.create_component(
                            component_type="checkbox",
                            label="8. Oświadczenie Wnioskodawcy o braku powiązań z podmiotami sankcjonowanymi:\n\nW związku z wejściem w życie dnia 16 kwietnia 2022 roku ustawy z dnia 13 kwietnia 2022 roku o szczególnych rozwiązaniach w zakresie przeciwdziałania wspieraniu agresji na Ukrainę oraz służących ochronie bezpieczeństwa narodowego (Dz.U. z 2022 r. poz. 835) (dalej „Ustawa o przeciwdziałaniu wspieraniu agresji”), która uzupełnia pakiet wiążących Polskę środków ograniczających (sankcji) przyjętych na poziomie Unii Europejskiej oraz międzynarodowym, celem egzekwowania tychże sankcji,</br>\nWnioskodawca składa oświadczenia jak poniżej.</br>\n</br>\n§ 1</br>\n1. Beneficjent oświadcza, że, bezpośrednio lub pośrednio:</br>\na) nie wspiera agresji Federacji Rosyjskiej na Ukrainę rozpoczętą w dniu 24 lutego 2022 r.,</br>\nb) nie wspiera naruszeń praw człowieka lub represji wobec społeczeństwa obywatelskiego i opozycji demokratycznej lub których działalność stanowi inne poważne zagrożenie dla demokracji lub praworządności w Federacji Rosyjskiej lub na Białorusi,</br>\nc) nie jest bezpośrednio związany z osobami lub podmiotami, które nie spełniają kryteriów o których mowa w lit. a i b powyżej, w szczególności ze względu na powiązania o charakterze osobistym, organizacyjnym, gospodarczym lub finansowym, lub wobec których istnieje prawdopodobieństwo wykorzystania w tym celu dysponowanych przez nie takich środków finansowych, funduszy lub zasobów gospodarczych,</br>\nd) nie uchyla się od jakichkolwiek środków ograniczających (sankcji), nie narusza przepisów nakładających sankcje ani nie ułatwia innym podmiotom uchylania się od sankcji.</br>\n</br>\n2. Beneficjent oświadcza, że nie znajduje się na liście osób i podmiotów, wobec których są stosowane środki ograniczające (sankcje), o których mowa w art. 2 ustawy o przeciwdziałaniu wspieraniu agresji, a w szczególności:</br>\na) nie jest wymieniony w wykazach określonych w rozporządzeniu Rady (WE) nr 765/2006 z dnia 18 maja 2006 r. dotyczącego środków ograniczających w związku z sytuacją na Białorusi i udziałem Białorusi w agresji Rosji wobec Ukrainy (dalej jako „Rozporządzenie 765/2006”),</br>\nb) nie jest wymieniony w wykazach określonych w rozporządzeniu Rady (UE) nr 269/2014 z dnia 17 marca 2014 r. w sprawie środków ograniczających w odniesieniu do działań podważających integralność terytorialną, suwerenność i niezależność Ukrainy lub im zagrażających (dalej jako „Rozporządzenie 269/2014”),</br>\nc) wobec Beneficjenta nie została wydana decyzja w sprawie wpisu na listę osób i podmiotów, wobec których są stosowane środki w celu przeciwdziałania wspieraniu agresji Federacji Rosyjskiej na Ukrainę, z zastosowaniem środka w postaci wykluczenia z postępowania o udzielenie zamówienia publicznego lub konkursu prowadzonego na podstawie ustawy z dnia 11 września 2019 r. - Prawo zamówień publicznych,</br>\nd) Beneficjent nie jest umieszczony w wykazie cudzoziemców, których pobyt na terytorium Rzeczypospolitej Polskiej jest niepożądany, o którym mowa w art. 434 ustawy z dnia 12 grudnia 2013 r. o cudzoziemcach (dalej jako „Ustawa o cudzoziemcach”),</br>\ne) w stosunku do Beneficjenta członkiem organów, pracownikiem szczebla kierowniczego lub beneficjentem rzeczywistym, w rozumieniu ustawy z dnia 1 marca 2018 r. o przeciwdziałaniu praniu pieniędzy oraz finansowaniu terroryzmu, ani ich krewnym (przy czym na potrzeby niniejszego oświadczenia krewny, w odniesieniu do osoby fizycznej, oznacza jej małżonka, rodzeństwo, zstępnych i wstępnych) nie jest osoba znajdująca się na liście osób i podmiotów, wobec których są stosowane środki ograniczające, o której mowa w art. 2 ustawy o przeciwdziałaniu wspierania agresji, w szczególności nie znajduje się w wykazach określonych w Rozporządzeniu 765/2006, Rozporządzeniu 269/2014 lub art. 434 Ustawy o cudzoziemcach,</br>\nf) w stosunku do Beneficjenta jednostką dominującą w rozumieniu art. 3 ust. 1 pkt 37 ustawy z dnia 29 września 1994 r. o rachunkowości nie jest podmiot wymieniony w wykazach określonych w Rozporządzeniu 765/2006 i Rozporządzeniu 269/2014;</br>\ng) żaden z udziałów w kapitale zakładowym Beneficjenta nie jest własnością bezpośrednio lub pośrednio, ani nie został na nim ustanowiony zastaw ani użytkowanie na rzecz podmiotów wobec których są stosowane środki ograniczające (sankcje), o których mowa w niniejszym § 2, lub jakiegokolwiek podmiotu lub osoby, która korzysta z kapitału lub finansowania zapewnionego przez taki podmiot ani władz rosyjskich; przy czym na potrzeby niniejszego oświadczenia przez władze rosyjskie należy rozumieć Federację Rosyjską (i jej kraje związkowe), federalne i lokalne władze państwowe, państwowe jednostki organizacyjne i przedsiębiorstwa państwowe, instytucje publiczne, wszelkie spółki i podmioty bezpośrednio lub pośrednio kontrolowane przez wyżej wymienione oraz wszelkie podmioty powiązane z wyżej wymienionymi.</br>\n</br>\n3. Ponadto Beneficjent oświadcza, że nie znajduje się na liście osób i podmiotów, wobec których są stosowane środki ograniczające (sankcje) nałożone przez Organizację Narodów Zjednoczonych, państwo członkowskie Organizacji Narodów Zjednoczonych lub każdą inną organizację międzyrządową wprowadzone w związku z naruszeniem integralności terytorialnej Ukrainy i inwazją na Ukrainę (w tym również aneksją Krymu i konfliktem w regionie Donbasu) przeciwko Federacji Rosyjskiej, Białorusi, wskazanym osobom fizycznym i podmiotom.</br>\n</br>\n§ 2</br>\n1. Beneficjent przyjmuje do wiadomości, że oświadczenia Beneficjenta, o których mowa w § 1 powyżej, dotyczą środków ograniczających (sankcji), które obowiązują w dniu zawarcia Umowy i powinny pozostać prawdziwe przez cały okres obowiązywania Umowy.</br>\n2. Beneficjent zobowiązuje się monitorować swoje inwestycje, relacje biznesowe i działalność gospodarczą/zawodową w celu zapewnienia zgodności z wyżej wymienionymi oświadczeniami, przy jednoczesnym dochowaniu należytej staranności ogólnie wymaganej w relacjach biznesowych.</br>\n3. Beneficjent zobowiązuje się niezwłocznie poinformować Polski Instytut Sztuki Filmowej o każdej zmianie okoliczności, o których mowa w § 1 powyżej, które wystąpiły, powstały lub istniały przed dniem zawarcia Umowy, a których nie był świadomy, lub które wystąpiły, powstały lub zaistniały po zawarciu Umowy.</br>\n</br>\n§ 3</br>\n1. W przypadku nieprawdziwości któregokolwiek ze złożonych oświadczeń, o których mowa w § 1 powyżej, Polski Instytut Sztuki Filmowej jest uprawniony do wypowiedzenia Umowy w trybie natychmiastowym i żądania zwrotu przekazanych środków finansowych wraz z odsetkami ustawowymi za opóźnienie liczonymi od dnia przekazania środków, w terminie wskazanym przez Polski Instytut Sztuki Filmowej, jednak nie dłuższym niż 14 dni od dnia doręczenia wezwania zwrotu.</br>\n2. Bez uszczerbku dla postanowień ust. 1, w przypadku, w którym na skutek niepełnych, nierzetelnych lub nieprawdziwych oświadczeń Beneficjenta na Polski Instytut Sztuki Filmowej nałożona zostanie jakakolwiek kara administracyjna, Beneficjent zobowiązuje się do zwrotu - regresowo na wezwanie Polskiego Instytutu Sztuki Filmowej - całości pokrytych kar oraz wszelkich związanych z tym wydatków, włączając koszty postępowania sądowego, arbitrażowego, administracyjnego lub ugodowego oraz koszty pomocy prawnej.</br>",
                            required=True,
                            name="applicantsStatementOfNoTies"
                        )
                    ]
                )
            ]
        )
        self.save_part(part=part)

    def create_application_attachments(self):
        part = self.create_part(
            title="XI. Obowiązkowe załączniki zgodnie z rodzajem przedsięwzięcia",
            short_name="XI. Załączniki",
            chapters=[
                self.create_chapter(
                    title="Deklaracje wkładu finansowego/rzeczowego lub listy intencyjne partnerów (dotyczy wszystkich rodzajów przedsięwzięć)",
                    multiple_forms_rules={
                        "minCount": 1,
                        "maxCount": 20
                    },
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="file",
                                    label="Plik",
                                    name="inputAttachments",
                                    required=True
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Oficjalne zaproszenie filmu / twórcy na festiwal",
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="requestedSupportType",
                            values=[
                                "Organizowanie promocyjnych kampanii lub stoisk na międzynarodowych targach, festiwalach oraz innych wydarzeniach branżowych z udziałem polskich twórców filmowych, związanych z polską twórczością filmową zgodnie z ust. 2 pkt 1",
                                "Organizowanie promocyjnych kampanii lub stoisk na międzynarodowych targach, festiwalach oraz innych wydarzeniach branżowych z udziałem polskich twórców filmowych, związanych z polską twórczością filmową zgodnie z ust. 2 pkt 2"
                            ]
                        )
                    ],
                    multiple_forms_rules={
                        "minCount": 1,
                        "maxCount": 20
                    },
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="file",
                                    label="Plik",
                                    name="invitationAttachment",
                                    required=True,
                                    validators=[
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "requestedSupportType",
                                                "value": "Organizowanie promocyjnych kampanii lub stoisk na międzynarodowych targach, festiwalach oraz innych wydarzeniach branżowych z udziałem polskich twórców filmowych, związanych z polską twórczością filmową zgodnie z ust. 2 pkt 1"
                                            }
                                        },
                                        {
                                            "name": "RelatedRequiredIfEqualValidator",
                                            "kwargs": {
                                                "field_name": "requestedSupportType",
                                                "value": "Organizowanie promocyjnych kampanii lub stoisk na międzynarodowych targach, festiwalach oraz innych wydarzeniach branżowych z udziałem polskich twórców filmowych, związanych z polską twórczością filmową zgodnie z ust. 2 pkt 2"
                                            }
                                        }
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Uwaga",
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Zapoznałem/łam się z poniższymi zasadami.<br/>- Wnioskodawca jest zobowiązany do przedstawienia rozliczenia dofinansowania zgodnie z warunkami określonymi w umowie o dofinansowanie, w tym w szczególności do przedłożenia raportu końcowego, który zawiera finansowe rozliczenie przedsięwzięcia, ocenę jakościową jego realizacji oraz dodatkowe materiały w postaci raportów dotyczących frekwencji, promocji i sprawozdań medialnych (WAŻNE: W przypadku dokumentów wystawionych w walucie obcej, należy przyjąć średni kurs NBP z dnia roboczego poprzedzającego wystawienie dokumentu księgowego).<br/>- Procentowy wkład dofinansowania PISF w finalnym budżecie przedsięwzięcia nie może przekroczyć wkładu zakładanego, określonego w umowie o dofinansowanie. Jeżeli faktycznie poniesiony koszt całkowity przedsięwzięcia okazał się niższy od planowanego lub beneficjent nie wykorzystał całego dofinansowania, należy dokonać zwrotu na rachunek PISF i dostarczyć wraz z raportem potwierdzenie przelewu.<br/>- Jedynie koszty poniesione od daty złożenia wniosku o dofinansowanie w ISSW do daty zakończenia przedsięwzięcia określonej w harmonogramie, mogą zostać uznane za koszty kwalifikowalne i opłacone z dofinasowania PISF (koszty poniesione przed datą złożenia wniosku o dofinansowanie nie będą uznane za koszty kwalifikowalne).<br/>- Wniosek o dofinansowanie wraz z załącznikami należy podpisać przy użyciu kwalifikowanego podpisu elektronicznego lub profilu zaufanego platformy E-PUAP.<br/>- Wszelkie załączniki do wniosku o dofinansowanie (w tym listy intencyjne, umowy z partnerami, itp.) wymagają poświadczenia za zgodność z oryginałem. Podpisanie wniosku o dofinansowanie przez wnioskodawcę kwalifikowanym podpisem elektronicznym lub profilem zaufanym platformy E-PUAP jest równoznaczne z poświadczeniem przez wnioskodawcę załączników do wniosku o dofinansowanie za zgodne z oryginałem.<br/>- Linki do zasobów zewnętrznych umieszczane we wniosku o dofinansowanie powinny zachować ważność co najmniej do czasu wydania decyzji przez Dyrektora PISF.<br/>- Do dokumentów przedkładanych do wniosku o dofinansowanie sporządzonych w językach obcych należy obligatoryjnie dołączyć tłumaczenie na język polski. wnioskodawca, na wniosek PISF, ma obowiązek przedstawić tłumaczenie przysięgłe wskazanego dokumentu.",
                            name="acknowledgeRules",
                            required=True
                        )
                    ]
                )
            ]
        )
        self.save_part(part=part)

    def create_application_schedule_data(self):
        part = self.create_part(
            title="XII. Harmonogram realizacji przedsięwzięcia",
            short_name="XII. Harmonogram",
            chapters=[
                self.create_chapter(
                    title="Nazwa przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="applciationTaskNameRepeats",
                            calculation_rules=[
                                self.calculation_rule.copy_value(from_name="applicationTaskName")
                            ],
                            read_only=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="<normal>Uwaga!\n\n-Harmonogram przedsięwzięcia powinien uwzględniać etapy: przygotowawczy (np. poszukiwania partnerów, zaproszenie uczestników, przygotowanie promocji wydarzenia itp.), realizacji przedsięwzięcia (np. wykonanie i/lub wysyłka materiałów promocyjnych, pokaz filmu na festiwalu) oraz podsumowania (ewaluacja i rozliczenie przedsięwzięcia – ostateczna data zakończenia realizacji przedsięwzięcia: dzień, miesiąc i rok). W zakresie każdego z tych etapów należy określić najważniejsze działania (tzw. „kamienie milowe” przedsięwzięcia) i terminy ich realizacji.\n- Harmonogram przedsięwzięcia powinien uwzględniać wszystkie działania wymienione w kosztorysie przedsięwzięcia.\n- Prosimy o chronologiczne ułożenie wszystkich pozycji harmonogramu.</normal>Wymagane jest uwzględnienie przynajmniej 3 etapów realizacji przedsięwzięcia.",
                    multiple_forms_rules={
                        "minCount": 3,
                        "maxCount": 20
                    },
                    components=[
                        self.create_chapter(
                            title=f"Pozycja {number}",
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
                                            component_type="date",
                                            label="Termin od",
                                            name=f"taskActionDateStart_{number}",
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="date",
                                            label="Termin do",
                                            name=f"taskActionDateEnd_{number}",
                                            required=True
                                        ),
                                    ]
                                ),
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="textarea",
                                            label="Działanie",
                                            name=f"taskActionDesc_{number}",
                                            help_text="Krótki opis działania",
                                            validators=[
                                                self.validator.length_validator(max_value=500)
                                            ],
                                            required=True
                                        )
                                    ]
                                )
                            ]
                        )
                        for number in range(1, 4)
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
