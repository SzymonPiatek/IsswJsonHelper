from classes_new.forms._2026.dpf.production.application_builder import \
    ProductionOperationalProgramApplicationFormBuilder
from classes_new.forms._2026.dpf.pisf_structure import FilmProjectDevelopmentPriority


class FilmProjectDevelopmentPriorityApplicationFormBuilder(ProductionOperationalProgramApplicationFormBuilder):
    def __init__(self):
        super().__init__(
            priority=FilmProjectDevelopmentPriority()
        )

        self.form_id = self.set_ids(
            local_id=16440,
            uat_id=None
        )

        # Variables
        self.task_type = "Przygotowanie projektów filmowych"

    def create_application_basic_data(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Dane podstawowe",
            chapters=[
                self.create_chapter(
                    title="1. Rodzaj przedsięwzięcia",
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
                            component_type="select",
                            label="Rodzaj przedsiewzięcia",
                            options=["Rozwój projektu"],
                            required=True,
                            name="scopeOfProject"
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
                        self.create_chapter(
                            title="2.1 Rodzaj filmowy",
                            components=[
                                self.create_component(
                                    component_type="select",
                                    label="Rodzaj filmowy",
                                    name="movieKind",
                                    options=[
                                        "fabularny",
                                        "dokumentalny",
                                        "animowany",
                                        "seria animowana"
                                    ],
                                    required=True,
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="2.2. Przedsięwzięcie to",
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="Przedsięwzięcie to",
                                    name="typeOfProject",
                                    required=True,
                                    read_only=True,
                                    calculation_rules=[
                                        self.calculation_rule.assign_value(
                                            options=[
                                                {
                                                    "fieldName": "movieKind",
                                                    "value": "fabularny",
                                                    "inputValue": "Rozwój projektu"
                                                },
                                                {
                                                    "fieldName": "movieKind",
                                                    "value": "dokumentalny",
                                                    "inputValue": "Rozwój projektu"
                                                },
                                                {
                                                    "fieldName": "movieKind",
                                                    "value": "animowany",
                                                    "inputValue": "Rozwój projektu"
                                                },
                                                {
                                                    "fieldName": "movieKind",
                                                    "value": "seria animowana",
                                                    "inputValue": "Seria animowana"
                                                },
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                    ]
                ),
                self.create_chapter(
                    title="3. Tematyka",
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
                            component_type="select",
                            label="Tematyka",
                            name="movieSubject",
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
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="4. Tytuł utworu audiowizualnego",
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Tytuł utworu audiowizualnego",
                            name="pieceTitle",
                            validators=[
                                self.validator.length_validator(
                                    max_value=200
                                )
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="5. Krótki opis",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            label="Krótki opis filmu",
                            name="shortMovieDescription",
                            validators=[
                                self.validator.length_validator(
                                    max_value=5400
                                )
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="6. Kategoria przedsięwzięcia",
                    class_list={
                        "main": [
                            "new_table",
                            "grid",
                            "grid-cols-2"
                        ],
                        "sub": [
                            "new_table_2__col"
                        ]
                    },
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="select",
                                    label="Kategoria przedsięwzięcia",
                                    name="categoryOfProject",
                                    options=[
                                        "produkcja krajowa",
                                        "koprodukcja międzynarodowa większościowa"
                                    ],
                                    required=True
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
                                self.create_component(
                                    component_type="select",
                                    label="Wyłączne prawa wnioskodawcy na terytorium Polski",
                                    name="movieRights",
                                    options=["Tak"],
                                    read_only=True,
                                    required=True
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
                            class_list={
                                "main": [
                                    "new_table_2__2-2"
                                ]
                            },
                            components=[
                                self.create_component(
                                    component_type="countryMulti",
                                    label="Kraje koprodukcji",
                                    name="coproductionCountries",
                                    required=True
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="7. Wniosek dotyczy",
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
                            component_type="select",
                            label="Wniosek dotyczy",
                            name="applicationRelates",
                            options=["umowa"],
                            read_only=True,
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="8. Rodzaj pomocy",
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
                                    component_type="select",
                                    label="Rodzaj pomocy",
                                    name="typeOfSupport",
                                    options=[
                                        "dotacja",
                                        "pożyczka",
                                        "poręczenie"
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="typeOfSupport",
                                    values=["pożyczka"]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    label="8.1. Sposób zabezpieczenia pożyczki",
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
                                    label="8.2. Proponowane raty spłaty pożyczki",
                                    name="proposedLoanPaymentInstallments",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=900
                                        )
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="typeOfSupport",
                                    values=["poręczenie"]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    label="8.1. Przedmiot zobowiązania",
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
                                    label="8.2. Wysokość i okres poręczenia",
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
                                    label="8.3. Zabezpieczenie poręczenia",
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
                    ]
                ),
                self.create_chapter(
                    title="9. Wybór lidera komisji eksperckiej",
                    components=[
                        self.create_chapter(
                            title="9.1. Komisja jednoetapowa",
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="movieKind",
                                    values=[
                                        "animowany",
                                        "seria animowana"
                                    ]
                                ),
                                self.visibility_rule.depends_on_value(
                                    field_name="movieSubject",
                                    values=[
                                        "film autorski",
                                        "film o tematyce historycznej",
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="9.1. Komisja jednoetapowa",
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="movieSubject",
                                    values=[
                                        "film dla młodego widza lub widowni familijnej"
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="9.1. Komisja dwuetapowa",
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="movieKind",
                                    values=[
                                        "fabularny",
                                        "dokumentalny"
                                    ]
                                ),
                                self.visibility_rule.depends_on_value(
                                    field_name="movieSubject",
                                    values=[
                                        "film autorski",
                                        "film o tematyce historycznej",
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
                                            component_type="select",
                                            label="9.1.1. Lista pierwszego wyboru",
                                            name="firstChoiceCommitteeFab",
                                            options=[
                                                "Lider: Beata Pisula",
                                                "Lider: Joanna Kos Krauze",
                                                "Lider: Anna Kazejak"
                                            ],
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="select",
                                            label="9.1.2. Lista drugiego wyboru",
                                            name="secondChoiceCommitteeFab",
                                            options=[
                                                "Lider: Beata Pisula",
                                                "Lider: Joanna Kos Krauze",
                                                "Lider: Anna Kazejak"
                                            ],
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="select",
                                            label="9.1.3. W przypadku niedostępności wybranej komisji",
                                            name="noCommitteeAvailableFab",
                                            options=[
                                                "w przypadku niedostępności żadnej z dwóch wybranych komisji składam wniosek do następnej wolnej komisji",
                                                "w przypadku niedostępności żadnej z dwóch wybranych komisji wycofuję wniosek z oceny"
                                            ],
                                            required=True,
                                            class_list=[
                                                "table-full",
                                                "col-span-2"
                                            ]
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
                                            component_type="select",
                                            label="9.1.1. Lista pierwszego wyboru",
                                            name="firstChoiceCommitteeDoc",
                                            options=[
                                                "Lider: Małgorzata Prociak",
                                                "Lider: Jakub Mikurda",
                                                "Lider: Bartosz Paduch"
                                            ],
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="select",
                                            label="9.1.2. Lista drugiego wyboru",
                                            name="secondChoiceCommitteeDoc",
                                            options=[
                                                "Lider: Małgorzata Prociak",
                                                "Lider: Jakub Mikurda",
                                                "Lider: Bartosz Paduch"
                                            ],
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="select",
                                            label="9.1.3. W przypadku niedostępności wybranej komisji",
                                            name="noCommitteeAvailableDoc",
                                            options=[
                                                "w przypadku niedostępności żadnej z dwóch wybranych komisji składam wniosek do następnej wolnej komisji",
                                                "w przypadku niedostępności żadnej z dwóch wybranych komisji wycofuję wniosek z oceny"
                                            ],
                                            required=True,
                                            class_list=[
                                                "table-full",
                                                "col-span-2"
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

    def create_application_applicant_data(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Dane wnioskodawcy",
            chapters=[
                self.create_chapter(
                    title="1. Pełna nazwa Wnioskodawcy",
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
                            label="Pełna nazwa Wnioskodawcy",
                            name="applicantName",
                            required=True,
                            class_list=[
                                "table-full",
                                "col-span-2"
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Rodzaj Wnioskodawcy",
                            name="applicantType",
                            value="Producent",
                            read_only=True,
                            required=True
                        )
                    ]
                ),
                self.section.eligible_person_data(number=2),
                self.create_chapter(
                    title="2.1. Pełnomocnictwo",
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
                                            name="eligiblePersonAttachments",
                                            help_text="Należy dołączyć pełnomocnictwo w przypadku, gdy wniosek podpisuje osoba inna niż wykazana w KRS lub CEIDG."
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.section.responsible_person_data(number=3),
                self.create_chapter(
                    title="4. Adres Wnioskodawcy",
                    components=[
                        self.create_chapter(
                            title="Siedziba",
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="radio",
                                            name=f"applicantResidence",
                                            options=["w Polsce", "za granicą"],
                                            required=True
                                        )
                                    ]
                                ),
                                *self.section.create_address_base(
                                    start_name="applicant",
                                    poland=True,
                                    foreign=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="checkbox",
                                    label="Należy zaznaczyć jeśli adres korespondencyjny jest inny",
                                    name=f"applicantHasDifferentContactAddress"
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Adres korespondencyjny",
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="applicantHasDifferentContactAddress",
                                    values=[True]
                                )
                            ],
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="radio",
                                            name=f"applicantContactResidence",
                                            options=["w Polsce", "za granicą"],
                                            required=True
                                        )
                                    ]
                                ),
                                *self.section.create_address_base(
                                    start_name="applicant",
                                    build_name="Contact",
                                    poland=True,
                                    foreign=True
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="5. Dane identyfikacyjne podmiotu",
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
                            label="Numer NIP",
                            name="applicantNip",
                            required=True,
                            validators=[
                                self.validator.nip_validator()
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Numer REGON",
                            name="applicant REGON",
                            required=True,
                            validators=[
                                self.validator.regon_validator()
                            ]
                        )
                    ]
                ),
                self.section.applicant_bank_data(number=6),
                self.section.applicant_legal_information(number=7),
                self.section.applicant_statistical_data(number=8)
            ]
        )

        self.save_part(part=part)
