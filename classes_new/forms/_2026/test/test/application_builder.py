from classes_new.form_builder.form_builder import ApplicationFormBuilder


class TestApplicationFormBuilder(ApplicationFormBuilder):
    def __init__(self):
        super().__init__(
            custom_dir_name="test/test",
            custom_file_name="test"
        )

        self.form_id = self.set_ids(
            local_id=16417,
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
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"]
                    },
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            name="checkbox",
                            label="Checkbox"
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            name="text",
                            label="Text fund"
                        )
                    ]
                ),
                self.create_chapter(
                    title="Required",
                    class_list={
                        "main": ["table-1-2"],
                        "sub": ["table-1-2__col"]
                    },
                    components=[

                    ]
                )
            ]
        )

        self.save_part(part)
