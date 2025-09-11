from classes.form_builder.components.component.dpf_component import DPFComponent
from classes.form_builder.components.section.section import Section
from classes.form_builder.form_builder_base import FormBuilderBase
from typing import List, Optional


class DPFSection(Section):
    def __init__(self):
        super().__init__()

        self.application_basic_data = ApplicationBasicData()
        self.application_statements = ApplicationStatements()
        self.application_attachments = ApplicationAttachments()


class ApplicationBasicData(FormBuilderBase):
    def __init__(self):
        super().__init__()

    def scope_of_project(self, number: int | str, options: List[str]):
        return self.create_chapter(
            title=f"{number}. Zakres przedsięwzięcia",
            components=[
                self.create_component(
                    component_type="select",
                    name="scopeOfProject",
                    options=options,
                    required=True
                )
            ]
        )

    def scope_of_project_kind(self, number: int | str, options: List[str], calculation_rules: Optional[List[dict]] = None):
        return self.create_chapter(
            title=f"{number}. Przedsięwzięcie jest:",
            components=[
                self.create_component(
                    component_type="select",
                    name="scopeOfProjectKind",
                    options=options,
                    required=True,
                    calculation_rules=calculation_rules
                )
            ]
        )

    def movie_kind(self, number: int | str, options: List[str]):
        return self.create_chapter(
            title=f"{number}. Rodzaj filmowy",
            components=[
                self.create_component(
                    component_type="select",
                    name="movieKind",
                    options=options,
                    required=True
                )
            ]
        )

    def movie_subject(self, number: int | str, options: List[str], validators: Optional[List[dict]] = None, is_film_about_history: bool = False):
        chapter = self.create_chapter(
            title=f"{number}. Tematyka",
            components=[
                self.create_component(
                    component_type="select",
                    name="movieSubject",
                    options=options,
                    validators=validators,
                    required=True
                )
            ]
        )
        if is_film_about_history:
            chapter["components"].append(
                self.create_component(
                    component_type="radio",
                    label="Czy film jest o tematyce historycznej?",
                    name="isFilmAboutHistory",
                    options=[
                        "Tak", "Nie"
                    ],
                    required=True
                )
            )

        return chapter

    def piece_title(self, number: int | str):
        return self.create_chapter(
            title=f"{number}. Tytuł utworu audiowizualnego",
            components=[
                self.create_component(
                    component_type="text",
                    name="pieceTitle",
                    required=True,
                    validators=[
                        self.validator.length_validator(max_value=200)
                    ]
                )
            ]
        )

    def short_movie_description(self, number: int | str):
        return self.create_chapter(
            title=f"{number}. Krótki opis filmu",
            components=[
                self.create_component(
                    component_type="textarea",
                    name="shortMovieDescription",
                    required=True,
                    validators=[
                        self.validator.length_validator(max_value=5400)
                    ]
                )
            ]
        )

    def category_of_project(self, number: int | str, options: List[str]):
        chapter = self.create_chapter(
            title=f"{number}. Kategoria przedsięwzięcia",
            components=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="select",
                            name="categoryOfProject",
                            options=options,
                            required=True
                        )
                    ]
                )
            ]
        )

        value = 'koprodukcja międzynarodowa większościowa'
        second_value = "koprodukcja międzynarodowa mniejszościowa"

        values = []
        if value in options:
            values.append(value)
        if second_value in options:
            values.append(second_value)

        if value in options or second_value in options:
            inside_chapter = self.create_chapter(
                visibility_rules=[
                    self.visibility_rule.depends_on_value(
                        field_name="categoryOfProject",
                        values=[values]
                    )
                ],
                components=[
                    self.create_component(
                        component_type="select",
                        label=f"{number}.1. Wyłączne prawa wnioskodawcy na terytorium Polski",
                        name="movieRights",
                        options=["Tak"],
                        required=True
                    ),
                    self.create_component(
                        component_type="countryMulti",
                        label=f"{number}.2. Kraje koprodukcji",
                        name="coproductionCountries",
                        required=True
                    )
                ]
            )

            if second_value in options:
                inside_chapter["components"].append(
                    self.create_component(
                        component_type="select",
                        label=f"{number}.3. Rodzaj koprodukcji",
                        name="coproductionKind",
                        options=[
                            "koprodukcja dwustronna",
                            "koprodukcja wielostronna"
                        ],
                        required=True
                    )
                )

            chapter["components"].append(inside_chapter)


        if value in options:
            chapter["components"].append(
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="categoryOfProject",
                            values=[value]
                        )
                    ],
                    components=[

                    ]
                )
            )

        return chapter

    def application_relates(self, number: int | str, options: List[str]):
        return self.create_chapter(
            title=f"{number}. Wniosek dotyczy",
            components=[
                self.create_component(
                    component_type="select",
                    name="applicationRelates",
                    options=options,
                    required=True
                )
            ]
        )

    def kind_of_support(self, number, options: List[str]):
        chapter = self.create_chapter(
            title=f"{number}. Rodzaj pomocy",
            components=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="select",
                            name="kindOfSupport",
                            options=options,
                            required=True
                        )
                    ]
                )
            ]
        )

        value = "pożyczka"
        if value in options:
            chapter["components"].append(
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="kindOfSupport",
                            values=[value]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="textarea",
                            label=f"{number}.1. Sposób zabezpieczenia pożyczki",
                            name="methodOfSecuringTheLoan",
                            validators=[
                                self.validator.length_validator(
                                    max_value=900
                                )
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="textarea",
                            label=f"{number}.2. Proponowane raty spłaty pożyczki",
                            name="proposedLoanPaymentInstallments",
                            validators=[
                                self.validator.length_validator(
                                    max_value=900
                                )
                            ],
                            required=True
                        )
                    ]
                )
            )

        value = "poręczenie"
        if value in options:
            chapter["components"].append(
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="kindOfSupport",
                            values=[value]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="textarea",
                            label=f"{number}.1. Przedmiot zobowiązania",
                            name="subjectOfObligation",
                            validators=[
                                self.validator.length_validator(
                                    max_value=900
                                )
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="textarea",
                            label=f"{number}.2. Wysokość i okres poręczenia",
                            name="amountAndPeriodOfGuarantee",
                            validators=[
                                self.validator.length_validator(
                                    max_value=900
                                )
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="textarea",
                            label=f"{number}.3. Zabezpieczenie poręczenia",
                            name="securityOfGuarantee",
                            validators=[
                                self.validator.length_validator(
                                    max_value=900
                                )
                            ],
                            required=True
                        )
                    ]
                )
            )

        return chapter

    def one_stage_commission(self, number: int | str):
        return self.create_chapter(
            title=f"{number}.1. Komisja jednoetapowa"
        )

    def two_stages_commission(self, number: int | str, options: List[str], after_name: Optional[str] = ''):
        return self.create_chapter(
            title=f"{number}.1. Komisja dwuetapowa",
            components=[
                self.create_component(
                    component_type="select",
                    label=f"{number}.1.1. Lista pierwszego wyboru",
                    name=f"firstChoiceCommittee{after_name}",
                    options=options,
                    required=True
                ),
                self.create_component(
                    component_type="select",
                    label=f"{number}.1.2. Lista drugiego wyboru",
                    name=f"secondChoiceCommittee{after_name}",
                    options=options,
                    required=True
                ),
                self.create_component(
                    component_type="select",
                    label=f"{number}.1.3. W przypadku niedostępności wybranej komisji",
                    name=f"noCommitteeAvailable{after_name}",
                    options=[
                        "w przypadku niedostępności żadnej z dwóch wybranych komisji składam wniosek do następnej wolnej komisji",
                        "w przypadku niedostępności żadnej z dwóch wybranych komisji wycofuję wniosek z oceny"
                    ],
                    required=True
                )
            ]
        )


class ApplicationStatements(FormBuilderBase):
    def __init__(self):
        super().__init__()

        self.component = DPFComponent()

    def script_meet_bechdel_test_criteria(self):
        return self.create_chapter(
            title="Badanie prowadzone jest dla celów naukowych i nie ma wpływu na ocenę wniosku",
            components=[
                self.create_component(
                    component_type="radio",
                    label="Czy scenariusz spełnia kryterium testu Bechdel",
                    name="scriptMeetBechdelTestCriteria",
                    options=[
                        "Tak", "Nie"
                    ],
                    required=True
                )
            ]
        )

    def storage_of_blank_public_documents(self):
        return self.create_chapter(
            title="Przechowywanie blankietów dokumentów publicznych oraz dokumentów publicznych",
            components=[
                self.create_chapter(
                    title="<small>Art. 43 ustawy z dnia 22 listopada 2018 r. o dokumentach publicznych. <br /><normal>1. Blankiety dokumentów publicznych przechowywane w miejscu ich personalizacji lub indywidualizacji oraz dokumenty publiczne przechowywane w miejscu ich wydawania zabezpiecza się przed dostępem osób nieuprawnionych, utratą, zniszczeniem lub uszkodzeniem. <br /> 2. Pomieszczenie, w którym są przechowywane dokumenty publiczne oraz blankiety tych dokumentów, jest zamykane, a dostęp do tego pomieszczenia mają wyłącznie osoby uprawnione. Jeżeli to pomieszczenie znajduje się na parterze, okna zewnętrzne są zabezpieczone: szybami odpornymi na przebicie lub rozbicie lub stalowymi żaluzjami albo siatkami stalowymi, lub okratowaniem. <br />3. Pomieszczenie, o którym mowa w ust.2, przeznaczone także do wydawania dokumentów publicznych posiada wydzieloną część, w której są przechowywane dokumenty publiczne, zabezpieczoną przed dostępem osób nieuprawnionych. <br />4. Dokumenty publiczne, o których mowa w art. 5 ust. 4, oraz blankiety tych dokumentów mogą być przechowywane w innym pomieszczeniu niż określone w ust. 2, jeżeli są przechowywane w szafie metalowej zamykanej lub w sejfie, do których dostęp mają wyłącznie osoby upoważnione. <br />5. Dostęp do pomieszczenia, o którym mowa w ust. 2, oraz do wydzielonej części pomieszczenia, o której mowa w ust. 3, a także do szafy metalowej zamykanej lub do sejfu, o którym mowa w ust. 4, jest rejestrowany. <br />6. Rejestrowanie dostępu, o którym mowa w ust. 5, może polegać na zamontowaniu systemu kontroli dostępu do pomieszczenia, o którym mowa w ust. 2, i wydzielonej części pomieszczenia, o której mowa w ust. 3, lub prowadzeniu rejestru wejść i wyjść do i z tego pomieszczenia oraz prowadzeniu rejestru wydawania i zwrotu kluczy do tego pomieszczenia i szafy metalowej zamykanej lub do sejfu, o których mowa w ust. 4.</small></normal><br /><small>Art. 44. <br /><normal>Dokumenty publiczne będące drukami ścisłego zarachowania oraz blankiety tych dokumentów są ewidencjonowane. Ewidencja dokumentów publicznych i blankietów tych dokumentów oraz dowody ich przekazania i odbioru zabezpiecza się przed dostępem osób nieuprawnionych w sposób przewidziany w art. 43 </small></normal>"
                )
            ]
        )

    def applicant_statements(self):
        return self.create_chapter(
            title="Oświadczenia wnioskodawcy",
            components=[
                self.component.application_statements.statement_act_on_cinematography(),
                self.component.application_statements.statement_necessary_resources(),
                self.component.application_statements.statement_article_twenty_two(),
                self.component.application_statements.statement_not_in_arrears(),
                self.component.application_statements.statement_pay_social_security(),
                self.component.application_statements.applicants_statement_of_no_ties()
            ]
        )

    def producer_statements(self):
        return self.create_chapter(
            title="Oświadczenia producenta",
            components=[
                self.create_chapter(
                    title="Jako producent oświadczam, że zapewnię, że dystrybucja filmu będzie odbywała się na zasadach zapewniających jak najszerszy, powszechny dostęp do filmu dofinansowanego przez PISF w szczególności z uwzględnieniem następujących zasad:",
                    components=[
                        self.component.application_statements.producer_statement_screening_to_all_cinemas(),
                        self.component.application_statements.screening_requirement_no_more_than_two(),
                        self.component.application_statements.film_had_no_public_screening()
                    ]
                )
            ]
        )

    def script_statements(self):
        return self.create_chapter(
            title="Oświadczenie dot. scenariusza",
            components=[
                self.script_meet_bechdel_test_criteria()
            ]
        )


class ApplicationAttachments(FormBuilderBase):
    def __init__(self):
        super().__init__()

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

    def distributor_explanation_and_film_promotion_and_distribution_plan(self):
        return self.create_chapter(
            title="Eksplikacja dystrybutora oraz plan promocji i dystrybucji filmu (dla filmów pełnometrażowych do kin)</br><normal><small>Należy załączyć dokument podpisany przez dystrybutora</small></normal>",
            components=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Nie dotyczy zgodnie z Programem Operacyjnym PISF - Produkcja Filmowa",
                            name="notApplicableDistributorsExplication"
                        )
                    ]
                ),
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="notApplicableDistributorsExplication",
                            values=[False]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="file",
                            name="distributorExplicationOnDistributionPlansAndStrategy",
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

    def animation_attachments(self):
        return self.create_chapter(
            title="ZAŁĄCZNIKI: FILM ANIMOWANY",
            components=[
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

    def other_additional_attachments(self):
        return self.create_chapter(
            title="INNE DODATKOWE ZAŁĄCZNIKI",
            components=[
                self.create_chapter(
                    title="Opinia historyka wraz z wykazem jego dorobku",
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="movieSubject",
                            values=[
                                "film o tematyce historycznej"
                            ]
                        )
                    ],
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
                                            name="opinionOfTheHistorian",
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
