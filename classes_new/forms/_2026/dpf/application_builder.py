from classes_new.form_builder.form_builder import ApplicationFormBuilder


class DPFDepartmentApplicationFormBuilder(ApplicationFormBuilder):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.parts = [
            self.create_application_metadata,
            self.create_application_basic_data,
            self.create_application_applicant_data,
            self.create_application_information_data,
            self.create_application_completion_date_data,
            self.create_application_financial_data,
            self.create_application_additional_data,
            self.create_application_attachments,
            self.create_application_statements
        ]

        self.task_type: str = None

    def create_application_metadata(self, number: int):
        part = self.create_part(
            title="Wniosek o dofinansowanie w ramach Programów Operacyjnych Polskiego Instytutu Sztuki Filmowej",
            short_name=f"{self.helpers.int_to_roman(number)}. Metadane wniosku",
            chapters=[
                self.create_chapter(
                    title="1. Tryb naboru",
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Nr sesji i rok",
                            name="sessionYear",
                            value=f"Sesja {self.session.roman_num}/{self.session.year}",
                            read_only=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Program operacyjny",
                    components=[
                        self.create_component(
                            component_type="text",
                            name="programName",
                            value=str(self.priority.operation_program),
                            read_only=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="3. Priorytet",
                    components=[
                        self.create_component(
                            component_type="text",
                            name="priorityName",
                            value=str(self.priority),
                            read_only=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="4. Zakres przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="text",
                            name="taskType",
                            value=self.task_type,
                            read_only=True
                        )
                    ]
                )
            ]
        )

        self.save_part(part)

    def create_application_basic_data(self, number: int):
        pass

    def create_application_applicant_data(self, number: int):
        pass

    def create_application_information_data(self, number: int):
        pass

    def create_application_completion_date_data(self, number: int):
        pass

    def create_application_financial_data(self, number: int):
        pass

    def create_application_additional_data(self, number: int):
        pass

    def create_application_attachments(self, number: int):
        pass

    def create_application_statements(self, number: int):
        pass
