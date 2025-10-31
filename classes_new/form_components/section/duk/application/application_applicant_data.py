from classes_new.form_components.section.section import Section


class ApplicationApplicantData(Section):
    def __init__(self):
        super().__init__()

    def create_address_base(self, start_name: str, build_name: str = '', poland: bool = True, foreign: bool = True):
        chapters = []

        if poland:
            chapters.append(
                self.create_chapter(
                    visibility_rules=[
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
                        ),
                        self.create_component(
                            component_type="text",
                            label="Adres do doreczeń elektronicznych",
                            name=f"{start_name}{build_name}ElectronicDeliveriesAddress",
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
                        ),
                        self.create_component(
                            component_type="text",
                            label="Adres do doreczeń elektronicznych",
                            name=f"{start_name}{build_name}ForeignElectronicDeliveriesAddress",
                            required=True,
                            validators=[
                                self.validator.email_validator()
                            ]
                        )
                    ]
                )
            )

        return chapters

    def applicant_statistical_data(
            self,
            number: int | str
    ):
        return self.create_chapter(
            title=f"{number}. Dane statystyczne",
            components=[
                self.create_chapter(
                    title="Identyfikator gminy (Kod JST)",
                    help_text="Kod JST gminy można znaleźć w wyszukiwarce pod adresem https://eteryt.stat.gov.pl",
                    components=[
                        self.create_component(
                            component_type="text",
                            name="applicantJst",
                            mask="jst",
                            required=True,
                            validators=[
                                self.validator.length_validator(
                                    min_value=7,
                                    max_value=7
                                )
                            ]
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
                self.create_chapter(
                    title="Przypisanie formy prawnej Wnioskodawcy dla potrzeb statystycznych PUP",
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
                    title="Określenie wielkości Wnioskodawcy dla potrzeb statystycznych PUP",
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
