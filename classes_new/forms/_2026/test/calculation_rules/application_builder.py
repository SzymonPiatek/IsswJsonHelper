from classes_new.form_builder.form_builder import ApplicationFormBuilder


class CalculationRulesApplicationFormBuilder(ApplicationFormBuilder):
    def __init__(self):
        super().__init__(
            custom_dir_name="test/calculation_rules",
            custom_file_name="calculation_rules"
        )

        self.form_id = self.set_ids(
            local_id=16416,
            uat_id=None
        )

        self.parts = [
            self.create_sum_inputs,
            self.create_multiply_inputs
        ]

        """
        Calculation rules:
        
        [x] sumInputs
        [x] multiplyInputs
        [ ] copyValue
        [ ] copyLocalValue
        [ ] copyTitle
        [ ] sumsShareCalculator
        [ ] shareCalculator
        [ ] localShareCalculator
        [ ] singlePositionShareCalculator
        [ ] assignValue
        [ ] lastDate
        [ ] firstDate
        [ ] relateToDate
        [ ] relateToLastDate
        [ ] halfwayDate
        [ ] dynamicSumInputs
        [ ] multiplyValues
        [ ] localSum
        [ ] getNBPCurrency
        [ ] conditionalCopyValue
        [ ] copyCompanyData
        [ ] sumInvoiceCosts
        """

    def create_sum_inputs(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. sumInputs",
            short_name=f"{self.helpers.int_to_roman(number)}. Sum inputs",
            chapters=[
                self.create_chapter(
                    title="Single",
                    components=[
                        self.create_chapter(
                            title="Koszty",
                            class_list={
                                "main": ["table-1-2"],
                                "sub": ["table-1-2__col"],
                            },
                            components=[
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    name="sumInputsSingle"
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    name="sumInputsSingle2"
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Single - Podsumowanie",
                            components=[
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    name="sumInputsSingleTotal",
                                    read_only=True,
                                    calculation_rules=[
                                        self.calculation_rule.sum_inputs(
                                            fields=[
                                                "sumInputsSingle",
                                                "sumInputsSingle2"
                                            ]
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_sum_validator(
                                            field_names=[
                                                "sumInputsSingle",
                                                "sumInputsSingle2"
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Multi",
                    components=[
                        self.create_chapter(
                            title="Koszty",
                            multiple_forms_rules={
                                "minCount": 2,
                                "maxCount": 10
                            },
                            class_list={
                                "main": ["table-1-2"],
                                "sub": ["table-1-2__col"],
                            },
                            components=[
                                self.create_chapter(
                                    title="Koszt",
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            name="sumInputsMulti"
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Multi - Podsumowanie",
                            components=[
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    name="sumInputsMultiTotal",
                                    read_only=True,
                                    calculation_rules=[
                                        self.calculation_rule.sum_inputs(
                                            fields=[
                                                "sumInputsMulti",
                                            ]
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_sum_validator(
                                            field_names=[
                                                "sumInputsMulti",
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

    def create_multiply_inputs(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. multiplyInputs",
            short_name=f"{self.helpers.int_to_roman(number)}. Multiply inputs",
            chapters=[
                self.create_chapter(
                    title="Single",
                    components=[
                        self.create_chapter(
                            title="Liczby",
                            class_list={
                                "main": ["table-1-2"],
                                "sub": ["table-1-2__col"],
                            },
                            components=[
                                self.create_component(
                                    component_type="number",
                                    name="multiplyInputsSingle"
                                ),
                                self.create_component(
                                    component_type="number",
                                    name="multiplyInputsSingle2"
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Liczby - Podsumowanie",
                            components=[
                                self.create_component(
                                    component_type="number",
                                    name="multiplyInputsSingleTotal",
                                    read_only=True,
                                    calculation_rules=[
                                        self.calculation_rule.multiply_inputs(
                                            fields=[
                                                "multiplyInputsSingle",
                                                "multiplyInputsSingle2"
                                            ]
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_multiplication_validator(
                                            field_names=[
                                                "multiplyInputsSingle",
                                                "multiplyInputsSingle2"
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Multi",
                    components=[
                        self.create_chapter(
                            title="Liczby",
                            multiple_forms_rules={
                                "minCount": 2,
                                "maxCount": 10
                            },
                            class_list={
                                "main": ["table-1-2"],
                                "sub": ["table-1-2__col"],
                            },
                            components=[
                                self.create_chapter(
                                    title="Liczba",
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            name="multiplyInputsMulti"
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Multi - Podsumowanie",
                            components=[
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    name="multiplyInputsMultiTotal",
                                    read_only=True,
                                    calculation_rules=[
                                        self.calculation_rule.multiply_inputs(
                                            fields=[
                                                "multiplyInputsMulti",
                                            ]
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_multiplication_validator(
                                            field_names=[
                                                "multiplyInputsMulti",
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

