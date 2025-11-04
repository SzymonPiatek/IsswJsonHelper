from classes_new.form_builder.form_builder import ApplicationFormBuilder
from classes_new.form_components.section.duk.section import DUKSection
from classes_new.forms._2026.duk.estimate.application_estimate_builder import DUKApplicationEstimateBuilder


class DUKDepartmentApplicationFormBuilder(ApplicationFormBuilder):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.parts = [
            self.create_application_metadata,
            self.create_application_basic_data,
            self.create_application_applicant_data,
            self.create_application_scope_of_project,
            self.create_application_sources_of_financing,
            self.create_application_project_costs,
            self.create_application_schedule,
            self.create_application_statements,
            self.create_application_attachments
        ]

        # Variables
        self.project_type: list[str] = []
        self.source_of_financing_tickets: bool = False
        self.is_dkf: bool = False

        # Estimate
        self.estimate_chapters = []

        self.section = DUKSection()

    def create_application_metadata(self, number: int):
        part = self.create_part(
            title="Wniosek o dofinansowanie przedsięwzięcia realizowanego w ramach Programów Operacyjnych Polskiego Instytutu Sztuki Filmowej",
            short_name=f"{self.helpers.int_to_roman(number)}. Metadane wniosku",
            chapters=[
                self.create_chapter(
                    title="1. Tryb naboru",
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Nr sesji i rok",
                            name="sessionYear",
                            value=f"Sesja {self.session.roman_num}/{self.session.year}",
                            read_only=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Program operacyjny",
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Program",
                            name="programName",
                            value=str(self.priority.operation_program),
                            read_only=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="3. Priorytet",
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Priorytet",
                            name="priorytetName",
                            value=str(self.priority),
                            read_only=True
                        )
                    ]
                )
            ]
        )
        self.save_part(part=part)

    def create_application_basic_data(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Dane podstawowe",
            chapters=[
                self.create_chapter(
                    title="1. Nazwa przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="applicationTaskName",
                            validators=[
                                self.validator.length_validator(max_value=200)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Rodzaj przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="radio",
                            name="projectType",
                            options=self.project_type
                        )
                    ]
                ),
                self.create_chapter(
                    title="3. Poprzednia edycja przedsięwzięcia",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    label="Czy poprzednia edycja przedsięwzięcia została dofinansowana przez PISF?",
                                    name="previousApplicationForProject",
                                    options=[
                                        "Tak", "Nie"
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="previousApplicationForProject",
                                    values=[
                                        "Tak"
                                    ]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="text",
                                    name="fiveDigitNumberOfApplication",
                                    label="Numer wniosku dotyczący poprzedniej, dofinansowanej edycji przedsięwzięcia",
                                    validators=[
                                        self.validator.related_required_if_equal_validator(
                                            field_name="previousApplicationForProject",
                                            value="Tak"
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

        self.save_part(part)

    def create_application_scope_of_project(self, number):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Zakres przedsięwzięcia i jego charakterystyka",
            short_name=f"{self.helpers.int_to_roman(number)}. Zakres przedsięwzięcia",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            label="Miejsce realizacji przedsięwzięcia",
                            name="projectLocation",
                            component_type="textarea",
                            validators=[
                                self.validator.length_validator(
                                    max_value=3000
                                )
                            ],
                            required=True
                        ),
                        self.create_component(
                            label="Opis przedsięwzięcia",
                            name="generalProjectDescription",
                            component_type="textarea",
                            validators=[
                                self.validator.length_validator(
                                    max_value=3000
                                )
                            ],
                            required=True,
                            help_text="Cel i zakres merytoryczny, zastosowane technologie, sposób realizacji przedsięwzięcia, promocja."
                        ),
                        self.create_component(
                            component_type="textarea",
                            name="offerEducationalValue",
                            label="Wartość merytoryczna oferty dydaktycznej",
                            validators=[
                                self.validator.length_validator(
                                    max_value=3000
                                )
                            ],
                            required=True,
                            help_text="W tym ciągłość realizacji oraz wartość edukacyjna przedsięwzięcia."
                        ),
                        self.create_component(
                            component_type="textarea",
                            name="teachingMethodsInnovation",
                            label="Innowacyjność w zakresie metod nauczania, z uwzględnieniem produkcji filmowej",
                            validators=[
                                self.validator.length_validator(
                                    max_value=3000
                                )
                            ],
                            required=True,
                        ),
                        self.create_component(
                            component_type="textarea",
                            name="skillsAcquiredByStudents",
                            label="Umiejętności lub kompetencje zawodowe nabywane przez studentów",
                            validators=[
                                self.validator.length_validator(
                                    max_value=3000
                                )
                            ],
                            required=True,
                        ),
                        self.create_component(
                            component_type="textarea",
                            name="numberAndDiversityOfStudents",
                            label="Liczba i zróżnicowanie struktury studentów",
                            validators=[
                                self.validator.length_validator(
                                    max_value=3000
                                )
                            ],
                            required=True,
                        ),
                        self.create_component(
                            component_type="textarea",
                            name="plannedImplementationAndEvaluationEffects",
                            label="Planowane efekty realizacji przedsięwzięcia oraz jego ewaluacja",
                            validators=[
                                self.validator.length_validator(
                                    max_value=3000
                                )
                            ],
                            required=True,
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Doświadczenie wnioskodawcy i kompetencje zespołu",
                            name="applicantAndTeamExperience",
                            help_text="Proszę o wyszczególnienie przedsięwzięć z zakresu kinematografii realizowanych przez wnioskodawcę w ostatnich 2 latach.",
                            validators=[
                                self.validator.length_validator(
                                    max_value=3000
                                )
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="textarea",
                            name="projectAccessibility",
                            label="Dostępność przedsięwzięcia",
                            help_text="Działania podejmowane na rzecz osób ze szczególnymi potrzebami oraz wspierania inkluzywności.",
                            validators=[
                                self.validator.length_validator(
                                    max_value=3000
                                )
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Czy przedsięwzięcie, na które składany jest wniosek jest powiązane z innymi przedsięwzięciami, o dofinansowanie których ubiega się Wnioskodawca w bieżącym roku z innych programów operacyjnych PISF? Jeżeli tak, proszę podać nazwę przedsięwzięcia, program oraz wnioskowaną kwotę dofinansowania",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    name="wasSubmittedBefore",
                                    options=["Tak", "Nie"],
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="wasSubmittedBefore",
                                    values=["Tak"])
                            ],
                            multiple_forms_rules={"minCount": 1, "maxCount": 20},
                            components=[
                                self.create_chapter(
                                    class_list=["grid", "grid-cols-3"],
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            label="Nazwa przedsięwzięcia",
                                            name="otherProjectName"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Program operacyjny",
                                            name="programmeName"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Wnioskowana kwota",
                                            name="otherProjectFundingAmount",
                                            unit="PLN",
                                            mask="fund"
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

    def create_application_applicant_data(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Dane wnioskodawcy",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_chapter(
                            title="Pełna nazwa wnioskodawcy",
                            class_list=["displayNoneFrontend"]
                        ),
                        self.create_chapter(
                            title="Pełna nazwa wnioskodawcy",
                            help_text="Pełna nazwa lub firma wnioskodawcy wpisana do odpowiedniego rejestru (KRS, CEiDG, Rejestr instytucji kultury, Rejestr Instytucji Filmowych itp.",
                            class_list=["no-title"],
                            components=[
                                self.create_component(
                                    component_type="text",
                                    name="applicantName",
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
                ),
                self.create_chapter(
                    title="Forma organizacyjno-prawna",
                    components=[
                        self.create_component(
                            component_type="select",
                            name="orgAndLegalStructure",
                            options=[
                                "Spółka z ograniczoną odpowiedzialnością",
                                "Spółka akcyjna",
                                "Spółka jawna",
                                "Spółka komandytowa",
                                "Spółka komandytowo-akcyjna",
                                "Osoba fizyczna prowadząca działalność gospodarczą",
                                "Spółka cywilna",
                                "Fundacja",
                                "Stowarzyszenie",
                                "Instytucja kultury",
                                "Instytucja filmowa",
                                "Publiczna szkoła lub uczelnia artystyczna",
                                "Niepubliczna szkoła lub uczelnia artystyczna",
                                "Kościół lub związek wyznaniowy",
                                "Jednostka samorządu terytorialnego",
                                "Inna (np. spółka w organizacji)"
                            ],
                            required=True,
                            help_text="Wybierz formę organizacyjno-prawną wnioskodawcy."
                        )
                    ]
                ),
                self.create_chapter(
                    title="1. Dane identyfikacyjne wnioskodawcy oraz informacje prawne",
                    components=[
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="orgAndLegalStructure",
                                    values=[
                                        "Spółka z ograniczoną odpowiedzialnością",
                                        "Spółka akcyjna",
                                        "Spółka jawna",
                                        "Spółka komandytowa",
                                        "Spółka komandytowo-akcyjna",
                                        "Osoba fizyczna prowadząca działalność gospodarczą",
                                        "Spółka cywilna",
                                        "Fundacja",
                                        "Stowarzyszenie",
                                        "Instytucja kultury",
                                        "Instytucja filmowa",
                                        "Publiczna szkoła lub uczelnia artystyczna",
                                        "Niepubliczna szkoła lub uczelnia artystyczna",
                                        "Kościół lub związek wyznaniowy",
                                        "Jednostka samorządu terytorialnego",
                                    ]
                                )
                            ],
                            components=[
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="orgAndLegalStructure",
                                            values=[
                                                "Osoba fizyczna prowadząca działalność gospodarczą"
                                            ]
                                        )
                                    ],
                                    title="Dane osobowe",
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
                                            component_type="text",
                                            label="PESEL",
                                            name="applicantPesel",
                                            required=True,
                                            validators=[
                                                self.validator.pesel_validator()
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="orgAndLegalStructure",
                                            values=[
                                                "Spółka z ograniczoną odpowiedzialnością",
                                                "Spółka akcyjna",
                                                "Spółka jawna",
                                                "Spółka komandytowa",
                                                "Spółka komandytowo-akcyjna",
                                                "Osoba fizyczna prowadząca działalność gospodarczą",
                                                "Spółka cywilna",
                                                "Fundacja",
                                                "Stowarzyszenie",
                                                "Instytucja kultury",
                                                "Instytucja filmowa",
                                                "Publiczna szkoła lub uczelnia artystyczna",
                                                "Niepubliczna szkoła lub uczelnia artystyczna",
                                                "Kościół lub związek wyznaniowy",
                                                "Jednostka samorządu terytorialnego",
                                            ]
                                        )
                                    ],
                                    title="Dane identyfikacyjne",
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
                                                self.create_chapter(
                                                    components=[
                                                        self.create_component(
                                                            component_type="text",
                                                            label="Numer NIP",
                                                            name="applicantNip",
                                                            required=True,
                                                            validators=[
                                                                self.validator.nip_validator()
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                self.create_chapter(
                                                    visibility_rules=[
                                                        self.visibility_rule.depends_on_value(
                                                            field_name="orgAndLegalStructure",
                                                            values=[
                                                                "Spółka z ograniczoną odpowiedzialnością",
                                                                "Spółka akcyjna",
                                                                "Spółka jawna",
                                                                "Spółka komandytowa",
                                                                "Spółka komandytowo-akcyjna",
                                                                "Osoba fizyczna prowadząca działalność gospodarczą",
                                                                "Fundacja",
                                                                "Stowarzyszenie",
                                                                "Instytucja kultury",
                                                                "Instytucja filmowa",
                                                                "Publiczna szkoła lub uczelnia artystyczna",
                                                                "Niepubliczna szkoła lub uczelnia artystyczna",
                                                                "Kościół lub związek wyznaniowy",
                                                                "Jednostka samorządu terytorialnego",
                                                            ]
                                                        )
                                                    ],
                                                    components=[
                                                        self.create_component(
                                                            component_type="text",
                                                            label="Numer REGON",
                                                            name="applicantRegon",
                                                            required=True,
                                                            validators=[
                                                                self.validator.regon_validator()
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                self.create_chapter(
                                                    visibility_rules=[
                                                        self.visibility_rule.depends_on_value(
                                                            field_name="orgAndLegalStructure",
                                                            values=[
                                                                "Spółka z ograniczoną odpowiedzialnością",
                                                                "Spółka akcyjna",
                                                                "Spółka jawna",
                                                                "Spółka komandytowa",
                                                                "Spółka komandytowo-akcyjna",
                                                                "Fundacja",
                                                                "Stowarzyszenie"
                                                            ]
                                                        )
                                                    ],
                                                    components=[
                                                        self.create_component(
                                                            component_type="text",
                                                            label="Numer KRS",
                                                            name="applicantKrs",
                                                            required=True,
                                                            validators=[
                                                                self.validator.length_validator(
                                                                    min_value=10,
                                                                    max_value=10
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
                                            field_name="orgAndLegalStructure",
                                            values=[
                                                "Spółka cywilna"
                                            ]
                                        )
                                    ],
                                    title="Dane wszystkich wspólników spółki cywilnej",
                                    components=[
                                        self.create_chapter(
                                            multiple_forms_rules={
                                                "minCount": 1,
                                                "maxCount": 50
                                            },
                                            components=[
                                                self.create_chapter(
                                                    title="Wspólnik",
                                                    components=[
                                                        self.create_chapter(
                                                            title="Dane identyfikacyjne",
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
                                                                    name="partnerFirstName",
                                                                    required=True
                                                                ),
                                                                self.create_component(
                                                                    component_type="text",
                                                                    label="Nazwisko",
                                                                    name="partnerLastName",
                                                                    required=True
                                                                ),
                                                                self.create_component(
                                                                    component_type="text",
                                                                    label="PESEL",
                                                                    name="partnerPesel",
                                                                    required=True,
                                                                    validators=[
                                                                        self.validator.pesel_validator()
                                                                    ]
                                                                ),
                                                                self.create_component(
                                                                    component_type="text",
                                                                    label="NIP",
                                                                    name="partnerNip",
                                                                    required=True,
                                                                    validators=[
                                                                        self.validator.nip_validator()
                                                                    ]
                                                                ),
                                                                self.create_component(
                                                                    component_type="text",
                                                                    label="REGON",
                                                                    name="partnerRegon",
                                                                    required=True,
                                                                    validators=[
                                                                        self.validator.regon_validator()
                                                                    ]
                                                                )
                                                            ]
                                                        ),
                                                        self.create_chapter(
                                                            title="Adres wykonywania działalności gospodarczej",
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
                                                                    label="Ulica",
                                                                    name="partnerStreet",
                                                                    required=True,
                                                                ),
                                                                self.create_component(
                                                                    component_type="text",
                                                                    label="Nr domu",
                                                                    name="partnerHouseNum",
                                                                    required=True,
                                                                ),
                                                                self.create_component(
                                                                    component_type="text",
                                                                    label="Nr lokalu",
                                                                    name="partnerApartmentNum",
                                                                    required=True,
                                                                ),
                                                                self.create_component(
                                                                    component_type="text",
                                                                    label="Kod pocztowy",
                                                                    mask="polishPostalCode",
                                                                    name="partnerPostalCode",
                                                                    required=True,
                                                                    validators=[
                                                                        self.validator.zip_code_validator()
                                                                    ]
                                                                ),
                                                                self.create_component(
                                                                    component_type="text",
                                                                    label="Miasto",
                                                                    name="partnerCity",
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
                                            field_name="orgAndLegalStructure",
                                            values=[
                                                "Spółka z ograniczoną odpowiedzialnością",
                                                "Spółka akcyjna",
                                                "Spółka jawna",
                                                "Spółka komandytowa",
                                                "Spółka komandytowo-akcyjna",
                                                "Fundacja",
                                                "Stowarzyszenie",
                                            ]
                                        )
                                    ],
                                    title="Oznaczenia sądu rejestrowego",
                                    components=[
                                        self.create_chapter(
                                            components=[
                                                self.create_component(
                                                    component_type="text",
                                                    label="Nazwa sądu",
                                                    name="courtName",
                                                    required=True
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    label="Numer wydziału",
                                                    name="courtNumber",
                                                    required=True
                                                ),
                                                self.create_component(
                                                    component_type="select",
                                                    label="Nazwa rejestru",
                                                    name="courtRegisterName",
                                                    required=True,
                                                    options=[
                                                        "Rejestr przedsiębiorców",
                                                        "Rejestr stowarzyszeń, innych organizacji społecznych i zawodowych, fundacji oraz publicznych zakładów opieki zdrowotnej"
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_chapter(
                                            visibility_rules=[
                                                self.visibility_rule.depends_on_value(
                                                    field_name="orgAndLegalStructure",
                                                    values=[
                                                        "Spółka z ograniczoną odpowiedzialnością",
                                                        "Spółka akcyjna",
                                                    ]
                                                )
                                            ],
                                            components=[
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Wysokość kapitału zakładowego (opłaconego)",
                                                    name="shareCapitalAmount",
                                                    required=True,
                                                    unit="PLN",
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="orgAndLegalStructure",
                                            values=[
                                                "Publiczna szkoła lub uczelnia artystyczna",
                                                "Niepubliczna szkoła lub uczelnia artystyczna",
                                            ]
                                        )
                                    ],
                                    title="Organ prowadzący/nadzorujący (jeśli dotyczy)",
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            label="Organ prowadzący/nadzorujący",
                                            name="governingBody"
                                        ),
                                        self.create_component(
                                            component_type="textarea",
                                            label="Podstawa utworzenia",
                                            name="basisOfCreation",
                                            validators=[
                                                self.validator.length_validator(
                                                    max_value=500
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
                    components=[
                        self.create_chapter(
                            title="2. Adres wnioskodawcy",
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
                                        *self.section.application_applicant_data.create_address_base(
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
                                        *self.section.application_applicant_data.create_address_base(
                                            start_name="applicant",
                                            build_name="Contact",
                                            poland=True,
                                            foreign=True
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="3. Osoby upoważnione do reprezentowania wnioskodawcy, składania oświadczeń woli i zaciągania w jego imieniu zobowiązań finansowych",
                    components=[
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 1,
                                "maxCount": 8
                            },
                            class_list={
                                "sub": [
                                    "table-1-2-top"
                                ]
                            },
                            components=[
                                self.create_chapter(
                                    title="Osoba upoważniona do reprezentowania Wnioskodawcy",
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
                                            name="eligiblePersonFirstName",
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Nazwisko",
                                            name="eligiblePersonLastName",
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Email",
                                            name="eligiblePersonEmail",
                                            required=True,
                                            validators=[
                                                self.validator.email_validator()
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Numer telefonu",
                                            name="eligiblePersonPhoneNum",
                                            required=True,
                                            mask="phoneNumber",
                                            validators=[
                                                self.validator.phone_number_validator()
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Stanowisko zgodnie z reprezentacją/ załączonym upoważnieniem",
                                            name="eligiblePersonPosition",
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="select",
                                            label="Sposób reprezentacji",
                                            name="eligiblePersonRepresentationType",
                                            options=[
                                                "Łącznie",
                                                "Samodzielnie"
                                            ],
                                            required=True
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.section.responsible_person_data(number="4"),
                self.section.applicant_bank_data(number="5"),
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="identificationData",
                            value="<small><b>Uwaga!</b><br/><br/><normal>Wszystkie koszty danego przedsięwzięcia muszą być opłacane z rachunku bankowego podanego we Wniosku o dofinansowanie. Na ten sam rachunek powinny też wpływać środki od innych podmiotów współfinansujących dane przedsięwzięcie. Możliwe są dwa rozwiązania:<br/>a) rachunek służący do rozliczeń przedsięwzięcia, którego dotyczy Wniosek o dofinansowanie, w tym wpływów i wydatków związanych z dotacją PISF,<br/>b) rachunek przeznaczony wyłącznie do obsługi środków z dotacji PISF, na który mogą trafiać środki z różnych dofinansowań udzielonych przez PISF.</br></br>Wybrany wariant rachunku obowiązuje przez cały okres trwania umowy. Rachunek ten powinien zapewniać pełną przejrzystość przepływów finansowych związanych z realizacją projektu oraz być ujęty w wykazie podatników VAT lub zgłoszony do właściwego urzędu skarbowego - o ile Wnioskodawca podlega obowiązkowi zgłoszenia, zgodnie z obowiązującymi przepisami prawa.</normal></small>"
                        )
                    ]
                ),
                self.section.application_applicant_data.applicant_statistical_data(number="6"),
            ]
        )

        self.save_part(part=part)

    def create_application_sources_of_financing(self, number: int):
        source_of_financing_help_text = "<small>Uwaga! </br><normal>Odznaczenie powyższego checkboxa nie prowadzi do automatycznego usunięcia zawartych w tej sekcji informacji. Dane te nadal będą brane pod uwagę w obliczeniach finansowych i będą uwzględnione we wniosku. Jeżeli dane te nie są już potrzebne, prosimy o ich ręczne usunięcie. </normal>"

        sources_of_financing_chapters = {
            "c": [
                {
                    "checkbox_title": "Środki z budżetów jednostek samorządu terytorialnego lub inne środki publiczne z wyjątkiem środków Ministerstwa Kultury i Dziedzictwa Narodowego",
                    "checkbox_name": "isLocalGovernmentFunding",
                    "section_title": f"<normal>a) z budżetów jednostek samorządu terytorialnego lub innych środków publicznych za wyjątkiem Ministerstwa Kultury i Dziedzictwa Narodowego </normal><br />{source_of_financing_help_text}</small>",
                    "section_name": "localGovernments",
                },
                {
                    "checkbox_title": "Środki Ministerstwa Kultury i Dziedzictwa Narodowego",
                    "checkbox_name": "isMinistryFunding",
                    "section_title": f"<normal>b) ze środków Ministerstwa Kultury i Dziedzictwa Narodowego w ramach Programów Ministra </normal><br />{source_of_financing_help_text}</small>",
                    "section_name": "ministry",
                },
                {
                    "checkbox_title": "Środki od sponsorów lub innych podmiotów niezaliczanych do sektora finansów publicznych",
                    "checkbox_name": "isOtherSponsorFunding",
                    "section_title": f"<normal>c) od sponsorów lub innych podmiotów niezaliczanych do sektora finansów publicznych </normal><br />{source_of_financing_help_text}</small>",
                    "section_name": "otherSponsors",
                },
                {
                    "checkbox_title": "Środki zagraniczne, w tym europejskie",
                    "checkbox_name": "isForeignFunding",
                    "section_title": f"<normal>d) ze środków zagranicznych, w tym europejskich </normal><br />{source_of_financing_help_text}</small>",
                    "section_name": "foreign",
                }
            ]
        }

        tickets_chapter = self.create_chapter(
            components=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Należy zaznaczyć, jeśli częścią wkładu finansowego są wpływy z biletów, akredytacji itp.",
                            name="isTicketRevenues"
                        )
                    ]
                ),
                self.create_chapter(
                    class_list={
                        "main": [
                            "table-1-3-narrow",
                            "grid",
                            "grid-cols-3"
                        ],
                        "sub": [
                            "table-1-3__col"
                        ]
                    },
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="isTicketRevenues",
                            values=[
                                True
                            ]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            name="proceedsFromSales",
                            label="Wpływy ze sprzedaży",
                            unit="PLN"
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            name="otherFinancialResources",
                            label="Pozostałe środki finansowe",
                            validators=[
                                self.validator.related_fraction_gte_validator(
                                    field_name="ownFinancialFundsAmount",
                                    ratio=1
                                )
                            ],
                            unit="PLN"
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            name="proceedsFromSalesTotal",
                            label="Suma",
                            calculation_rules=[
                                self.calculation_rule.dynamic_sum_inputs(
                                    fields=[
                                        "proceedsFromSales",
                                        "otherFinancialResources"
                                    ]
                                )
                            ],
                            validators=[
                                self.validator.related_fraction_gte_validator(
                                    field_name="ownFinancialFundsAmount",
                                    ratio=1
                                )
                            ],
                            read_only=True,
                            unit="PLN"
                        )
                    ]
                )
            ]
        )

        own_financial_chapter = self.create_chapter(
            title="<small>a) Wkład finansowy</small>",
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
                            component_type="text",
                            mask="fund",
                            name="ownFinancialFundsAmount",
                            label="Kwota",
                            unit="PLN"
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            name="ownFinancialFundsShare",
                            label="Udział w koszcie całkowitym",
                            calculation_rules=[
                                self.calculation_rule.share_calculator(
                                    dividend_field="ownFinancialFundsAmount",
                                    divisor_field="totalProjectCost"
                                )
                            ],
                            validators=[
                                self.validator.related_share_validator(
                                    dividend="ownFinancialFundsAmount",
                                    divisor="totalProjectCost"
                                )
                            ],
                            required=True,
                            read_only=True,
                            unit="%"
                        )
                    ]
                )
            ]
        )
        if self.source_of_financing_tickets:
            own_financial_chapter["components"].append(
                tickets_chapter
            )

        own_in_kind_chapter = self.create_chapter(
            title="<small>b) Wkład rzeczowy</small>",
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
                    mask="fund",
                    name="ownInKindFundsAmount",
                    label="Kwota",
                    unit="PLN",
                    validators=[
                        self.validator.related_fraction_gte_validator(
                            field_name="ownFundsSumAmount",
                            ratio=0.5,
                            message="Wartość nie może przekroczyć 50% całkowitego wkładu własnego."
                        )
                    ]
                ),
                self.create_component(
                    component_type="text",
                    mask="fund",
                    name="ownInKindFundsShare",
                    label="Udział w koszcie całkowitym",
                    calculation_rules=[
                        self.calculation_rule.share_calculator(
                            dividend_field="ownInKindFundsAmount",
                            divisor_field="totalProjectCost"
                        )
                    ],
                    validators=[
                        self.validator.related_share_validator(
                            dividend="ownInKindFundsAmount",
                            divisor="totalProjectCost"
                        )
                    ],
                    required=True,
                    read_only=True,
                    unit="%"
                )
            ]
        )

        own_financial_and_in_kind_total_chapter = self.create_chapter(
            title="<small>Łączny wkład własny</small>",
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
                    mask="fund",
                    name="ownFundsSumAmount",
                    read_only=True,
                    unit="PLN",
                    calculation_rules=[
                        self.calculation_rule.dynamic_sum_inputs(
                            fields=[
                                "ownFinancialFundsAmount",
                                "ownInKindFundsAmount"
                            ]
                        )
                    ],
                    validators=[
                        self.validator.related_sum_validator(
                            field_names=[
                                "ownFinancialFundsAmount",
                                "ownInKindFundsAmount"
                            ]
                        )
                    ]
                )
            ]
        )

        own_financial_and_in_kind_chapter = self.create_chapter(
            title="<normal>1) Wkład własny</normal>",
            help_text="Minimum 10% budżetu przedsięwzięcia. Wkład rzeczowy nie może być wyższy niż 50% całkowitego wkładu własnego.",
            components=[
                own_financial_chapter,
                own_in_kind_chapter,
                own_financial_and_in_kind_total_chapter
            ]
        )

        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Źródła finansowania",
            chapters=[
                self.create_chapter(
                    title="1. Wyszczególnienie źródeł finansowaniania",
                    help_text="Maksymalna kwota dofinansowania PISF wynosi 15 000 zł." if self.is_dkf else "",
                    components=[
                        own_financial_and_in_kind_chapter,
                        self.create_chapter(
                            title="<normal>2) Dotacja PISF</normal>",
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
                                    mask="fund",
                                    label="Wnioskowana dotacja z PISF",
                                    name="pisfSupportAmountInput",
                                    required=True,
                                    unit="PLN"
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Udział w koszcie całkowitym",
                                    name="pisfSupportShare",
                                    calculation_rules=[
                                        self.calculation_rule.share_calculator(
                                            dividend_field="pisfSupportAmountInput",
                                            divisor_field="totalProjectCost"
                                        )
                                    ],
                                    read_only=True,
                                    validators=[
                                        self.validator.related_share_validator(
                                            dividend="pisfSupportAmountInput",
                                            divisor="totalProjectCost"
                                        )
                                    ],
                                    required=True,
                                    unit="%"
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="<normal>3) Pozostałe źródła finansowania</normal>",
                            components=[
                                *[self.create_chapter(
                                    components=[
                                        self.create_chapter(
                                            components=[
                                                self.create_component(
                                                    component_type="checkbox",
                                                    label=chapter["checkbox_title"],
                                                    name=chapter["checkbox_name"]
                                                )
                                            ]
                                        ),
                                        self.create_chapter(
                                            visibility_rules=[
                                                self.visibility_rule.depends_on_value(
                                                    field_name=chapter["checkbox_name"],
                                                    values=[
                                                        True
                                                    ]
                                                )
                                            ],
                                            components=[
                                                self.create_chapter(
                                                    title=chapter["section_title"],
                                                    components=[
                                                        self.create_chapter(
                                                            multiple_forms_rules={
                                                                "minCount": 1,
                                                                "maxCount": 20
                                                            },
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
                                                                            component_type="text",
                                                                            label="Nazwa podmiotu finansującego",
                                                                            name=f"{chapter["section_name"]}Name",
                                                                            class_list=[
                                                                                "table-full"
                                                                            ],
                                                                            required=True,
                                                                            validators=[
                                                                                self.validator.related_required_if_equal_validator(
                                                                                    field_name=chapter["checkbox_name"],
                                                                                    value=True
                                                                                )
                                                                            ]
                                                                        ),
                                                                        self.create_component(
                                                                            component_type="text",
                                                                            mask="fund",
                                                                            label="Kwota",
                                                                            name=f"{chapter["section_name"]}FundingAmount",
                                                                            required=True,
                                                                            unit="PLN",
                                                                            validators=[
                                                                                self.validator.related_required_if_equal_validator(
                                                                                    field_name=chapter["checkbox_name"],
                                                                                    value=True
                                                                                )
                                                                            ]
                                                                        ),
                                                                        self.create_component(
                                                                            component_type="text",
                                                                            mask="fund",
                                                                            label="Udział w koszcie całkowitym",
                                                                            name=f"{chapter["section_name"]}FundingShare",
                                                                            calculation_rules=[
                                                                                self.calculation_rule.single_position_share_calculator(
                                                                                    dividend_field=f"{chapter["section_name"]}FundingAmount",
                                                                                    divisor_field="totalProjectCost"
                                                                                )
                                                                            ],
                                                                            read_only=True,
                                                                            required=True,
                                                                            unit="%"
                                                                        )
                                                                    ]
                                                                )
                                                            ]
                                                        ),
                                                        self.create_chapter(
                                                            title="<normal>Łącznie</normal>",
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
                                                                    mask="fund",
                                                                    label="Kwota",
                                                                    name=f"{chapter["section_name"]}FundsSumAmount",
                                                                    calculation_rules=[
                                                                        self.calculation_rule.dynamic_sum_inputs(
                                                                            fields=[
                                                                                f"{chapter["section_name"]}FundingAmount"
                                                                            ]
                                                                        )
                                                                    ],
                                                                    read_only=True,
                                                                    required=True,
                                                                    unit="PLN"
                                                                ),
                                                                self.create_component(
                                                                    component_type="text",
                                                                    mask="fund",
                                                                    label="Udział w koszcie całkowitym",
                                                                    name=f"{chapter["section_name"]}FundsShare",
                                                                    calculation_rules=[
                                                                        self.calculation_rule.dynamic_sum_inputs(
                                                                            fields=[
                                                                                f"{chapter["section_name"]}FundingShare"
                                                                            ]
                                                                        )
                                                                    ],
                                                                    read_only=True,
                                                                    required=True,
                                                                    unit="%"
                                                                )
                                                            ]
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                ) for chapter in sources_of_financing_chapters["c"]]
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Podsumowanie źródeł finansowania",
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
                            mask="fund",
                            label="Koszt całkowity",
                            name="totalProjectCost",
                            calculation_rules=[
                                self.calculation_rule.sum_inputs(
                                    fields=[
                                        "ownFinancialFundsAmount",
                                        "ownInKindFundsAmount",
                                        "pisfSupportAmountTotal",
                                        "localGovernmentsFundsSumAmount",
                                        "ministryFundsSumAmount",
                                        "otherSponsorsFundsSumAmount",
                                        "foreignFundsSumAmount"
                                    ]
                                )
                            ],
                            validators=[
                                self.validator.related_sum_validator(
                                    field_names=[
                                        "ownFinancialFundsAmount",
                                        "ownInKindFundsAmount",
                                        "pisfSupportAmountTotal",
                                        "localGovernmentsFundsSumAmount",
                                        "ministryFundsSumAmount",
                                        "otherSponsorsFundsSumAmount",
                                        "foreignFundsSumAmount"
                                    ]
                                )
                            ],
                            read_only=True,
                            unit="PLN",
                            class_list=[
                                "table-full"
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="Wkład własny",
                            name="ownFundsSumAmountRepeat",
                            calculation_rules=[
                                self.calculation_rule.copy_value(
                                    from_name="ownFundsSumAmount"
                                )
                            ],
                            validators=[
                                self.validator.related_sum_validator(
                                    field_names=[
                                        "ownFundsSumAmount"
                                    ]
                                )
                            ],
                            read_only=True,
                            unit="PLN"
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="Udział w koszcie całkowitym",
                            name="ownFundsSumAmountRepeatShare",
                            calculation_rules=[
                                self.calculation_rule.share_calculator(
                                    dividend_field="ownFundsSumAmountRepeat",
                                    divisor_field="totalProjectCost"
                                )
                            ],
                            validators=[
                                self.validator.related_share_validator(
                                    dividend="ownFundsSumAmountRepeat",
                                    divisor="totalProjectCost"
                                )
                            ],
                            read_only=True,
                            unit="%"
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="Wnioskowana dotacja z PISF",
                            name="pisfSupportAmountTotal",
                            calculation_rules=[
                                self.calculation_rule.dynamic_sum_inputs(
                                    fields=[
                                        "pisfSupportAmountInput"
                                    ]
                                )
                            ],
                            validators=[
                                self.validator.related_sum_validator(
                                    field_names=[
                                        "pisfSupportAmountInput",
                                    ]
                                ),
                                self.validator.range_validator(
                                    max_value=15000
                                )
                            ] if self.is_dkf else [
                                self.validator.related_sum_validator(
                                    field_names=[
                                        "pisfSupportAmountInput",
                                    ]
                                )
                            ],
                            read_only=True,
                            unit="PLN"
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="Udział w koszcie całkowitym",
                            name="pisfSupportAmountTotalShare",
                            calculation_rules=[
                                self.calculation_rule.share_calculator(
                                    dividend_field="pisfSupportAmountInput",
                                    divisor_field="totalProjectCost"
                                )
                            ],
                            validators=[
                                self.validator.related_share_validator(
                                    dividend="pisfSupportAmountInput",
                                    divisor="totalProjectCost"
                                )
                            ],
                            read_only=True,
                            unit="%"
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="Środki publiczne razem (w tym wnioskowana dotacja z PISF)",
                            name="publicSupportAltogether",
                            calculation_rules=[
                                self.calculation_rule.dynamic_sum_inputs(
                                    fields=[
                                        "localGovernmentsFundsSumAmount",
                                        "ministryFundsSumAmount",
                                        "pisfSupportAmountTotal"
                                    ]
                                ),
                            ],
                            validators=[
                                self.validator.related_fraction_gte_validator(
                                    field_name="totalProjectCost",
                                    ratio=0.9,
                                    message="Kwota środków publicznych nie może przekroczyć 90% kwoty całkowitej."
                                ),
                                self.validator.related_sum_validator(
                                    field_names=[
                                        "localGovernmentsFundsSumAmount",
                                        "ministryFundsSumAmount",
                                        "pisfSupportAmountTotal"
                                    ]
                                ),
                            ],
                            read_only=True,
                            unit="PLN"
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="Udział w koszcie całkowitym",
                            name="publicSupportAltogetherShare",
                            calculation_rules=[
                                self.calculation_rule.share_calculator(
                                    dividend_field="publicSupportAltogether",
                                    divisor_field="totalProjectCost"
                                )
                            ],
                            validators=[
                                self.validator.related_share_validator(
                                    dividend="publicSupportAltogether",
                                    divisor="totalProjectCost"
                                )
                            ],
                            read_only=True,
                            unit="%"
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="Pozostałe środki razem",
                            name="otherFundsAltogether",
                            calculation_rules=[
                                self.calculation_rule.dynamic_sum_inputs(
                                    fields=[
                                        "otherSponsorsFundsSumAmount",
                                        "foreignFundsSumAmount",
                                    ]
                                )
                            ],
                            validators=[
                                self.validator.related_sum_validator(
                                    field_names=[
                                        "otherSponsorsFundsSumAmount",
                                        "foreignFundsSumAmount",
                                    ]
                                )
                            ],
                            read_only=True,
                            unit="PLN"
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="Udział w koszcie całkowitym",
                            name="otherFundsAltogetherShare",
                            calculation_rules=[
                                self.calculation_rule.share_calculator(
                                    dividend_field="otherFundsAltogether",
                                    divisor_field="totalProjectCost"
                                )
                            ],
                            validators=[
                                self.validator.related_share_validator(
                                    dividend="otherFundsAltogether",
                                    divisor="totalProjectCost"
                                )
                            ],
                            read_only=True,
                            unit="%"
                        )
                    ]
                ),
                self.create_chapter(
                    title="Informacje uzupełniające",
                    help_text="Inne istotne informacje dotyczące finansowania przedsięwzięcia, nieuwzględnione powyżej.",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="supplementaryInformationAboutFinancing",
                            validators=[
                                self.validator.length_validator(
                                    max_value=500
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        self.save_part(part)

    def create_application_project_costs(self, number: int):
        estimate_base = DUKApplicationEstimateBuilder(estimate_sections=[])

        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Kosztorys przedsięwzięcia",
            chapters=[
                estimate_base.generate_estimate_top(),
                self.create_chapter(
                    title="<p style='text-align: center;'>Koszty z podziałem na źródło finansowania<p>",
                    components=[
                        estimate_base.generate_estimate_headers(),
                        *self.estimate_chapters
                    ]
                )
            ]
        )

        self.save_part(part=part)

    def create_application_statements(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Oświadczenia",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            name="limitedAudienceSupportStatement",
                            label="Oświadczam, że ze względu na ograniczony krąg odbiorców lub ze względu na niską wartość komercyjną, wydarzenie nie mogłoby się odbyć bez dofinansowania PISF.",
                            help_text="Należy zaznaczyć, jeśli dofinansowanie PISF przekracza 50% całkowitego budżetu.",
                            validators=[
                                self.validator.related_universal_required_validator(
                                    field_name="pisfSupportAmountTotalShare",
                                    condition={
                                        "min_range": 50.0001
                                    }
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="checkbox",
                            name="previousEditionCostsStatement",
                            label="Oświadczam, że koszty realizacji poprzedniej edycji przedsięwzięcia nie będą pokrywane z dotacji udzielonej w ramach niniejszych Programów Operacyjnych.",
                            help_text="Należy zaznaczyć, jeśli poprzednia edycja przedsięwzięcia nie została jeszcze rozliczona."
                        ),
                        self.create_component(
                            component_type="checkbox",
                            name="resourcesDeclarationStatement",
                            label="Oświadczam, że posiadam zasoby rzeczowe, finansowe i kadrowe niezbędne do realizacji zadania.",
                            required=True,
                        ),
                        self.create_component(
                            component_type="checkbox",
                            name="noPublicDebtStatement",
                            label="Oświadczam, że nie zalegam z płatnościami na rzecz podmiotów publiczno-prawnych.",
                            required=True,
                        ),
                        self.create_component(
                            component_type="checkbox",
                            name="pisfGrantEligibilityStatement",
                            label="Oświadczam, że spełniam warunki do otrzymania dofinansowania określone w Ustawie o kinematografii oraz w Rozporządzeniu Ministra Kultury w sprawie udzielenia przez PISF dofinansowania przedsięwzięć z zakresu kinematografii.",
                            required=True,
                        ),
                        self.create_component(
                            component_type="checkbox",
                            name="noDisqualificationGroundsStatement",
                            label="Oświadczam, że nie zachodzą przesłanki określone w art. 22 ust. 2 ustawy o kinematografii z dnia 30 czerwca 2005 r., które uniemożliwiają udzielenie dofinansowania.",
                            required=True,
                        ),
                        self.create_component(
                            component_type="checkbox",
                            name="isswDocumentsSubmissionStatement",
                            label='W przypadku uzyskania dofinansowania zobowiązuję się do uzupełnienia za pośrednictwem ISSW (zakładka "Dokumenty") aktualnych dokumentów potwierdzających status prawny wnioskodawcy, w tym:<br/>– aktualnego wypisu z właściwego rejestru (w zależności od formy prawnej: KRS – wystawionego nie wcześniej niż trzy miesiące przed datą złożenia, RIK, RIF, zaświadczenia o wpisie do ewidencji działalności gospodarczej lub innego właściwego dokumentu),<br/>– dokumentu potwierdzającego powołanie dyrektora instytucji,<br/>– zaświadczenia o nadaniu numeru REGON,<br/>– decyzji o nadaniu numeru NIP,<br/>– a w przypadku spółki cywilnej – kopii umowy spółki.',
                            required=True,
                        ),
                        self.create_component(
                            component_type="checkbox",
                            name="sanctionsComplianceDeclarationStatement",
                            label="§ 1<br/>1. Beneficjent oświadcza, że, bezpośrednio lub pośrednio:<br/>a) nie wspiera agresji Federacji Rosyjskiej na Ukrainę rozpoczętą w dniu 24 lutego 2022 r.,<br/>b) nie wspiera naruszeń praw człowieka lub represji wobec społeczeństwa obywatelskiego i opozycji demokratycznej lub których działalność stanowi inne poważne zagrożenie dla demokracji lub praworządności w Federacji Rosyjskiej lub na Białorusi,<br/>c) nie jest bezpośrednio związany z osobami lub podmiotami, które nie spełniają kryteriów o których mowa w lit. a i b powyżej, w szczególności ze względu na powiązania o charakterze osobistym, organizacyjnym, gospodarczym lub finansowym, lub wobec których istnieje prawdopodobieństwo wykorzystania w tym celu dysponowanych przez nie takich środków finansowych, funduszy lub zasobów gospodarczych,<br/>d) nie uchyla się od jakichkolwiek środków ograniczających (sankcji), nie narusza przepisów nakładających sankcje ani nie ułatwia innym podmiotom uchylania się od sankcji.<br/>2. Beneficjent oświadcza, że nie znajduje się na liście osób i podmiotów, wobec których są stosowane środki ograniczające (sankcje), o których mowa w art. 2 ustawy o przeciwdziałaniu wspieraniu agresji, a w szczególności:<br/>a) nie jest wymieniony w wykazach określonych w rozporządzeniu Rady (WE) nr 765/2006 z dnia 18 maja 2006 r. dotyczącego środków ograniczających w związku z sytuacją na Białorusi i udziałem Białorusi w agresji Rosji wobec Ukrainy (dalej jako „Rozporządzenie 765/2006”),<br/>b) nie jest wymieniony w wykazach określonych w rozporządzeniu Rady (UE) nr 269/2014 z dnia 17 marca 2014 r. w sprawie środków ograniczających w odniesieniu do działań podważających integralność terytorialną, suwerenność i niezależność Ukrainy lub im zagrażających (dalej jako „Rozporządzenie 269/2014”),<br/>c) wobec Beneficjenta nie została wydana decyzja w sprawie wpisu na listę osób i podmiotów, wobec których są stosowane środki w celu przeciwdziałania wspieraniu agresji Federacji Rosyjskiej na Ukrainę, z zastosowaniem środka w postaci wykluczenia z postępowania o udzielenie zamówienia publicznego lub konkursu prowadzonego na podstawie ustawy z dnia 11 września 2019 r. - Prawo zamówień publicznych,<br/>d) Beneficjent nie jest umieszczony w wykazie cudzoziemców, których pobyt na terytorium Rzeczypospolitej Polskiej jest niepożądany, o którym mowa w art. 434 ustawy z dnia 12 grudnia 2013 r. o cudzoziemcach (dalej jako „Ustawa o cudzoziemcach”),<br/>e) w stosunku do Beneficjenta członkiem organów, pracownikiem szczebla kierowniczego lub beneficjentem rzeczywistym, w rozumieniu ustawy z dnia 1 marca 2018 r. o przeciwdziałaniu praniu pieniędzy oraz finansowaniu terroryzmu, ani ich krewnym (przy czym na potrzeby niniejszego oświadczenia krewny, w odniesieniu do osoby fizycznej, oznacza jej małżonka, rodzeństwo, zstępnych i wstępnych) nie jest osoba znajdująca się na liście osób i podmiotów, wobec których są stosowane środki ograniczające, o której mowa w art. 2 ustawy o przeciwdziałaniu wspierania agresji, w szczególności nie znajduje się w wykazach określonych w Rozporządzeniu 765/2006, Rozporządzeniu 269/2014 lub art. 434 Ustawy o cudzoziemcach,<br/>f) w stosunku do Beneficjenta jednostką dominującą w rozumieniu art. 3 ust. 1 pkt 37 ustawy z dnia 29 września 1994 r. o rachunkowości nie jest podmiot wymieniony w wykazach określonych w Rozporządzeniu 765/2006 i Rozporządzeniu 269/2014;<br/>g) żaden z udziałów w kapitale zakładowym Beneficjenta nie jest własnością bezpośrednio lub pośrednio, ani nie został na nim ustanowiony zastaw ani użytkowanie na rzecz podmiotów wobec których są stosowane środki ograniczające (sankcje), o których mowa w niniejszym § 2, lub jakiegokolwiek podmiotu lub osoby, która korzysta z kapitału lub finansowania zapewnionego przez taki podmiot ani władz rosyjskich; przy czym na potrzeby niniejszego oświadczenia przez władze rosyjskie należy rozumieć Federację Rosyjską (i jej kraje związkowe), federalne i lokalne władze państwowe, państwowe jednostki organizacyjne i przedsiębiorstwa państwowe, instytucje publiczne, wszelkie spółki i podmioty bezpośrednio lub pośrednio kontrolowane przez wyżej wymienione oraz wszelkie podmioty powiązane z wyżej wymienionymi.<br/>3. Ponadto Beneficjent oświadcza, że nie znajduje się na liście osób i podmiotów, wobec których są stosowane środki ograniczające (sankcje) nałożone przez Organizację Narodów Zjednoczonych, państwo członkowskie Organizacji Narodów Zjednoczonych lub każdą inną organizację międzyrządową wprowadzone w związku z naruszeniem integralności terytorialnej Ukrainy i inwazją na Ukrainę (w tym również aneksją Krymu i konfliktem w regionie Donbasu) przeciwko Federacji Rosyjskiej, Białorusi, wskazanym osobom fizycznym i podmiotom.<br/>§ 2<br/>1. Beneficjent przyjmuje do wiadomości, że oświadczenia Beneficjenta, o których mowa w § 1 powyżej, dotyczą środków ograniczających (sankcji), które obowiązują w dniu zawarcia Umowy i powinny pozostać prawdziwe przez cały okres obowiązywania Umowy.<br/>2. Beneficjent zobowiązuje się monitorować swoje inwestycje, relacje biznesowe i działalność gospodarczą/zawodową w celu zapewnienia zgodności z wyżej wymienionymi oświadczeniami, przy jednoczesnym dochowaniu należytej staranności ogólnie wymaganej w relacjach biznesowych.<br/>3. Beneficjent zobowiązuje się niezwłocznie poinformować Polski Instytut Sztuki Filmowej o każdej zmianie okoliczności, o których mowa w § 1 powyżej, które wystąpiły, powstały lub istniały przed dniem zawarcia Umowy, a których nie był świadomy, lub które wystąpiły, powstały lub zaistniały po zawarciu Umowy.<br/>§ 3<br/>1. W przypadku nieprawdziwości któregokolwiek ze złożonych oświadczeń, o których mowa w § 1 powyżej, Polski Instytut Sztuki Filmowej jest uprawniony do wypowiedzenia Umowy w trybie natychmiastowym i żądania zwrotu przekazanych środków finansowych wraz z odsetkami ustawowymi za opóźnienie liczonymi od dnia przekazania środków, w terminie wskazanym przez Polski Instytut Sztuki Filmowej, jednak nie dłuższym niż 14 dni od dnia doręczenia wezwania zwrotu.\n2. Bez uszczerbku dla postanowień ust. 1, w przypadku, w którym na skutek niepełnych, nierzetelnych lub nieprawdziwych oświadczeń Beneficjenta na Polski Instytut Sztuki Filmowej nałożona zostanie jakakolwiek kara administracyjna, Beneficjent zobowiązuje się do zwrotu - regresowo na wezwanie Polskiego Instytutu Sztuki Filmowej - całości pokrytych kar oraz wszelkich związanych z tym wydatków, włączając koszty postępowania sądowego, arbitrażowego, administracyjnego lub ugodowego oraz koszty pomocy prawnej.",
                            required=True,
                        )
                    ]
                )
            ]
        )

        self.save_part(part)

    def create_application_attachments(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Załączniki",
            chapters=[
                self.create_chapter(
                    title="Obowiązkowe załączniki",
                    components=[
                        self.section.application_attachment.document_confirming_represent_applicant(),
                        self.section.application_attachment.schedule_information()
                    ]
                ),
                self.section.application_attachment.other_attachments(),
                self.section.application_attachment.storage_of_blanks()
            ]
        )
        self.save_part(part)

    def create_application_schedule(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Harmonogram realizacji zadania",
            short_name=f"{self.helpers.int_to_roman(number)}. Harmonogram",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Nazwa przedsięwzięcia",
                            name="projectNameRepeatSchedule",
                            read_only=True,
                            required=True,
                            calculation_rules=[
                                self.calculation_rule.copy_value(
                                    from_name="applicationTaskName"
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="<small>Uwaga!</br><normal>Harmonogram powinien uwzględniać trzy główne etapy realizacji projektu:</br><b>- etap przygotowawczy</b> - np. poszukiwania partnerów, zaproszenie uczestników, przygotowanie i zaplanowanie promocji wydarzenia, inne czynności niezbędne do rozpoczęcia realizacji zadania;</br><b>- etap realizacji</b> - wszystkie działania związane z bezpośrednim wykonaniem projektu, np. przygotowanie i przeprowadzenie przedsięwzięcia oraz realizacja pozostałych zadań przewidzianych w kosztorysie;</br><b>- etap podsumowania</b> - ewaluacja rezultatów projektu, rozliczenie końcowe.</br></br>Harmonogram powinien być <b>ułożony chronologicznie</b>, obejmować <b>wszystkie działania ujęte w kosztorysie</b>, wyróżniać <b>kluczowe kamienie milowe</b>, tj. najważniejsze momenty realizacji projektu.</br></br>Ostateczny termin zakończenia realizacji zadania (z uwzględnieniem etapu podsumowania) powinien zostać wskazany poprzez podanie dokładnej daty: dzień, miesiąc i rok.</normal></small>",
                    components=[]
                ),
                self.create_chapter(
                    title="Etap przygotowawczy",
                    components=[
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 1,
                                "maxCount": 20
                            },
                            components=[
                                self.create_chapter(
                                    title="Pozycja",
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
                                            component_type="date",
                                            label="Termin od",
                                            name="preparatoryStageStartDate",
                                            validators=[
                                                self.validator.related_local_date_lte_validator(
                                                    field_name="preparatoryStageEndDate",
                                                    message="Termin rozpoczęcia działania musi być wcześniejszy niż termin jego zakończenia."
                                                )
                                            ],
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="date",
                                            label="Termin do",
                                            name="preparatoryStageEndDate",
                                            validators=[
                                                self.validator.related_local_date_gte_validator(
                                                    field_name="preparatoryStageStartDate",
                                                    message="Termin zakończenia działania musi być późniejszy niż termin jego rozpoczęcia."
                                                )
                                            ],
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="textarea",
                                            label="Działanie",
                                            name="preparatoryStageDescription",
                                            help_text="Krótki opis działania",
                                            class_list=[
                                                "table-full",
                                                "col-span-2"
                                            ],
                                            validators=[
                                                self.validator.length_validator(max_value=250)
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                    ]
                ),
                self.create_chapter(
                    title="Etap realizacji zadania",
                    components=[
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 1,
                                "maxCount": 20
                            },
                            components=[
                                self.create_chapter(
                                    title="Pozycja",
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
                                            component_type="date",
                                            label="Termin od",
                                            name="implementationStageStartDate",
                                            validators=[
                                                self.validator.related_local_date_lte_validator(
                                                    field_name="implementationStageEndDate",
                                                    message="Termin rozpoczęcia działania musi być wcześniejszy niż termin jego zakończenia."
                                                )
                                            ],
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="date",
                                            label="Termin do",
                                            name="implementationStageEndDate",
                                            validators=[
                                                self.validator.related_local_date_gte_validator(
                                                    field_name="implementationStageStartDate",
                                                    message="Termin zakończenia działania musi być późniejszy niż termin jego rozpoczęcia."
                                                )
                                            ],
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="textarea",
                                            label="Działanie",
                                            name="implementationStageDescription",
                                            help_text="Krótki opis działania.",
                                            class_list=[
                                                "table-full",
                                                "col-span-2"
                                            ],
                                            validators=[
                                                self.validator.length_validator(max_value=250)
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                    ]
                ),
                self.create_chapter(
                    title="Etap podsumowania zadania",
                    components=[
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 1,
                                "maxCount": 20
                            },
                            components=[
                                self.create_chapter(
                                    title="Pozycja",
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
                                            component_type="date",
                                            label="Termin od",
                                            name="summaryStageStartDate",
                                            validators=[
                                                self.validator.related_local_date_lte_validator(
                                                    field_name="summaryStageEndDate",
                                                    message="Termin rozpoczęcia działania musi być wcześniejszy niż termin jego zakończenia."
                                                )
                                            ],
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="date",
                                            label="Termin do",
                                            name="summaryStageEndDate",
                                            validators=[
                                                self.validator.related_local_date_gte_validator(
                                                    field_name="summaryStageStartDate",
                                                    message="Termin zakończenia działania musi być późniejszy niż termin jego rozpoczęcia."
                                                )
                                            ],
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="textarea",
                                            label="Działanie",
                                            name="summaryStageDescription",
                                            help_text="Krótki opis działania.",
                                            class_list=[
                                                "table-full",
                                                "col-span-2"
                                            ],
                                            validators=[
                                                self.validator.length_validator(max_value=250)
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                    ]
                ),
                self.create_chapter(
                    title="Podsumowanie harmonogramu",
                    class_list={
                        "main": [
                            "dates"
                        ],
                        "sub": [
                            "dates-item"
                        ]
                    },
                    components=[
                        self.create_component(
                            component_type="date",
                            label="Rozpoczęcie realizacji przedsięwzięcia",
                            name="projectCommencement",
                            read_only=True,
                            required=True,
                            calculation_rules=[
                                self.calculation_rule.first_date(
                                    field="preparatoryStageStartDate",
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="date",
                            label="Zakończenie realizacji przedsięwzięcia",
                            name="projectCompletion",
                            required=True,
                            read_only=True,
                            calculation_rules=[
                                self.calculation_rule.last_date(
                                    field="summaryStageEndDate"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="date",
                            label="Termin rozliczenia z PISF",
                            name="settlementDeadline",
                            read_only=True,
                            required=True,
                            calculation_rules=[
                                self.calculation_rule.relate_to_last_date(
                                    field="projectCompletion",
                                    parameter=30
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        self.save_part(part)
