from classes.form_builder.dpf.application_builder import DPFApplicationBuilder


class ScreenplayScholarshipApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'I. Stypendia scenariuszowe'
    PRIORITY_NUM = 1
    FORM_ID = 9194

    def __init__(self):
        super().__init__()

        self.task_type = "Stypendium scenariuszowe"
        self.priority_data_path = self.department_data_path / 'screenplay_scholarship'

    def create_application_basic_data(self):
        part = self.create_part(
            title='I. Dane podstawowe',
            short_name='I. Dane podstawowe',
            chapters=[
                self.section.application_basic_data.scope_of_project(
                    number="1",
                    options=[
                        "Stypendium scenariuszowe"
                    ]
                ),
                self.section.application_basic_data.movie_kind(
                    number="2",
                    options=[
                        "fabularny",
                        "dokumentalny",
                        "animowany"
                    ]
                ),
                self.section.application_basic_data.scope_of_project_kind(
                    number="3",
                    options=[
                        "stypendium scenariuszowe"
                    ]
                ),
                self.section.application_basic_data.movie_subject(
                    number="4",
                    options=[
                        "film autorski",
                        "film o tematyce historycznej",
                        "film dla młodego widza i widowni familijnej"
                    ],
                    validators=[
                        self.validator.related_allowed_options_validator(
                            field_name="movieKind",
                            mapping={
                                "fabularny": [
                                    "film autorski",
                                    "film o tematyce historycznej",
                                    "film dla młodego widza i widowni familijnej"
                                ],
                                "animowany": [
                                    "film autorski",
                                    "film o tematyce historycznej",
                                    "film dla młodego widza i widowni familijnej"
                                ],
                                "dokumentalny": [
                                    "film autorski",
                                    "film o tematyce historycznej"
                                ]
                            }
                        )
                    ]
                ),
                self.section.application_basic_data.piece_title(
                    number="5",
                ),
                self.section.application_basic_data.short_movie_description(
                    number="6",
                ),
                self.section.application_basic_data.application_relates(
                    number="7",
                    options=[
                        "umowa"
                    ]
                ),
                self.section.application_basic_data.kind_of_support(
                    number="8",
                    options=[
                        "stypendium scenariuszowe"
                    ]
                )
            ]
        )

        self.save_part(part)

    def create_application_applicant_data(self):
        part = self.create_part(
            title="II. Dane wnioskodawcy",
            short_name="II. Dane wnioskodawcy",
            chapters=[
                self.section.applicant_name(number="1"),
                self.section.applicant_type(number="2"),
                self.create_chapter(
                    title="3. Dane wnioskodawcy",
                    multiple_forms_rules={
                        "minCount": 1,
                        "maxCount": 5
                    },
                    components=[
                        self.create_chapter(
                            title="3.1. Dane identyfikacyjne wnioskodawcy",
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
                                    name="applicantFirstName",
                                    required=True
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Nazwisko",
                                    name="applicantLastName",
                                    required=True
                                ),
                                self.create_component(
                                    component_type="select",
                                    label="Płeć",
                                    name="applicantSex",
                                    required=True,
                                    options=[
                                        "Kobieta",
                                        "Mężczyzna",
                                        "Inna"
                                    ]
                                ),
                                self.create_component(
                                    component_type="country",
                                    label="Obywatelstwo",
                                    name="applicantCitizenship",
                                    required=True
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Numer PESEL",
                                    name="applicatnPeselNum",
                                    validators=[
                                        self.validator.pesel_validator()
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Seria i numer dowodu osobistego",
                                    required=True,
                                    name="applicantIdCardSeries"
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Numer telefonu",
                                    mask="phoneNumber",
                                    required=True,
                                    name="applicantPhoneNum",
                                    validators=[
                                        self.validator.phone_number_validator()
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Email",
                                    name="applicantPersonalEmail",
                                    required=True,
                                    validators=[
                                        self.validator.email_validator()
                                    ]
                                )
                            ]
                        ),
                        self.section.applicant_address(
                            number="3.2",
                            main_poland=True,
                            main_foreign=False,
                            contact_poland=True,
                            contact_foreign=True,
                            is_local=True
                        ),
                        self.section.applicant_bank_data(
                            number="3.3",
                            poland=True,
                            foreign=False
                        )
                    ]
                ),
                self.section.responsible_person_data(number="4")
            ]
        )

        self.save_part(part=part)

    def create_application_financial_data(self):
        part = self.create_part(
            title="V. Dane finansowe",
            short_name="V. Dane finansowe",
            class_list=[
                "full-width-grid"
            ],
            chapters=[
                self.create_chapter(
                    class_list={
                        "sub": [
                            "table-1-2-top"
                        ]
                    },
                    components=[
                        self.create_chapter(
                            title="1. Wnioskowana wysokość dofinansowania ze środków PISF",
                            class_list={
                                "main": [
                                    "full-width"
                                ],
                                "sub": [
                                    "full-width"
                                ]
                            },
                            components=[
                                self.create_chapter(
                                    class_list={
                                        "main": [
                                            "table-1-3",
                                            "grid",
                                            "grid-cols-3"
                                        ],
                                        "sub": [
                                            "table-1-3__col"
                                        ]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Kwota",
                                            name="requestedPisfSupportAmount",
                                            read_only=True,
                                            unit="PLN",
                                            calculation_rules=[
                                                self.calculation_rule.assign_value(
                                                    options=[
                                                        {
                                                            "fieldName": "movieKind",
                                                            "value": "fabularny",
                                                            "inputValue": 50000
                                                        },
                                                        {
                                                            "fieldName": "movieKind",
                                                            "value": "animowany",
                                                            "inputValue": 50000
                                                        },
                                                        {
                                                            "fieldName": "movieKind",
                                                            "value": "dokumentalny",
                                                            "inputValue": 35000
                                                        }
                                                    ]
                                                )
                                            ]
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

    def create_application_statements(self):
        part = self.create_part(
            title="VIII. Oświadczenia",
            short_name="VIII. Oświadczenia",
            chapters=[
                self.section.application_statements.applicant_statements(),
                self.section.application_statements.script_statements(),
                self.section.application_statements.storage_of_blank_public_documents()
            ]
        )

        self.save_part(part)

    def create_application_attachments(self):
        part = self.create_part(
            title="VII. Załączniki",
            short_name="VII. Załączniki",
            chapters=[
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="movieKind",
                            values=[
                                "fabularny",
                                "animowany"
                            ]
                        )
                    ],
                    components=[
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="movieKind",
                                    values=["animowany"]
                                )
                            ],
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="checkbox",
                                            label="Nie dotyczy zgodnie z Programem Operacyjnym PISF - Produkcja Filmowa",
                                            name="notDialogScene"
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="notDialogScene",
                                            values=[False]
                                        )
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="file",
                                            label="Scena dialogowa",
                                            name="dialogSceneAni",
                                            required=True
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="movieKind",
                                    values=["fabularny"]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="file",
                                    label="Scena dialogowa",
                                    name="dialogSceneFab",
                                    required=True
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    components=[
                        self.component.application_attachments.description_of_artistic_qualities()
                    ]
                ),
                self.section.application_attachments.other_additional_attachments()
            ]
        )

        self.save_part(part=part)

    def create_application_information_data(self):
        part = self.create_part(
            title="III. Informacje o przedsięwzięciu",
            short_name="III. Informacje",
            chapters=[
                self.create_chapter(
                    title="A. Charakterystyka przedsięwzięcia",
                    components=[
                        # Długość filmu
                        self.create_chapter(
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="radio",
                                            name="eventMovieDuration",
                                            label="Metraż",
                                            options=[
                                                "pełnometrażowy",
                                            ],
                                            required=True
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="eventMovieDuration",
                                            values=["pełnometrażowy"]
                                        )
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="number",
                                            unit="min.",
                                            label="Liczba minut",
                                            name="fullLengthLong",
                                            help_text="Minimalna liczba minut dla wybranego metrażu to 71.",
                                            validators=[
                                                self.validator.range_validator(min_value=71)
                                            ],
                                            required=True
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            components=[
                                self.create_chapter(
                                    class_list=[
                                        "grid",
                                        "grid-cols-2"
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="select",
                                            label="Cel realizacji przedsięwzięcia",
                                            name="projectGoal",
                                            options=[
                                                "artystyczny",
                                                "edukacyjny",
                                                "historyczny"
                                            ],
                                            required=True,
                                        ),
                                        self.create_component(
                                            component_type="select",
                                            label="Gatunek filmu",
                                            name="movieGenre",
                                            options=[
                                                "Dramat",
                                                "Komedia",
                                                "Horror",
                                                "Thriller",
                                                "Przygodowy",
                                                "Familijny",
                                                "Akcji",
                                                "Wojenny",
                                                "Biograficzny",
                                                "Historyczny",
                                                "Sensacyjny",
                                                "Fantastyczny",
                                                "Kostiumowy",
                                                "Western",
                                                "Film noir",
                                                "Anime",
                                                "Inny"
                                            ],
                                            required=True,
                                        ),
                                        self.create_component(
                                            component_type="select",
                                            label="Nośnik kopii wzorcowej",
                                            name="masterCopyMedium",
                                            options=[
                                                "taśma 35 mm",
                                                "cyfrowy"
                                            ],
                                            required=True,
                                            class_list=[
                                                "col-span-2"
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            components=[
                                self.create_chapter(
                                    class_list=[
                                        'grid',
                                        'grid-cols-2'
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            label="Główna wersja językowa",
                                            name="mainLanguage",
                                            validators=[
                                                self.validator.length_validator(max_value=200)
                                            ],
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="textarea",
                                            label="Przyznane nagrody (jeśli dotyczy)",
                                            name="receivedAwards",
                                            validators=[
                                                self.validator.length_validator(max_value=5400)
                                            ],
                                        ),
                                        self.create_component(
                                            component_type="textarea",
                                            label="Dodatkowe informacje o przedsięwzięciu",
                                            name="additionalInfo",
                                            validators=[
                                                self.validator.length_validator(max_value=5400)
                                            ],
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="B. Scenariusz",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="radio",
                                            label="Typ scenariusza",
                                            name="screenplayType",
                                            options=[
                                                "oryginalny",
                                                "adaptowany"
                                            ],
                                            required=True,
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="screenplayType",
                                            values=["adaptowany"]
                                        )
                                    ],
                                    class_list=[
                                        "grid",
                                        "grid-cols-2"
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            label="Tytuł utworu adaptowanego",
                                            name="adaptedWorkTitle",
                                            required=True,
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Autor/Autorzy utworu adaptowanego",
                                            name="adaptedWorkAuthor",
                                            required=True,
                                        ),
                                        self.create_component(
                                            component_type="file",
                                            label="Umowa nabycia autorskich praw majątkowych do utworu pierwotnego lub odpowiednia umowa opcji (jeśli dotyczy) wraz z potwierdzeniem uiszczenia opłaty",
                                            name="adaptationRightsContract",
                                            required=True,
                                            class_list=[
                                                "col-span-2"
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="textarea",
                                            label="Streszczenie",
                                            name="screenplaySynopsis",
                                            validators=[
                                                self.validator.length_validator(
                                                    max_value=5400
                                                )
                                            ],
                                            class_list=[
                                                "full-width"
                                            ],
                                            required=True
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            components=[
                                self.create_chapter(
                                    title="Treatment",
                                    components=[
                                        self.create_chapter(
                                            multiple_forms_rules={
                                                "minCount": 1,
                                                "maxCount": 10
                                            },
                                            components=[
                                                self.create_chapter(
                                                    components=[
                                                        self.create_component(
                                                            component_type="file",
                                                            name="treatmentAttachment",
                                                            required=True,
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_chapter(
                                            components=[
                                                self.create_component(
                                                    component_type="textarea",
                                                    label="Tagi/Słowa klucze",
                                                    name="tagsKetWords",
                                                    help_text="Wprowadź wartości oddzielone przecinkiem.",
                                                    validators=[
                                                        self.validator.length_validator(
                                                            max_value=1000
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                    ]
                ),
                self.section.application_information_data.screenwriter(number="C"),
                self.section.application_information_data.director(number="D"),
            ]
        )

        self.save_part(part=part)

    def create_application_completion_date_data(self):
        part = self.create_part(
            title="IV. Termin realizacji przedsięwzięcia",
            short_name="IV. Termin realizacji",
            chapters=[
                self.create_chapter(
                    title="Stypendium scenariuszowe",
                    components=[
                        self.create_chapter(
                            title="Termin realizacji stypendium scenariuszowego 12 miesięcy od daty podpisania umowy",
                            class_list={
                                "main": [
                                    "dates",
                                    "grid",
                                    "grid-cols-2"
                                ],
                                "sub": [
                                    "dates-item"
                                ]
                            },
                            components=[
                                self.create_component(
                                    component_type="date",
                                    label="Termin od",
                                    name="activityScheduleStart",
                                    validators=[
                                        self.validator.related_date_lte_validator(
                                            field_name="activityScheduleEnd",
                                            message="Termin rozpoczęcia działania musi być wcześniejszy niż termin jego zakończenia."
                                        )
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="date",
                                    label="Termin do",
                                    name="activityScheduleEnd",
                                    validators=[
                                        self.validator.related_date_gte_validator(
                                            field_name="activityScheduleStart",
                                            message="Termin zakończenia działania musi być późniejszy niż termin jego zakończenia."
                                        ),
                                        self.validator.related_date_offset_validator(
                                            field_name="activityScheduleStart",
                                            offset=365,
                                            message="Stypendium scenariuszowe nie może trwać dłużej niz rok."
                                        )
                                    ],
                                    required=True
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="OBLIGATORYJNE CZYNNOŚCI W PRZYPADKU ZAWARCIA UMOWY O DOFINANSOWANIE",
                    components=[
                        self.create_chapter(
                            title="Akceptacja scenariusza"
                        ),
                        self.create_chapter(
                            title="Raport końcowy po zakończeniu rozwoju projektu filmowego"
                        ),
                        self.create_chapter(
                            title="Wykonanie i udokumentowanie działań obligatoryjnych w ramach rozwoju projektu filmowego wymagane Programem operacyjnym PISF"
                        )
                    ]
                )
            ]
        )

        self.save_part(part=part)

    def create_application_additional_data(self):
        part = self.create_part(
            title="VI. Dane dodatkowe",
            short_name="VI. Dane dodatkowe",
            chapters=[
                self.create_chapter(
                    title="Czy przedsięwzięcie było wcześniej ocenianie w PISF?",
                    components=[
                        self.create_component(
                            component_type="select",
                            name="isProjectRatedInPisf",
                            options=[
                                "Tak",
                                "Nie"
                            ],
                            required=True,
                        )
                    ]
                ),
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="isProjectRatedInPisf",
                            values=["Tak"]
                        )
                    ],
                    components=[
                        self.create_chapter(
                            title="Na etapie",
                            components=[
                                self.create_component(
                                    component_type="checkbox",
                                    label=comp["label"],
                                    name=comp["name"],
                                ) for comp in [
                                    {
                                        "label": "Stypendium scenariuszowe",
                                        "name": "scriptScholarshipStage"
                                    },
                                    {
                                        "label": "Dewelopmentu scenariuszowe",
                                        "name": "scriptDevelopmentStage"
                                    },
                                    {
                                        "label": "Rozwoju projektu",
                                        "name": "projectDevelopmentStage"
                                    },
                                    {
                                        "label": "Produkcji",
                                        "name": "productionStage"
                                    },
                                    {
                                        "label": "W ramach systemu wsparcia finansowego produkcji audiowizualnej tzw. Zachęt",
                                        "name": "financialSupportSystemStage"
                                    },
                                    {
                                        "label": "Inne dotyczące projektu w innym Programie Operacyjnym PISF",
                                        "name": "otherStage"
                                    }
                                ]
                            ]
                        ),
                        # Stypendium sceniurszowe
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="scriptScholarshipStage",
                                    values=[True]
                                )
                            ],
                            components=[
                                self.create_chapter(
                                    title="Na etapie stypendium scenariuszowego",
                                    components=[
                                        self.create_component(
                                            component_type="select",
                                            label="Decyzja Dyrektora",
                                            name="scriptScholarshipDirectorDecision",
                                            options=[
                                                "Pozytywna",
                                                "Negatywna"
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="scriptScholarshipDirectorDecision",
                                            values=["Pozytywna"]
                                        )
                                    ],
                                    components=[
                                        self.create_chapter(
                                            title="Autorzy scenariusza",
                                            multiple_forms_rules={
                                                "minCount": 1,
                                                "maxCount": 20
                                            },
                                            components=[
                                                self.create_chapter(
                                                    class_list=[
                                                        "grid",
                                                        "grid-cols-2"
                                                    ],
                                                    components=[
                                                        self.create_component(
                                                            component_type="text",
                                                            label="Imię",
                                                            name="scriptwriterName"
                                                        ),
                                                        self.create_component(
                                                            component_type="text",
                                                            label="Nazwisko",
                                                            name="scriptwriterSurname"
                                                        ),
                                                        self.create_component(
                                                            component_type="text",
                                                            mask="fund",
                                                            label="Kwota",
                                                            name="scriptwriterPLNAmount",
                                                            unit="PLN"
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Udział procentowy",
                                                            name="scriptwriterPercentage",
                                                            unit="%"
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_chapter(
                                            class_list=[
                                                "grid",
                                                "grid-cols-4"
                                            ],
                                            components=[
                                                self.create_component(
                                                    component_type="number",
                                                    label="Suma udziałów",
                                                    name="scriptwriterTotalShares",
                                                    help_text="Suma udziałów musi być równa 100%.",
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=["scriptwriterPercentage"]
                                                        )
                                                    ],
                                                    validators=[
                                                        self.validator.range_validator(
                                                            min_value=100,
                                                            max_value=100,
                                                            message="Suma udziałów musi być równa 100%."
                                                        )
                                                    ],
                                                    read_only=True,
                                                    required=True,
                                                    class_list=[
                                                        "col-start-1",
                                                        "col-end-2"
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                *self.section.application_additional_data.create_section_with_positive_and_negative_decision(
                                    name="scriptScholarship"
                                )
                            ]
                        ),
                        # Dewelopment scenariuszowy
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="scriptDevelopmentStage",
                                    values=[True]
                                )
                            ],
                            components=[
                                self.create_chapter(
                                    title="Na etapie dewelopmentu scenariuszowego",
                                    components=[
                                        self.create_component(
                                            component_type="select",
                                            label="Decyzja Dyrektora",
                                            name="scriptDevelopmentDirectorDecision",
                                            options=[
                                                "Pozytywna",
                                                "Negatywna"
                                            ]
                                        )
                                    ]
                                ),
                                *self.section.application_additional_data.create_section_with_positive_and_negative_decision(
                                    name="scriptDevelopment"
                                )
                            ]
                        ),
                        # Rozwój projektu
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectDevelopmentStage",
                                    values=[True]
                                )
                            ],
                            components=[
                                self.create_chapter(
                                    title="Na etapie rozwoju projektu",
                                    components=[
                                        self.create_component(
                                            component_type="select",
                                            label="Decyzja Dyrektora",
                                            name="projectDevelopmentDirectorDecision",
                                            options=[
                                                "Pozytywna",
                                                "Negatywna"
                                            ]
                                        )
                                    ]
                                ),
                                *self.section.application_additional_data.create_section_with_positive_and_negative_decision(
                                    name="projectDevelopment"
                                )
                            ]
                        ),
                        # Produkcja
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="productionStage",
                                    values=[True]
                                )
                            ],
                            components=[
                                self.create_chapter(
                                    title="Na etapie rozwoju projektu",
                                    components=[
                                        self.create_component(
                                            component_type="select",
                                            label="Decyzja Dyrektora",
                                            name="productionDirectorDecision",
                                            options=[
                                                "Pozytywna",
                                                "Negatywna"
                                            ]
                                        )
                                    ]
                                ),
                                *self.section.application_additional_data.create_section_with_positive_and_negative_decision(
                                    name="production"
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Wykaz wniosków podmiotu w PISF",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_chapter(
                                    title=chapter["title"],
                                    components=[
                                        self.create_chapter(
                                            components=[
                                                self.create_component(
                                                    component_type="checkbox",
                                                    label="Nie dotyczy",
                                                    name=f"notApplicable{chapter["name"]}"
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name=f"notApplicable{chapter["name"]}",
                                            values=[False]
                                        )
                                    ],
                                    multiple_forms_rules={
                                        "minCount": 1,
                                        "maxCount": 30
                                    },
                                    components=[
                                        self.create_chapter(
                                            class_list=[
                                                "grid",
                                                "grid-cols-3"
                                            ],
                                            components=[
                                                self.create_component(
                                                    component_type="select",
                                                    label="Priorytet",
                                                    name=f"entityApplicationsListPriority{chapter["name"]}",
                                                    options=[
                                                        "rozwój projektu animowanego",
                                                        "rozwój projektu fabularnego",
                                                        "rozwój projektu dokumentalnego",
                                                        "development scenariuszowy filmu animowanego",
                                                        "development scenariuszowy filmu fabularnego",
                                                        "development scenariuszowy filmu dokumentalnego",
                                                        "produkcja filmu animowanego",
                                                        "produkcja filmu fabularnego",
                                                        "produkcja filmu dokumentalnego"
                                                    ],
                                                    required=True,
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    label="Reżyser",
                                                    name=f"entityApplicationsListDirector{chapter["name"]}",
                                                    validators=[
                                                        self.validator.length_validator(
                                                            max_value=100
                                                        )
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    label="Tytuł",
                                                    name=f"entityApplicationsListTitle{chapter["name"]}",
                                                    validators=[
                                                        self.validator.length_validator(
                                                            max_value=100
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ) for chapter in [
                            {
                                "title": "Wnioski składane do PO Produkcja filmowa w bieżącej sesji",
                                "name": "CurrentSession"
                            },
                            {
                                "title": "Wykaz aktualnych promes (filmy przed umową z PISF)",
                                "name": "CurrentPromises"
                            },
                            {
                                "title": "Wykaz filmów w produkcji z umową na dofinansowanie PISF",
                                "name": "CurrentProductionContracts"
                            },
                            {
                                "title": "Projekty w realizacji z dofinansowaniem PISF w zakresie rozwoju projektu",
                                "name": "CurrentProjectDevelopment"
                            },
                            {
                                "title": "Wnioski dotyczące rozwoju projektu z poprzednich sesji, oczekujące na decyzję Dyrektora PISF",
                                "name": "PreviousProjectDevelopment"
                            },
                            {
                                "title": "Wnioski dotyczące produkcji filmowej z poprzednich sesji, oczekujące na decyzję Dyrektora PISF",
                                "name": "PreviousSessionProduction"
                            }
                        ]
                    ]
                )
            ]
        )

        self.save_part(part=part)
