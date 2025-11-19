from classes_new.form_builder.form_builder import ApplicationFormBuilder


class VisualityTestApplicationFormBuilder(ApplicationFormBuilder):
    def __init__(self):
        super().__init__(
            custom_dir_name="test/visuality_test",
            custom_file_name="visuality_test"
        )

        self.form_id = self.set_ids(
            local_id=16420,
            uat_id=None
        )

        self.parts = [
            self.create_visuality_test_enabled,
            self.create_visuality_test_disabled
        ]

        """
        Visuality test:
        
        [x] Enabled
        [x] Disabled
        """

    def create_visuality_test_enabled(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Component visual - enabled",
            chapters=[
                self.create_chapter(
                    title="Text",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="text",
                            name="visualityText",
                            label="Text"
                        ),
                        self.create_component(
                            component_type="textarea",
                            name="visualityTextarea",
                            label="Textarea"
                        ),
                    ]
                ),
                self.create_chapter(
                    title="Number",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="number",
                            name="visualityNumber",
                            label="Number",
                            help_text="Test"
                        )
                    ]
                ),
                self.create_chapter(
                    title="Select",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="select",
                            name="visualitySelect",
                            options=[
                                "Test",
                                "Test 2"
                            ],
                            label="Select"
                        ),
                        self.create_component(
                            component_type="country",
                            name="visualityCountrySelect",
                            label="Country"
                        ),
                        self.create_component(
                            component_type="currency",
                            name="visualityCurrencySelect",
                            label="Currency"
                        ),
                        self.create_component(
                            component_type="countryMulti",
                            name="visualityCountryMultiSelect",
                            label="CountryMulti"
                        ),
                    ]
                ),
                self.create_chapter(
                    title="Other",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            name="visualityCheckbox",
                            label="Checkbox",
                            help_text="Test"
                        ),
                        self.create_component(
                            component_type="radio",
                            name="visualityRadio",
                            options=[
                                "Test",
                                "Test 2"
                            ],
                            label="Radio"
                        ),
                        self.create_component(
                            component_type="header",
                            name="visualityHeader",
                            value="Header"
                        ),
                        self.create_component(
                            component_type="date",
                            name="visualityDate",
                            label="Date"
                        ),
                        self.create_component(
                            component_type="file",
                            name="visualityFile",
                            label="File"
                        )
                    ]
                )
            ]
        )
        self.save_part(part)

    def create_visuality_test_disabled(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Component visual - disabled",
            chapters=[
                self.create_chapter(
                    title="Text",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="text",
                            name="visualityTextDisabled",
                            label="Text",
                            read_only=True
                        ),
                        self.create_component(
                            component_type="textarea",
                            name="visualityTextareaDisabled",
                            label="Textarea",
                            read_only=True
                        ),
                    ]
                ),
                self.create_chapter(
                    title="Number",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="number",
                            name="visualityNumberDisabled",
                            label="Number",
                            read_only=True
                        ),
                    ]
                ),
                self.create_chapter(
                    title="Select",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="select",
                            name="visualitySelectDisabled",
                            options=[
                                "Test",
                                "Test 2"
                            ],
                            label="Select",
                            read_only=True
                        ),
                        self.create_component(
                            component_type="currency",
                            name="visualityCurrencySelectDisabled",
                            label="Currency",
                            read_only=True
                        ),
                        self.create_component(
                            component_type="country",
                            name="visualityCountrySelectDisabled",
                            label="Country",
                            read_only=True
                        ),
                        self.create_component(
                            component_type="countryMulti",
                            name="visualityCountryMultiSelectDisabled",
                            label="CountryMulti",
                            read_only=True
                        ),
                    ]
                ),
                self.create_chapter(
                    title="Other",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"],
                    },
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            name="visualityCheckboxDisabled",
                            label="Checkbox",
                            read_only=True
                        ),
                        self.create_component(
                            component_type="radio",
                            name="visualityRadioDisabled",
                            options=[
                                "Test",
                                "Test 2"
                            ],
                            label="Radio",
                            read_only=True
                        ),
                        self.create_component(
                            component_type="header",
                            name="visualityHeaderDisabled",
                            value="Header",
                            read_only=True
                        ),
                        self.create_component(
                            component_type="date",
                            name="visualityDateDisabled",
                            label="Date",
                            read_only=True
                        ),
                        self.create_component(
                            component_type="file",
                            name="visualityFileDisabled",
                            label="File",
                            read_only=True
                        )
                    ]
                )
            ]
        )
        self.save_part(part)
