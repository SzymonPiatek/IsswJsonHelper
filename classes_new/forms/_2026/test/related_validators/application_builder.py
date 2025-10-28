from classes_new.form_builder.form_builder import ApplicationFormBuilder


class RelatedValidatorsApplicationFormBuilder(ApplicationFormBuilder):
    def __init__(self):
        super().__init__(
            custom_dir_name="test/related_validators",
            custom_file_name="related_validators"
        )

        self.form_id = self.set_ids(
            local_id=32,
            uat_id=None
        )

        self.parts = [
            self.create_related_equality_validator,
            self.create_related_local_equality_validator,
            self.create_related_numeric_equality_validator,
            self.create_related_required_if_equal_validator,
            self.create_related_date_lte_validator,
            self.create_related_local_date_lte_validator,
            self.create_related_date_gte_validator,
            self.create_related_local_date_gte_validator,
            self.create_related_date_offset_validator,
            self.create_related_date_increment_validator,
            self.create_related_sum_validator,
            self.create_related_multiplication_validator,
            self.create_related_local_multiplication_validator,
            self.create_related_share_validator,
            self.create_related_local_division_validator,
            self.create_related_map_validator,
            self.create_related_boolean_sum_validator,
            self.create_related_sum_of_weights_validator,
            self.create_related_equal_if_in_range_validator,
            self.create_related_empty_if_validator,
            self.create_related_fraction_validator,
            self.create_related_gte_fraction_validator,
            self.create_related_lte_fraction_validator,
            self.create_related_local_sum_validator,
            self.create_related_any_of_validator,
            self.create_related_mapped_limit_validator,
            self.create_related_allowed_options_validator,
            self.create_related_unique_value_validator,

            self.create_related_last_date_validator
        ]

        """
        Related validators:
        
        [x] RelatedEqualityValidator
        [x] RelatedLocalEqualityValidator
        [x] RelatedNumericEqualityValidator
        [x] RelatedRequiredIfEqualValidator
        [x] RelatedDateLTEValidator
        [x] RelatedLocalDateLTEValidator
        [x] RelatedDateGTEValidator
        [x] RelatedLocalDateGTEValidator
        [x] RelatedDateOffsetValidator
        [x] RelatedDateIncrementValidator
        [x] RelatedSumValidator
        [x] RelatedMultiplicationValidator
        [x] RelatedLocalMultiplicationValidator
        [x] RelatedShareValidator
        [x] RelatedLocalDivisionValidator
        [x] RelatedMapValidator
        [x] RelatedBooleanSumValidator
        [x] RelatedSumOfWeightsValidator
        [x] RelatedEqualIfInRangeValidator
        [x] RelatedEmptyIfValidator
        [x] RelatedFractionValidator
        [x] RelatedFractionGTEValidator
        [x] RelatedFractionLTEValidator
        [x] RelatedLocalSumValidator
        [x] RelatedAnyOfValidator
        [x] RelatedMappedLimitValidator
        [x] RelatedAllowedOptionsValidator
        [x] RelatedUniqueValueValidator
        [ ] RelatedConditionRatioValidator
        [ ] RelatedConditionRangeValidator
        [x] RelatedLastDateValidator
        """

    def create_related_equality_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedEqualityValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Equality Validator",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="relatedEqualityValidator",
                            value="Walidator sprawdza, czy wartości są sobie równe."
                        )
                    ]
                ),
                self.create_chapter(
                    title="Text to text",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"]
                    },
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Value 1",
                            name="firstText"
                        ),
                        self.create_component(
                            component_type="text",
                            label="Value 2",
                            name="secondText",
                            validators=[
                                self.validator.related_equality_validator(
                                    field_name="firstText"
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Number to number",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"]
                    },
                    components=[
                        self.create_component(
                            component_type="number",
                            label="Value 1",
                            name="firstNumber"
                        ),
                        self.create_component(
                            component_type="number",
                            label="Value 2",
                            name="secondNumber",
                            validators=[
                                self.validator.related_equality_validator(
                                    field_name="firstNumber"
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Boolean to boolean",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"]
                    },
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Value 1",
                            name="firstBoolean"
                        ),
                        self.create_component(
                            component_type="checkbox",
                            label="Value 2",
                            name="secondBoolean",
                            validators=[
                                self.validator.related_equality_validator(
                                    field_name="firstBoolean"
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Text (fund) to number",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"]
                    },
                    components=[
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="Value 1",
                            name="firstTextNumber"
                        ),
                        self.create_component(
                            component_type="number",
                            label="Value 2",
                            name="secondTextNumber",
                            validators=[
                                self.validator.related_equality_validator(
                                    field_name="firstTextNumber"
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        self.save_part(part)

    def create_related_local_equality_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedLocalEqualityValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Local Equality Validator",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="relatedLocalEqualityValidator",
                            value="Walidator sprawdza, czy wartości lokalne są sobie równe."
                        )
                    ]
                ),
                self.create_chapter(
                    title="Text to text",
                    components=[
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 2,
                                "maxCount": 10
                            },
                            components=[
                                self.create_chapter(
                                    title="Pozycja",
                                    class_list={
                                        "main": ["table-1-2"],
                                        "sub": ["table-1-2__col"]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            label="Value 1",
                                            name="firstTextLocal"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Value 2",
                                            name="secondTextLocal",
                                            validators=[
                                                self.validator.related_local_equality_validator(
                                                    field_name="firstTextLocal"
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
                    title="Number to number",
                    components=[
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 2,
                                "maxCount": 10
                            },
                            components=[
                                self.create_chapter(
                                    title="Pozycja",
                                    class_list={
                                        "main": ["table-1-2"],
                                        "sub": ["table-1-2__col"]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="number",
                                            label="Value 1",
                                            name="firstNumberLocal"
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Value 2",
                                            name="secondNumberLocal",
                                            validators=[
                                                self.validator.related_local_equality_validator(
                                                    field_name="firstNumberLocal"
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
                    title="Boolean to boolean",
                    components=[
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 2,
                                "maxCount": 10
                            },
                            components=[
                                self.create_chapter(
                                    title="Pozycja",
                                    class_list={
                                        "main": ["table-1-2"],
                                        "sub": ["table-1-2__col"]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="checkbox",
                                            label="Value 1",
                                            name="firstBooleanLocal"
                                        ),
                                        self.create_component(
                                            component_type="checkbox",
                                            label="Value 2",
                                            name="secondBooleanLocal",
                                            validators=[
                                                self.validator.related_local_equality_validator(
                                                    field_name="firstBooleanLocal"
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
                    title="Text (fund) to number",
                    components=[
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 2,
                                "maxCount": 10
                            },
                            components=[
                                self.create_chapter(
                                    title="Pozycja",
                                    class_list={
                                        "main": ["table-1-2"],
                                        "sub": ["table-1-2__col"]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Value 1",
                                            name="firstTextNumberLocal"
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Value 2",
                                            name="secondTextNumberLocal",
                                            validators=[
                                                self.validator.related_local_equality_validator(
                                                    field_name="firstTextNumberLocal"
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
        self.save_part(part)

    def create_related_numeric_equality_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedNumericEqualityValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Numeric Equality Validator",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="relatedNumericEqualityValidator",
                            value="Walidator sprawdza, czy wartości numeryczne są sobie równe."
                        )
                    ]
                ),
                self.create_chapter(
                    title="Number to number",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"]
                    },
                    components=[
                        self.create_component(
                            component_type="number",
                            label="Value 1",
                            name="numberNumeric",
                            default_value=0
                        ),
                        self.create_component(
                            component_type="number",
                            label="Value 2",
                            name="secondNumberNumeric",
                            validators=[
                                self.validator.related_numeric_equality_validator(
                                    field_name="numberNumeric"
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Text to number",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"]
                    },
                    components=[
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="Value 1",
                            name="textNumberNumeric"
                        ),
                        self.create_component(
                            component_type="number",
                            label="Value 2",
                            name="secondTextNumberNumeric",
                            validators=[
                                self.validator.related_numeric_equality_validator(
                                    field_name="textNumberNumeric"
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Text to text",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"]
                    },
                    components=[
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="Value 1",
                            name="textNumeric"
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="Value 2",
                            name="secondTextNumeric",
                            validators=[
                                self.validator.related_numeric_equality_validator(
                                    field_name="textNumeric"
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        self.save_part(part)

    def create_related_required_if_equal_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedRequiredIfEqualValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Required If Equal Validator",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="relatedRequiredIfEqualValidator",
                            value="Walidator sprawdza, czy pole jest obowiązkowe po spełnieniu warunku."
                        )
                    ]
                ),
                self.create_chapter(
                    title="Test",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    label="Pytanie?",
                                    name="question",
                                    options=[
                                        "Tak",
                                        "Nie"
                                    ],
                                    class_list=[
                                        "table-full"
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            class_list={
                                "main": ["table-1-2"],
                                "sub": ["table-1-2__col"],
                            },
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="Required - Tak",
                                    name="questionYes",
                                    read_only=True,
                                    validators=[
                                        self.validator.related_required_if_equal_validator(
                                            field_name="question",
                                            value="Tak"
                                        )
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Required - Nie",
                                    name="questionNo",
                                    read_only=True,
                                    validators=[
                                        self.validator.related_required_if_equal_validator(
                                            field_name="question",
                                            value="Nie"
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

    def create_related_date_lte_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedDateLTEValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Date LTE Validator",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="relatedDateLTEValidator",
                            value="Walidator sprawdza, czy data jest mniejsza lub równa dacie z danego pola."
                        )
                    ]
                ),
                self.create_chapter(
                    title="Test",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="date",
                            label="Data od",
                            name="startDate",
                            validators=[
                                self.validator.related_date_lte_validator(
                                    field_name="endDate"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="date",
                            label="Data do",
                            name="endDate"
                        )
                    ]
                )
            ]
        )
        self.save_part(part)

    def create_related_local_date_lte_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedLocalDateLTEValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Local Date LTE Validator",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="relatedLocalDateLTEValidator",
                            value="Walidator sprawdza, czy data jest mniejsza lub równa dacie z danego pola - lokalnie."
                        )
                    ]
                ),
                self.create_chapter(
                    title="Test",
                    components=[
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 2,
                                "maxCount": 10
                            },
                            components=[
                                self.create_chapter(
                                    title="Zakres dat",
                                    class_list={
                                        "main": ["table-1-2"],
                                        "sub": ["table-1-2__col"],
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="date",
                                            label="Data od",
                                            name="startDateLocal",
                                            validators=[
                                                self.validator.related_local_date_lte_validator(
                                                    field_name="endDateLocal"
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="date",
                                            label="Data do",
                                            name="endDateLocal"
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

    def create_related_date_gte_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedDateGTEValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Date GTE Validator",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="relatedDateGTEValidator",
                            value="Walidator sprawdza, czy data jest większa lub równa dacie z danego pola."
                        )
                    ]
                ),
                self.create_chapter(
                    title="Test",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="date",
                            label="Data od",
                            name="startDateGte"
                        ),
                        self.create_component(
                            component_type="date",
                            label="Data do",
                            name="endDateGte",
                            validators=[
                                self.validator.related_date_gte_validator(
                                    field_name="startDateGte"
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        self.save_part(part)

    def create_related_local_date_gte_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedLocalDateGTEValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Local Date GTE Validator",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="relatedLocalDateGTEValidator",
                            value="Walidator sprawdza, czy data jest większa lub równa dacie z danego pola - lokalnie."
                        )
                    ]
                ),
                self.create_chapter(
                    title="Test",
                    components=[
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 2,
                                "maxCount": 10
                            },
                            components=[
                                self.create_chapter(
                                    title="Zakres dat",
                                    class_list={
                                        "main": ["table-1-2"],
                                        "sub": ["table-1-2__col"],
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="date",
                                            label="Data od",
                                            name="startDateLocalGte"
                                        ),
                                        self.create_component(
                                            component_type="date",
                                            label="Data do",
                                            name="endDateLocalGte",
                                            validators=[
                                                self.validator.related_local_date_gte_validator(
                                                    field_name="startDateLocalGte"
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
        self.save_part(part)

    def create_related_date_offset_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedDateOffsetValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Date Offset Validator",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="relatedDateOffsetValidator",
                            value="Walidator sprawdza, czy data nie jest późniejsza niż data z danego pola + offest (liczba dni)."
                        )
                    ]
                ),
                self.create_chapter(
                    title="Test (+5 dni)",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="date",
                            label="Data od",
                            name="startDateOffset"
                        ),
                        self.create_component(
                            component_type="date",
                            label="Data do",
                            name="endDateOffset",
                            validators=[
                                self.validator.related_date_offset_validator(
                                    field_name="startDateOffset",
                                    offset=5
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Test (-5 dni)",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="date",
                            label="Data od",
                            name="secondStartDateOffset"
                        ),
                        self.create_component(
                            component_type="date",
                            label="Data do",
                            name="secondEndDateOffset",
                            validators=[
                                self.validator.related_date_offset_validator(
                                    field_name="secondStartDateOffset",
                                    offset=-5
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        self.save_part(part)

    def create_related_date_increment_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedDateIncrementValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Date Increment Validator",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="relatedDateIncrementValidator",
                            value="Walidator sprawdza, czy data jest równa dacie z danego pola + amount (liczba dni)."
                        )
                    ]
                ),
                self.create_chapter(
                    title="Test (+5 dni)",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="date",
                            label="Data od",
                            name="startDateIncrement"
                        ),
                        self.create_component(
                            component_type="date",
                            label="Data do",
                            name="endDateIncrement",
                            validators=[
                                self.validator.related_date_increment_validator(
                                    field_name="startDateIncrement",
                                    amount=5
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Test (-5 dni)",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="date",
                            label="Data od",
                            name="secondStartDateIncrement"
                        ),
                        self.create_component(
                            component_type="date",
                            label="Data do",
                            name="secondEndDateIncrement",
                            validators=[
                                self.validator.related_date_increment_validator(
                                    field_name="secondStartDateIncrement",
                                    amount=-5
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        self.save_part(part)

    def create_related_sum_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedSumValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Sum Validator",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="relatedSumValidator",
                            value="Walidator sprawdza sumę danych pól."
                        )
                    ]
                ),
                self.create_chapter(
                    title="Single",
                    class_list={
                        "main": ["table-1-3-narrow"],
                        "sub": ["table-1-3__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            name="firstSum",
                            label="firstSum"
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            name="secondSum",
                            label="secondSum"
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="totalSum",
                            name="totalSum",
                            read_only=True,
                            calculation_rules=[
                                self.calculation_rule.dynamic_sum_inputs(
                                    fields=[
                                        "firstSum",
                                        "secondSum",
                                    ]
                                )
                            ],
                            validators=[
                                self.validator.related_sum_validator(
                                    field_names=[
                                        "firstSum",
                                        "secondSum",
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Mutli",
                    components=[
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 2,
                                "maxCount": 10,
                            },
                            components=[
                                self.create_chapter(
                                    title="Wartość",
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            name="firstSumMulti",
                                            label="firstSumMulti"
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Suma",
                            components=[
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    name="firstSumMultiTotal",
                                    calculation_rules=[
                                        self.calculation_rule.dynamic_sum_inputs(
                                            fields=["firstSumMulti"]
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_sum_validator(
                                            field_names=["firstSumMulti"]
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

    def create_related_multiplication_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedMultiplicationValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Multiplication Validator",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="relatedMultiplicationValidator",
                            value="Walidator sprawdza, czy poprawnie przemnożono wartości."
                        )
                    ]
                ),
                self.create_chapter(
                    title="Test",
                    class_list={
                        "main": ["table-1-3-narrow"],
                        "sub": ["table-1-3__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="number",
                            label="Liczba odcinków",
                            name="numberOfEpisodes",
                            unit="szt."
                        ),
                        self.create_component(
                            component_type="number",
                            label="Średnia liczba minut odcinka",
                            name="lengthOfEpisode",
                            unit="min."
                        ),
                        self.create_component(
                            component_type="number",
                            label="Łączna liczba minut",
                            name="multiplicationResult",
                            calculation_rules=[
                                self.calculation_rule.multiply_inputs(
                                    fields=[
                                        "numberOfEpisodes",
                                        "lengthOfEpisode",
                                    ]
                                )
                            ],
                            validators=[
                                self.validator.related_multiplication_validator(
                                    field_names=[
                                        "numberOfEpisodes",
                                        "lengthOfEpisode",
                                    ]
                                )
                            ],
                            read_only=True,
                            unit="min."
                        )
                    ]
                )
            ]
        )
        self.save_part(part)

    def create_related_local_multiplication_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedLocalMultiplicationValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Local Multiplication Validator",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="relatedLocalMultiplicationValidator",
                            value="Walidator sprawdza, czy poprawnie przemnożono wartości - lokalnie."
                        )
                    ]
                ),
                self.create_chapter(
                    multiple_forms_rules={
                        "minCount": 2,
                        "maxCount": 10,
                    },
                    components=[
                        self.create_chapter(
                            title="Sezon",
                            class_list={
                                "main": ["table-1-3-narrow"],
                                "sub": ["table-1-3__col"],
                            },
                            components=[
                                self.create_component(
                                    component_type="number",
                                    label="Liczba odcinków",
                                    name="numberOfEpisodesLocal",
                                    unit="szt."
                                ),
                                self.create_component(
                                    component_type="number",
                                    label="Średnia liczba minut odcinka",
                                    name="lengthOfEpisodeLocal",
                                    unit="min."
                                ),
                                self.create_component(
                                    component_type="number",
                                    label="Łączna liczba minut",
                                    name="multiplicationResultLocal",
                                    calculation_rules=[
                                        self.calculation_rule.local_multiply_inputs(
                                            fields=[
                                                "numberOfEpisodesLocal",
                                                "lengthOfEpisodeLocal",
                                            ]
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_local_multiplication_validator(
                                            field_names=[
                                                "numberOfEpisodesLocal",
                                                "lengthOfEpisodeLocal",
                                            ]
                                        )
                                    ],
                                    read_only=True,
                                    unit="min."
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        self.save_part(part)

    def create_related_share_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedShareValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Share Validator",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="relatedShareValidator",
                            value="Walidator sprawdza, czy poprawnie wyliczono wartość procentową."
                        )
                    ]
                ),
                self.create_chapter(
                    title="Test",
                    class_list={
                        "main": ["table-1-3-narrow"],
                        "sub": ["table-1-3__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            name="shareCostTotal"
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            name="shareCost"
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            name="shareResult",
                            calculation_rules=[
                                self.calculation_rule.share_calculator(
                                    dividend_field="shareCost",
                                    divisor_field="shareCostTotal",
                                )
                            ],
                            validators=[
                                self.validator.related_share_validator(
                                    dividend="shareCost",
                                    divisor="shareCostTotal",
                                )
                            ],
                            read_only=True,
                            unit="%"
                        )
                    ]
                )
            ]
        )
        self.save_part(part)

    def create_related_local_division_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedLocalDivisionValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Local Division Validator",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="relatedLocalDivisionValidator",
                            value="Walidator sprawdza, czy poprawnie wyliczono wartość procentową - lokalnie."
                        )
                    ]
                ),
                self.create_chapter(
                    title="Costs with shares",
                    components=[
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 3,
                                "maxCount": 20
                            },
                            components=[
                                self.create_chapter(
                                    title="Koszt",
                                    class_list={
                                        "main": [
                                            "table-1-3-narrow"
                                        ],
                                        "sub": [
                                            "table-1-3__col"
                                        ]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            name="total",
                                            label="Kwota całkowita",
                                            unit="PLN"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            name="cost",
                                            label="Kwota udziału",
                                            unit="PLN"
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            name="share",
                                            label="Udział",
                                            unit="%",
                                            read_only=True,
                                            calculation_rules=[
                                                self.calculation_rule.local_share_calculator(
                                                    dividend_field="cost",
                                                    divisor_field="total"
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_local_division_validator(
                                                    dividend="cost",
                                                    divisor="total"
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
                    title="Podsumowanie",
                    class_list={
                        "main": [
                            "table-1-3-narrow"
                        ],
                        "sub": [
                            "table-1-3__col"
                        ]
                    },
                    components=[
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            name="totalTotal",
                            label="Koszt całkowity",
                            unit="PLN",
                            value="10000",
                            read_only=True,
                            calculation_rules=[
                                self.calculation_rule.dynamic_sum_inputs(
                                    fields=["total"]
                                )
                            ],
                            validators=[
                                self.validator.related_sum_validator(
                                    field_names=["total"]
                                )
                            ],
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            name="costTotal",
                            label="Koszt udziału",
                            unit="PLN",
                            value="10000",
                            read_only=True,
                            calculation_rules=[
                                self.calculation_rule.dynamic_sum_inputs(
                                    fields=["cost"]
                                )
                            ],
                            validators=[
                                self.validator.related_sum_validator(
                                    field_names=["cost"]
                                )
                            ],
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            name="shareTotal",
                            label="Udział całkowity",
                            unit="%",
                            calculation_rules=[
                                self.calculation_rule.dynamic_sum_inputs(
                                    fields=["share"]
                                )
                            ],
                            validators=[
                                self.validator.related_sum_validator(
                                    field_names=["share"]
                                )
                            ],
                            read_only=True
                        )
                    ]
                )
            ]
        )
        self.save_part(part)

    def create_related_map_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedMapValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Map Validator",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="relatedMapValidator",
                            value="Walidator sprawdza, czy wartość pola odpowiada wartości zdefiniowanej dla wybranej opcji innego pola."
                        )
                    ]
                ),
                self.create_chapter(
                    title="Test",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="select",
                            name="relatedMapText",
                            label="Kraj",
                            options=[
                                "Polska",
                                "Niemcy"
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            name="secondRelatedMapText",
                            label="Stolica",
                            validators=[
                                self.validator.related_map_validator(
                                    field_name="relatedMapText",
                                    mapping={
                                        "Polska": "Warszawa",
                                        "Niemcy": "Berlin"
                                    }
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        self.save_part(part)

    def create_related_boolean_sum_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedBooleanSumValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Boolean Sum Validator",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="relatedBooleanSumValidator",
                            value="Walidator sprawdza, czy co najmniej jedna z badanych wartości jest prawdziwa. Jeśli tak, wymaga, aby wartość komponentu również była prawdziwa. Jeżeli natomiast żadna z badanych wartości nie jest prawdziwa, walidator wymaga, aby wartość komponentu była fałszywa."
                        )
                    ]
                ),
                self.create_chapter(
                    title="Only booleans",
                    class_list={
                        "main": ["table-1-3-narrow"],
                        "sub": ["table-1-3__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            name="firstBooleanValue",
                            label="firstBoolean"
                        ),
                        self.create_component(
                            component_type="checkbox",
                            name="secondBooleanValue",
                            label="secondBoolean"
                        ),
                        self.create_component(
                            component_type="checkbox",
                            name="thirdBooleanValue",
                            label="checkValue",
                            validators=[
                                self.validator.related_boolean_sum_validator(
                                    field_names=[
                                        "firstBooleanValue",
                                        "secondBooleanValue",
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        self.save_part(part)

    def create_related_sum_of_weights_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedSumOfWeightsValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Sum of Weights Validator",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="relatedSumOfWeightsValidator",
                            value="Walidator sprawdza, czy dana wartość jest równa wartości po spełnieniu wszystkich warunków."
                        )
                    ]
                ),
                self.create_chapter(
                    title="Test",
                    class_list={
                        "main": ["table-1-3-narrow"],
                        "sub": ["table-1-3__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            name="firstWeightCheckbox",
                            label="Tak (1 punkt)"
                        ),
                        self.create_component(
                            component_type="checkbox",
                            name="secondWeightCheckbox",
                            label="Tak (2 punkty)"
                        ),
                        self.create_component(
                            component_type="number",
                            name="weightCheck",
                            label="Check",
                            value="3",
                            validators=[
                                self.validator.related_sum_of_weights_validator(
                                    weights={
                                        "firstWeightCheckbox": 1,
                                        "secondWeightCheckbox": 2
                                    }
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        self.save_part(part)

    def create_related_equal_if_in_range_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedEqualIfInRangeValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Equal If In Range Validator",
            chapters=[
                self.create_chapter(
                    title="Number",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="number",
                            label="Number",
                            name="firstEqualNumber"
                        ),
                        self.create_component(
                            component_type="number",
                            label="Check",
                            name="firstEqualNumberCheck",
                            validators=[
                                self.validator.related_equal_if_in_range_validator(
                                    field_name="firstEqualNumber",
                                    required_value=True,
                                    min_value=0,
                                    max_value=100
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Text (fund)",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="Text",
                            name="firstEqualNumberText"
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="Check",
                            name="firstEqualNumberCheckText",
                            validators=[
                                self.validator.related_equal_if_in_range_validator(
                                    field_name="firstEqualNumberText",
                                    required_value=42,
                                    min_value=0,
                                    max_value=100
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        self.save_part(part)

    def create_related_empty_if_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedEmptyIfValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Empty IF Validator",
            chapters=[
                self.create_chapter(
                    title="Checkbox",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            name="emptyCheckbox",
                            label="Value"
                        ),
                        self.create_component(
                            component_type="checkbox",
                            name="emptyCheckboxCheck",
                            label="Check",
                            validators=[
                                self.validator.related_empty_if_validator(
                                    field_name="emptyCheckbox",
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Text",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="text",
                            name="emptyText",
                            label="Value"
                        ),
                        self.create_component(
                            component_type="text",
                            name="emptyTextCheck",
                            label="Check",
                            validators=[
                                self.validator.related_empty_if_validator(
                                    field_name="emptyText",
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        self.save_part(part)

    def create_related_fraction_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedFractionValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Fraction Validator",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="relatedFractionValidator",
                            value="Walidator sprawdza, czy wartość jest dokładnie równa wyliczonej proporcji wartości danego pola, z uwzględnieniem limitu maksymalnego."
                        )
                    ]
                ),
                self.create_chapter(
                    title="Test",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            name="fractionTotal",
                            label="Kwota całkowita",
                            unit="PLN",
                            class_list=[
                                "table-full"
                            ]
                        ),
                        self.create_component(
                            component_type="number",
                            name="fractionShare",
                            label="Udział (80%)",
                            validators=[
                                self.validator.related_fraction_validator(
                                    field_name="fractionTotal",
                                    ratio=0.8
                                )
                            ],
                            unit="PLN"
                        ),
                        self.create_component(
                            component_type="number",
                            name="fractionShareMax",
                            label="Udział (80% lub 1000 PLN)",
                            validators=[
                                self.validator.related_fraction_validator(
                                    field_name="fractionTotal",
                                    ratio=0.8,
                                    max_value=1000
                                )
                            ],
                            unit="PLN"
                        )
                    ]
                )
            ]
        )
        self.save_part(part)

    def create_related_gte_fraction_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedFractionGTEValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Fraction GTE Validator",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="relatedFractionGTEValidator",
                            value="Walidator sprawdza, czy wartość nie jest większa niż wyliczona proporcja wartości danego pola, z uwzględnieniem limitu maksymalnego."
                        )
                    ]
                ),
                self.create_chapter(
                    title="Test",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            name="fractionGteTotal",
                            label="Kwota całkowita",
                            unit="PLN"
                        ),
                        self.create_component(
                            component_type="number",
                            name="fractionGteShare",
                            label="Udział (max 80%)",
                            validators=[
                                self.validator.related_fraction_gte_validator(
                                    field_name="fractionGteTotal",
                                    ratio=0.8
                                )
                            ],
                            unit="PLN"
                        )
                    ]
                )
            ]
        )
        self.save_part(part)

    def create_related_lte_fraction_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedFractionLTEValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Fraction LTE Validator",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="relatedFractionLTEValidator",
                            value="Walidator sprawdza, czy wartość nie jest mniejsza niż wyliczona proporcja wartości danego pola, z uwzględnieniem limitu maksymalnego."
                        )
                    ]
                ),
                self.create_chapter(
                    title="Test",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            name="fractionLteTotal",
                            label="Kwota całkowita",
                            unit="PLN"
                        ),
                        self.create_component(
                            component_type="number",
                            name="fractionLteShare",
                            label="Udział (max 80%)",
                            validators=[
                                self.validator.related_fraction_gte_validator(
                                    field_name="fractionLteTotal",
                                    ratio=0.8
                                )
                            ],
                            unit="PLN"
                        )
                    ]
                )
            ]
        )
        self.save_part(part)

    def create_related_local_sum_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedLocalSumValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Local Sum Validator",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="relatedLocalSumValidator",
                            value="Walidator sprawdza, czy suma wartości pól jest poprawna."
                        )
                    ]
                ),
                self.create_chapter(
                    title="Kwoty",
                    class_list={
                        "main": ["table-1-3-narrow"],
                        "sub": ["table-1-3__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            name="firstLocalSumCost",
                            unit="PLN",
                            label="Koszt 1"
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            name="secondLocalSumCost",
                            unit="PLN",
                            label="Koszt 2"
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            name="localSumTotal",
                            calculation_rules=[
                                self.calculation_rule.dynamic_sum_inputs(
                                    fields=["firstLocalSumCost", "secondLocalSumCost"]
                                )
                            ],
                            validators=[
                                self.validator.related_local_sum_validator(
                                    field_names=["firstLocalSumCost", "secondLocalSumCost"]
                                )
                            ],
                            label="Suma",
                            unit="PLN",
                            read_only=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Udziały",
                    components=[
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 2,
                                "maxCount": 10
                            },
                            components=[
                                self.create_chapter(
                                    title="Pozycja",
                                    class_list={
                                        "main": ["table-1-3-narrow"],
                                        "sub": ["table-1-3__col"],
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            name="firstLocalShare",
                                            unit="PLN",
                                            label="Koszt 1"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            name="secondLocalShare",
                                            unit="PLN",
                                            label="Koszt 2"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            name="localSumTotalShare",
                                            calculation_rules=[
                                                self.calculation_rule.local_share_calculator(
                                                    dividend_field="secondLocalShare",
                                                    divisor_field="firstLocalShare",
                                                )
                                            ],
                                            label="Udział",
                                            unit="%",
                                            read_only=True
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Podsumowanie",
                            components=[
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    name="localSumTotalShareTotal",
                                    calculation_rules=[
                                        self.calculation_rule.dynamic_sum_inputs(
                                            fields=["localSumTotalShare"]
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_sum_validator(
                                            field_names=["localSumTotalShare"]
                                        )
                                    ],
                                    label="Suma",
                                    unit="PLN",
                                    read_only=True
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        self.save_part(part)

    def create_related_any_of_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedAnyOfValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Any Of Validator",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="relatedAnyOfValidator",
                            value="Walidator sprawdza, czy została zaznaczona chociaż jedna z wartości."
                        )
                    ]
                ),
                self.create_chapter(
                    title="Test",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            name="firstAnyCheckbox",
                            label="Opcja 1",
                            validators=[
                                self.validator.related_any_of_validator(
                                    field_names=[
                                        "firstAnyCheckbox",
                                        "secondAnyCheckbox",
                                    ]
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="checkbox",
                            name="secondAnyCheckbox",
                            label="Opcja 2",
                            validators=[
                                self.validator.related_any_of_validator(
                                    field_names=[
                                        "firstAnyCheckbox",
                                        "secondAnyCheckbox",
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        self.save_part(part)

    def create_related_mapped_limit_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedMappedLimitValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Mapped Limit Validator",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="relatedMappedLimitValidator",
                            value="Walidator sprawdza, czy wartość dla wybranej opcji nie przekracza danego limitu."
                        )
                    ]
                ),
                self.create_chapter(
                    title="Test",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="select",
                            name="mappedSelect",
                            options=[
                                "Opcja A",
                                "Opcja B",
                                "Opcja C"
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            name="mappedSelectFinal",
                            validators=[
                                self.validator.related_mapped_limit_validator(
                                    default_limit=0,
                                    options=[
                                        {
                                            "limit": 10000,
                                            "conditions": [
                                                {
                                                    "field_name": "mappedSelect",
                                                    "value": "Opcja A"
                                                }
                                            ]
                                        },
                                        {
                                            "limit": 20000,
                                            "conditions": [
                                                {
                                                    "field_name": "mappedSelect",
                                                    "value": "Opcja B"
                                                }
                                            ]
                                        }
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        self.save_part(part)

    def create_related_allowed_options_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedAllowedOptionsValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Allowed Options Validator",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="relatedAllowedOptionsValidator",
                            value="Walidator sprawdza, czy dana wartość jest dozwolona na podstawie wartości innego pola."
                        )
                    ]
                ),
                self.create_chapter(
                    title="Test",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="select",
                            name="allowedSelect",
                            options=[
                                "Polska",
                                "Niemcy"
                            ],
                            label="Kraj"
                        ),
                        self.create_component(
                            component_type="select",
                            name="allowedOptionsSelect",
                            options=[
                                "Warszawa",
                                "Berlin",
                                "Kraków"
                            ],
                            validators=[
                                self.validator.related_allowed_options_validator(
                                    field_name="allowedSelect",
                                    mapping={
                                        "Polska": ["Warszawa", "Kraków"],
                                        "Niemcy": ["Berlin"],
                                    }
                                )
                            ],
                            label="Miasto"
                        )
                    ]
                )
            ]
        )
        self.save_part(part)

    def create_related_unique_value_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedUniqueValueValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Unique Value Validator",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="relatedUniqueValueValidator",
                            value="Walidator sprawdza, czy dana wartość jest unikalna w polach o danej nazwie."
                        )
                    ]
                ),
                self.create_chapter(
                    title="Lista gości",
                    components=[
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 2,
                                "maxCount": 10
                            },
                            components=[
                                self.create_chapter(
                                    title="Gość",
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            name="questName",
                                            validators=[
                                                self.validator.related_unique_value_validator(
                                                    field_name="questName"
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
                    title="Lista gości - normalized",
                    components=[
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 2,
                                "maxCount": 10
                            },
                            components=[
                                self.create_chapter(
                                    title="Gość",
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            name="questNameNormalized",
                                            validators=[
                                                self.validator.related_unique_value_validator(
                                                    field_name="questNameNormalized",
                                                    normalize=True
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
        self.save_part(part)

    def create_related_last_date_validator(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. RelatedLastDateValidator",
            short_name=f"{self.helpers.int_to_roman(number)}. Related Last Date Validator",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="relatedLastDateValidator",
                            value="Walidator sprawdza, czy data jest większa lub równa najpóźniejszej dacie z danego pola."
                        )
                    ]
                ),
                self.create_chapter(
                    title="Harmonogram",
                    components=[
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 2,
                                "maxCount": 10
                            },
                            components=[
                                self.create_chapter(
                                    class_list={
                                        "main": ["table-1-2"],
                                        "sub": ["table-1-2__col"],
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="date",
                                            label="Data od",
                                            name="lastStartDate",
                                            required=True,
                                            validators=[
                                                self.validator.related_local_date_lte_validator(
                                                    field_name="lastEndDate"
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="date",
                                            label="Data do",
                                            name="lastEndDate",
                                            required=True,
                                            validators=[
                                                self.validator.related_local_date_gte_validator(
                                                    field_name="lastStartDate"
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
                    title="Podsumowanie",
                    components=[
                        self.create_component(
                            component_type="date",
                            label="Data premiery",
                            name="premiereDate",
                            validators=[
                                self.validator.related_last_date_validator(
                                    field_name="lastEndDate"
                                )
                            ],
                            required=True
                        )
                    ]
                )
            ]
        )
        self.save_part(part)
