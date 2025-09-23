from classes.form_builder.departments.dpf.application_builder import DPFApplicationBuilder


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

    def create_application_completion_date_data(self):
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
                self.section.application_completion_date_data.shooting_days(),
                self.section.application_completion_date_data.planned_date_of_master_copy(),
                self.section.application_completion_date_data.planned_date_of_film_release(),
                self.section.application_completion_date_data.mandatory_activities(),
                self.section.application_completion_date_data.operational_reports(),
                self.create_chapter(
                    title="PLANOWANE MIEJSCA REALIZACJI FILMU",
                    components=[
                        self.create_chapter(
                            title="Baza produkcyjna",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="plannedProductionBase",
                                    required=True,
                                    validators=[
                                        self.validator.length_validator(max_value=200)
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Lokacje zdjęciowe",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="plannedShootingLocations",
                                    required=True,
                                    validators=[
                                        self.validator.length_validator(max_value=200)
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Laboratorium",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="plannedLaboratory",
                                    required=True,
                                    validators=[
                                        self.validator.length_validator(max_value=200)
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="OŚWIADCZENIA",
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Oświadczam, że przedsięwzięcie przed datą złożenia wniosku nie miało publicznego pokazu, premiery, pierwszej emisji, pokazu festiwalowego, przeglądu publicznego itp.",
                            name="schedulePublicPremiereDeclaration",
                            required=True
                        )
                    ]
                )
            ]
        )

        self.save_part(part=part)

    def create_application_financial_data(self):
        part = self.create_part(
            title="V. Dane finansowe przedsięwziecia",
            short_name="V. Dane finansowe",
            class_list=[
                "full-width-grid"
            ],
            chapters=[
                self.create_chapter(
                    title="OGÓLNE KOSZTY WEDŁUG UDOKUMENTOWANYCH ŹRÓDEŁ FINANSOWANIA",
                    class_list={
                        "sub": [
                            "table-1-2-top"
                        ]
                    },
                    components=[
                        self.create_chapter(
                            title="<small>UWAGA! <normal>Dane dotyczące kosztów produkcji powinny być identyczne z danymi zawartymi w planowanym kosztorysie stanowiącym załącznik do wniosku oraz z deklaracjami koproducentów wynikającymi z umów lub listów intencyjnych załączonych do wniosku.</small></normal>"
                        ),
                        self.create_chapter(
                            title="<normal><small><red>Przed wypełnieniem danych finansowych upewnij się, że zakładki I. Dane podstawowe i III. Informacje zostały wypełnione w całości i zgodnie z właściwościami produkcji.  </red><br />W przypadku braku automatycznego przeliczenia wartości finansowych prosimy o użycie przycisku „Przelicz i waliduj”, który znajduje się w prawym, dolnym rogu ekranu. Wymusi to dokonanie niezbędnych przeliczeń oraz podświetli nieuzupełnione pola formularza. </small></normal>"
                        ),
                        self.create_chapter(
                            title="1. Całkowity przewidywany koszt realizacji przedsięwzięcia",
                            class_list={
                                "main": [
                                    "table-1-2",
                                    "grid",
                                    "grid-cols-3"
                                ],
                                "sub": [
                                    "table-1-2__col"
                                ]
                            },
                            components=[
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Kwota",
                                    name="totalTaskCost",
                                    calculation_rules=[
                                        self.calculation_rule.dynamic_sum_inputs(
                                            fields=[
                                                "requestedPisfSupportAmount",
                                                "ownFundsTotalAmount",
                                                "financingEntitiesTotalAmount",
                                                "publicEntitiesTotalAmount"
                                            ]
                                        )
                                    ],
                                    read_only=True,
                                    validators=[
                                        self.validator.related_sum_validator(
                                            field_names=[
                                                "requestedPisfSupportAmount",
                                                "ownFundsTotalAmount",
                                                "financingEntitiesTotalAmount",
                                                "publicEntitiesTotalAmount"
                                            ]
                                        )
                                    ],
                                    unit="PLN"
                                ),
                                self.create_component(
                                    component_type="number",
                                    label="Udział w budżecie całkowitym",
                                    name="totalTaskCostShare",
                                    calculation_rules=[
                                        self.calculation_rule.share_calculator(
                                            dividend_field="totalTaskCost",
                                            divisor_field="totalTaskCost",
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_share_validator(
                                            dividend="totalTaskCost",
                                            divisor="totalTaskCost",
                                        )
                                    ],
                                    unit="%",
                                    read_only=True,
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="2. Wnioskowana wysokość dofinansowania ze środków PISF",
                            class_list={
                                "sub": [
                                    "table-1-2-top",
                                ]
                            },
                            components=[
                                self.create_chapter(
                                    class_list={
                                        "main": [
                                            "table-1-3",
                                            "grid",
                                            "grid-cols-5"
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
                                            validators=[
                                                self.validator.related_mapped_limit_validator(
                                                    options=[
                                                        {
                                                            "limit": 7000000.0,
                                                            "conditions": [
                                                                {
                                                                    "field_name": "movieKind",
                                                                    "value": "animowany"
                                                                },
                                                                {
                                                                    "field_name": "movieSubject",
                                                                    "value": "film autorski"
                                                                },
                                                                {
                                                                    "field_name": "eventMovieDuration",
                                                                    "value": "pełnometrażowy"
                                                                },
                                                                {
                                                                    "field_name": "isFirstExploitedInCinemas",
                                                                    "value": "Tak"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "limit": 7000000.0,
                                                            "conditions": [
                                                                {
                                                                    "field_name": "movieKind",
                                                                    "value": "animowany"
                                                                },
                                                                {
                                                                    "field_name": "movieSubject",
                                                                    "value": "film o tematyce historycznej"
                                                                },
                                                                {
                                                                    "field_name": "eventMovieDuration",
                                                                    "value": "pełnometrażowy"
                                                                },
                                                                {
                                                                    "field_name": "isFirstExploitedInCinemas",
                                                                    "value": "Tak"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "limit": 3000000.0,
                                                            "conditions": [
                                                                {
                                                                    "field_name": "movieKind",
                                                                    "value": "animowany"
                                                                },
                                                                {
                                                                    "field_name": "movieSubject",
                                                                    "value": "film autorski"
                                                                },
                                                                {
                                                                    "field_name": "eventMovieDuration",
                                                                    "value": "pełnometrażowy"
                                                                },
                                                                {
                                                                    "field_name": "isFirstExploitedInCinemas",
                                                                    "value": "Nie"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "limit": 3000000.0,
                                                            "conditions": [
                                                                {
                                                                    "field_name": "movieKind",
                                                                    "value": "animowany"
                                                                },
                                                                {
                                                                    "field_name": "movieSubject",
                                                                    "value": "film o tematyce historycznej"
                                                                },
                                                                {
                                                                    "field_name": "eventMovieDuration",
                                                                    "value": "pełnometrażowy"
                                                                },
                                                                {
                                                                    "field_name": "isFirstExploitedInCinemas",
                                                                    "value": "Nie"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "limit": 700000.0,
                                                            "conditions": [
                                                                {
                                                                    "field_name": "movieKind",
                                                                    "value": "animowany"
                                                                },
                                                                {
                                                                    "field_name": "movieSubject",
                                                                    "value": "film autorski"
                                                                },
                                                                {
                                                                    "field_name": "eventMovieDuration",
                                                                    "value": "średniometrażowy"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "limit": 700000.0,
                                                            "conditions": [
                                                                {
                                                                    "field_name": "movieKind",
                                                                    "value": "animowany"
                                                                },
                                                                {
                                                                    "field_name": "movieSubject",
                                                                    "value": "film o tematyce historycznej"
                                                                },
                                                                {
                                                                    "field_name": "eventMovieDuration",
                                                                    "value": "średniometrażowy"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "limit": 700000.0,
                                                            "conditions": [
                                                                {
                                                                    "field_name": "movieKind",
                                                                    "value": "animowany"
                                                                },
                                                                {
                                                                    "field_name": "movieSubject",
                                                                    "value": "film dla młodego widza lub widowni familijnej"
                                                                },
                                                                {
                                                                    "field_name": "eventMovieDurationFamily",
                                                                    "value": "średniometrażowy"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "limit": 400000.0,
                                                            "conditions": [
                                                                {
                                                                    "field_name": "movieKind",
                                                                    "value": "animowany"
                                                                },
                                                                {
                                                                    "field_name": "movieSubject",
                                                                    "value": "film autorski"
                                                                },
                                                                {
                                                                    "field_name": "eventMovieDuration",
                                                                    "value": "krótkometrażowy"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "limit": 400000.0,
                                                            "conditions": [
                                                                {
                                                                    "field_name": "movieKind",
                                                                    "value": "animowany"
                                                                },
                                                                {
                                                                    "field_name": "movieSubject",
                                                                    "value": "film o tematyce historycznej"
                                                                },
                                                                {
                                                                    "field_name": "eventMovieDuration",
                                                                    "value": "krótkometrażowy"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "limit": 400000.0,
                                                            "conditions": [
                                                                {
                                                                    "field_name": "movieKind",
                                                                    "value": "animowany"
                                                                },
                                                                {
                                                                    "field_name": "movieSubject",
                                                                    "value": "film dla młodego widza lub widowni familijnej"
                                                                },
                                                                {
                                                                    "field_name": "eventMovieDurationFamily",
                                                                    "value": "krótkometrażowy"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "limit": 6000000.0,
                                                            "conditions": [
                                                                {
                                                                    "field_name": "movieKind",
                                                                    "value": "seria animowana"
                                                                },
                                                                {
                                                                    "field_name": "numberOfEpisodes",
                                                                    "value": "52"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "limit": 3000000.0,
                                                            "conditions": [
                                                                {
                                                                    "field_name": "movieKind",
                                                                    "value": "seria animowana"
                                                                },
                                                                {
                                                                    "field_name": "numberOfEpisodes",
                                                                    "value": "26"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "limit": 1500000.0,
                                                            "conditions": [
                                                                {
                                                                    "field_name": "movieKind",
                                                                    "value": "seria animowana"
                                                                },
                                                                {
                                                                    "field_name": "numberOfEpisodes",
                                                                    "value": "13"
                                                                }
                                                            ]
                                                        }
                                                    ],
                                                    default_limit=0
                                                )
                                            ],
                                            unit="PLN"
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Udział w budżecie całkowitym",
                                            name="requestedPisfSupportShare",
                                            read_only=True,
                                            validators=[
                                                self.validator.related_mapped_limit_validator(
                                                    options=[
                                                        {
                                                            "limit": 90.0,
                                                            "conditions": [
                                                                {
                                                                    "field_name": "isDifficultPiece",
                                                                    "value": "Tak"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "limit": 50.0,
                                                            "conditions": [
                                                                {
                                                                    "field_name": "isDifficultPiece",
                                                                    "value": "Nie"
                                                                }
                                                            ]
                                                        }
                                                    ],
                                                    default_limit=50
                                                )
                                            ],
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field="requestedPisfSupportAmount",
                                                    divisor_field="totalTaskCost"
                                                )
                                            ],
                                            unit="%"
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Udział w budżecie strony polskiej",
                                            name="requestedPisfSupportSharePl",
                                            read_only=True,
                                            validators=[
                                                self.validator.related_mapped_limit_validator(
                                                    default_limit=100.01
                                                )
                                            ],
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    divisor_field="requestedPisfSupportAmount",
                                                    dividend_field="domesticFinancingTotalAmount"
                                                )
                                            ],
                                            unit="%"
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="3. Łączna wysokość pozostałych środków publicznych",
                            class_list={
                                "main": [
                                    "table-1-2",
                                    "grid",
                                    "grid-cols-3"
                                ],
                                "sub": [
                                    "table-1-2__col"
                                ]
                            },
                            components=[
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Kwota",
                                    name="requestedOtherPublicSupportAmount",
                                    read_only=True,
                                    calculation_rules=[
                                        self.calculation_rule.dynamic_sum_inputs(
                                            fields=[
                                                "publicEntitiesTotalAmountPoland",
                                                "publicEntitiesTotalAmountOther"
                                            ]
                                        )
                                    ],
                                    unit="PLN"
                                ),
                                self.create_component(
                                    component_type="number",
                                    label="Udział w budżecie całkowitym",
                                    name="requestedOtherPublicSupportShare",
                                    read_only=True,
                                    calculation_rules=[
                                        self.calculation_rule.share_calculator(
                                            dividend_field="publicEntitiesTotalAmount",
                                            divisor_field="totalTaskCost"
                                        )
                                    ],
                                    unit="%"
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="4. Deklarowana wysokość środków własnych producenta",
                            class_list={
                                "sub": [
                                    "table-1-2-top"
                                ]
                            },
                            components=[
                                self.create_chapter(
                                    title="<normal>- źródło pochodzenia: Polska </normal>",
                                    multiple_forms_rules={
                                        "minCount": 1,
                                        "maxCount": 10
                                    },
                                    class_list={
                                        "sub": [
                                            "table-1-2-top"
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
                                                    component_type="country",
                                                    label="Kraj pochodzenia środków",
                                                    name="ownFundsCountryNamePoland",
                                                    value="Polska",
                                                    default_value="Polska",
                                                    read_only=True,
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Wkład finansowy",
                                                    name="ownFundsFinancialInputAmountPoland",
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Wkład rzeczowy",
                                                    name="ownFundsInKindInputsAmountPoland",
                                                    unit="PLN",
                                                    help_text="Kwota PLN (pole do uzupełnienia tylko w przypadku wyboru źródła: wkład finansowo-rzeczowy Producenta)"
                                                ),
                                                self.create_component(
                                                    component_type="select",
                                                    label="Źródło wkładu",
                                                    name="ownFundsSourcePoland",
                                                    options=[
                                                        "wkład finansowo-rzeczowy Producenta",
                                                        "minimum gwarantowane",
                                                        "licencja",
                                                        "pożyczka",
                                                        "kredyt",
                                                        "środki od sponsora"
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Wkład łącznie",
                                                    name="ownFundsTotalInputPoland",
                                                    read_only=True,
                                                    calculation_rules=[
                                                        self.calculation_rule.local_sum(
                                                            fields=[
                                                                "ownFundsFinancialInputAmountPoland",
                                                                "ownFundsInKindInputsAmountPoland"
                                                            ]
                                                        )
                                                    ],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Udział w budżecie całkowitym",
                                                    name="ownFundsTotalSharePoland",
                                                    read_only=True,
                                                    calculation_rules=[
                                                        self.calculation_rule.single_position_share_calculator(
                                                            dividend_field="ownFundsTotalInputPoland",
                                                            divisor_field="totalTaskCost"
                                                        )
                                                    ],
                                                    unit="%"
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    class_list={
                                        "sub": [
                                            "displayNone"
                                        ]
                                    },
                                    components=[
                                        self.create_chapter(
                                            title="<normal>- źródło pochodzenia inne niż Polska </normal>",
                                            multiple_forms_rules={
                                                "minCount": 1,
                                                "maxCount": 10
                                            },
                                            class_list={
                                                "sub": [
                                                    "table-1-2-top"
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
                                                            component_type="country",
                                                            label="Kraj pochodzenia środków",
                                                            name="ownFundsCountryNameOther",
                                                        ),
                                                        self.create_component(
                                                            component_type="text",
                                                            mask="fund",
                                                            label="Wkład finansowy",
                                                            name="ownFundsFinancialInputAmountOther",
                                                            unit="PLN"
                                                        ),
                                                        self.create_component(
                                                            component_type="text",
                                                            mask="fund",
                                                            label="Wkład rzeczowy",
                                                            name="ownFundsInKindInputsAmountOther",
                                                            unit="PLN",
                                                        ),
                                                        self.create_component(
                                                            component_type="text",
                                                            mask="fund",
                                                            label="Wkład łącznie",
                                                            name="ownFundsTotalInputOther",
                                                            read_only=True,
                                                            calculation_rules=[
                                                                self.calculation_rule.local_sum(
                                                                    fields=[
                                                                        "ownFundsFinancialInputAmountOther",
                                                                        "ownFundsInKindInputsAmountOther"
                                                                    ]
                                                                )
                                                            ],
                                                            unit="PLN"
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Udział w budżecie całkowitym",
                                                            name="ownFundsTotalShareOther",
                                                            read_only=True,
                                                            calculation_rules=[
                                                                self.calculation_rule.single_position_share_calculator(
                                                                    dividend_field="ownFundsTotalInputOther",
                                                                    divisor_field="totalTaskCost"
                                                                )
                                                            ],
                                                            unit="%"
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>Razem</normal>",
                                    class_list={
                                        "sub": [
                                            "table-1-2-top"
                                        ]
                                    },
                                    components=[
                                        self.create_chapter(
                                            class_list={
                                                "main": [
                                                    "table-1-3",
                                                    "grid",
                                                    "grid-cols-5"
                                                ],
                                                "sub": [
                                                    "table-1-3__col"
                                                ]
                                            },
                                            components=[
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Wkład finansowy łącznie dla kraju: Polska",
                                                    name="ownFinancialInputAmountPolandSum",
                                                    read_only=True,
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "ownFundsFinancialInputAmountPoland"
                                                            ]
                                                        )
                                                    ],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Wkład finansowy łącznie dla krajów innych niż Polska",
                                                    name="ownFinancialInputAmountOtherSum",
                                                    read_only=True,
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "ownFundsFinancialInputAmountOther"
                                                            ]
                                                        )
                                                    ],
                                                    class_list=["displayNone"],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Wkład finansowy łącznie",
                                                    name="ownFinancialInputAmountAltogether",
                                                    read_only=True,
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "ownFinancialInputAmountPolandSum",
                                                                "ownFinancialInputAmountOtherSum"
                                                            ]
                                                        )
                                                    ],
                                                    class_list=["displayNone"],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Wkład rzeczowy łącznie dla kraju: Polska",
                                                    name="ownInKindInputAmountPolandSum",
                                                    read_only=True,
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "ownFundsInKindInputsAmountPoland"
                                                            ]
                                                        )
                                                    ],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Wkład rzeczowy łącznie dla krajów innych niż Polska",
                                                    name="ownInKindInputAmountOtherSum",
                                                    read_only=True,
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "ownFundsInKindInputsAmountOther"
                                                            ]
                                                        )
                                                    ],
                                                    class_list=["displayNone"],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Wkład rzeczowy łącznie",
                                                    name="ownInKindInputAmountAltogether",
                                                    read_only=True,
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "ownInKindInputAmountPolandSum",
                                                                "ownInKindInputAmountOtherSum"
                                                            ]
                                                        )
                                                    ],
                                                    class_list=["displayNone"],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Kwota całkowita dla kraju pochodzenia: Polska",
                                                    name="ownFundsTotalAmountPoland",
                                                    read_only=True,
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "ownFinancialInputAmountPolandSum",
                                                                "ownInKindInputAmountPolandSum"
                                                            ]
                                                        )
                                                    ],
                                                    class_list=["displayNone"],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Kwota całkowita dla krajów pochodzenia innych niż Polska",
                                                    name="ownFundsTotalAmountOther",
                                                    read_only=True,
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "ownFinancialInputAmountOtherSum",
                                                                "ownInKindInputAmountOtherSum"
                                                            ]
                                                        )
                                                    ],
                                                    class_list=["displayNone"],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Kwota całkowita",
                                                    name="ownFundsTotalAmount",
                                                    read_only=True,
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "ownFundsTotalAmountPoland",
                                                                "ownFundsTotalAmountOther"
                                                            ]
                                                        )
                                                    ],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Udział w budżecie całkowitym",
                                                    name="ownFundsTotalShare",
                                                    read_only=True,
                                                    calculation_rules=[
                                                        self.calculation_rule.share_calculator(
                                                            dividend_field="ownFundsTotalAmount",
                                                            divisor_field="totalTaskCost"
                                                        )
                                                    ],
                                                    unit="%"
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Udział wkładu finansowego w łącznym wkładzie producenta",
                                                    name="ownFundsFinancialToTotalShare",
                                                    read_only=True,
                                                    validators=[
                                                        self.validator.range_validator(
                                                            min_value=5,
                                                            message="Wkład finansowy nie może być mniejszy niż 5% łącznego wkładu producenta."
                                                        )
                                                    ],
                                                    calculation_rules=[
                                                        self.calculation_rule.share_calculator(
                                                            dividend_field="ownFinancialInputAmountAltogether",
                                                            divisor_field="ownFundsTotalAmount"
                                                        )
                                                    ],
                                                    unit="%"
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Udział wkładu rzeczowego w łącznym wkładzie producenta",
                                                    name="ownFundsInKindToTotalShare",
                                                    read_only=True,
                                                    validators=[
                                                        self.validator.range_validator(
                                                            max_value=95,
                                                            message="Wkład rzeczowy nie może przekroczyć 95% łącznego wkładu producenta."
                                                        )
                                                    ],
                                                    calculation_rules=[
                                                        self.calculation_rule.share_calculator(
                                                            dividend_field="ownInKindInputAmountAltogether",
                                                            divisor_field="ownFundsTotalAmount"
                                                        )
                                                    ],
                                                    unit="%"
                                                )
                                            ]
                                        ),
                                        self.create_chapter(
                                            visibility_rules=[
                                                self.visibility_rule.depends_on_value(
                                                    field_name="categoryOfProject",
                                                    values=[
                                                        "produkcja krajowa",
                                                        "koprodukcja międzynarodowa większościowa"
                                                    ]
                                                )
                                            ],
                                            components=[
                                                self.create_component(
                                                    component_type="number",
                                                    label="Udział wkładu własnego do kwoty dofinansowania",
                                                    name="ownFundsTotalShareToRequestedAmount",
                                                    read_only=True,
                                                    calculation_rules=[
                                                        self.calculation_rule.share_calculator(
                                                            dividend_field="ownFundsTotalAmount",
                                                            divisor_field="requestedPisfSupportAmount"
                                                        )
                                                    ],
                                                    validators=[
                                                        self.validator.range_validator(
                                                            max_value=5,
                                                            message="Wkład własny nie może stanowić mniej niż 5% wnioskowanej kwoty dofinansowania."
                                                        )
                                                    ],
                                                    unit="%"
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>Opinia bankowa o rachunku firmy producenta zgodnie z Programem Operacyjnym Produkcja Filmowa</normal>",
                                    multiple_forms_rules={
                                        "minCount": 1,
                                        "maxCount": 5
                                    },
                                    components=[
                                        self.create_chapter(
                                            components=[
                                                self.create_component(
                                                    component_type="file",
                                                    name="bankReviewAttachments",
                                                    required=True
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="5. Pozostałe źródła finansowania prywatne oraz środki z programów wspólnotowych Eurimages, Creative Europe",
                            class_list={
                                "sub": [
                                    "table-1-2-top"
                                ]
                            },
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="checkbox",
                                            label="Zaznacz, aby dodać środki finansowania w tej kategorii",
                                            name="isOtherPrivateFinancing"
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="isOtherPrivateFinancing",
                                            values=[True]
                                        )
                                    ],
                                    components=[
                                        self.create_chapter(
                                            title="<normal>Wyszczególnienie podmiotów finansujących </normal><br /><small> Uwaga! <normal>Odznaczenie checkboxa nie prowadzi do automatycznego usunięcia zawartych w danej sekcji informacji. Dane te nadal będą brane pod uwagę w obliczeniach finansowych i będą uwzględnione we wniosku. Jeżeli dane te nie są już potrzebne, prosimy o ich ręczne usunięcie. </small></normal>",

                                            components=[
                                                self.create_chapter(
                                                    components=[
                                                        self.create_chapter(
                                                            components=[
                                                                self.create_component(
                                                                    component_type="checkbox",
                                                                    label="Dodaj środki o kraju pochodzenia: Polska",
                                                                    name="addOtherPrivateSourcesPolish"
                                                                )
                                                            ]
                                                        ),
                                                        self.create_chapter(
                                                            title="<normal>- źródło pochodzenia: Polska </normal>",
                                                            visibility_rules=[
                                                                self.visibility_rule.depends_on_value(
                                                                    field_name="addOtherPrivateSourcesPolish",
                                                                    values=[True]
                                                                )
                                                            ],
                                                            multiple_forms_rules={
                                                                "minCount": 1,
                                                                "maxCount": 10
                                                            },
                                                            components=[
                                                                self.create_chapter(
                                                                    class_list={
                                                                        "sub": [
                                                                            "table-1-2-top"
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
                                                                                    component_type="country",
                                                                                    label="Kraj pochodzenia środków",
                                                                                    name="financingEntityCountryNamePoland",
                                                                                    value="Polska",
                                                                                    default_value="Polska",
                                                                                    read_only=True
                                                                                ),
                                                                                self.create_component(
                                                                                    component_type="text",
                                                                                    label="Nazwa podmiotu",
                                                                                    name="financingPrivateEntityNamePoland"
                                                                                ),
                                                                                self.create_component(
                                                                                    component_type="select",
                                                                                    label="Rodzaj podmiotu",
                                                                                    name="financingEntityTypePoland",
                                                                                    options=[
                                                                                        "koproducent",
                                                                                        "dystrybutor",
                                                                                        "agent sprzedaży",
                                                                                        "inwestor",
                                                                                        "sponsor",
                                                                                        "instytucja kultury",
                                                                                        "fundusz",
                                                                                        "nadawca telewizyjny",
                                                                                        "stowarzyszenie",
                                                                                        "platforma streamingowa",
                                                                                        "inne"
                                                                                    ]
                                                                                ),
                                                                                self.create_component(
                                                                                    component_type="text",
                                                                                    mask="fund",
                                                                                    label="Wkład finansowy",
                                                                                    name="financingEntityFinancialInputAmountPoland",
                                                                                    unit="PLN"
                                                                                ),
                                                                                self.create_component(
                                                                                    component_type="text",
                                                                                    mask="fund",
                                                                                    label="Wkład rzeczowy",
                                                                                    name="financingEntityInKindInputsAmountPoland",
                                                                                    unit="PLN"
                                                                                ),
                                                                                self.create_component(
                                                                                    component_type="text",
                                                                                    mask="fund",
                                                                                    label="Wkład łącznie",
                                                                                    name="financingEntityTotalInputPoland",
                                                                                    unit="PLN",
                                                                                    calculation_rules=[
                                                                                        self.calculation_rule.local_sum(
                                                                                            fields=[
                                                                                                "financingEntityFinancialInputAmountPoland",
                                                                                                "financingEntityInKindInputsAmountPoland"
                                                                                            ]
                                                                                        )
                                                                                    ]
                                                                                ),
                                                                                self.create_component(
                                                                                    component_type="number",
                                                                                    label="Udział w budżecie całkowitym",
                                                                                    name="financingEntityTotalSharePoland",
                                                                                    read_only=True,
                                                                                    calculation_rules=[
                                                                                        self.calculation_rule.single_position_share_calculator(
                                                                                            dividend_field="financingEntityTotalInputPoland",
                                                                                            divisor_field="totalTaskCost"
                                                                                        )
                                                                                    ],
                                                                                    unit="%"
                                                                                )
                                                                            ]
                                                                        ),
                                                                        self.create_chapter(
                                                                            visibility_rules=[
                                                                                self.visibility_rule.depends_on_value(
                                                                                    field_name="applicationRelates",
                                                                                    values=[
                                                                                        "promesa"
                                                                                    ]
                                                                                )
                                                                            ],
                                                                            components=[
                                                                                self.create_component(
                                                                                    component_type="file",
                                                                                    label="Umowa na podstawie której nastąpi finansowanie przedsięwzięcia bądź aktualny (nie starszy niż 6 miesięcy w dniu składania wniosku do PISF) list intencyjny z konkretnymi kwotami netto deklarowanego udziału",
                                                                                    name="pledgePrivateFinancingAttachmentPoland"
                                                                                )
                                                                            ]
                                                                        ),
                                                                        self.create_chapter(
                                                                            visibility_rules=[
                                                                                self.visibility_rule.depends_on_value(
                                                                                    field_name="applicationRelates",
                                                                                    values=[
                                                                                        "umowa"
                                                                                    ]
                                                                                )
                                                                            ],
                                                                            components=[
                                                                                self.create_component(
                                                                                    component_type="file",
                                                                                    label="Umowa na podstawie której nastąpi finansowanie przedsięwzięcia",
                                                                                    name="contractPrivateFinancingAttachmentPoland"
                                                                                )
                                                                            ]
                                                                        )
                                                                    ]
                                                                )
                                                            ]
                                                        ),
                                                    ]
                                                ),
                                                self.create_chapter(
                                                    components=[
                                                        self.create_chapter(
                                                            components=[
                                                                self.create_component(
                                                                    component_type="checkbox",
                                                                    label="Dodaj środki o kraju pochodzenia innym niż Polska",
                                                                    name="addOtherPrivateSourcesNonPolish"
                                                                )
                                                            ]
                                                        ),
                                                        self.create_chapter(
                                                            title="<normal>- źródło pochodzenia inne niż Polska </normal>",
                                                            visibility_rules=[
                                                                self.visibility_rule.depends_on_value(
                                                                    field_name="addOtherPrivateSourcesNonPolish",
                                                                    values=[True]
                                                                )
                                                            ],
                                                            multiple_forms_rules={
                                                                "minCount": 1,
                                                                "maxCount": 10
                                                            },
                                                            components=[
                                                                self.create_chapter(
                                                                    class_list={
                                                                        "sub": [
                                                                            "table-1-2-top"
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
                                                                                    component_type="country",
                                                                                    label="Kraj pochodzenia środków",
                                                                                    name="financingEntityCountryNameOther"
                                                                                ),
                                                                                self.create_component(
                                                                                    component_type="text",
                                                                                    label="Nazwa podmiotu",
                                                                                    name="financingPrivateEntityNameOther"
                                                                                ),
                                                                                self.create_component(
                                                                                    component_type="select",
                                                                                    label="Rodzaj podmiotu",
                                                                                    name="financingEntityTypeOther",
                                                                                    options=[
                                                                                        "koproducent",
                                                                                        "dystrybutor",
                                                                                        "agent sprzedaży",
                                                                                        "inwestor",
                                                                                        "sponsor",
                                                                                        "instytucja kultury",
                                                                                        "fundusz",
                                                                                        "nadawca telewizyjny",
                                                                                        "stowarzyszenie",
                                                                                        "platforma streamingowa",
                                                                                        "inne"
                                                                                    ]
                                                                                ),
                                                                                self.create_component(
                                                                                    component_type="text",
                                                                                    mask="fund",
                                                                                    label="Wkład finansowy",
                                                                                    name="financingEntityFinancialInputAmountOther",
                                                                                    unit="PLN"
                                                                                ),
                                                                                self.create_component(
                                                                                    component_type="text",
                                                                                    mask="fund",
                                                                                    label="Wkład rzeczowy",
                                                                                    name="financingEntityInKindInputsAmountOther",
                                                                                    unit="PLN"
                                                                                ),
                                                                                self.create_component(
                                                                                    component_type="text",
                                                                                    mask="fund",
                                                                                    label="Wkład łącznie",
                                                                                    name="financingEntityTotalInputOther",
                                                                                    unit="PLN",
                                                                                    calculation_rules=[
                                                                                        self.calculation_rule.local_sum(
                                                                                            fields=[
                                                                                                "financingEntityFinancialInputAmountOther",
                                                                                                "financingEntityInKindInputsAmountOther"
                                                                                            ]
                                                                                        )
                                                                                    ]
                                                                                ),
                                                                                self.create_component(
                                                                                    component_type="number",
                                                                                    label="Udział w budżecie całkowitym",
                                                                                    name="financingEntityTotalShareOther",
                                                                                    read_only=True,
                                                                                    calculation_rules=[
                                                                                        self.calculation_rule.single_position_share_calculator(
                                                                                            dividend_field="financingEntityTotalInputOther",
                                                                                            divisor_field="totalTaskCost"
                                                                                        )
                                                                                    ],
                                                                                    unit="%"
                                                                                )
                                                                            ]
                                                                        ),
                                                                        self.create_chapter(
                                                                            visibility_rules=[
                                                                                self.visibility_rule.depends_on_value(
                                                                                    field_name="applicationRelates",
                                                                                    values=[
                                                                                        "promesa"
                                                                                    ]
                                                                                )
                                                                            ],
                                                                            components=[
                                                                                self.create_component(
                                                                                    component_type="file",
                                                                                    label="Umowa na podstawie której nastąpi finansowanie przedsięwzięcia bądź aktualny (nie starszy niż 6 miesięcy w dniu składania wniosku do PISF) list intencyjny z konkretnymi kwotami netto deklarowanego udziału",
                                                                                    name="pledgePrivateFinancingAttachmentOther"
                                                                                )
                                                                            ]
                                                                        ),
                                                                        self.create_chapter(
                                                                            visibility_rules=[
                                                                                self.visibility_rule.depends_on_value(
                                                                                    field_name="applicationRelates",
                                                                                    values=[
                                                                                        "umowa"
                                                                                    ]
                                                                                )
                                                                            ],
                                                                            components=[
                                                                                self.create_component(
                                                                                    component_type="file",
                                                                                    label="Umowa na podstawie której nastąpi finansowanie przedsięwzięcia",
                                                                                    name="contractPrivateFinancingAttachmentOther"
                                                                                )
                                                                            ]
                                                                        )
                                                                    ]
                                                                )
                                                            ]
                                                        ),
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_chapter(
                                            title="<normal>Razem </normal>",
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
                                                    label="Wkład finansowy łącznie dla kraju: Polska",
                                                    name="financingEntitiesFinancialInputAmountPolandSum",
                                                    read_only=True,
                                                    class_list=["displayNone"],
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "financingEntityFinancialInputAmountPoland"
                                                            ]
                                                        )
                                                    ],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Wkład finansowy łącznie dla krajów innych niż Polska",
                                                    name="financingEntitiesFinancialInputAmountOtherSum",
                                                    read_only=True,
                                                    class_list=["displayNone"],
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "financingEntityFinancialInputAmountOther"
                                                            ]
                                                        )
                                                    ],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Wkład finansowy łącznie",
                                                    name="financingEntitiesFinancialInputAmountAltogether",
                                                    read_only=True,
                                                    class_list=["displayNone"],
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "financingEntitiesFinancialInputAmountPolandSum",
                                                                "financingEntitiesFinancialInputAmountOtherSum"
                                                            ]
                                                        )
                                                    ],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Wkład rzeczowy łącznie dla kraju: Polska",
                                                    name="financingEntitiesInKindInputAmountPolandSum",
                                                    read_only=True,
                                                    class_list=["displayNone"],
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "financingEntityInKindInputsAmountPoland"
                                                            ]
                                                        )
                                                    ],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Wkład rzeczowy łącznie dla krajów innych niż Polska",
                                                    name="financingEntitiesInKindInputAmountOtherSum",
                                                    read_only=True,
                                                    class_list=["displayNone"],
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "financingEntityInKindInputsAmountOther"
                                                            ]
                                                        )
                                                    ],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Wkład rzeczowy łącznie",
                                                    name="financingEntitiesInKindInputAmountAltogether",
                                                    read_only=True,
                                                    class_list=["displayNone"],
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "financingEntitiesInKindInputAmountPolandSum",
                                                                "financingEntitiesInKindInputAmountOtherSum"
                                                            ]
                                                        )
                                                    ],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Kwota całkowita dla kraju: Polska",
                                                    name="financingEntitiesTotalAmountPoland",
                                                    read_only=True,
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "financingEntitiesFinancialInputAmountPolandSum",
                                                                "financingEntitiesInKindInputAmountPolandSum"
                                                            ]
                                                        )
                                                    ],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Kwota całkowita dla krajów innych niż Polska",
                                                    name="financingEntitiesTotalAmountOther",
                                                    read_only=True,
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "financingEntitiesFinancialInputAmountOtherSum",
                                                                "financingEntitiesInKindInputAmountOtherSum"
                                                            ]
                                                        )
                                                    ],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Kwota całkowita",
                                                    name="financingEntitiesTotalAmount",
                                                    read_only=True,
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "financingEntitiesTotalAmountPoland",
                                                                "financingEntitiesTotalAmountOther"
                                                            ]
                                                        )
                                                    ],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Udział w budżecie całkowitym",
                                                    name="financingEntitiesTotalShare",
                                                    read_only=True,
                                                    calculation_rules=[
                                                        self.calculation_rule.share_calculator(
                                                            dividend_field="financingEntitiesTotalAmount",
                                                            divisor_field="totalTaskCost"
                                                        )
                                                    ],
                                                    unit="%"
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="6. Pozostałe publiczne źródła finansowania",
                            class_list={
                                "sub": [
                                    "table-1-2-top"
                                ]
                            },
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="checkbox",
                                            label="Zaznacz, aby dodać środki finansowania w tej kategorii",
                                            name="isOtherPublicFinancing"
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="isOtherPublicFinancing",
                                            values=[True]
                                        )
                                    ],
                                    components=[
                                        self.create_chapter(
                                            title="<normal>Wyszczególnienie podmiotów finansujących </normal><br /><small> Uwaga! <normal>Odznaczenie checkboxa nie prowadzi do automatycznego usunięcia zawartych w danej sekcji informacji. Dane te nadal będą brane pod uwagę w obliczeniach finansowych i będą uwzględnione we wniosku. Jeżeli dane te nie są już potrzebne, prosimy o ich ręczne usunięcie. </small></normal>",
                                            components=[
                                                self.create_chapter(
                                                    components=[
                                                        self.create_chapter(
                                                            components=[
                                                                self.create_component(
                                                                    component_type="checkbox",
                                                                    label="Dodaj środki o kraju pochodzenia: Polska",
                                                                    name="addOtherPublicSourcesPolish"
                                                                )
                                                            ]
                                                        ),
                                                        self.create_chapter(
                                                            title="<normal>- źródło pochodzenia: Polska </normal>",
                                                            visibility_rules=[
                                                                self.visibility_rule.depends_on_value(
                                                                    field_name="addOtherPublicSourcesPolish",
                                                                    values=[True]
                                                                )
                                                            ],
                                                            multiple_forms_rules={
                                                                "minCount": 1,
                                                                "maxCount": 10
                                                            },
                                                            components=[
                                                                self.create_chapter(
                                                                    class_list={
                                                                        "sub": [
                                                                            "table-1-2-top"
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
                                                                                    component_type="country",
                                                                                    label="Kraj pochodzenia środków",
                                                                                    name="publicEntityCountryNamePoland",
                                                                                    value="Polska",
                                                                                    default_value="Polska",
                                                                                    read_only=True
                                                                                ),
                                                                                self.create_component(
                                                                                    component_type="text",
                                                                                    label="Nazwa podmiotu",
                                                                                    name="publicPrivateEntityNamePoland"
                                                                                ),
                                                                                self.create_component(
                                                                                    component_type="select",
                                                                                    label="Rodzaj podmiotu",
                                                                                    name="publicEntityTypePoland",
                                                                                    options=[
                                                                                        "instytut filmowy",
                                                                                        "instytucja kultury",
                                                                                        "fundusz",
                                                                                        "inne"
                                                                                    ]
                                                                                ),
                                                                                self.create_component(
                                                                                    component_type="text",
                                                                                    mask="fund",
                                                                                    label="Wkład finansowy",
                                                                                    name="publicEntityFinancialInputAmountPoland",
                                                                                    unit="PLN"
                                                                                ),
                                                                                self.create_component(
                                                                                    component_type="text",
                                                                                    mask="fund",
                                                                                    label="Wkład rzeczowy",
                                                                                    name="publicEntityInKindInputsAmountPoland",
                                                                                    unit="PLN"
                                                                                ),
                                                                                self.create_component(
                                                                                    component_type="text",
                                                                                    mask="fund",
                                                                                    label="Wkład łącznie",
                                                                                    name="publicEntityTotalInputPoland",
                                                                                    unit="PLN",
                                                                                    calculation_rules=[
                                                                                        self.calculation_rule.local_sum(
                                                                                            fields=[
                                                                                                "financingEntityFinancialInputAmountPoland",
                                                                                                "financingEntityInKindInputsAmountPoland"
                                                                                            ]
                                                                                        )
                                                                                    ]
                                                                                ),
                                                                                self.create_component(
                                                                                    component_type="number",
                                                                                    label="Udział w budżecie całkowitym",
                                                                                    name="publicEntityTotalSharePoland",
                                                                                    read_only=True,
                                                                                    calculation_rules=[
                                                                                        self.calculation_rule.single_position_share_calculator(
                                                                                            dividend_field="publicEntityTotalInputPoland",
                                                                                            divisor_field="totalTaskCost"
                                                                                        )
                                                                                    ],
                                                                                    unit="%"
                                                                                )
                                                                            ]
                                                                        ),
                                                                        self.create_chapter(
                                                                            visibility_rules=[
                                                                                self.visibility_rule.depends_on_value(
                                                                                    field_name="applicationRelates",
                                                                                    values=[
                                                                                        "promesa"
                                                                                    ]
                                                                                )
                                                                            ],
                                                                            components=[
                                                                                self.create_component(
                                                                                    component_type="file",
                                                                                    label="Umowa na podstawie której nastąpi finansowanie przedsięwzięcia bądź oświadczenie producenta dot. pokrycia finansowania",
                                                                                    name="pledgePublicFinancingAttachmentPoland"
                                                                                )
                                                                            ]
                                                                        ),
                                                                        self.create_chapter(
                                                                            visibility_rules=[
                                                                                self.visibility_rule.depends_on_value(
                                                                                    field_name="applicationRelates",
                                                                                    values=[
                                                                                        "umowa"
                                                                                    ]
                                                                                )
                                                                            ],
                                                                            components=[
                                                                                self.create_component(
                                                                                    component_type="file",
                                                                                    label="Umowa na podstawie której nastąpi finansowanie przedsięwzięcia bądź oświadczenie producenta dot. pokrycia finansowania",
                                                                                    name="contractPublicFinancingAttachmentPoland"
                                                                                )
                                                                            ]
                                                                        )
                                                                    ]
                                                                )
                                                            ]
                                                        ),
                                                    ]
                                                ),
                                                self.create_chapter(
                                                    components=[
                                                        self.create_chapter(
                                                            components=[
                                                                self.create_component(
                                                                    component_type="checkbox",
                                                                    label="Dodaj środki o kraju pochodzenia innym niż Polska",
                                                                    name="addOtherPublicSourcesNonPolish"
                                                                )
                                                            ]
                                                        ),
                                                        self.create_chapter(
                                                            title="<normal>- źródło pochodzenia inne niż Polska </normal>",
                                                            visibility_rules=[
                                                                self.visibility_rule.depends_on_value(
                                                                    field_name="addOtherPublicSourcesNonPolish",
                                                                    values=[True]
                                                                )
                                                            ],
                                                            multiple_forms_rules={
                                                                "minCount": 1,
                                                                "maxCount": 10
                                                            },
                                                            components=[
                                                                self.create_chapter(
                                                                    class_list={
                                                                        "sub": [
                                                                            "table-1-2-top"
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
                                                                                    component_type="country",
                                                                                    label="Kraj pochodzenia środków",
                                                                                    name="publicEntityCountryNameOther"
                                                                                ),
                                                                                self.create_component(
                                                                                    component_type="text",
                                                                                    label="Nazwa podmiotu",
                                                                                    name="publicPrivateEntityNameOther"
                                                                                ),
                                                                                self.create_component(
                                                                                    component_type="select",
                                                                                    label="Rodzaj podmiotu",
                                                                                    name="publicEntityTypeOther",
                                                                                    options=[
                                                                                        "instytut filmowy",
                                                                                        "instytucja kultury",
                                                                                        "fundusz",
                                                                                        "inne"
                                                                                    ]
                                                                                ),
                                                                                self.create_component(
                                                                                    component_type="text",
                                                                                    mask="fund",
                                                                                    label="Wkład finansowy",
                                                                                    name="publicEntityFinancialInputAmountOther",
                                                                                    unit="PLN"
                                                                                ),
                                                                                self.create_component(
                                                                                    component_type="text",
                                                                                    mask="fund",
                                                                                    label="Wkład rzeczowy",
                                                                                    name="publicEntityInKindInputsAmountOther",
                                                                                    unit="PLN"
                                                                                ),
                                                                                self.create_component(
                                                                                    component_type="text",
                                                                                    mask="fund",
                                                                                    label="Wkład łącznie",
                                                                                    name="publicEntityTotalInputOther",
                                                                                    unit="PLN",
                                                                                    calculation_rules=[
                                                                                        self.calculation_rule.local_sum(
                                                                                            fields=[
                                                                                                "publicEntityFinancialInputAmountOther",
                                                                                                "publicEntityInKindInputsAmountOther"
                                                                                            ]
                                                                                        )
                                                                                    ]
                                                                                ),
                                                                                self.create_component(
                                                                                    component_type="number",
                                                                                    label="Udział w budżecie całkowitym",
                                                                                    name="publicEntityTotalShareOther",
                                                                                    read_only=True,
                                                                                    calculation_rules=[
                                                                                        self.calculation_rule.single_position_share_calculator(
                                                                                            dividend_field="publicEntityTotalInputOther",
                                                                                            divisor_field="totalTaskCost"
                                                                                        )
                                                                                    ],
                                                                                    unit="%"
                                                                                )
                                                                            ]
                                                                        ),
                                                                        self.create_chapter(
                                                                            visibility_rules=[
                                                                                self.visibility_rule.depends_on_value(
                                                                                    field_name="applicationRelates",
                                                                                    values=[
                                                                                        "promesa"
                                                                                    ]
                                                                                )
                                                                            ],
                                                                            components=[
                                                                                self.create_component(
                                                                                    component_type="file",
                                                                                    label="Umowa na podstawie której nastąpi finansowanie przedsięwzięcia bądź oświadczenie producenta dot. pokrycia finansowania",
                                                                                    name="pledgePublicFinancingAttachmentOther"
                                                                                )
                                                                            ]
                                                                        ),
                                                                        self.create_chapter(
                                                                            visibility_rules=[
                                                                                self.visibility_rule.depends_on_value(
                                                                                    field_name="applicationRelates",
                                                                                    values=[
                                                                                        "umowa"
                                                                                    ]
                                                                                )
                                                                            ],
                                                                            components=[
                                                                                self.create_component(
                                                                                    component_type="file",
                                                                                    label="Umowa na podstawie której nastąpi finansowanie przedsięwzięcia bądź oświadczenie producenta dot. pokrycia finansowania",
                                                                                    name="contractPublicFinancingAttachmentOther"
                                                                                )
                                                                            ]
                                                                        )
                                                                    ]
                                                                )
                                                            ]
                                                        ),
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_chapter(
                                            title="<normal>Razem </normal>",
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
                                                    label="Wkład finansowy łącznie dla kraju: Polska",
                                                    name="publicEntitiesFinancialInputAmountPolandSum",
                                                    read_only=True,
                                                    class_list=["displayNone"],
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "publicEntityFinancialInputAmountPoland"
                                                            ]
                                                        )
                                                    ],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Wkład finansowy łącznie dla krajów innych niż Polska",
                                                    name="publicEntitiesFinancialInputAmountOtherSum",
                                                    read_only=True,
                                                    class_list=["displayNone"],
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "publicEntityFinancialInputAmountOther"
                                                            ]
                                                        )
                                                    ],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Wkład finansowy łącznie",
                                                    name="publicEntitiesFinancialInputAmountAltogether",
                                                    read_only=True,
                                                    class_list=["displayNone"],
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "publicEntitiesFinancialInputAmountPolandSum",
                                                                "publicEntitiesFinancialInputAmountOtherSum"
                                                            ]
                                                        )
                                                    ],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Wkład rzeczowy łącznie dla kraju: Polska",
                                                    name="publicEntitiesInKindInputAmountPolandSum",
                                                    read_only=True,
                                                    class_list=["displayNone"],
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "publicEntityInKindInputsAmountPoland"
                                                            ]
                                                        )
                                                    ],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Wkład rzeczowy łącznie dla krajów innych niż Polska",
                                                    name="publicEntitiesInKindInputAmountOtherSum",
                                                    read_only=True,
                                                    class_list=["displayNone"],
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "publicEntityInKindInputsAmountOther"
                                                            ]
                                                        )
                                                    ],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Wkład rzeczowy łącznie",
                                                    name="publicEntitiesInKindInputAmountAltogether",
                                                    read_only=True,
                                                    class_list=["displayNone"],
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "publicEntitiesInKindInputAmountPolandSum",
                                                                "publicEntitiesInKindInputAmountOtherSum"
                                                            ]
                                                        )
                                                    ],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Kwota całkowita dla kraju: Polska",
                                                    name="publicEntitiesTotalAmountPoland",
                                                    read_only=True,
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "publicEntitiesFinancialInputAmountPolandSum",
                                                                "publicEntitiesInKindInputAmountPolandSum"
                                                            ]
                                                        )
                                                    ],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Kwota całkowita dla krajów innych niż Polska",
                                                    name="publicEntitiesTotalAmountOther",
                                                    read_only=True,
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "publicEntitiesFinancialInputAmountOtherSum",
                                                                "publicEntitiesInKindInputAmountOtherSum"
                                                            ]
                                                        )
                                                    ],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Kwota całkowita",
                                                    name="publicEntitiesTotalAmount",
                                                    read_only=True,
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "publicEntitiesTotalAmountPoland",
                                                                "publicEntitiesTotalAmountOther"
                                                            ]
                                                        )
                                                    ],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Udział w budżecie całkowitym",
                                                    name="publicEntitiesTotalShare",
                                                    read_only=True,
                                                    calculation_rules=[
                                                        self.calculation_rule.share_calculator(
                                                            dividend_field="publicEntitiesTotalAmount",
                                                            divisor_field="totalTaskCost"
                                                        )
                                                    ],
                                                    unit="%"
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
                    title="OŚWIADCZENIA",
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Oświadczam, że w projekcie nie występują inne środki publiczne niż te, wskazane w strukturze finansowania powyżej, a łączny udział środków publicznych nie przekracza limitów określonych w Rozporządzeniu Ministra Kultury w sprawie udzielania przez Polski Instytut Sztuki Filmowej dofinansowania przedsięwzięć z zakresu kinematografii/wystawionego listu intencyjnego załączonego do wniosku o dofinansowanie.",
                            name="noOtherPublicFundsStatement",
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="KOSZTORYS",
                    components=[
                        self.create_chapter(
                            title="<normal>Kosztorys szczegółowy (według wzoru elektronicznego dostępnego na stronie internetowej PISF) </normal>",
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="categoryOfProject",
                                    values=[
                                        "produkcja krajowa",
                                    ]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="file",
                                    name="costEstimateDomesticProductionAttachmentXlsm",
                                    help_text="Plik XLSM. Maksymalny rozmiar pliku: 50 MB.",
                                    required=True
                                ),
                                self.create_component(
                                    component_type="file",
                                    name="costEstimateDomesticProductionAttachmentPdf",
                                    help_text="Plik PDF. Maksymalny rozmiar pliku: 50 MB."
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="categoryOfProject",
                                    values=[
                                        "koprodukcja międzynarodowa większościowa"
                                    ]
                                )
                            ],
                            components=[
                                self.create_chapter(
                                    title="<normal>Kosztorys szczegółowy (według wzoru elektronicznego dostępnego na stronie internetowej PISF) </normal>",
                                    components=[
                                        self.create_component(
                                            component_type="file",
                                            name="costEstimateMajorityProductionAttachmentXlsm",
                                            help_text="Plik XLSM. Maksymalny rozmiar pliku: 50 MB.",
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="file",
                                            name="costEstimateMajorityProductionAttachmentPdf",
                                            help_text="Plik PDF. Maksymalny rozmiar pliku: 50 MB."
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>Spis polskich elementów twórczych i produkcyjnych z uwzględnieniem minimum określonego w PO Produkcja filmowa </normal>",
                                    components=[
                                        self.create_component(
                                            component_type="file",
                                            name="polishElementsMajorityAttachmentPdf",
                                            help_text="Plik PDF. Maksymalny rozmiar pliku: 50 MB.",
                                            required=True
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>Wykaz innych środków publiczych (przeliczone na PLN z podaniem przyjętego kursu waluty)</normal>",
                                    multiple_forms_rules={
                                        "minCount": 1,
                                        "maxCount": 5
                                    },
                                    components=[
                                        self.create_chapter(
                                            components=[
                                                self.create_component(
                                                    component_type="file",
                                                    name="listOfOtherPublicFunds",
                                                    required=True,
                                                    help_text="Plik PDF. Maksymalny rozmiar pliku: 50 MB."
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
                    title="DODATKOWE ZAŁĄCZNIKI (opcjonalne)",
                    multiple_forms_rules={
                        "minCount": 1,
                        "maxCount": 20
                    },
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="file",
                                    name="optionalAttachments"
                                )
                            ]
                        )
                    ]
                )
            ]
        )

        self.save_part(part)

