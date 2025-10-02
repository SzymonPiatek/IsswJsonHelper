from classes.form_builder.application_builder import ApplicationBuilder


class TestApplicationBuilder(ApplicationBuilder):
    FORM_ID = 9228
    DEPARTMENT_NAME = "TEST"
    OPERATION_NAME = "TEST"
    OPERATION_NUM = "test"
    PRIORITY_NAME = "TEST"
    PRIORITY_NUM = "test"

    def __init__(self):
        super().__init__()

        """ 
        Validators:
        [x] RelatedEqualityValidator
        [x] RelatedLocalEqualityValidator
        [x] RelatedNumericEqualityValidator
        [x] RelatedRequiredIfEqualValidator
        [x] RelatedDateLTEValidator
        [ ]
        [ ]
        [ ]
        [x] RelatedLocalDivisionValidator
        
        CalculationRules:
        [ ] 
        [ ] 
        [ ] 
        [ ] 
        [ ] 
        [ ] 
        """

    def generate(self):
        self.create_base()

        self.create_related_equality_validator()
        self.create_related_local_equality_validator()
        self.create_related_numeric_equality_validator()
        self.create_related_required_if_equal_validator()
        self.create_related_lte_validator()
        self.create_related_local_division_validator()

        self.save_output()

    def create_related_equality_validator(self):
        part = self.create_part(
            title="RelatedEqualityValidator",
            chapters=[
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

    def create_related_local_equality_validator(self):
        part = self.create_part(
            title="RelatedLocalEqualityValidator",
            chapters=[
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

    def create_related_numeric_equality_validator(self):
        part = self.create_part(
            title="RelatedNumericEqualityValidator",
            chapters=[
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
                            name="numberNumeric"
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

    def create_related_required_if_equal_validator(self):
        part = self.create_part(
            title="RelatedRequiredIfEqualValidator",
            chapters=[
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

    def create_related_lte_validator(self):
        part = self.create_part(
            title="RelatedDateLTEValidator",
            chapters=[
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

    def create_related_local_division_validator(self):
        part = self.create_part(
            title="RelatedLocalDivisionValidator",
            chapters=[
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
                                            mask="share",
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
