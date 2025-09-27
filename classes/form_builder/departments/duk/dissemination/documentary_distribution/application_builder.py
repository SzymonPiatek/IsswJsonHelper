from classes.form_builder.departments.duk.dissemination.application_builder import DisseminationApplicationBuilder
from classes.form_builder.departments.duk.application_builder import DUKApplicationBuilder
from classes.form_builder.departments.duk.dissemination.documentary_distribution.estimate_data import estimate_sections


class DocumentaryDistributionApplicationBuilder(DisseminationApplicationBuilder):
    PRIORITY_NAME = 'VI. Dystrybucja filmów dokumentalnych'
    PRIORITY_NUM = 6
    FORM_ID = 9189

    def __init__(self):
        super().__init__()

        self.estimate_sections = estimate_sections

    def create_application_basic_data(self, **kwargs):
        data = {
            'projectType': {
                'options': [
                    "Dystrybucja kinowa pełnometrażowych filmów dokumentalnych na terenie Polski"
                ]
            }
        }
        DUKApplicationBuilder.create_application_basic_data(self=self, data=data)

    def create_application_attachments(self):
        part = self.create_part(
            title="VI. Załączniki",
            short_name="VI. Załączniki",
            chapters=[
                self.create_chapter(
                    title="Obowiązkowe załączniki",
                    components=[
                        self.section.application_attachment.document_confirming_represent_applicant(),
                        self.section.application_attachment.schedule_information(),
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type='file',
                                    label="Umowa potwierdzająca prawa do dystrybucji filmu, zawierająca w szczególności postanowienia w zakresie przeniesienia praw albo udzielenia licencji wyłącznej na polu eksploatacji publicznego wyświetlania w kinach",
                                    name="agreementConfirmingRights",
                                    required=True
                                ),
                                self.create_component(
                                    component_type='file',
                                    label="Podział przychodów i zysków z dystrybucji, o ile umowa potwierdzająca prawa do dystrybucji nie zawiera wyżej wymienionych informacji",
                                    name="divisionRevenuesAndProfits",
                                    required=True
                                )
                            ]
                        )
                    ]
                ),
                self.section.application_attachment.other_attachments(),
                self.section.application_attachment.storage_of_blanks()
            ]
        )
        self.save_part(part)

    def create_application_scope_of_project(self):
        part = self.create_part(
            title="III. Zakres przedsięwzięcia i jego charakterystyka",
            short_name="III. Zakres przedsięwzięcia",
            chapters=[
                self.create_chapter(
                    title="1. Informacje o filmie przeznaczonym do dystrybucji",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type='text',
                                    label="Tytuł filmu",
                                    name="filmName",
                                    required=True,
                                    validators=[
                                        self.validator.length_validator(max_value=100)
                                    ]
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
                                    component_type='number',
                                    label="Rok produkcji",
                                    required=True,
                                    name="productionYear",
                                    validators=[
                                        self.validator.length_validator(max_value=4)
                                    ]
                                ),
                                self.create_component(
                                    component_type='number',
                                    label="Metraż filmu w minutach",
                                    name="filmFullLength",
                                    required=True,
                                    validators=[
                                        self.validator.range_validator(
                                            min_value=70,
                                            message="Długość filmu musi wynosić co najmniej 70 minut"
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Klasyfikacja filmu jako filmu polskiego",
                            components=[
                                self.create_chapter(
                                    title="<normal><small><b>a) Film jest filmem polskim w rozumieniu art. 4, ust. 2, pkt. 1 Ustawy:</b><br>Autor scenariusza lub adaptowanego utworu literackiego, reżyser oraz wykonawca jednej z głównych ról są obywatelami polskimi, udział środków finansowych producenta mającego siedzibę na terytorium Rzeczypospolitej Polskiej w kosztach produkcji filmu stanowi 100%, przy czym środki te, do wysokości 80% kosztów produkcji filmu, muszą być wydatkowane na terytorium Rzeczypospolitej Polskiej, a ponadto kopia wzorcowa jest wykonana w języku polskim.<br><br><b>b) Film jest filmem polskim w rozumieniu art. 4, ust. 2, pkt. 2 Ustawy:</b><br>Autor scenariusza lub adaptowanego utworu literackiego lub reżyser, lub wykonawca jednej z głównych ról są obywatelami polskimi, udział środków finansowych koproducenta mającego siedzibę na terytorium Rzeczypospolitej Polskiej w kosztach produkcji filmu stanowi co najmniej 20% przy filmie będącym koprodukcją dwustronną oraz co najmniej 10% przy filmie będącym koprodukcją wielostronną, przy czym środki te, do wysokości 80% kosztów produkcji filmu, muszą być wydatkowane na terytorium Rzeczypospolitej Polskiej, a ponadto główna wersja językowa wykonana jest w języku polskim.</normal></small>",
                                ),
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="radio",
                                            label="Klasyfikacja filmu",
                                            name="filmClassification",
                                            required=True,
                                            options=[
                                                "a) Film jest filmem polskim w rozumieniu art. 4, ust. 2, pkt. 1 Ustawy",
                                                "b) Film jest filmem polskim w rozumieniu art. 4, ust. 2, pkt. 2 Ustawy"
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Reżyser",
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
                                    name="directorFirstName",
                                    required=True
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Nazwisko",
                                    name="directorLastName",
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Producent",
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="Nazwa",
                                    name="producerName",
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Koproducenci</br><normal><small>Należy wymienić koproducentów, jeśli dotyczy</small></normal>",
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="checkbox",
                                            label="Nie dotyczy",
                                            name="notCoproducer"
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="notProducer",
                                            values=[
                                                False
                                            ]
                                        )
                                    ],
                                    multiple_forms_rules={
                                        "minCount": 1,
                                        "maxCount": 10
                                    },
                                    components=[
                                        self.create_chapter(
                                            title="Koproducent",
                                            components=[
                                                self.create_chapter(
                                                    title="Nazwa koproducenta",
                                                    components=[
                                                        self.create_component(
                                                            component_type="text",
                                                            label="Nazwa",
                                                            name="coproducerName",
                                                            required=True,
                                                            validators=[
                                                                self.validator.related_required_if_equal_validator(
                                                                    field_name="notCoproducer",
                                                                    value=False
                                                                )
                                                            ]
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
                                                            component_type="text",
                                                            label="Kraj koproducenta",
                                                            name="coproducerCountry",
                                                            required=True
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Udział w kosztach produkcji",
                                                            name="coproducerCountryShare",
                                                            validators=[
                                                                self.validator.related_mapped_limit_validator(
                                                                    default_limit=100.0
                                                                )
                                                            ],
                                                            unit="%",
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
                            title="Czy dystrybuowany film został wsparty przez PISF",
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="radio",
                                            label="Czy dystrybuowany film został wsparty przez PISF",
                                            name="isDistributedFilmPISF",
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
                                            field_name="isDistributedFilmPISF",
                                            values=[
                                                "Tak"
                                            ]
                                        )
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            label="Program Operacyjny",
                                            name="distributedOperationalProgram",
                                            required=True,
                                            validators=[
                                                self.validator.related_required_if_equal_validator(
                                                    field_name="isDistributedFilmPISF",
                                                    value="Tak"
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Priorytet",
                                            name="distributedPriority",
                                            required=True,
                                            validators=[
                                                self.validator.related_required_if_equal_validator(
                                                    field_name="isDistributedFilmPISF",
                                                    value="Tak"
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Numer wniosku",
                                            name="distributedApplicationNumber",
                                            required=True,
                                            validators=[
                                                self.validator.related_required_if_equal_validator(
                                                    field_name="isDistributedFilmPISF",
                                                    value="Tak"
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Kwota",
                                            name="distirbutedCost",
                                            required=True,
                                            validators=[
                                                self.validator.related_required_if_equal_validator(
                                                    field_name="isDistributedFilmPISF",
                                                    value="Tak"
                                                ),
                                                self.validator.range_validator(
                                                    min_value=0.01,
                                                    message="Kwota wsparcia musi być większa od 0."
                                                )
                                            ],
                                            unit="PLN"
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Czy dystrybuowany film jest filmem trudnym w rozumieniu art. 23, ust. 2 Ustawy?</br><normal><small>Treść i forma filmu mają charakter ambitny artystycznie i  mają ograniczone walory komercyjne lub film jest debiutem reżyserskim.</small></normal>",
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="radio",
                                            label="Czy dystrybuowany film jest filmem trudnym",
                                            name="isDifficultPiece",
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
                                            field_name="isDifficultPiece",
                                            values=[
                                                "Tak"
                                            ]
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
                                            required=True,
                                            class_list=[
                                                "full-width"
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    label="Opis filmu",
                                    name="movieDescription",
                                    validators=[
                                        self.validator.length_validator(max_value=5400)
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Link do filmu lub kopia DVD",
                                    name="movieLink"
                                ),
                                self.create_component(
                                    component_type="textarea",
                                    label="Zdobyte nagrody, obecność na festiwalach w Polsce i za granicą",
                                    name="movieRewards",
                                    validators=[
                                        self.validator.length_validator(max_value=1800)
                                    ],
                                    required=True
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Opis i zakres przedsięwzięcia",
                    components=[
                        self.create_chapter(
                            title="<normal>Opis i zakres przedsięwzięcia z uwzględnieniem spodziewanych efektów jego realizacji, w tym zakładanej liczby widzów w kinach</normal>",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    label="Opis i zakres przedsięwzięcia",
                                    name="scopeOfProjectDesc",
                                    validators=[
                                        self.validator.length_validator(max_value=1500)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="<normal>Liczba kin i ekranów przeznaczonych do dystrybucji</normal>",
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
                                    component_type="number",
                                    label="Liczba kin",
                                    name="cinemasNum",
                                    validators=[
                                        self.validator.range_validator(
                                            min_value=20,
                                            message="Licza kin musi być większa lub równa 20."
                                        )
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="number",
                                    label="Liczba ekranów",
                                    name="cinemaScreensNum",
                                    validators=[
                                        self.validator.range_validator(
                                            min_value=20,
                                            message="Licza ekranów musi być większa lub równa 20."
                                        )
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    label="Opis planowanych działań promocyjnych dystrybutora",
                                    name="descDistributorPlannedActivities",
                                    validators=[
                                        self.validator.length_validator(max_value=1800)
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="textarea",
                                    label="Minimalne i maksymalne koszty P&A",
                                    name="maxMinPAndACost",
                                    validators=[
                                        self.validator.length_validator(max_value=100)
                                    ],
                                    required=True
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="3. Opis dotychczasowej działalności Wnioskodawcy",
                    components=[
                        self.create_chapter(
                            title="<normal>Opis dotychczasowej działalności Wnioskodawcy, w tym przedsięwzięcia z zakresu dystrybucji filmów dokumentalnych</normal>",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="descApplicantCurrentActivities",
                                    validators=[
                                        self.validator.length_validator(max_value=1800)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="<normal>Wykaz aktualnie dystrybuowanych filmów</normal>",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="listCurrentlyDistributedFilms",
                                    validators=[
                                        self.validator.length_validator(max_value=1800)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="<normal>Wykaz dotychczasowych wniosków złożonych do PISF w ostatnich dwóch latach</normal>",
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="checkbox",
                                            label="Nie dotyczy",
                                            name="notListApplicationSubmittedLastTwoYears"
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="notListApplicationSubmittedLastTwoYears",
                                            values=[
                                                False
                                            ]
                                        )
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="textarea",
                                            name="listApplicationSubmittedLastTwoYears",
                                            validators=[
                                                self.validator.related_required_if_equal_validator(
                                                    field_name="notListApplicationSubmittedLastTwoYears",
                                                    value=False
                                                ),
                                                self.validator.length_validator(max_value=1800)
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
        self.save_part(part)
