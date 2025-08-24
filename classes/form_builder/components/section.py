from classes.form_builder.form_builder_base import FormBuilderBase
from classes.form_builder.components.component import Component


class Section(FormBuilderBase):
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

    def eligible_person_data(self, number: int | str):
        return self.create_chapter(
            title=f"{number}. Osoby upoważnione do reprezentowania wnioskodawcy, składania oświadczeń woli i zaciągania w jego imieniu zobowiązań finansowych",
            is_multiple_forms=True,
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
                            label="Stanowisko zgodnie z reprezentacją/ załączonym upoważnieniem",
                            name="eligiblePersonPosition",
                            required=True
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
                            label="Email",
                            name="eligiblePersonEmail",
                            required=True,
                            validators=[
                                self.validator.email_validator()
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

    def applicant_address_base(self, build_name: str = '', poland: bool = True, foreign: bool = True):
        chapters = []
        if poland:
            chapters.append(
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name=f"applicant{build_name}Residence",
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
                            name=f"applicant{build_name}Voivodeship",
                            required_if_name=f"applicant{build_name}Residence",
                            required_if_value="w Polsce"
                        ),
                        self.create_component(
                            component_type="text",
                            label="Powiat",
                            name=f"applicant{build_name}County",
                            required=True,
                            validators=[
                                self.validator.related_required_if_equal_validator(
                                    field_name=f"applicant{build_name}Residence",
                                    value="w Polsce"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Miejscowość",
                            name=f"applicant{build_name}Location",
                            required=True,
                            validators=[
                                self.validator.related_required_if_equal_validator(
                                    field_name=f"applicant{build_name}Residence",
                                    value="w Polsce"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Gmina",
                            name=f"applicant{build_name}Municipality",
                            required=True,
                            validators=[
                                self.validator.related_required_if_equal_validator(
                                    field_name=f"applicant{build_name}Residence",
                                    value="w Polsce"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Ulica",
                            name=f"applicant{build_name}Street",
                            required=True,
                            validators=[
                                self.validator.related_required_if_equal_validator(
                                    field_name=f"applicant{build_name}Residence",
                                    value="w Polsce"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Numer domu",
                            name=f"applicant{build_name}HouseNum",
                            required=True,
                            validators=[
                                self.validator.related_required_if_equal_validator(
                                    field_name=f"applicant{build_name}Residence",
                                    value="w Polsce"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Numer lokalu",
                            name=f"applicant{build_name}ApartmentNum"
                        ),
                        self.create_component(
                            component_type="text",
                            label="Kod pocztowy",
                            name=f"applicant{build_name}ZipCode",
                            required=True,
                            validators=[
                                self.validator.related_required_if_equal_validator(
                                    field_name=f"applicant{build_name}Residence",
                                    value="w Polsce"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Poczta",
                            name=f"applicant{build_name}PostOffice",
                            required=True,
                            validators=[
                                self.validator.related_required_if_equal_validator(
                                    field_name=f"applicant{build_name}Residence",
                                    value="w Polsce"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            mask="phoneNumber",
                            label="Numer telefonu",
                            name=f"applicant{build_name}PhoneNum",
                            required=True,
                            validators=[
                                self.validator.related_required_if_equal_validator(
                                    field_name=f"applicant{build_name}Residence",
                                    value="w Polsce"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Email kontaktowy",
                            name=f"applicant{build_name}Email",
                            required=True,
                            validators=[
                                self.validator.email_validator(),
                                self.validator.related_required_if_equal_validator(
                                    field_name=f"applicant{build_name}Residence",
                                    value="w Polsce"
                                )
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
                            field_name=f"applicant{build_name}Residence",
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
                            component_type="text",
                            label="Kraj",
                            name=f"applicant{build_name}Country",
                            required=True,
                            validators=[
                                self.validator.related_required_if_equal_validator(
                                    field_name=f"applicant{build_name}Residence",
                                    value="za granicą"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Miejscowość",
                            name=f"applicant{build_name}ForeignLocation",
                            required=True,
                            validators=[
                                self.validator.related_required_if_equal_validator(
                                    field_name=f"applicant{build_name}Residence",
                                    value="za granicą"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Ulica",
                            name=f"applicant{build_name}ForeignStreet",
                            required=True,
                            validators=[
                                self.validator.related_required_if_equal_validator(
                                    field_name=f"applicant{build_name}Residence",
                                    value="za granicą"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Numer domu",
                            name=f"applicant{build_name}ForeignHouseNum",
                            required=True,
                            validators=[
                                self.validator.related_required_if_equal_validator(
                                    field_name=f"applicant{build_name}Residence",
                                    value="za granicą"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Numer lokalu",
                            name=f"applicant{build_name}ForeignApartmentNum"
                        ),
                        self.create_component(
                            component_type="text",
                            label="Kod pocztowy",
                            name=f"applicant{build_name}ForeignZipCode",
                            required=True,
                            validators=[
                                self.validator.related_required_if_equal_validator(
                                    field_name=f"applicant{build_name}Residence",
                                    value="za granicą"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Poczta",
                            name=f"applicant{build_name}ForeignPostOffice"
                        ),
                        self.create_component(
                            component_type="text",
                            mask="phoneNumber",
                            label="Numer telefonu",
                            name=f"applicant{build_name}ForeignPhoneNum",
                            required=True,
                            validators=[
                                self.validator.related_required_if_equal_validator(
                                    field_name=f"applicant{build_name}Residence",
                                    value="za granicą"
                                )
                            ]

                        ),
                        self.create_component(
                            component_type="text",
                            label="Email kontaktowy",
                            name=f"applicant{build_name}ForeignEmail",
                            validators=[
                                self.validator.email_validator(),
                                self.validator.related_required_if_equal_validator(
                                    field_name=f"applicant{build_name}Residence",
                                    value="za granicą"
                                )
                            ],
                            required=True
                        )
                    ]
                )
            )
        return chapters

    def applicant_address(self, number: int | str, poland: bool = True, foreign: bool = True):
        return self.create_chapter(
            title=f"{number}. Adres i dane wnioskodawcy",
            components=[
                self.create_chapter(
                    title=f"{number}a. Adres siedziby",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    name="applicantResidence",
                                    value="" if poland and foreign else "w Polsce" if poland else "za granicą",
                                    options=["w Polsce", "za granicą"] if poland and foreign else ["w Polsce"] if poland else ["za granicą"],
                                    read_only=False if poland and foreign else True,
                                    required=True
                                )
                            ]
                        ),
                        *self.applicant_address_base(
                            poland=poland,
                            foreign=foreign,
                        )
                    ]
                ),
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Należy zaznaczyć jeśli adres korespondencyjny jest inny",
                            name="applicantHasDifferentContactAddress"
                        )
                    ]
                ),
                self.create_chapter(
                    title=f"{number}b. Adres korespondencyjny",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    name="applicantContactResidence",
                                    value="" if poland and foreign else "w Polsce" if poland else "za granicą",
                                    options=["w Polsce", "za granicą"] if poland and foreign else ["w Polsce"] if poland else ["za granicą"],
                                    read_only=False if poland and foreign else True,
                                    required=True
                                )
                            ]
                        ),
                        *self.applicant_address_base(
                            build_name="Contact",
                            poland=poland,
                            foreign=foreign,
                        )
                    ]
                )
            ]
        )
