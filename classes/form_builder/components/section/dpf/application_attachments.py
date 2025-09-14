from classes.form_builder.components.component.dpf_component import DPFComponent
from classes.form_builder.form_builder_base import FormBuilderBase


class ApplicationAttachments(FormBuilderBase):
    def __init__(self):
        super().__init__()

        self.component = DPFComponent()

    def factual_report_on_goals_and_effects_of_development_of_film_project(self):
        return self.create_chapter(
            title="Raport merytoryczny o celach i skutakach rozwoju projektu filmowego",
            components=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Nie dotyczy zgodnie z Programem Operacyjnym PISF - Produkcja Filmowa",
                            name="notApplicableReportOnTheObjectives"
                        )
                    ]
                ),
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="notApplicableReportOnTheObjectives",
                            values=[False]
                        )
                    ],
                    multiple_forms_rules={
                        "minCount": 1,
                        "maxCount": 5,
                    },
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="file",
                                    name="reportOnTheObjectivesAndEffectsOfProject",
                                    required=True
                                )
                            ]
                        )
                    ]
                )
            ]
        )

    def declaration_of_division_of_rights_coproduced_by_television_broadcaster(self):
        return self.create_chapter(
            title="Oświadczenie o podziale praw w przypadku projektów filmowych, których koproducentem jest nadawca telewizyjny bądź jednym ze źródeł finansowania są środki uzyskane od nadawcy telewizyjnego.",
            components=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Nie dotyczy zgodnie z Programem Operacyjnym PISF - Produkcja Filmowa",
                            name="notApplicablerightsSharingStatementTvBroadcaster"
                        )
                    ]
                ),
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="notApplicablerightsSharingStatementTvBroadcaster",
                            values=[False]
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
                                    name="rightsSharingStatementTvBroadcaster",
                                    required=True
                                )
                            ]
                        )
                    ]
                )
            ]
        )

    def film_promotion_and_distribution_plan(self):
        return self.create_chapter(
            title="Plan promocji i dystrybucji filmu",
            components=[
                self.create_component(
                    component_type="textarea",
                    label="Plan promocji i dystrybucji filmu",
                    name="promotionAndDistributionPlan",
                    validators=[
                        self.validator.length_validator(
                            max_value=5400
                        )
                    ],
                    required=True
                ),
                self.create_component(
                    component_type="file",
                    label="Plan promocji i dystrybucji filmu - Plik",
                    name="promotionAndDistributionPlanFile",
                    required=True
                )
            ]
        )

    def distributor_explanation_and_film_promotion_and_distribution_plan(self, after_name: str = ''):
        return self.create_chapter(
            title="Eksplikacja dystrybutora oraz plan promocji i dystrybucji filmu (dla filmów pełnometrażowych do kin)</br><normal><small>Należy załączyć dokument podpisany przez dystrybutora</small></normal>",
            components=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Nie dotyczy zgodnie z Programem Operacyjnym PISF - Produkcja Filmowa",
                            name=f"notApplicableDistributorsExplication{after_name}"
                        )
                    ]
                ),
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name=f"notApplicableDistributorsExplication{after_name}",
                            values=[False]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="file",
                            name=f"distributorExplicationOnDistributionPlansAndStrategy{after_name}",
                            help_text="Dokument nie jest obligatoryjny w przypadku debiutu reżyserskiego i drugiego filmu reżysera, jeżeli producent ubiega się o dotację dla Filmu trudnego.",
                            required=True
                        )
                    ]
                )
            ]
        )

    def letter_of_intent_from_distributor(self):
        return self.create_chapter(
            title="List intencyjny od dystrybutora. W przypadku filmów z polem eksploatacji innym niż kino należy załączyć dokument od firmy gwarantującej publiczną eksploatację.</br><normal><small>Należy załączyć dokument podpisany przez dystrybutora. W przypadku filmów z polem eksploatacji inne niż kino należy załączyć dokument podpisany przez firmę gwarantującą publiczną eksploatację.</small></normal>",
            components=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Nie dotyczy zgodnie z Programem Operacyjnym PISF - Produkcja Filmowa",
                            name="notApplicableLetterOfIntent"
                        )
                    ]
                ),
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="notApplicableLetterOfIntent",
                            values=[False]
                        )
                    ],
                    multiple_forms_rules={
                        "minCount": 1,
                        "maxCount": 5,
                    },
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="file",
                                    name="letterOfIntentFromDistributor",
                                    help_text="Dokument nie jest obligatoryjny w przypadku debiutu reżyserskiego i drugiego filmu reżysera, jeżeli producent ubiega się o dotację dla filmu trudnego.",
                                    required=True
                                )
                            ]
                        )
                    ]
                )
            ]
        )

    def animation_attachments(self, moodboard: bool = False):
        main_chapter = self.create_chapter(
            visibility_rules=[
                self.visibility_rule.depends_on_value(
                    field_name="movieKind",
                    values=["animowany", "seria animowana"]
                )
            ]
        )

        inside_chapter = self.create_chapter(
            title="ZAŁĄCZNIKI: FILM ANIMOWANY",
            components=[
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="movieKind",
                            values=["animowany"]
                        ),
                        self.visibility_rule.depends_on_value(
                            field_name="eventMovieDuration",
                            values=["pełnometrażowy"]
                        )
                    ],
                    components=[
                        self.distributor_explanation_and_film_promotion_and_distribution_plan(after_name="Ani")
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
                        self.create_chapter(
                            title="Jeden pełny odcinek serii",
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="checkbox",
                                            label="Nie dotyczy zgodnie z Programem Operacyjnym PISF - Produkcja Filmowa",
                                            name="fullEpisodeNotApplicable"
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="fullEpisodeNotApplicable",
                                            values=[False]
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
                                                    component_type="text",
                                                    label="Opis linku",
                                                    name="fullEpisodeDesc",
                                                    required=True,
                                                    validators=[
                                                        self.validator.length_validator(
                                                            max_value=200
                                                        )
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    label="Adres linku",
                                                    name="fullEpisodeLink",
                                                    required=True,
                                                    validators=[
                                                        self.validator.length_validator(
                                                            max_value=300
                                                        )
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    label="Dodatkowe informacje, np. hasło",
                                                    name="fullEpisodeAdditionalInfo",
                                                    required=True,
                                                    validators=[
                                                        self.validator.length_validator(
                                                            max_value=200
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
                            title="Projekty plastyczne",
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="checkbox",
                                            label="Nie dotyczy zgodnie z Programem Operacyjnym PISF - Produkcja Filmowa",
                                            name="animationDesignsNotApplicable"
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="animationDesignsNotApplicable",
                                            values=[False]
                                        )
                                    ],
                                    multiple_forms_rules={
                                        "minCount": 6,
                                        "maxCount": 20,
                                    },
                                    components=[
                                        self.create_chapter(
                                            components=[
                                                self.create_component(
                                                    component_type="file",
                                                    label="Projekty plastyczne",
                                                    name="animationDesigns",
                                                    required=True,
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Scenopis obrazkowy",
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="checkbox",
                                            label="Nie dotyczy zgodnie z Programem Operacyjnym PISF - Produkcja Filmowa",
                                            name="pictureStoryboardNotApplicable"
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="pictureStoryboardNotApplicable",
                                            values=[False]
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
                                                    label="Scenopis obrazkowy",
                                                    name="pictureStoryboard",
                                                    help_text="Obejmujący min. 25% planowanego czasu.",
                                                    required=True,
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Projekty plastyczne - linki",
                            multiple_forms_rules={
                                "minCount": 1,
                                "maxCount": 10,
                            },
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            label="Opis linku",
                                            name="animationDesignLinkDesc",
                                            validators=[
                                                self.validator.length_validator(
                                                    max_value=1000
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Adres linku",
                                            name="animationDesignsLinkAddress",
                                            validators=[
                                                self.validator.length_validator(
                                                    max_value=2000
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Dodatkowe informacje, np. hasło",
                                            name="animationDesignLinkAdditionalInfo",
                                            validators=[
                                                self.validator.length_validator(
                                                    max_value=100
                                                )
                                            ]
                                        ),
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )

        if moodboard:
            inside_chapter["components"].append(
                self.moodboard(after_name="Ani")
            )

        main_chapter["components"].append(inside_chapter)

        return main_chapter

    def feature_attachments(self):
        return self.create_chapter(
            visibility_rules=[
                self.visibility_rule.depends_on_value(
                    field_name="movieKind",
                    values=["fabularny"]
                )
            ],
            components=[
                self.create_chapter(
                    title="ZAŁĄCZNIKI: FILM FABULARNY",
                    components=[
                        self.distributor_explanation_and_film_promotion_and_distribution_plan("Fab"),
                        self.letter_of_intent_from_distributor(),
                        self.cast_and_characters(),
                        self.mood_book(after_name="Fab")
                    ]
                )
            ]
        )

    def document_attachments(self):
        return self.create_chapter(
            visibility_rules=[
                self.visibility_rule.depends_on_value(
                    field_name="movieKind",
                    values=["dokumentalny"]
                )
            ],
            components=[
                self.create_chapter(
                    title="ZAŁACZNIKI: FILM DOKUMENTALNY",
                    components=[
                        self.create_chapter(
                            title="Prezentacja bohatera lub tematu",
                            components=[
                                self.create_chapter(
                                    multiple_forms_rules={
                                        "minCount": 1,
                                        "maxCount": 5,
                                    },
                                    components=[
                                        self.create_chapter(
                                            components=[
                                                self.create_component(
                                                    component_type="file",
                                                    name="protagonistPresentationFile"
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Linki",
                            multiple_forms_rules={
                                "minCount": 1,
                                "maxCount": 10
                            },
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            label="Opis linku",
                                            name="linkDescriptionProtagonistPresentation"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Adres linku",
                                            name="linkAddressProtagonistPresentation"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Dodatkowe informacje, np. hasło",
                                            name="linkAdditionalInformationProtagonistPresentation"
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Umowa z bohaterem lub spadkobiercami (lub list intencyjny), na podstawie której udzielona została zgoda na udział w filmie oraz na wykorzystanie wizerunku",
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="checkbox",
                                            label="Nie dotyczy zgodnie z Programem Operacyjnym PISF - Produkcja Filmowa",
                                            name="notApplicableAgreementWithProtagonistOrHeirs"
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="notApplicableAgreementWithProtagonistOrHeirs",
                                            values=[False]
                                        )
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="file",
                                            name="agreementWithProtagonistOrHeirs",
                                            required=True,
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.mood_book(after_name="Doc")
                    ]
                )
            ]
        )

    def opinion_of_the_historian(self, is_film_about_history: bool = False):
        return self.create_chapter(
            visibility_rules=[
                self.visibility_rule.depends_on_value(
                    field_name="isFilmAboutHistory" if is_film_about_history else "movieSubject",
                    values=[
                        "Tak" if is_film_about_history else "film o tematyce historycznej"
                    ]
                )
            ],
            components=[
                self.create_chapter(
                    title="Opinia historyka wraz z wykazem jego dorobku",
                    multiple_forms_rules={
                        "minCount": 1,
                        "maxCount": 5,
                    },
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="file",
                                    name="opinionOfTheHistorian",
                                    required=True,
                                )
                            ]
                        )
                    ]
                )
            ]
        )

    def opition_of_the_child_psychologist(self):
        return self.create_chapter(
            visibility_rules=[
                self.visibility_rule.depends_on_value(
                    field_name="movieSubject",
                    values=[
                        "film dla młodego widza lub widowni familijnej"
                    ]
                ),
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
                    title="Opinia psychologa dziecięcego wraz z wykazem jego dorobku",
                    multiple_forms_rules={
                        "minCount": 1,
                        "maxCount": 5,
                    },
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="file",
                                    name="opinionOfChildPsychologist",
                                    required=True,
                                )
                            ]
                        )
                    ]
                )
            ]
        )

    def other_additional_attachments(self):
        return self.create_chapter(
            title="INNE DODATKOWE ZAŁĄCZNIKI",
            multiple_forms_rules={
                "minCount": 1,
                "maxCount": 20,
            },
            components=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="file",
                            name="otherAttachments"
                        )
                    ]
                )
            ]
        )

    def cast_and_characters(self):
        return self.create_chapter(
            title="Obsada aktorska wraz z charakterystyką postaci",
            components=[
                self.create_component(
                    component_type="file",
                    name="castAndCharacters",
                    required=True,
                )
            ]
        )

    def mood_book(self, after_name: str = ''):
        return self.create_chapter(
            title="Mood book wraz z listą lokacji",
            components=[
                self.create_component(
                    component_type="file",
                    label="Mood book wraz z listą lokacji",
                    name=f"moodBook{after_name}",
                ),
                self.create_component(
                    component_type="text",
                    label="Opis linku",
                    name=f"linkDescriptionMoodBook{after_name}",
                ),
                self.create_component(
                    component_type="text",
                    label="Adres linku",
                    name=f"linkAddressMoodBook{after_name}",
                ),
                self.create_component(
                    component_type="text",
                    label="Dodatkowe informacje, np. hasło",
                    name=f"linkAdditionalInformationMoodBook{after_name}",
                )
            ]
        )

    def moodboard(self, after_name: str = ''):
        return self.create_chapter(
            title="Moodboard",
            multiple_forms_rules={
                "minCount": 1,
                "maxCount": 5,
            },
            components=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="file",
                            label="Moodboard",
                            name=f"moodboard{after_name}",
                            required=True,
                        )
                    ]
                )
            ]
        )

    def detailed_list_of_tasks(self):
        return self.create_chapter(
            title="Lista szczegółowych zadań zaplanowanych do realizacji",
            components=[
                self.create_component(
                    component_type="textarea",
                    name="detailedListOfTasks",
                    validators=[
                        self.validator.length_validator(
                            max_value=5400
                        )
                    ],
                    required=True,
                )
            ]
        )

    def common_part(self):
        return self.create_chapter(
            title="Część wspólna",
            components=[
                self.component.application_attachments.description_of_artistic_qualities(),
                self.component.application_attachments.expected_results_indicator()
            ]
        )

    def additional_info_about_hero(self):
        return self.create_chapter(
            visibility_rules=[
                self.visibility_rule.depends_on_value(
                    field_name="movieKind",
                    values=["dokumentalny"]
                )
            ],
            components=[
                self.create_chapter(
                    title="Dodatkowe informacje o bohaterze",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="checkbox",
                                    label="Nie dotyczy",
                                    name="additionalHeroInfoDoesntApply"
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="additionalHeroInfoDoesntApply",
                                    values=[False]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="file",
                                    label="Dodatkowe informacje o bohaterze",
                                    name="additionalHeroInfo",
                                    required=True,
                                ),
                                self.create_component(
                                    component_type="textarea",
                                    label="Opis linku",
                                    name="additionalHeroInfoDesc",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=1000
                                        )
                                    ]
                                ),
                                self.create_component(
                                    component_type="textarea",
                                    label="Adres linku",
                                    name="additionalHeroInfoLink",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=2000
                                        )
                                    ]
                                ),
                                self.create_component(
                                    component_type="textarea",
                                    label="Dodatkowe informacje, np. hasło",
                                    name="additionalHeroInfoAdditionalInfo",
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
        )
