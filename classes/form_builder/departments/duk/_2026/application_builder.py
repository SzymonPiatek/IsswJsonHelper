from classes.form_builder.departments.duk.application_builder import DUKApplicationBuilder
from classes.form_builder.departments.duk._2026.application_estimate_builder import DUKApplicationEstimateBuilder
from classes.helpers import int_to_roman


class DUKApplicationBuilder2026(DUKApplicationBuilder):
    YEAR = 2026

    def __init__(self):
        super().__init__()

        self.project_type = []
        self.estimate_chapters = []
        self.parts: list = [
            self.create_application_metadata,
            self.create_application_basic_data,
            self.create_application_applicant_data,
            self.create_application_scope_of_project,
            self.create_application_sources_of_financing,
            self.create_application_statements,
            self.create_application_attachments,
            self.create_application_project_costs,
            self.create_application_schedule
        ]

    def create_application_metadata(self, number: int):
        part = self.create_part(
            title="Wniosek o dofinansowanie przedsięwzięcia realizowanego w ramach Programów Operacyjnych Polskiego Instytutu Sztuki Filmowej",
            short_name=f"{int_to_roman(number)}. Metadane wniosku",
            chapters=[
                self.create_chapter(
                    title="1. Tryb naboru",
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Nr sesji i rok",
                            name="sessionYear",
                            value=f"Sesja {self.session}/{self.year}",
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
                            value=self.operation_name,
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
                            value=self.priority_name,
                            read_only=True
                        )
                    ]
                )
            ]
        )
        self.save_part(part=part)

    def create_application_basic_data(self, number: int):
        part = self.create_part(
            title=f"{int_to_roman(number)}. Dane podstawowe",
            short_name=f"{int_to_roman(number)}. Dane podstawowe",
            chapters=[
                self.create_chapter(
                    title="1. Nazwa przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="applicationTaskName",
                            validators=[
                                self.validator.length_validator(max_value=1000)
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
                                    label="Numer wniosku dotyczący poprzedniej edycji przedsięwzięcia",
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

    def create_application_applicant_data(self, number: int):
        part = self.create_part(
            title=f"{int_to_roman(number)}. Dane wnioskodawcy",
            short_name=f"{int_to_roman(number)}. Dane wnioskodawcy",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_chapter(
                            title="Pełna nazwa wnioskodawcy",
                            class_list=["displayNoneFrontend"]
                        ),
                        self.create_chapter(
                            title="Pełna nazwa wnioskodawcy<br/><normal><small>Oficjalna nazwa firmy lub podmiotu wpisana do odpowiedniego rejestru (KRS, CEiDG, Rejestr instytucji kultury, Rejestr Instytucji Filmowych itp.</small></normal>",
                            class_list=["no-title"],
                            components=[
                                self.create_component(
                                    component_type="text",
                                    name="applicantName",
                                    required=True
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Forma organizacyjno-prawna",
                    components=[
                        self.component.org_and_legal_structure_select()
                    ]
                ),
                self.section.eligible_person_data(number="1"),
                self.section.responsible_person_data(number="2"),
                self.create_chapter(
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
                            title="3. Adres wnioskodawcy",
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
                        ),
                        self.create_chapter(
                            title="4. Dane identyfikacyjne wnioskodawcy oraz informacje prawne",
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
                                                            title="Adres wykonania działalności gospodarczej",
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
                                    title="Oznaczenia sądu rejonowego",
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
                                                    component_type="text",
                                                    label="Nazwa rejestru",
                                                    name="courtRegisterName",
                                                    required=True
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
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="orgAndLegalStructure",
                                            values=[
                                                "Spółka z ograniczoną odpowiedzialnością",
                                                "Spółka akcyjna",
                                                "Spółka jawna",
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
                                    title="Reprezentacja",
                                    components=[
                                        self.create_chapter(
                                            multiple_forms_rules={
                                                "minCount": 1,
                                                "maxCount": 10
                                            },
                                            components=[
                                                self.create_chapter(
                                                    title="Osoba reprezentująca",
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
                                                            name="applicantRepresentativeFirstName",
                                                            required=True
                                                        ),
                                                        self.create_component(
                                                            component_type="text",
                                                            label="Nazwisko",
                                                            name="applicantRepresentativeLastName",
                                                            required=True
                                                        ),
                                                        self.create_component(
                                                            component_type="text",
                                                            label="Stanowisko",
                                                            name="applicantRepresentativePosition",
                                                            required=True,
                                                            class_list=[
                                                                "table-full"
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
                                                "Spółka komandytowa",
                                                "Spółka komandytowo-akcyjna",
                                            ]
                                        )
                                    ],
                                    title="Reprezentacja",
                                    components=[
                                        # TODO - Reprezentacja dla spółki komandytowej
                                    ]
                                ),
                                self.create_chapter(
                                    title="Identyfikator gminy (Kod JST)",
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            name="applicantJst",
                                            mask="jst",
                                            required=True,
                                            help_text="Kod JST gminy można znaleźć w wyszukiwarce pod adresem https://eteryt.stat.gov.pl"
                                        ),
                                    ]
                                ),
                                self.create_chapter(
                                    title="Kod PKD",
                                    components=[
                                        self.create_component(
                                            component_type="radio",
                                            name="applicantPkd",
                                            options=[
                                                "59.11 – Działalność związana z produkcją filmów, nagrań wideo i programów telewizyjnych",
                                                "59.12 - Działalność postprodukcyjna związana z filmami, nagraniami wideo i programami telewizyjnymi",
                                                "59.13 - Działalność związana z dystrybucją filmów, nagrań wideo i programów telewizyjnych",
                                                "59.14 - Działalność związana z projekcją filmów",
                                                "59.20 - Działalność w zakresie nagrań dźwiękowych i muzycznych"
                                            ],
                                            required=True
                                        )
                                    ]
                                ),
                            ]
                        )
                    ]
                ),
                self.section.applicant_bank_data(number="5"),
                self.create_chapter(
                    title="Uwaga!<br/><br/><normal>Wszystkie koszty danego przedsięwzięcia muszą być opłacane z rachunku bankowego podanego we Wniosku o dofinansowanie. Na ten sam rachunek powinny też wpływać środki od innych podmiotów współfinansujących dane przedsięwzięcie. Możliwe są dwa rozwiązania:<br/>a) rachunek służący do rozliczeń przedsięwzięcia, którego dotyczy Wniosek o dofinansowanie, w tym wpływów i wydatków związanych z dotacją PISF,<br/>b) rachunek przeznaczony wyłącznie do obsługi środków z dotacji PISF, na który mogą trafiać środki z różnych dofinansowań udzielonych przez PISF.</normal>"
                ),
                self.section.applicant_statistical_data(number="6"),
            ]
        )

        self.save_part(part=part)

    def create_application_sources_of_financing(self, number: int):
        sources_of_financing_chapters = {
            "c": [
                {
                    "checkbox_title": "Czy występują środki z budżetów jednostek samorządu terytorialnego lub innych środków publicznych za wyjątkiem Ministerstwa Kultury i Dziedzictwa Narodowego?",
                    "checkbox_name": "isLocalGovernmentFunding",
                    "section_title": "<normal>a) z budżetów jednostek samorządu terytorialnego lub innych środków publicznych za wyjątkiem Ministerstwa Kultury i Dziedzictwa Narodowego </normal><br /><small>Uwaga! <normal>Odznaczenie powyższego checkboxa nie prowadzi do automatycznego usunięcia zawartych w tej sekcji informacji. Dane te nadal będą brane pod uwagę w obliczeniach finansowych i będą uwzględnione we wniosku. Jeżeli dane te nie są już potrzebne, prosimy o ich ręczne usunięcie. </small></normal>",
                    "section_name": "localGovernments",
                },
                {
                    "checkbox_title": "Czy występują środki Ministerstwa Kultury i Dziedzictwa Narodowego w ramach Programów Ministra?",
                    "checkbox_name": "isMinistryFunding",
                    "section_title": "<normal>b) ze środków Ministerstwa Kultury i Dziedzictwa Narodowego w ramach Programów Ministra </normal><br /><small>Uwaga! <normal>Odznaczenie powyższego checkboxa nie prowadzi do automatycznego usunięcia zawartych w tej sekcji informacji. Dane te nadal będą brane pod uwagę w obliczeniach finansowych i będą uwzględnione we wniosku. Jeżeli dane te nie są już potrzebne, prosimy o ich ręczne usunięcie. </small></normal>",
                    "section_name": "ministry",
                },
                {
                    "checkbox_title": "Czy występują środki od sponsorów lub innych podmiotów niezaliczanych do sektora finansów publicznych?",
                    "checkbox_name": "isOtherSponsorFunding",
                    "section_title": "<normal>c) od sponsorów lub innych podmiotów niezaliczanych do sektora finansów publicznych </normal><br /><small>Uwaga! <normal>Odznaczenie powyższego checkboxa nie prowadzi do automatycznego usunięcia zawartych w tej sekcji informacji. Dane te nadal będą brane pod uwagę w obliczeniach finansowych i będą uwzględnione we wniosku. Jeżeli dane te nie są już potrzebne, prosimy o ich ręczne usunięcie. </small></normal>",
                    "section_name": "otherSponsors",
                },
                {
                    "checkbox_title": "Czy występują środki zagraniczne, w tym europejskie?",
                    "checkbox_name": "isForeignFunding",
                    "section_title": "<normal>d) ze środków zagranicznych, w tym europejskich </normal><br /><small>Uwaga! <normal>Odznaczenie powyższego checkboxa nie prowadzi do automatycznego usunięcia zawartych w tej sekcji informacji. Dane te nadal będą brane pod uwagę w obliczeniach finansowych i będą uwzględnione we wniosku. Jeżeli dane te nie są już potrzebne, prosimy o ich ręczne usunięcie. </small></normal>",
                    "section_name": "foreign",
                }
            ]
        }

        part = self.create_part(
            title=f"{int_to_roman(number)}. Źródła finansowania",
            short_name=f"{int_to_roman(number)}. Źródła finansowania",
            chapters=[
                self.create_chapter(
                    title="1. Podstawowe dane finansowe",
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
                    components=[
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="Kwota całkowita",
                            name="totalProjectCost",
                            calculation_rules=[
                                self.calculation_rule.sum_inputs(
                                    fields=[
                                        "ownFundsSumAmount",
                                        "pisfSupportAmount",
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
                                        "ownFundsSumAmount",
                                        "pisfSupportAmount",
                                        "localGovernmentsFundsSumAmount",
                                        "ministryFundsSumAmount",
                                        "otherSponsorsFundsSumAmount",
                                        "foreignFundsSumAmount"
                                    ]
                                )
                            ],
                            read_only=True,
                            unit="PLN"
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="Wnioskowana dotacja z PISF",
                            name="pisfSupportAmounRepeat",
                            calculation_rules=[
                                self.calculation_rule.copy_value(
                                    from_name="pisfSupportAmountInput"
                                )
                            ],
                            validators=[
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
                            label="Środki publiczne razem",
                            name="publicSupportAltogether",
                            read_only=True,
                            unit="PLN"
                        )
                    ]
                ),
                self.create_chapter(
                    components=[
                        self.create_chapter(
                            title="2. Wyszczególnienie źródeł finansowaniania",
                            components=[
                                self.create_chapter(
                                    title="<normal>1) Wkład własny</normal><br/><normal><small>Minimum 10% budżetu przedsięwzięcia. Wkład rzeczowy nie może być wyższy niż 50% całkowitego wkładu własnego.</small></normal>",
                                    class_list=[
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>1) Wkład własny</normal>",
                                    components=[
                                        self.create_chapter(
                                            title="<small>a) Wkład finansowy</small>",
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
                                        ),
                                        self.create_chapter(
                                            title="<small>b) Wkład rzeczowy</small>"
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
                                                    mask="fund",
                                                    name="ownInKindFundsAmount",
                                                    label="Kwota",
                                                    unit="PLN"
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
                                        ),
                                        self.create_chapter(
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
                                    ]
                                ),
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
                                            validators=[
                                                self.validator.related_fraction_gte_validator(
                                                    field_name="totalProjectCost",
                                                    ratio=0.9,
                                                    message="Dotacja PISF nie może przekroczyć 90% kosztu realizacji przedsięwzięcia."
                                                )
                                            ],
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
                                                                                    unit="%",
                                                                                    validators=[
                                                                                        self.validator.related_required_if_equal_validator(
                                                                                            field_name=chapter["checkbox_name"],
                                                                                            value=True
                                                                                        )
                                                                                    ]
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
                                                                                self.calculation_rule.single_position_share_calculator(
                                                                                    dividend_field=f"{chapter["section_name"]}FundsSumAmount",
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
                                                        )
                                                    ]
                                                )
                                            ]
                                        ) for chapter in sources_of_financing_chapters["c"]]
                                    ]
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
            title=f"{int_to_roman(number)}. Kosztorys przedsięwzięcia",
            short_name=f"{int_to_roman(number)}. Kosztorys przedsięwzięcia",
            chapters=[
                estimate_base.generate_estimate_top(),
                self.create_chapter(
                    title="Koszty z podziałem na źródło finansowania",
                    components=[
                        estimate_base.generate_estimate_headers(),
                        *self.estimate_chapters
                    ]
                ),
                estimate_base.generate_estimate_bottom()
            ]
        )

        self.save_part(part=part)

    def generate(self):
        # Base
        self.create_base()

        index = 0

        for part in self.parts:
            index += 1
            part(number=index)

        # Zapis
        self.save_output()
