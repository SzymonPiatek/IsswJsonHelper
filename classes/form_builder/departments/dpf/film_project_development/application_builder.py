from classes.form_builder.departments.dpf.application_builder import DPFApplicationBuilder


class FilmProjectDevelopmentApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'II. Rozwój projektów filmowych'
    PRIORITY_NUM = 2
    FORM_ID = 9195

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.department_data_path / 'film_project_development'
        self.task_type = "Przygotowania projektów filmowych"

    def create_application_basic_data(self):
        part = self.create_part(
            title='I. Dane podstawowe',
            short_name='I. Dane podstawowe',
            chapters=[
                self.section.application_basic_data.scope_of_project(
                    number='1',
                    options=[
                        "Rozwój projektu"
                    ]
                ),
                self.section.application_basic_data.movie_kind(
                    number='2',
                    options=[
                        "fabularny",
                        "dokumentalny",
                        "animowany",
                        "seria animowana"
                    ]
                ),
                self.section.application_basic_data.scope_of_project_kind(
                    number='3',
                    options=[
                        "rozwój projektu",
                        "seria animowana"
                    ],
                    calculation_rules=[
                        self.calculation_rule.assign_value(
                            options=[
                                {
                                    "fieldName": "movieKind",
                                    "value": "fabularny",
                                    "inputValue": "rozwój projektu"
                                },
                                {
                                    "fieldName": "movieKind",
                                    "value": "animowany",
                                    "inputValue": "rozwój projektu"
                                },
                                {
                                    "fieldName": "movieKind",
                                    "value": "dokumentalny",
                                    "inputValue": "rozwój projektu"
                                },
                                {
                                    "fieldName": "movieKind",
                                    "value": "seria animowana",
                                    "inputValue": "seria animowana"
                                }
                            ]
                        )
                    ]
                ),
                self.section.application_basic_data.movie_subject(
                    number='4',
                    options=[
                        "film autorski",
                        "film o tematyce historycznej",
                        "film dla młodego widza i widowni familijnej"
                    ],
                    validators=[
                        self.validator.related_allowed_options_validator(
                            field_name='movieKind',
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
                                    "film o tematyce historycznej",
                                    "film dla młodego widza i widowni familijnej"
                                ],
                                "seria animowana": [
                                    "film dla młodego widza i widowni familijnej"
                                ]
                            }
                        )
                    ]
                ),
                self.section.application_basic_data.piece_title(
                    number='5',
                ),
                self.section.application_basic_data.short_movie_description(
                    number='6',
                ),
                self.section.application_basic_data.category_of_project(
                    number='7',
                    options=[
                        "produkcja krajowa",
                        "koprodukcja międzynarodowa większościowa"
                    ]
                ),
                self.section.application_basic_data.application_relates(
                    number='8',
                    options=[
                        "umowa"
                    ]
                ),
                self.section.application_basic_data.kind_of_support(
                    number='9',
                    options=[
                        "dotacja",
                        "pożyczka",
                        "poręczenie"
                    ]
                ),
                self.create_chapter(
                    title="10. Wybór lidera komisji eksperckiej",
                    components=[
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="movieKind",
                                    values=[
                                      "animowany",
                                      "seria animowana"
                                    ]
                                )
                            ],
                            components=[
                                self.section.application_basic_data.one_stage_commission(
                                    number="10"
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="movieKind",
                                    values=[
                                        "fabularny",
                                        "dokumentalny"
                                    ]
                                )
                            ],
                            components=[
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="movieKind",
                                            values=[
                                                "fabularny"
                                            ]
                                        )
                                    ],
                                    components=[
                                        self.section.application_basic_data.two_stages_commission(
                                            number="10",
                                            options=[
                                                "Lider: Beata Pisula",
                                                "Lider: Joanna Kos Krauze",
                                                "Lider: Anna Kazejak"
                                            ],
                                            after_name="Fab"
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="movieKind",
                                            values=[
                                                "dokumentalny"
                                            ]
                                        )
                                    ],
                                    components=[
                                        self.section.application_basic_data.two_stages_commission(
                                            number="10",
                                            options=[
                                                "Lider: Małgorzata Prociak",
                                                "Lider: Jakub Mikurda",
                                                "Lider: Bartosz Paduch"
                                            ],
                                            after_name="doc"
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
                self.section.application_attachments.detailed_list_of_tasks(),
                self.create_chapter(
                    components=[
                        self.component.application_attachments.description_of_artistic_qualities(),
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
                                                "średniometrażowy",
                                                "seria"
                                            ],
                                            validators=[
                                                self.validator.related_allowed_options_validator(
                                                    field_name="movieKind",
                                                    mapping={
                                                        "fabularny": [
                                                            "pełnometrażowy",
                                                        ],
                                                        "dokumentalny": [
                                                            "pełnometrażowy",
                                                            "średniometrażowy"
                                                        ],
                                                        "animowany": [
                                                            "pełnometrażowy",
                                                            "średniometrażowy"
                                                        ],
                                                        "seria animowana": [
                                                            "seria"
                                                        ]
                                                    }
                                                ),
                                                self.validator.related_allowed_options_validator(
                                                    field_name="movieSubject",
                                                    mapping={
                                                        "film autorski": [
                                                            "pełnometrażowy",
                                                            "średniometrażowy",
                                                            "seria"
                                                        ],
                                                        "film o tematyce historycznej": [
                                                            "pełnometrażowy",
                                                            "średniometrażowy",
                                                            "seria"
                                                        ],
                                                        "film dla młodego widza lub widowni familijnej": [
                                                            "pełnometrażowy",
                                                            "seria"
                                                        ]
                                                    }
                                                )
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
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="eventMovieDuration",
                                            values=["średniometrażowy"]
                                        )
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="number",
                                            unit="min.",
                                            label="Liczba minut",
                                            name="fullLengthMedium",
                                            help_text="Minimalna liczba minut dla wybranego metrażu to 16. Maksymalna liczba minut dla wybranego metrażu to 70.",
                                            validators=[
                                                self.validator.range_validator(max_value=70, min_value=16)
                                            ],
                                            required=True
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="eventMovieDuration",
                                            values=["krótkometrażowy"]
                                        )
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="number",
                                            unit="min.",
                                            label="Liczba minut",
                                            name="fullLengthShort",
                                            help_text="Maksymalna liczba minut dla wybranego metrażu to 15.",
                                            validators=[
                                                self.validator.range_validator(max_value=15)
                                            ],
                                            required=True
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="movieKind",
                                            values=[
                                                "seria animowana"
                                            ]
                                        )
                                    ],
                                    class_list=[
                                        "grid",
                                        "grid-cols-2"
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="select",
                                            label="Liczba odcinków serii",
                                            name="numberOfEpisodes",
                                            options=[
                                                "13", "26", "52"
                                            ],
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Liczba minut odcinka serii",
                                            name="seriesEpisodeLength",
                                            help_text="Maksymalna długość odcinka to 15 minut.",
                                            required=True,
                                            validators=[
                                                self.validator.range_validator(
                                                    max_value=15
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Liczba minut łącznie",
                                            name="totalDurationTime",
                                            calculation_rules=[
                                                self.calculation_rule.multiply_inputs(
                                                    fields=[
                                                        "numberOfEpisodes",
                                                        "seriesEpisodeLength"
                                                    ]
                                                )
                                            ],
                                            required=True,
                                            validators=[
                                                self.validator.related_multiplication_validator(
                                                    field_names=[
                                                        "numberOfEpisodes",
                                                        "seriesEpisodeLength"
                                                    ]
                                                )
                                            ],
                                            read_only=True
                                        )
                                    ]
                                )
                            ]
                        ),
                        # Czy film jest przeznaczony w pierwszej kolejności do kin
                        self.create_chapter(
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="radio",
                                            label="Film przeznaczony w pierwszej kolejności do eksploatacji w kinach",
                                            name="isFirstExploitedInCinemas",
                                            options=[
                                                "Tak", "Nie"
                                            ],
                                            required=True,
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="isFirstExploitedInCinemas",
                                            values=["Nie"]
                                        )
                                    ],
                                    class_list=[
                                        "grid",
                                        "grid-cols-2"
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            label="Należy podać planowane pierwsze pole eksploatacji niebędące kinem",
                                            name="exploitationFieldNotCinema",
                                            required=True
                                        )
                                    ]
                                )
                            ]
                        ),
                        # Czy film jest filmem trudnym
                        self.create_chapter(
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="radio",
                                            label="Film trudny w rozumieniu Ustawy z dn. 30 czerwca 2005 roku o kinematografii",
                                            name="isDifficultPiece",
                                            options=[
                                                "Tak", "Nie"
                                            ],
                                            validators=[
                                                self.validator.related_allowed_options_validator(
                                                    field_name="movieKind",
                                                    mapping={
                                                        "seria animowana": [
                                                            "Nie"
                                                        ],
                                                        "animowany": [
                                                            "Tak", "Nie"
                                                        ]
                                                    }
                                                )
                                            ],
                                            required=True
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="isDifficultPiece",
                                            values=["Tak"]
                                        )
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="textarea",
                                            label="Uzasadnienie kwalifikacji filmu jako trudnego",
                                            name="descDifficultPiece",
                                            validators=[
                                                self.validator.length_validator(max_value=1800)
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
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="masterCopyMedium",
                                            values=["cyfrowy"]
                                        )
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="select",
                                            label="Rodzaj nośnika cyfrowego",
                                            name="digitalMediumFormat",
                                            options=[
                                                "Digital Cinema Package (DCP)",
                                                "Digital Cinema Distribution Master (DCDM)"
                                            ],
                                            required=True,
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
                                            component_type="text",
                                            label="Planowany dystrybutor/nadawca",
                                            name="distributor",
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
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="movieKind",
                                            values=[
                                                "seria animowana"
                                            ]
                                        )
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="textarea",
                                            label="Grupa docelowa",
                                            name="targetGroup",
                                            validators=[
                                                self.validator.length_validator(max_value=5400)
                                            ],
                                            class_list=[
                                                "full-width"
                                            ],
                                            required=True
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
                                    title="Scenariusz filmu",
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
                                                            label="Scenariusz filmu",
                                                            name="movieScreenplayAttachment",
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
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="movieKind",
                                    values=[
                                        "seria animowana"
                                    ]
                                )
                            ],
                            multiple_forms_rules={
                                "minCount": 1,
                                "maxCount": 10,
                            },
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="file",
                                            label="Lista odcinków serii z podaniem: numeru, tytułu oraz autora odcinka",
                                            name="seriesScreenplayAttachmentAdditional",
                                            help_text="Należy oznaczyć, które tytuły są scenariuszami a które treatmentami.",
                                            required=True
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
                                    name="tagsKeyWords",
                                    help_text="Wprowadź wartości oddzielone przecinkiem.",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=1800
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.section.application_information_data.screenwriter(number="C"),
                self.section.application_information_data.director(number="D"),
                self.section.application_information_data.producer(number="E"),
                self.section.application_information_data.coproducer(number="F"),
                self.create_chapter(
                    title="G. Członkowie ekipy realizacyjnej",
                    components=[
                        self.section.application_information_data.production_team_member(
                            title="Konsultant scenariuszowy",
                            name="screenplayConsultant",
                            is_vacant=True,
                            is_not_applicable=True
                        ),
                        self.section.application_information_data.production_team_member(
                            title="Kierownik produkcji",
                            name="productionSupervisor",
                            is_vacant=True,
                        ),
                        self.section.application_information_data.production_team_member(
                            title="Dodatkowi członkowie ekipy realizacyjnej",
                            name="additionalCrew",
                            is_multi=True,
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="movieKind",
                                    values=[
                                        "dokumentalny"
                                    ]
                                )
                            ],
                            components=[
                                self.section.application_information_data.production_team_member(
                                    title="Bohater",
                                    name="protagonist",
                                    is_vacant=True,
                                )
                            ]
                        )
                    ]
                )
            ]
        )

        self.save_part(part=part)

    def create_application_completion_date_data(self):
        part = self.create_part(
            title="IV. Termin realizacji przedsięwzięcia",
            short_name="IV. Termin realizacji",
            chapters=[
                self.create_chapter(
                    title="Rozwój projektu filmowego",
                    components=[
                        self.create_chapter(
                            title="Termin realizacji rozwoju projektu do 36 miesięcy",
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
                                    name="activityScheduleStartProject",
                                    validators=[
                                        self.validator.related_date_lte_validator(
                                            field_name="activityScheduleEndProject",
                                            message="Termin rozpoczęcia działania musi być wcześniejszy niż termin jego zakończenia."
                                        )
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="date",
                                    label="Termin do",
                                    name="activityScheduleEndProject",
                                    validators=[
                                        self.validator.related_date_gte_validator(
                                            field_name="activityScheduleStartProject",
                                            message="Termin zakończenia działania musi być późniejszy niż termin jego rozpoczęcia."
                                        ),
                                        self.validator.related_date_offset_validator(
                                            field_name="activityScheduleStartProject",
                                            offset=1095,
                                            message="Rozwój projektu nie może trwać dłużej niz trzy lata."
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

    def create_application_financial_data(self):
        pass
