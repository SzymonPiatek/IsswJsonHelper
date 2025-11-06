from classes_new.form_builder.form_builder import ApplicationFormBuilder


class TestApplicationFormBuilder(ApplicationFormBuilder):
    def __init__(self):
        super().__init__(
            custom_dir_name="test/test",
            custom_file_name="test"
        )

        self.form_id = self.set_ids(
            local_id=16424,
            uat_id=None
        )

        self.parts = [
            self.create_test_part
        ]

    def create_test_part(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Test",
            chapters=[
                self.create_chapter(
                    title="Values",
                    class_list={
                        "main": ["table-1-3-narrow"],
                        "sub": ["table-1-3__col"]
                    },
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            name="checkbox",
                            label="Checkbox"
                        ),
                        self.create_component(
                            component_type="select",
                            name="select",
                            label="Select",
                            options=[
                                "Test 1",
                                "Test 2",
                                "Test 3"
                            ]
                        ),
                        self.create_component(
                            component_type="number",
                            name="number",
                            label="Number"
                        )
                    ]
                ),
                self.create_chapter(
                    title="Required - isChecked",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"]
                    },
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Required if isChecked",
                            name="requiredIfIsChecked",
                            validators=[
                                self.validator.related_universal_required_validator(
                                    field_name="checkbox",
                                    condition={
                                        "is_checked": True
                                    }
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="checkbox",
                            label="Required if isChecked = False",
                            name="requiredIfIsCheckedFalse",
                            validators=[
                                self.validator.related_universal_required_validator(
                                    field_name="checkbox",
                                    condition={
                                        "is_checked": False
                                    }
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Required - equalValues",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"]
                    },
                    components=[
                        self.create_component(
                            component_type="text",
                            name="textRequiredIfSelectEqualValues",
                            label="Required if 'Test 1' or 'Test 2' in select",
                            validators=[
                                self.validator.related_universal_required_validator(
                                    field_name="select",
                                    condition={
                                        "equal_values": ["Test 1", "Test 2"]
                                    }
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Required like RequiredValidator",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"]
                    },
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            name="requiredValidatorCheckbox",
                            label="Required like RequiredValidator",
                            validators=[
                                self.validator.related_universal_required_validator()
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Required - min and max range",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"]
                    },
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            name="checkboxRequiredMinAndMaxRange",
                            label="Required if 50 <= number <= 100",
                            validators=[
                                self.validator.related_universal_required_validator(
                                    field_name="number",
                                    condition={
                                        "min_range": 50,
                                        "max_range": 100
                                    }
                                )
                            ]
                        )
                    ]
                )
            ]
        )

        self.save_part(part)
