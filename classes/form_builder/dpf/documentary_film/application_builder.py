from classes.form_builder.dpf.application_builder import DPFApplicationBuilder


class DocumentaryFilmApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'IV. Produkcja filmów dokumentalnych'
    PRIORITY_NUM = 4
    FORM_ID = 9197

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.department_data_path / 'documentary_film'

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
                self.section.application_basic_data.scope_of_project_kind(
                    number="2",
                    options=[
                        "produkcja koprodukcji mniejszościowej"
                    ]
                ),
                self.section.application_basic_data.movie_kind(
                    number="3",
                    options=[
                        "dokumentalny"
                    ]
                ),
                self.section.application_basic_data.movie_subject(
                    number="4",
                    options=[
                        "film autorski",
                        "film o tematyce historycznej",
                        "film dla młodego widza lub widowni familijnej"
                    ],
                    validators=[
                        self.validator.related_allowed_options_validator(
                            field_name="movieKind",
                            mapping={
                                "fabularny": [
                                    "film autorski",
                                    "film o tematyce historycznej",
                                    "film dla młodego widza lub widowni familijnej"
                                ],
                                "animowany": [
                                    "film autorski",
                                    "film o tematyce historycznej",
                                    "film dla młodego widza lub widowni familijnej"
                                ],
                                "dokumentalny": [
                                    "film autorski",
                                    "film o tematyce historycznej"
                                ],
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
                self.section.application_basic_data.category_of_project(
                    number="7",
                    options=[
                        "koprodukcja międzynarodowa mniejszościowa"
                    ]
                ),
                self.section.application_basic_data.application_relates(
                    number="8",
                    options=[
                        "promesa",
                        "umowa"
                    ]
                ),
                self.section.application_basic_data.kind_of_support(
                    number="9",
                    options=[
                        "dotacja",
                        "pożyczka",
                        "poręczenie"
                    ]
                ),
                self.create_chapter(
                    title="10. Wybór lidera komisji eksperckiej",
                    components=[
                        self.section.application_basic_data.one_stage_commission(
                            number="10",
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
                self.section.application_attachments.document_attachments(),
                self.section.application_attachments.opinion_of_the_historian(),
                self.section.application_attachments.opition_of_the_child_psychologist(),
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
                                                "fabularny",
                                                "animowany"
                                            ]
                                        )
                                    ],
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
                                ),
                                self.create_chapter(
                                    title="Scenariusz filmu</br><normal><small>lub treatment wraz z podaniem uzasadnienia w oddzielnym pliku</small></normal>",
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="movieKind",
                                            values=[
                                                "dokumentalny"
                                            ]
                                        )
                                    ],
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
                                                            label="Scenariusz filmu lub treatment",
                                                            name="movieScreenplayAttachmentDoc",
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
                                                    name="tagsKetWordsDoc",
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
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="movieKind",
                                    values=[
                                        "animowany"
                                    ]
                                )
                            ],
                            components=[
                                self.section.application_information_data.production_team_member(
                                    title="Autor opracowania plastycznego",
                                    name="animationDesigner",
                                    is_vacant=True,
                                ),
                            ]
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
                        ),
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
                                self.section.application_information_data.production_team_member(
                                    title="Wiodący aktorzy",
                                    name="leadingActor",
                                    is_multi=True,
                                    is_not_applicable=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Minimalny wkład artystyczny polskich twórców",
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="categoryOfProject",
                                    values=[
                                        "koprodukcja międzynarodowa mniejszościowa"
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
                                        self.create_chapter(
                                            title="zaangażowanie co najmniej jednego z polskich twórców",
                                            class_list=[
                                                "grid",
                                                "grid-cols-3"
                                            ],
                                            components=[
                                                self.create_component(
                                                    component_type="checkbox",
                                                    label=comp["label"],
                                                    name=f"minorityCoproductionAtLeastOne{comp["name"]}Fab"
                                                ) for comp in [
                                                    {
                                                        "label": "Reżyser",
                                                        "name": "Director"
                                                    },
                                                    {
                                                        "label": "Scenarzysta",
                                                        "name": "Screenwriter"
                                                    },
                                                    {
                                                        "label": "Aktor pierwszoplanowy",
                                                        "name": "LeadingActor"
                                                    },
                                                    {
                                                        "label": "Operator",
                                                        "name": "DirectorOfPhotography"
                                                    },
                                                    {
                                                        "label": "Scenograf",
                                                        "name": "SceneDirector"
                                                    },
                                                    {
                                                        "label": "Montażysta",
                                                        "name": "Editor"
                                                    },
                                                    {
                                                        "label": "Kompozytor",
                                                        "name": "Composer"
                                                    }
                                                ]
                                            ]
                                        ),
                                        self.create_chapter(
                                            title="zaangażowanie co najmniej trzech z polskich twórców",
                                            class_list=[
                                                "grid",
                                                "grid-cols-3"
                                            ],
                                            components=[
                                                self.create_component(
                                                    component_type="checkbox",
                                                    label=comp["label"],
                                                    name=f"minorityCoproductionAtLeastThree{comp["name"]}Fab"
                                                ) for comp in [
                                                    {
                                                        "label": "VFX Supervisor",
                                                        "name": "VfxSupervisor"
                                                    },
                                                    {
                                                        "label": "Charakteryzator",
                                                        "name": "MakeupArtist"
                                                    },
                                                    {
                                                        "label": "Kostiumograf",
                                                        "name": "CostumeDesigner"
                                                    },
                                                    {
                                                        "label": "Główny realizator dźwięku",
                                                        "name": "SoundDesigner"
                                                    },
                                                    {
                                                        "label": "Jeden aktor drugoplanowy",
                                                        "name": "SupportingActor"
                                                    },
                                                    {
                                                        "label": "Dwóch aktorów drugoplanowych (wymaga zaangażowania dwóch dodatkowych osób spośród wyżej wymienionych)",
                                                        "name": "SupportingActors"
                                                    }
                                                ]
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="movieKind",
                                            values=[
                                                "animowany"
                                            ]
                                        )
                                    ],
                                    components=[
                                        self.create_chapter(
                                            title="zaangażowanie co najmniej jednego z polskich twórców",
                                            class_list=[
                                                "grid",
                                                "grid-cols-3"
                                            ],
                                            components=[
                                                self.create_component(
                                                    component_type="checkbox",
                                                    label=comp["label"],
                                                    name=f"minorityCoproductionAtLeastOne{comp["name"]}Ani"
                                                ) for comp in [
                                                    {
                                                        "label": "Reżyser animacji",
                                                        "name": "Director"
                                                    },
                                                    {
                                                        "label": "Scenarzysta",
                                                        "name": "Screenwriter"
                                                    },
                                                    {
                                                        "label": "Montażysta",
                                                        "name": "Editor"
                                                    },
                                                    {
                                                        "label": "Kompozytor",
                                                        "name": "Composer"
                                                    },
                                                    {
                                                        "label": "Animator",
                                                        "name": "Animator"
                                                    },
                                                    {
                                                        "label": "Polski autor scenopisu obrazkowego (storyboardu)",
                                                        "name": "PolishStoryboardCreator"
                                                    },
                                                    {
                                                        "label": "Polski autor projektów plastycznych",
                                                        "name": "PolishAnimationDesigner"
                                                    }
                                                ]
                                            ]
                                        ),
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
                                        self.create_chapter(
                                            title="wykotzystanie przynajmniej jednego z poniższych",
                                            components=[
                                                self.create_component(
                                                    component_type="checkbox",
                                                    label=comp["label"],
                                                    name=f"minorityCoproductionAtLeastOne{comp["name"]}Doc"
                                                ) for comp in [
                                                    {
                                                        "label": "Reżyser animacji",
                                                        "name": "Director"
                                                    },
                                                    {
                                                        "label": "Scenarzysta",
                                                        "name": "Screenwriter"
                                                    },
                                                    {
                                                        "label": "Montażysta",
                                                        "name": "Editor"
                                                    },
                                                    {
                                                        "label": "Autor zdjęć",
                                                        "name": "DirectorOfPhotography"
                                                    },
                                                    {
                                                        "label": "Kompozytor",
                                                        "name": "Composer"
                                                    },
                                                    {
                                                        "label": "Zostaną wykorzystane materiały z polskich archiwów filmowych",
                                                        "name": "PolishMaterialsFromArchives"
                                                    },
                                                    {
                                                        "label": "Weźmie udział polski bohater",
                                                        "name": "PolishHeroTakePart"
                                                    },
                                                    {
                                                        "label": "Dominująca tematyka związana z Polską (historycznie lub geograficznie)",
                                                        "name": "DominantTopicOfPoland"
                                                    }
                                                ]
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
                            title="Okres zdjęciowy",
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
                                    name="scheduleShootingPeriodStart",
                                    calculation_rules=[
                                        self.calculation_rule.relate_to_last_date(
                                            field="schedulePrepPeriodEnd",
                                            parameter=1
                                        )
                                    ],
                                    read_only=True,
                                    validators=[
                                        self.validator.related_date_lte_validator(
                                            field_name="scheduleShootingPeriodEnd",
                                            message="Termin rozpoczęcia działania musi być wcześniejszy niż termin jego rozpoczęcia."
                                        )
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="date",
                                    label="Termin do",
                                    name="scheduleShootingPeriodEnd",
                                    validators=[
                                        self.validator.related_date_gte_validator(
                                            field_name="scheduleShootingPeriodStart",
                                            message="Termin zakończenia działania musi być późniejszy niż termin jego rozpoczęcia."
                                        )
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Okres montażu i udźwiękowienia",
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
                                            field="scheduleShootingPeriodEnd",
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
                        ),
                        self.create_chapter(
                            title="Baza produkcyjna producenta wiodącego (w przypadku koprodukcji międzynarodowych)",
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="categoryOfProject",
                                    values=[
                                        "koprodukcja międzynarodowa mniejszościowa"
                                    ]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="plannedLeadProducerBase",
                                    validators=[
                                        self.validator.length_validator(max_value=200)
                                    ],
                                    required=True
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="OŚWIADCZENIA",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="checkbox",
                                    label="Oświadczam, że przedsięwzięcie przed datą złożenia wniosku nie miało publicznego pokazu, premiery, pierwszej emisji, pokazu festiwalowego, przeglądu publicznego itp.",
                                    name="schedulePublicPremiereDeclaration",
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="categoryOfProject",
                                    values=[
                                        "koprodukcja międzynarodowa mniejszościowa"
                                    ]
                                )
                            ],
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="checkbox",
                                            name="scheduleShootingPeriodDeclaration",
                                            validators=[
                                                self.validator.checkbox_true_date_lte_today(
                                                    field_name="scheduleShootingPeriodStart"
                                                )
                                            ],
                                            label="Oświadczam, że nie rozpoczął się jeszcze okres zdjęciowy dla przedsięwzięcia",
                                            help_text="W przeciwnym razie należy załączyć do wniosku zgodę Dyrektora na złożenie wniosku"
                                        ),
                                    ]
                                ),
                                self.create_chapter(
                                    title="Zgoda Dyrektora PISF",
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="scheduleShootingPeriodDeclaration",
                                            values=[
                                                False
                                            ]
                                        )
                                    ],
                                    multiple_forms_rules={
                                        "minCount": 1,
                                        "maxCount": 100
                                    },
                                    components=[
                                        self.create_chapter(
                                            components=[
                                                self.create_component(
                                                    component_type="file",
                                                    name="schedulePisfDirectorAgreement",
                                                    required=True,
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

        self.save_part(part=part)

    def create_application_financial_data(self):
        pass
