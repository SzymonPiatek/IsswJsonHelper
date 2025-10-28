from classes_new.form_builder.form_builder import ApplicationFormBuilder


class SpecialValidatorsApplicationFormBuilder(ApplicationFormBuilder):
    def __init__(self):
        super().__init__(
            custom_dir_name="test/special_validators",
            custom_file_name="special_validators"
        )

        self.parts = [
            self.create_checkbox_true_date_lte_todat_test
        ]

        self.form_id = self.set_ids(
            local_id=16413,
            uat_id=None
        )

        """
        Special validators:
        
        [x] CheckboxTrueDateLTEToday
        """

    def create_checkbox_true_date_lte_todat_test(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. CheckboxTrueDateLTEToday",
            short_name=f"{self.helpers.int_to_roman(number)}. Checkbox True Date LTE Today",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            value="Walidator pilnuje, by użytkownik nie zaznaczył checkboxa, jeśli powiązana data jest wcześniejsza lub dzisiejsza.",
                            name="checkboxTrueDateLTEToday"
                        )
                    ]
                ),
                self.create_chapter(
                    class_list={
                        "main": [
                            "table-1-2",
                        ],
                        "sub": [
                            "table-1-2__col"
                        ]
                    },
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            name="checkbox",
                            label="Checkbox",
                            validators=[
                                self.validator.checkbox_true_date_lte_today(
                                    field_name="date"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="date",
                            name="date",
                            label="Data",
                            required=True,
                        )
                    ]
                )
            ]
        )

        self.save_part(part)
