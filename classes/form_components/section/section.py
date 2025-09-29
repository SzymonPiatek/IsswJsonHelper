from classes.form_components.component import Component
from classes.form_factory.form_factory import FormFactory


class Section(FormFactory):
    def __init__(self):
        super().__init__()
        self.component = Component()

    def applicant_name(self, number: int | str):
        return self.create_chapter(
            title=f"{number}. Pełna nazwa wnioskodawcy",
            components=[
                self.create_component(
                    component_type="text",
                    name="applicantName",
                    required=True
                )
            ]
        )

    def applicant_full_name(self, number: int | str):
        return self.create_chapter(
            title=f"{number}. Imię i nazwisko wnioskodawcy",
            components=[
                self.create_component(
                    component_type="text",
                    name="applicantFullName",
                    required=True
                )
            ]
        )

    def applicant_type(self, number: int | str):
        return self.create_chapter(
            title=f"{number}. Rodzaj wnioskodawcy",
            components=[
                self.create_component(
                    component_type="text",
                    name="applicantType",
                    required=True
                )
            ]
        )

    def eligible_person_attachments(self, number: int | str):
        return self.create_chapter(
            title=f"{number}. Pełnomocnictwa",
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

    def eligible_person_data(self, number: int | str):
        return self.create_chapter(
            title=f"{number}. Osoby upoważnione do reprezentowania wnioskodawcy, składania oświadczeń woli i zaciągania w jego imieniu zobowiązań finansowych",
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
                    title="Osoba",
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
                            required=True,
                            class_list=[
                                "table-full"
                            ]
                        )
                    ]
                )
            ]
        )

    def responsible_person_data(self, number: int | str):
        return self.create_chapter(
            title=f"{number}. Osoba odpowiedzialna za przygotowanie wniosku i kontakty z PISF",
            class_list={
                "sub": [
                    "table-1-2-top"
                ]
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
                            label="Imię",
                            name="authPersonFirstName",
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Nazwisko",
                            name="authPersonLastName",
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Numer telefonu stacjonarnego",
                            name="authPersonPhoneNum",
                            mask="landline",
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Numer telefonu komórkowego",
                            name="authPersonMobileNum",
                            mask="phoneNumber",
                            required=True,
                            validators=[
                                self.validator.phone_number_validator()
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Email kontaktowy",
                            name="authPersonEmail",
                            required=True,
                            validators=[
                                self.validator.email_validator()
                            ],
                            class_list=[
                                "col-span-2"
                            ]
                        )
                    ]
                )
            ]
        )

    def create_address_base(self, start_name: str, build_name: str = '', poland: bool = True, foreign: bool = True, is_local: bool = False):
        chapters = []

        if poland:
            chapters.append(
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.local_equals_value(
                            field_name=f"{start_name}{build_name}Residence",
                            values=["w Polsce"]
                        ) if is_local else
                        self.visibility_rule.depends_on_value(
                            field_name=f"{start_name}{build_name}Residence",
                            values=["w Polsce"]
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
                        self.component.voivodeship_select(
                            name=f"{start_name}{build_name}Voivodeship"
                        ),
                        self.create_component(
                            component_type="text",
                            label="Powiat",
                            name=f"{start_name}{build_name}County",
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Gmina",
                            name=f"{start_name}{build_name}Municipality",
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Identyfikator gminy (Kod JST)",
                            name=f"{start_name}{build_name}Jst",
                            mask="jst",
                            required=True,
                            help_text="Kod JST gminy można znaleźć w wyszukiwarce pod adresem https://eteryt.stat.gov.pl"
                        ),
                        self.create_component(
                            component_type="text",
                            label="Miejscowość",
                            name=f"{start_name}{build_name}Location",
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Ulica",
                            name=f"{start_name}{build_name}Street",
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Numer domu",
                            name=f"{start_name}{build_name}HouseNum",
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Numer lokalu",
                            name=f"{start_name}{build_name}ApartmentNum"
                        ),
                        self.create_component(
                            component_type="text",
                            label="Kod pocztowy",
                            name=f"{start_name}{build_name}ZipCode",
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Poczta",
                            name=f"{start_name}{build_name}PostOffice",
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            mask="phoneNumber",
                            label="Numer telefonu",
                            name=f"{start_name}{build_name}PhoneNum",
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Email kontaktowy",
                            name=f"{start_name}{build_name}Email",
                            required=True,
                            validators=[
                                self.validator.email_validator()
                            ]
                        )
                    ]
                )
            )

        if foreign:
            chapters.append(
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.local_equals_value(
                            field_name=f"{start_name}{build_name}Residence",
                            values=["za granicą"]
                        ) if is_local else
                        self.visibility_rule.depends_on_value(
                            field_name=f"{start_name}{build_name}Residence",
                            values=["za granicą"]
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
                            component_type="country",
                            label="Kraj",
                            name=f"{start_name}{build_name}Country",
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Miejscowość",
                            name=f"{start_name}{build_name}ForeignLocation",
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Ulica",
                            name=f"{start_name}{build_name}ForeignStreet",
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Numer domu",
                            name=f"{start_name}{build_name}ForeignHouseNum",
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Numer lokalu",
                            name=f"{start_name}{build_name}ForeignApartmentNum"
                        ),
                        self.create_component(
                            component_type="text",
                            label="Kod pocztowy",
                            name=f"{start_name}{build_name}ForeignZipCode",
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Poczta",
                            name=f"{start_name}{build_name}ForeignPostOffice"
                        ),
                        self.create_component(
                            component_type="text",
                            mask="phoneNumber",
                            label="Numer telefonu",
                            name=f"{start_name}{build_name}ForeignPhoneNum",
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Email kontaktowy",
                            name=f"{start_name}{build_name}ForeignEmail",
                            validators=[
                                self.validator.email_validator()
                            ],
                            required=True
                        )
                    ]
                )
            )

        return chapters

    def applicant_address_base(self, build_name: str = '', poland: bool = True, foreign: bool = True, is_local: bool = False):
        return self.create_address_base(
            start_name="applicant",
            build_name=build_name,
            poland=poland,
            foreign=foreign,
            is_local=is_local
        )

    def create_full_address_section(self, who: str, name: str, number: int | str, main_poland: bool = True, main_foreign: bool = True, contact_poland: bool = True, contact_foreign: bool = True, is_local: bool = False):
        return self.create_chapter(
            title=f"{number}. Adres i dane {who}",
            components=[
                self.create_chapter(
                    title=f"{number}a. Adres siedziby",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    name=f"{name}Residence",
                                    value="" if main_poland and main_foreign else "w Polsce" if main_poland else "za granicą",
                                    options=["w Polsce", "za granicą"] if main_poland and main_foreign else ["w Polsce"] if main_poland else ["za granicą"],
                                    read_only=False if main_poland and main_foreign else True,
                                    required=True
                                )
                            ]
                        ),
                        *self.create_address_base(
                            start_name=name,
                            poland=main_poland,
                            foreign=main_foreign,
                            is_local=is_local
                        )
                    ]
                ),
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Należy zaznaczyć jeśli adres korespondencyjny jest inny",
                            name=f"{name}HasDifferentContactAddress"
                        )
                    ]
                ),
                self.create_chapter(
                    title=f"{number}b. Adres korespondencyjny",
                    visibility_rules=[
                        self.visibility_rule.local_equals_value(
                            field_name=f"{name}HasDifferentContactAddress",
                            values=[True]
                        ) if is_local else self.visibility_rule.depends_on_value(
                            field_name=f"{name}HasDifferentContactAddress",
                            values=[True]
                        )
                    ],
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    name=f"{name}ContactResidence",
                                    value="" if contact_poland and contact_foreign else "w Polsce" if contact_poland else "za granicą",
                                    options=["w Polsce", "za granicą"] if contact_poland and contact_foreign else ["w Polsce"] if contact_poland else ["za granicą"],
                                    read_only=False if contact_poland and contact_foreign else True,
                                    required=True
                                )
                            ]
                        ),
                        *self.create_address_base(
                            start_name=name,
                            build_name="Contact",
                            poland=main_poland,
                            foreign=main_foreign,
                            is_local=is_local
                        )
                    ]
                )
            ]
        )

    def applicant_address(self, number: int | str, main_poland: bool = True, main_foreign: bool = True, contact_poland: bool = True, contact_foreign: bool = True, is_local: bool = False):
        return self.create_full_address_section(
            name="applicant",
            who='Wnioskodawcy',
            number=number,
            main_poland=main_poland,
            main_foreign=main_foreign,
            contact_poland=contact_poland,
            contact_foreign=contact_foreign,
            is_local=is_local
        )

    def applicant_identification_data(self, number: int | str):
        return self.create_chapter(
            title=f"{number}. Dane identyfikacyjne",
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
                    name="applicantRegon",
                    required=True,
                    validators=[
                        self.validator.regon_validator()
                    ]
                )
            ]
        )

    def applicant_bank_data(self, number: int | str, poland: bool = True, foreign: bool = True):
        chapter = self.create_chapter(
            title=f"{number}. Nazwa i numer rachunku bankowego"
        )

        if poland:
            chapter["components"].append(
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="applicantResidence",
                            values=[
                                "w Polsce"
                            ]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Nazwa banku",
                            name="applicantBank",
                            required=True,
                            validators=[
                                self.validator.related_required_if_equal_validator(
                                    field_name="applicantResidence",
                                    value="w Polsce"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            mask="bankAccount",
                            label="Numer konta bankowego",
                            name="applicantBankAccountNum",
                            validators=[
                                self.validator.length_validator(
                                    min_value=26,
                                    max_value=26
                                ),
                                self.validator.related_required_if_equal_validator(
                                    field_name="applicantResidence",
                                    value="w Polsce"
                                )
                            ],
                            required=True
                        )
                    ]
                )
            )
        if foreign:
            chapter["components"].append(
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="applicantResidence",
                            values=[
                                "za granicą"
                            ]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Nazwa banku",
                            name="applicantForeignBank",
                            required=True,
                            validators=[
                                self.validator.related_required_if_equal_validator(
                                    field_name="applicantResidence",
                                    value="za granicą"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Międzynarodowy Numer Rachunku Bankowego (IBAN)",
                            name="applicantIban",
                            mask="ibanAccount",
                            required=True,
                            validators=[
                                self.validator.iban_validator(),
                                self.validator.related_required_if_equal_validator(
                                    field_name="applicantResidence",
                                    value="za granicą"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Kod SWIFT banku",
                            name="applicantForeignBankSwift",
                            validators=[
                                self.validator.swift_validator(),
                                self.validator.related_required_if_equal_validator(
                                    field_name="applicantResidence",
                                    value="za granicą"
                                )
                            ],
                            required=True
                        )
                    ]
                )
            )

        return chapter

    def applicant_legal_information(self, number: int | str):
        return self.create_chapter(
            title=f"{number}. Informacje prawne",
            components=[
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
                                "Placówka dyplomatyczna",
                                "Instytut Polski",
                                "Inna (np. spółka w organizacji)"
                            ],
                            required=True,
                            help_text="Wybierz formę organizacyjno-prawną wnioskodawcy."
                        )
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
                self.create_chapter(
                    title="Numer właściwego rejestru",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="select",
                                    label="Typ rejestru",
                                    name="registrationType",
                                    options=[
                                        "KRS",
                                        "Ewidencja działalności gospodarczej",
                                        "Rejestr Instytucji Filmowych",
                                        "Rejestr Instytucji Kultury",
                                        "Inny"
                                    ],
                                    help_text="Wskaż rejestr, w którym Wnioskodawca został zarejestrowany.",
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="registrationType",
                                    values=[
                                        "KRS",
                                        "Rejestr Instytucji Filmowych",
                                        "Rejestr Instytucji Kultury",
                                        "Inny"
                                    ]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="Numer rejestru",
                                    name="registrationNumber",
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="registrationType",
                                    values=[
                                        "Inny"
                                    ]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="Nazwa rejestru",
                                    name="registrationName",
                                    help_text="Podaj nazwę rejestru, w którym Wnioskodawca został zarejestrowany.",
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="registrationType",
                                    values=[
                                        "Rejestr Instytucji Filmowych",
                                        "Rejestr Instytucji Kultury",
                                        "Inny"
                                    ]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="Prowadzony przez",
                                    name="registrationAuthority",
                                    help_text="Podaj nazwę podmiotu, który odpowiada za prowadzenie wskazanego rejestru.",
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="registrationType",
                                    values=[
                                        "Ewidencja działalności gospodarczej"
                                    ]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="Numer PESEL",
                                    name="applicantPeselNum",
                                    validators=[
                                        self.validator.pesel_validator(),
                                    ],
                                    required=True
                                )
                            ]
                        )
                    ]
                )
            ]
        )

    def applicant_statistical_data(self, number: int | str):
        return self.create_chapter(
            title=f"{number}. Dane statystyczne",
            components=[
                self.create_chapter(
                    title="Przypisanie formy prawnej beneficjenta dla potrzeb statystycznych PUP",
                    components=[
                        self.create_component(
                            component_type="radio",
                            label="Forma prawna",
                            name="legalFormStats",
                            options=[
                                "przedsiębiorstwo państwowe",
                                "jednoosobowa spółka Skarbu Państwa",
                                "jednoosobowa spółka jednostki samorządu terytorialnego, w rozumieniu przepisów o gospodarce komunalnej",
                                "spółka akcyjna albo spółka z o.o., jeżeli Skarb Państwa albo jednostka samorządu terytorialnego albo przedsiębiorstwo państwowe albo jednoosobowa spółka Skarbu Państwa mają wobec nich uprawnienia jak przedsiębiorca dominujący w rozumieniu przepisów o ochronie konkurencji i konsumentów",
                                "jednostka sektora finansów publicznych w rozumieniu przepisów ustawy z dnia 27 sierpnia 2009 r. o finansach publicznych (Dz. U. z 2013 r. poz. 885, z późn. zm.)",
                                "pozostali, którzy nie mieszczą się w klasyfikacji 1.A, 1.B, 1.C ani 1.D"
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Kod formy prawnej",
                            name="legalFormCode",
                            read_only=True,
                            calculation_rules=[
                                {
                                    "name": "assignValue",
                                    "kwargs": {
                                        "options": [
                                            {
                                                "fieldName": "legalFormStats",
                                                "value": "przedsiębiorstwo państwowe",
                                                "inputValue": "1.A"
                                            },
                                            {
                                                "fieldName": "legalFormStats",
                                                "value": "jednoosobowa spółka Skarbu Państwa",
                                                "inputValue": "1.B"
                                            },
                                            {
                                                "fieldName": "legalFormStats",
                                                "value": "jednoosobowa spółka jednostki samorządu terytorialnego, w rozumieniu przepisów o gospodarce komunalnej",
                                                "inputValue": "1.C"
                                            },
                                            {
                                                "fieldName": "legalFormStats",
                                                "value": "spółka akcyjna albo spółka z o.o., jeżeli Skarb Państwa albo jednostka samorządu terytorialnego albo przedsiębiorstwo państwowe albo jednoosobowa spółka Skarbu Państwa mają wobec nich uprawnienia jak przedsiębiorca dominujący w rozumieniu przepisów o ochronie konkurencji i konsumentów",
                                                "inputValue": "1.D"
                                            },
                                            {
                                                "fieldName": "legalFormStats",
                                                "value": "jednostka sektora finansów publicznych w rozumieniu przepisów ustawy z dnia 27 sierpnia 2009 r. o finansach publicznych (Dz. U. z 2013 r. poz. 885, z późn. zm.)",
                                                "inputValue": "1.E"
                                            },
                                            {
                                                "fieldName": "legalFormStats",
                                                "value": "pozostali, którzy nie mieszczą się w klasyfikacji 1.A, 1.B, 1.C ani 1.D",
                                                "inputValue": "2"
                                            }
                                        ]
                                    }
                                }
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Określenie wielkości wnioskodawcy dla potrzeb statystycznych PUP",
                    components=[
                        self.create_component(
                            component_type="select",
                            label="Wielkość wnioskodawcy",
                            name="applicantSize",
                            options=[
                                "mikroprzedsiębiorca (zatrudnia mniej niż 10 pracowników, a roczny obrót i/lub całkowity bilans roczny nie przekracza 2 milionów EUR)",
                                "mały przedsiębiorca (zatrudnia mniej niż 50 pracowników, a roczny obrót i/lub całkowity bilans roczny nie przekracza 10 milionów EUR)",
                                "średni przedsiębiorca (zatrudnia mniej niż 250 pracowników, a roczny obrót i/lub całkowity bilans roczny nie przekracza 50 milionów EUR)",
                                "inny przedsiębiorca"
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Kod wielkości wnioskodawcy",
                            name="applicantSizeCode",
                            read_only=True,
                            calculation_rules=[
                                {
                                    "name": "assignValue",
                                    "kwargs": {
                                        "options": [
                                            {
                                                "fieldName": "applicantSize",
                                                "value": "mikroprzedsiębiorca (zatrudnia mniej niż 10 pracowników, a roczny obrót i/lub całkowity bilans roczny nie przekracza 2 milionów EUR)",
                                                "inputValue": "0"
                                            },
                                            {
                                                "fieldName": "applicantSize",
                                                "value": "mały przedsiębiorca (zatrudnia mniej niż 50 pracowników, a roczny obrót i/lub całkowity bilans roczny nie przekracza 10 milionów EUR)",
                                                "inputValue": "1"
                                            },
                                            {
                                                "fieldName": "applicantSize",
                                                "value": "średni przedsiębiorca (zatrudnia mniej niż 250 pracowników, a roczny obrót i/lub całkowity bilans roczny nie przekracza 50 milionów EUR)",
                                                "inputValue": "2"
                                            },
                                            {
                                                "fieldName": "applicantSize",
                                                "value": "inny przedsiębiorca",
                                                "inputValue": "3"
                                            }
                                        ]
                                    }
                                }
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Sposób wykorzystania dofinansowania oraz rodzaj jednostki, której przekazywane są środki",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="select",
                                    label="Cel dofinansowania",
                                    name="applicationGrantUsage",
                                    options=[
                                        "Wnioskowane dofinansowanie zostanie wykorzystane na realizację przedsięwzięć bieżących",
                                        "Wnioskowane dofinansowanie zostanie wykorzystane na finansowanie lub dofinansowanie kosztów realizacji inwestycji i zakupów inwestycyjnych"
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="select",
                                    label="Rodzaj jednostki",
                                    name="applicationGrantUsageTargetEntity",
                                    options=[
                                        "Dla jednostek zaliczanych do sektora finansów publicznych wymienionych w art. 9 Ustawy o finansach publicznych",
                                        "Dla jednostek niezaliczanych do sektora finansów publicznych"
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="applicationGrantUsageTargetEntity",
                                    values=[
                                        "Dla jednostek zaliczanych do sektora finansów publicznych wymienionych w art. 9 Ustawy o finansach publicznych"
                                    ]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="select",
                                    label="Rodzaj podmiotu",
                                    name="applicationGrantUsageTargetEntityType",
                                    options=[
                                        "Organy władzy publicznej, w tym organy administracji rządowej, organy kontroli państwowej i ochrony prawa oraz sądy i trybunały",
                                        "Jednostki samorządu terytorialnego oraz ich związki",
                                        "Jednostki budżetowe",
                                        "Samorządowe zakłady budżetowe",
                                        "Agencje wykonawcze",
                                        "Instytucja gospodarki budżetowej",
                                        "Państwowe fundusze celowe",
                                        "Zakład Ubezpieczeń Społecznych i zarządzane przez niego fundusze oraz Kasa Rolniczego Ubezpieczenia społecznego i fundusze zarządzane przez Prezesa Kasy Rolniczego Ubezpieczenia Społecznego",
                                        "Narodowy Fundusz Zdrowia",
                                        "Samodzielna publiczne zakłady opieki zdrowotnej",
                                        "Uczelnie publiczne",
                                        "Polska Akademia Nauk i tworzone przez nią jednostki organizacyjne",
                                        "Państwowe samorządowe instytucje kultury oraz państwowe instytucje filmowe",
                                        "Inne państwowe lub samorządowe osoby prawne utworzone na podstawie odrębnych ustaw w celu wykonywania przedsięwzięć publicznych, z wyłączeniem przedsiębiorstw, instytutów badawczych, banku w I spółek prawa handlowego"
                                    ],
                                    required=True
                                )
                            ]
                        )
                    ]
                )
            ]
        )
