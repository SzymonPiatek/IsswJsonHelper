from classes.form_builder.dpf.application_builder import DPFApplicationBuilder


class AnimatedFilmApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'V. Produkcja filmów animowanych'
    PRIORITY_NUM = 5
    FORM_ID = 9198

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.department_data_path / 'animated_film'

    def create_application_basic_data(self):
        part = self.create_part(
            title="I. Dane podstawowe",
            short_name="I. Dane podstawowe",
            chapters=[
                self.section.application_basic_data.scope_of_project(
                    number="1",
                    options=[
                        "Produkcja filmowa"
                    ]
                ),
                self.section.application_basic_data.movie_kind(
                    number="2",
                    options=[
                        "animowany",
                        "seria animowana"
                    ]
                ),
                self.section.application_basic_data.movie_subject(
                    number="3",
                    options=[
                        "film autorski",
                        "film o tematyce historycznej",
                        "film dla młodego widza lub widowni familijnej"
                    ],
                    validators=[
                        self.validator.related_allowed_options_validator(
                            field_name="movieKind",
                            mapping={
                                "animowany": [
                                    "film autorski",
                                    "film o tematyce historycznej",
                                    "film dla młodego widza lub widowni familijnej"
                                ],
                                "seria animowana": [
                                    "film dla młodego widza lub widowni familijnej"
                                ]
                            }
                        )
                    ]
                ),
                self.section.application_basic_data.piece_title(
                    number="4",
                ),
                self.section.application_basic_data.short_movie_description(
                    number="5",
                ),
                self.section.application_basic_data.category_of_project(
                    number="6",
                    options=[
                        "produkcja krajowa",
                        "koprodukcja międzynarodowa większościowa"
                    ]
                ),
                self.section.application_basic_data.application_relates(
                    number="7",
                    options=[
                        "promesa",
                        "umowa"
                    ]
                ),
                self.section.application_basic_data.kind_of_support(
                    number="8",
                    options=[
                        "dotacja",
                        "pożyczka",
                        "poręczenie"
                    ]
                ),
                self.create_chapter(
                    title="9. Wybór lidera komisji eksperckiej",
                    components=[
                        self.section.application_basic_data.one_stage_commission(
                            number="9",
                        )
                    ]
                )
            ]
        )

        self.save_part(part=part)

    def create_application_attachments(self):
        part = self.create_part(
            title="VII. Załączniki",
            short_name="VII. Załączniki",
            chapters=[
                self.section.application_attachments.common_part(),
                self.section.application_attachments.factual_report_on_goals_and_effects_of_development_of_film_project(),
                self.section.application_attachments.declaration_of_division_of_rights_coproduced_by_television_broadcaster(),
                self.section.application_attachments.film_promotion_and_distribution_plan(),
                self.section.application_attachments.letter_of_intent_from_distributor(),
                self.section.application_attachments.animation_attachments(),
                self.section.application_attachments.opinion_of_the_historian(),
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
                                                "krótkometrażowy",
                                                "seria"
                                            ],
                                            validators=[
                                                self.validator.related_allowed_options_validator(
                                                    field_name="movieKind",
                                                    mapping={
                                                        "animowany": [
                                                            "pełnometrażowy",
                                                            "średniometrażowy",
                                                            "krótkometrażowy"
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
                                                            "krótkometrażowy",
                                                            "seria"
                                                        ],
                                                        "film o tematyce historycznej": [
                                                            "pełnometrażowy",
                                                            "średniometrażowy",
                                                            "krótkometrażowy",
                                                            "seria"
                                                        ],
                                                        "film dla młodego widza lub widowni familijnej": [
                                                            "średniometrażowy",
                                                            "krótkometrażowy",
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
                                        self.create_chapter(
                                            visibility_rules=[
                                                self.visibility_rule.depends_on_value(
                                                    field_name="movieKind",
                                                    values=[
                                                        "animowany"
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
                                                            label="Scenariusz filmu lub treatment",
                                                            name="movieScreenplayAttachment",
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
                                                    values=[
                                                        "seria animowana"
                                                    ]
                                                )
                                            ],
                                            multiple_forms_rules={
                                                "minCount": 1,
                                                "maxCount": 52,
                                            },
                                            components=[
                                                self.create_chapter(
                                                    components=[
                                                        self.create_component(
                                                            component_type="file",
                                                            label="Scenariusze filmu/treatmenty",
                                                            name="movieScreenplayAttachmentSeries",
                                                            help_text="W zależności od ilości odcinków należy dostarczyć odpowiednią liczbę scenariuszy i treatmentów:</br>a) 13 odcinków - minimum 6 scenariuszy oraz treatmenty pozostałych odcinków </br>b) 26 odcinków - minimum 13 scenariuszy oraz treatmenty pozostałych odcinków </br>c) 52 odcinków - minimum 26 scenariuszy oraz treatmenty pozostałych odcinków",
                                                            required=True
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
                            title="Kierownik produkcji",
                            name="productionSupervisor",
                            is_vacant=True,
                        ),
                        self.section.application_information_data.production_team_member(
                            title="Operator obrazu",
                            name="directorOfPhotography",
                            is_vacant=True,
                        ),
                        self.section.application_information_data.production_team_member(
                            title="Scenograf",
                            name="sceneDesigner",
                            is_vacant=True,
                        ),
                        self.section.application_information_data.production_team_member(
                            title="Montażysta",
                            name="editor",
                            is_vacant=True,
                        ),
                        self.section.application_information_data.production_team_member(
                            title="Kompozytor",
                            name="composer",
                            is_vacant=True,
                            is_not_applicable=True
                        ),
                        self.section.application_information_data.production_team_member(
                            title="Autor opracowania plastycznego",
                            name="animationDesigner",
                            is_vacant=True,
                        ),
                        self.section.application_information_data.production_team_member(
                            title="Dodatkowi członkowie ekipy realizacyjnej",
                            name="additionalCrew",
                            is_multi=True
                        ),
                    ]
                )
            ]
        )

        self.save_part(part=part)

    def application_completion_date_data(self):
        part = self.create_part(
            title="IV. Termin realizacji przedsięwzięcia",
            short_name="IV. Termin realizacji",
            chapters=[
                self.create_chapter(
                    title="Harmonogram produkcji filmowej",
                    components=[
                        self.create_chapter(
                            title="Okres wstępny (jeśli dotyczy)",
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
                                    name="scheduleInitialPeriodStart",
                                    validators=[
                                        self.validator.related_date_lte_validator(
                                            field_name="scheduleInitialPeriodEnd",
                                            message="Termin rozpoczęcia działania musi być wcześniejszy niż termin jego zakończenia."
                                        )
                                    ]
                                ),
                                self.create_component(
                                    component_type="date",
                                    label="Termin do",
                                    name="scheduleInitialPeriodEnd",
                                    validators=[
                                        self.validator.related_date_gte_validator(
                                            field_name="scheduleInitialPeriodStart",
                                            message="Termin zakończenia działania musi być późniejszy niż termin jego rozpoczęcia."
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Okres przygotowawczy",
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
                                    name="schedulePrepPeriodStart",
                                    validators=[
                                        self.validator.related_date_lte_validator(
                                            field_name="schedulePrepPeriodEnd",
                                            message="Termin rozpoczęcia działania musi być wcześniejszy niż termin jego rozpoczęcia."
                                        )
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="date",
                                    label="Termin do",
                                    name="schedulePrepPeriodEnd",
                                    validators=[
                                        self.validator.related_date_gte_validator(
                                            field_name="schedulePrepPeriodStart",
                                            message="Termin zakończenia działania musi być późniejszy niż termin jego rozpoczęcia."
                                        )
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Okres animacji",
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
                                    name="scheduleAnimationPeriodStart",
                                    calculation_rules=[
                                        self.calculation_rule.relate_to_last_date(
                                            field="schedulePrepPeriodEnd",
                                            parameter=1
                                        )
                                    ],
                                    read_only=True,
                                    validators=[
                                        self.validator.related_date_lte_validator(
                                            field_name="scheduleAnimationPeriodEnd",
                                            message="Termin rozpoczęcia działania musi być wcześniejszy niż termin jego rozpoczęcia."
                                        )
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="date",
                                    label="Termin do",
                                    name="scheduleAnimationPeriodEnd",
                                    validators=[
                                        self.validator.related_date_gte_validator(
                                            field_name="scheduleAnimationPeriodStart",
                                            message="Termin zakończenia działania musi być późniejszy niż termin jego rozpoczęcia."
                                        )
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Okres obróbki cyfrowej obrazu i udźwiękowienia",
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
                                    name="schedulePostProdPeriodStart",
                                    calculation_rules=[
                                        self.calculation_rule.relate_to_last_date(
                                            field="scheduleAnimationPeriodEnd",
                                            parameter=1
                                        )
                                    ],
                                    read_only=True,
                                    validators=[
                                        self.validator.related_date_lte_validator(
                                            field_name="schedulePostProdPeriodEnd",
                                            message="Termin rozpoczęcia działania musi być wcześniejszy niż termin jego rozpoczęcia."
                                        )
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="date",
                                    label="Termin do",
                                    name="schedulePostProdPeriodEnd",
                                    validators=[
                                        self.validator.related_date_gte_validator(
                                            field_name="schedulePostProdPeriodStart",
                                            message="Termin zakończenia działania musi być późniejszy niż termin jego rozpoczęcia."
                                        )
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Okres prac końcowych (w tym wykonanie kopii wzorcowej)",
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
                                    name="scheduleFinalWorksPeriodStart",
                                    calculation_rules=[
                                        self.calculation_rule.relate_to_last_date(
                                            field="schedulePostProdPeriodEnd",
                                            parameter=1
                                        )
                                    ],
                                    read_only=True,
                                    validators=[
                                        self.validator.related_date_lte_validator(
                                            field_name="scheduleFinalWorksPeriodEnd",
                                            message="Termin rozpoczęcia działania musi być wcześniejszy niż termin jego rozpoczęcia."
                                        )
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="date",
                                    label="Termin do",
                                    name="scheduleFinalWorksPeriodEnd",
                                    validators=[
                                        self.validator.related_date_gte_validator(
                                            field_name="scheduleFinalWorksPeriodStart",
                                            message="Termin zakończenia działania musi być późniejszy niż termin jego rozpoczęcia."
                                        )
                                    ],
                                    required=True
                                )
                            ]
                        ),
                    ]
                ),
                self.create_chapter(
                    title="Dni zdjęciowe",
                    class_list=[
                        "grid",
                        "grid-cols-2"
                    ],
                    components=[
                        self.create_component(
                            component_type="number",
                            label="Łączna liczba dni zdjęciowych",
                            name="scheduleShootingDaysAll",
                            required=True
                        ),
                        self.create_component(
                            component_type="number",
                            label="Liczba dni zdjęciowych na terenie Polski",
                            name="scheduleShootingDaysPoland",
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Planowany termin wykonania kopii wzorcowej",
                    class_list=[
                        "grid",
                        "grid-cols-2"
                    ],
                    components=[
                        self.create_component(
                            component_type="date",
                            name="scheduleFinalCopyDate",
                            validators=[
                                self.validator.related_date_gte_validator(
                                    field_name="scheduleFinalWorksPeriodStart",
                                    message="Wykonanie kopii wzorcowej nie może odbyć się wcześniej niż data początku prac końcowych."
                                ),
                                self.validator.related_date_lte_validator(
                                    field_name="scheduleFinalWorksPeriodEnd",
                                    message="Wykonanie kopii wzorcowej nie może odbyć się później niż data zakończenia prac końcowych."
                                )
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Planowany termin wprowadzenia filmu do obrotu (premiera/eksploatacja)",
                    class_list=[
                        "grid",
                        "grid-cols-2"
                    ],
                    components=[
                        self.create_component(
                            component_type="date",
                            name="schedulePremiereDate",
                            validators=[
                                self.validator.related_date_gte_validator(
                                    field_name="scheduleFinalCopyDate",
                                    message="Planowany termin wprowadzenia filmu do obrotu musi nastąpić po planowanym terminie wykonania kopii wzorcowej."
                                )
                            ],
                            required=True
                        )
                    ]
                )
            ]
        )

        self.save_part(part=part)
