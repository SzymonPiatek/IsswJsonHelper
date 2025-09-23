from classes.form_builder.additional.components.section.section import Section
from classes.form_builder.form_builder_base import FormBuilderBase


class ApplicationInformationData(FormBuilderBase):
    def __init__(self):
        super().__init__()

        self.section = Section()

    def screenwriter(self, number: str):
        return self.create_chapter(
            title=f"{number}. Scenarzysta",
            components=[
                self.create_chapter(
                    multiple_forms_rules={
                        "minCount": 1,
                        "maxCount": 10,
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
                                    label="Imię i nazwisko scenarzysty",
                                    name="screenwriterFullName",
                                    required=True
                                ),
                                self.create_component(
                                    component_type="country",
                                    label="Obywatelstwo scenarzysty",
                                    name="screenwriterCitizenship",
                                    required=True
                                ),
                                self.create_component(
                                    component_type="select",
                                    label="Płeć scenarzysty",
                                    name="screenwriterSex",
                                    options=[
                                        "Kobieta",
                                        "Mężczyzna",
                                        "Inna"
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="number",
                                    unit="%",
                                    label="Procent udziału",
                                    name="screenwriterRightsShare",
                                    required=True,
                                    validators=[
                                        self.validator.range_validator(
                                            max_value=100
                                        )
                                    ]
                                ),
                                self.create_component(
                                    component_type="file",
                                    label="Umowa nabycia praw do scenariusza",
                                    name="screenplayRightsContract",
                                    help_text="W przypadku ubiegania się o Promesę istnieje możliwość przedłożenia umowy opcji. W przypadku dofinansowania Przygotowania projektu filmowego przez PISF wymagane jest przedłożenie umowy nabycia praw do scenariusza.",
                                    required=True
                                ),
                                self.create_component(
                                    component_type="select",
                                    label="Rodzaj umowy zawartej ze scenarzystą",
                                    name="screenplayRightsContractType",
                                    options=[
                                        "umowa opcji",
                                        "umowa nabycia praw"
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="file",
                                    label="Potwierdzenie uiszczenia opłaty scenarzyście",
                                    name="scriptwriterPaymentConfirmation",
                                    help_text="Zgodnie z zasadami Programu Operacyjnego PISF.",
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
                        self.create_component(
                            component_type="number",
                            unit="%",
                            label="Suma udziałów",
                            name="allScreenwritersRightsShare",
                            help_text="Suma udziałów nie może być większa niż 100%",
                            calculation_rules=[
                                self.calculation_rule.sum_inputs(
                                    fields=[
                                        "screenwriterRightsShare",
                                    ]
                                )
                            ],
                            validators=[
                                self.validator.range_validator(
                                    min_value=100,
                                    max_value=100,
                                    message="Suma udziałów musi wynosić 100%"
                                )
                            ],
                            required=True,
                            read_only=True
                        )
                    ]
                )
            ]
        )

    def director(self, number: str):
        return self.create_chapter(
            title=f"{number}. Reżyser",
            multiple_forms_rules={
                "minCount": 1,
                "maxCount": 10,
            },
            components=[
                self.create_chapter(
                    components=[
                        self.create_chapter(
                            class_list=[
                                "grid",
                                "grid-cols-2"
                            ],
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="Imię i nazwisko reżysera",
                                    name="directorFullName",
                                    required=True
                                ),
                                self.create_component(
                                    component_type="country",
                                    label="Obywatelstwo reżysera",
                                    name="directorCitizenship",
                                    required=True
                                ),
                                self.create_component(
                                    component_type="select",
                                    label="Płeć reżysera",
                                    name="directorSex",
                                    options=[
                                        "Mężczyzna",
                                        "Kobieta",
                                        "Inna"
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="radio",
                                    label="Czy reżyser ma ukończone pełnowymiarowe studia kierunkowe?",
                                    name="hasDirectorFullyGraduated",
                                    options=[
                                        "Tak", "Nie"
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="select",
                                    label="Czy film jest debiutem reżyserskim?",
                                    name="directorIsDebuting",
                                    options=[
                                        "debiut reżyserski",
                                        "film drugi reżysera",
                                        "inny film reżysera"
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="textarea",
                                    label="Opis dorobku reżyserskiego",
                                    name="directorResume",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=5400
                                        )
                                    ],
                                    class_list=[
                                        "full-width"
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="file",
                                    label="CV reżysera",
                                    name="directorResumeAttachment",
                                    required=True,
                                )
                            ]
                        ),
                        self.create_chapter(
                            components=[
                                self.create_chapter(
                                    title="Link do zrealizowanego filmu",
                                    visibility_rules=[
                                        self.visibility_rule.local_equals_value(
                                            field_name="directorIsDebuting",
                                            values=[
                                                "inny film reżysera",
                                            ]
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
                                                    component_type="textarea",
                                                    label="Opis linku",
                                                    name="directorFinishedFilmDescription",
                                                    validators=[
                                                        self.validator.length_validator(
                                                            max_value=3000
                                                        )
                                                    ],
                                                    required=True,
                                                    class_list=[
                                                        "full-width"
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    label="Adres linku",
                                                    name="directorFinishedFilmLink",
                                                    validators=[
                                                        self.validator.length_validator(
                                                            max_value=200
                                                        )
                                                    ],
                                                    required=True
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    label="Dodatkowe informacje, np. hasło",
                                                    name="directorFinishedFilmAdditionalInfo",
                                                    validators=[
                                                        self.validator.length_validator(
                                                            max_value=200
                                                        )
                                                    ],
                                                    required=True
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="Link do próbek pracy dotychczasowej",
                                    visibility_rules=[
                                        self.visibility_rule.local_equals_value(
                                            field_name="directorIsDebuting",
                                            values=[
                                                "debiut reżyserski"
                                            ]
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
                                                    component_type="textarea",
                                                    label="Opis linku",
                                                    name="directorCurrentSamplesDescription",
                                                    validators=[
                                                        self.validator.length_validator(
                                                            max_value=3000
                                                        )
                                                    ],
                                                    required=True,
                                                    class_list=[
                                                        "full-width"
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    label="Adres linku",
                                                    name="directorCurrentSamplesLink",
                                                    validators=[
                                                        self.validator.length_validator(
                                                            max_value=200
                                                        )
                                                    ],
                                                    required=True
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    label="Dodatkowe informacje, np. hasło",
                                                    name="directorCurrentSamplesAdditionalInfo",
                                                    validators=[
                                                        self.validator.length_validator(
                                                            max_value=200
                                                        )
                                                    ],
                                                    required=True
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="Link do zrealizowanego debiutu reżyserskiego",
                                    visibility_rules=[
                                        self.visibility_rule.local_equals_value(
                                            field_name="directorIsDebuting",
                                            values=[
                                                "film drugi reżysera"
                                            ]
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
                                                    component_type="textarea",
                                                    label="Opis linku",
                                                    name="directorDebutDescription",
                                                    validators=[
                                                        self.validator.length_validator(
                                                            max_value=3000
                                                        )
                                                    ],
                                                    required=True,
                                                    class_list=[
                                                        "full-width"
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    label="Adres linku",
                                                    name="directorDebutLink",
                                                    validators=[
                                                        self.validator.length_validator(
                                                            max_value=200
                                                        )
                                                    ],
                                                    required=True
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    label="Dodatkowe informacje, np. hasło",
                                                    name="directorDebutAdditionalInfo",
                                                    validators=[
                                                        self.validator.length_validator(
                                                            max_value=200
                                                        )
                                                    ],
                                                    required=True
                                                )
                                            ]
                                        )
                                    ]
                                ),
                            ]
                        ),
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="file",
                                    label="Eksplikacja reżyserska",
                                    name="directorExplanation",
                                    help_text="Należy załączyć dokument podpisany przez reżysera.",
                                    required=True,
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Oświadczenie dot. Reżysera",
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    name="directorsStatementOtherFilm",
                                    options=[
                                        "reżyser nie jest zaangażowany jako reżyser w żaden inny, oprócz niniejszego, projekt ubiegający sie w bieżącej sesji o dofinansowanie produkcji (niezależnie od rodzaju filmowego)",
                                        "reżyser jest zaangażowany jako reżyser w inny projekt ubiegający się w bieżącej sesji o dofinansowanie produkcji"
                                    ],
                                    required=True,
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.local_equals_value(
                                    field_name="directorsStatementOtherFilm",
                                    values=[
                                        "reżyser jest zaangażowany jako reżyser w inny projekt ubiegający się w bieżącej sesji o dofinansowanie produkcji"
                                    ]
                                )
                            ],
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="textarea",
                                            label="Tytuły innych projektów",
                                            name="otherProjectsTitlesOfDirector",
                                            required=True,
                                            validators=[
                                                self.validator.length_validator(max_value=200)
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal><small>W przypadku, gdy wielu producentów angażuje tego samego reżysera i ubiega się o dofinansowanie w ramach jednego naboru, w wykazaniu dyspozycyjności oraz zaangażowania tego reżysera, powinien zostać spełniony jeden z poniższych warunków:</small></normal>",
                                    components=[
                                        self.create_component(
                                            component_type="radio",
                                            name="availabilityStatementCompletion",
                                            options=[
                                                "daty wskazane w harmonogramie produkcji, w szczególności daty okresu zdjęciowego lub animacji nie pokrywają się",
                                                "jeden z filmów to wieloletni dokument obserwacyjny",
                                                "jeden z filmów to animacja z długim okresem produkcji bądź seria filmów animowanych reżyserowanych przez więcej niż jednego reżysera"
                                            ],
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

    def producer(self, number: str):
        return self.create_chapter(
            title=f"{number}. Producent",
            components=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="radio",
                            label="Debiut producencki aplikującego podmiotu",
                            name="isProducerDebuting",
                            options=[
                                "Tak",
                                "Nie"
                            ],
                            required=True,
                        )
                    ]
                ),
                self.create_chapter(
                    title="Producent osoba fizyczna - aplikującego podmiotu",
                    class_list=[
                        "grid",
                        "grid-cols-2"
                    ],
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Imię i nazwisko producenta",
                            name="individualProducerFullname",
                            required=True,
                            class_list=[
                                "col-span-2"
                            ]
                        ),
                        self.create_component(
                            component_type="country",
                            label="Obywatelstwo",
                            name="individualProducerCitizenship",
                            required=True,
                        ),
                        self.create_component(
                            component_type="select",
                            label="Płeć",
                            name="individualProducerSex",
                            options=[
                                "Mężczyzna",
                                "Kobieta",
                                "Inna"
                            ],
                            required=True,
                        )
                    ]
                ),
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="textarea",
                            label="Informacje o dorobku wnioskodawcy, tj. podmiotu wnioskującego",
                            name="applicantBodyOfWork",
                            validators=[
                                self.validator.length_validator(
                                    max_value=5400
                                )
                            ],
                            class_list=[
                                "full-width"
                            ],
                            required=True,
                        )
                    ]
                ),
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="orgAndLegalStructure",
                            values=[
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
                            ]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Dokumenty rejestrowe: nie dotyczy zgodnie z Programem Operacyjnym PISF - Produkcja Filmowa",
                            name="applicantDocumentsOtherThanKrsOrCeidgDoesntApply",
                        ),
                        self.create_component(
                            component_type="file",
                            label="Dokumenty rejestrowe podmiotu wnioskującego, który nie polega wpisowi do KRS, CEIG, z których wynika uprawnienie do prowadzenia działalności z zakresu produkcji filmowej (w przypadku fundacji - status, stowarzyszeń - umowa spółki)",
                            name="applicantDocumentsOtherThanKrsOrCeidg",
                            required=True,
                            validators=[
                                self.validator.related_required_if_equal_validator(
                                    field_name="applicantDocumentsOtherThanKrsOrCeidgDoesntApply",
                                    value=False
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="checkbox",
                                    label="Skład organu reprezentującego: nie dotyczy zgodnie z Programem Operacyjnym PISF - Produkcja Filmowa",
                                    name="documentConfirmingTheRepresentingBodyDoesntApply"
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="documentConfirmingTheRepresentingBodyDoesntApply",
                                    values=[False]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="file",
                                    label="Dokument potwierdzający skład organu reprezentującego w przypadku braku ujawnienia zmian w Rejestrze do dnia złożenia wniosku",
                                    name="documentConfirmingTheRepresentingBody",
                                    validators=[
                                        self.validator.related_required_if_equal_validator(
                                            field_name="documentConfirmingTheRepresentingBodyDoesntApply",
                                            value=False
                                        )
                                    ],
                                    required=True
                                )
                            ]
                        )
                    ]
                )
            ]
        )

    def coproducer(self, number: str):
        return self.create_chapter(
            title=f"{number}. Informacje o koproducentach",
            components=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Nie dotyczy",
                            name="coproducerDoesntApply"
                        )
                    ]
                ),
                self.create_chapter(
                    multiple_forms_rules={
                        "minCount": 1,
                        "maxCount": 10
                    },
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="coproducerDoesntApply",
                            values=[False]
                        )
                    ],
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            label="Pełna nazwa koproducenta",
                                            name="coproducerFullname",
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Osoby upoważnione do reprezentowania koproducenta",
                                            name="coproducerRepresentative",
                                            required=True
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    components=[
                                        self.create_chapter(
                                            components=[
                                                self.create_component(
                                                    component_type="radio",
                                                    label="Siedziba",
                                                    name="coproducerResidence",
                                                    options=[
                                                        "w Polsce",
                                                        "za granicą"
                                                    ],
                                                    required=True
                                                )
                                            ]
                                        ),
                                        *self.section.create_address_base(
                                            start_name="coproducer",
                                            poland=True,
                                            foreign=True,
                                            is_local=True
                                        ),
                                        self.create_chapter(
                                            title="Dorobek koproducenta",
                                            components=[
                                                self.create_component(
                                                    component_type="file",
                                                    name="coproducerBodyOfWork",
                                                    required=True,
                                                    class_list=[
                                                        "full-width"
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

    def production_team_member(self, title: str, name: str, is_multi: bool = False, is_vacant: bool = False, is_not_applicable: bool = False):
        visibility_rules = []

        main_chapter = self.create_chapter(
            title=title,
        )

        condition_chapter = self.create_chapter(
            class_list={
                "main": [
                    "table-1-2",
                    "grid",
                    "grid-cols-2"
                ],
                "sub": [
                    "table-1-2__col"
                ]
            } if is_vacant and is_not_applicable else []
        )

        if is_not_applicable:
            condition_chapter["components"].append(
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Nie dotyczy",
                            name=f"{name}DoesntApply"
                        )
                    ]
                )
            )
            visibility_rules.append(
                self.visibility_rule.depends_on_value(
                    field_name=f"{name}DoesntApply",
                    values=[
                        False
                    ]
                )
            )

        if is_vacant:
            condition_chapter["components"].append(
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name=f"{name}DoesntApply",
                            values=[False]
                        )
                    ] if is_not_applicable else [],
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="WAKAT",
                            name=f"{name}IsVacant"
                        )
                    ]
                )
            )
            visibility_rules.append(
                self.visibility_rule.depends_on_value(
                    field_name=f"{name}IsVacant",
                    values=[
                        False
                    ]
                )
            )

        if is_not_applicable or is_vacant:
            main_chapter["components"].append(condition_chapter)

        visibility_chapter = self.create_chapter(
            visibility_rules=visibility_rules,
            multiple_forms_rules={
                "minCount": 1,
                "maxCount": 10
            } if is_multi else {},
            components=[
                self.create_chapter(
                    class_list=[
                        "grid",
                        "grid-cols-2"
                    ],
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Imię i nazwisko",
                            name=f"{name}Fullname",
                            required=True,
                            class_list=[
                                "col-span-2"
                            ]
                        ),
                        self.create_component(
                            component_type="country",
                            label="Obywatelstwo",
                            name=f"{name}Citizenship",
                            required=True
                        ),
                        self.create_component(
                            component_type="select",
                            label="Płeć",
                            name=f"{name}Sex",
                            options=[
                                "Mężczyzna",
                                "Kobieta",
                                "Inna"
                            ],
                            required=True
                        )
                    ]
                )
            ]
        )

        main_chapter["components"].append(visibility_chapter)

        return main_chapter
