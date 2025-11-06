from classes_new.form_builder.form_builder import ApplicationFormBuilder


class SimpleValidatorsApplicationFormBuilder(ApplicationFormBuilder):
    def __init__(self):
        super().__init__(
            custom_dir_name="test/simple_validators",
            custom_file_name="simple_validators"
        )

        self.form_id = self.set_ids(
            local_id=16421,
            uat_id=None
        )

        self.parts = [
            self.create_simple_validators
        ]

        """
        Simple validators:
        
        [x] RequiredValidator
        [x] ExactValidator
        [x] LengthValidator
        [x] RangeValidator
        [x] ZipCodeValidator
        [x] PhoneNumberValidator
        [x] LandlineValidator
        [x] EmailValidator
        [x] KRSValidator
        [x] PeselValidator
        [x] IBANValidator
        [x] RegonValidator
        [x] SwiftValidator
        """

    def create_simple_validators(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Simple validators",
            short_name=f"{self.helpers.int_to_roman(number)}. Simple validators",
            chapters=[
                self.create_chapter(
                    title="RequiredValidator",
                    help_text="Walidator sprawdza, czy pole jest uzupełnione.",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"]
                    },
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            name="requiredValidatorCheckbox",
                            label="Checkbox",
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            name="requiredValidatorText",
                            label="Text",
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="ExactValidator",
                    help_text="Walidator sprawdza, czy jest wybrana poprawna wartość z listy wartości.",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"]
                    },
                    components=[
                        self.create_component(
                            component_type="select",
                            name="exactValidatorSelect",
                            label="Select",
                            options=[
                                "Opcja 1",
                                "Opcja 2",
                                "Opcja 3"
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="LengthValidator",
                    help_text="Walidator sprawdza, czy długość tekstu jest w danym zakresie.",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"]
                    },
                    components=[
                        self.create_component(
                            component_type="textarea",
                            label="Min 10",
                            name="lengthValidatorMin",
                            validators=[
                                self.validator.length_validator(min_value=10)
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Max 10",
                            name="lengthValidatorMax",
                            validators=[
                                self.validator.length_validator(max_value=10)
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Min 10 - Max 20",
                            name="lengthValidatorMinMax",
                            validators=[
                                self.validator.length_validator(
                                    min_value=10,
                                    max_value=20
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="RangeValidator",
                    help_text="Walidator sprawdza, czy wartość jest w danym zakresie.",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"]
                    },
                    components=[
                        self.create_component(
                            component_type="number",
                            label="Min 10",
                            name="rangeValidatorMin",
                            validators=[
                                self.validator.range_validator(min_value=10)
                            ]
                        ),
                        self.create_component(
                            component_type="number",
                            label="Max 10",
                            name="rangeValidatorMax",
                            validators=[
                                self.validator.range_validator(max_value=10)
                            ]
                        ),
                        self.create_component(
                            component_type="number",
                            label="Min 10 - Max 20",
                            name="rangeValidatorMinMax",
                            validators=[
                                self.validator.range_validator(
                                    min_value=10,
                                    max_value=20
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"]
                    },
                    components=[
                        self.create_chapter(
                            title="ZipCodeValidator",
                            help_text="Walidator sprawdza, czy podany kod pocztowy jest poprawny.",
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="Zip code",
                                    name="zipCodeValidator",
                                    mask="polishPostalCode",
                                    validators=[
                                        self.validator.zip_code_validator()
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="PhoneNumberValidator",
                            help_text="Walidator sprawdza, czy podany numer telefonu jest poprawny.",
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="Phone number",
                                    mask="phoneNumber",
                                    name="phoneNumberValidator",
                                    validators=[
                                        self.validator.phone_number_validator()
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="LandlineValidator",
                            help_text="Walidator sprawdza, czy podany numer telefonu stacjonarnego jest poprawny.",
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="Landline",
                                    mask="landline",
                                    name="landlineValidator",
                                    validators=[
                                        self.validator.landline_validator()
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="EmailValidator",
                            help_text="Walidator sprawdza, czy podany adres email jest poprawny.",
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="Email",
                                    name="emailValidator",
                                    validators=[
                                        self.validator.email_validator()
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="KRSValidator",
                            help_text="Walidator sprawdza, czy podany numer KRS jest poprawny.",
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="KRS",
                                    name="krsValidator",
                                    validators=[
                                        self.validator.krs_validator()
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="PeselValidator",
                            help_text="Walidator sprawdza, czy podany numer PESEL jest poprawny.",
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="Pesel",
                                    name="peselValidator",
                                    validators=[
                                        self.validator.pesel_validator()
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="IBANValidator",
                            help_text="Walidator sprawdza, czy podany identyfikator IBAN jest poprawny.",
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="IBAN",
                                    name="ibanValidator",
                                    validators=[
                                        self.validator.iban_validator()
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="RegonValidator",
                            help_text="Walidator sprawdza, czy podany numer REGON jest poprawny.",
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="REGON",
                                    name="regonValidator",
                                    validators=[
                                        self.validator.regon_validator()
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="SwiftValidator",
                            help_text="Walidator sprawdza, czy podany identyfikator SWIFT jest poprawny.",
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="SWIFT",
                                    name="swiftValidator",
                                    validators=[
                                        self.validator.swift_validator()
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )

        self.save_part(part)
