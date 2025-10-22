from classes_new.form_builder.form_builder import ApplicationFormBuilder


class DWMDepartmentApplicationFormBuilder(ApplicationFormBuilder):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.parts = [
            self.create_application_metadata,
            self.create_application_name_data,
            self.create_application_applicant_data,
            self.create_application_applicant_achievements_data,
            self.create_application_description_of_the_project_data,
            self.create_application_logo_data,
            self.create_application_implementation_effects_data,
            self.create_application_other_information_data,
            self.create_application_financial_data,
            self.create_application_statements,
            self.create_application_attachments,
            self.create_application_schedule_data
        ]

    def create_application_metadata(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Metadane wniosku",
            chapters=[
                self.create_chapter(
                    title="1. Program",
                    components=[
                        self.create_component(
                            component_type="text",
                            name="programName",
                            read_only=True,
                            value=self.priority.operation_program.name
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Priorytet",
                    components=[
                        self.create_component(
                            component_type="text",
                            name="priorityName",
                            read_only=True,
                            value=self.priority.name
                        )
                    ]
                ),
                self.create_chapter(
                    title="3. Rodzaj przedsięwzięcia określony w programie operacyjnym",
                    components=[
                        self.create_component(
                            component_type="radio",
                            options=[
                                "Organizowanie promocyjnych kampanii lub stoisk na międzynarodowych targach, festiwalach oraz innych wydarzeniach branżowych z udziałem polskich twórców filmowych, związanych z polską twórczością filmową zgodnie z ust. 2 pkt 1",
                                "Organizowanie promocyjnych kampanii lub stoisk na międzynarodowych targach, festiwalach oraz innych wydarzeniach branżowych z udziałem polskich twórców filmowych, związanych z polską twórczością filmową zgodnie z ust. 2 pkt 2",
                                "Organizowanie albo współorganizowanie poza granicami Polski wydarzeń promujących dorobek polskich twórców filmowych oraz polską twórczość filmową, w tym przeglądów, retrospektyw, wystaw, konferencji zgodnie z ust. 2 pkt 3",
                                "Organizowanie albo współorganizowanie w Polsce wizyt, spotkań zagranicznych inwestorów, producentów i twórców filmowych, które służą rozwojowi koprodukcji, usług filmowych oraz dystrybucji polskiej twórczości filmowej za granicą zgodnie z ust. 2 pkt 4",
                                "Organizowanie albo współorganizowanie z partnerami zagranicznymi wydarzeń dla przedstawicieli branży filmowej w formie szkoleń, warsztatów, prezentacji zgodnie z ust. 2 pkt 5"
                            ],
                            name="requestedSupportType",
                            required=True
                        )
                    ]
                )
            ]
        )

        self.save_part(part)

    def create_application_name_data(self, number: int):
        pass

    def create_application_applicant_data(self, number: int):
        pass

    def create_application_applicant_achievements_data(self, number: int):
        pass

    def create_application_description_of_the_project_data(self, number: int):
        pass

    def create_application_logo_data(self, number: int):
        pass

    def create_application_implementation_effects_data(self, number: int):
        pass

    def create_application_other_information_data(self, number: int):
        pass

    def create_application_financial_data(self, number: int):
        pass

    def create_application_statements(self, number: int):
        pass

    def create_application_attachments(self, number: int):
        pass

    def create_application_schedule_data(self, number: int):
        pass
