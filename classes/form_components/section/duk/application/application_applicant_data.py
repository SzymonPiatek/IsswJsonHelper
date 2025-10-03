from classes.form_components.section.section import Section


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
