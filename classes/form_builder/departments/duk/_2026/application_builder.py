from classes.form_builder.departments.duk.application_builder import DUKApplicationBuilder


class DUKApplicationBuilder2026(DUKApplicationBuilder):
    YEAR = 2026

    def __init__(self):
        super().__init__()

    def create_application_metadata(self):
        part = self.create_part(
            title="Wniosek o dofinansowanie przedsięwzięcia realizowanego w ramach Programów Operacyjnych Polskiego Instytutu Sztuki Filmowej",
            short_name="I. Metadane wniosku",
            chapters=[
                self.create_chapter(
                    title="1. Tryb naboru",
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Nr sesji i rok",
                            name="sessionYear",
                            value=f"Sesja {self.session}/{self.year}",
                            read_only=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Program operacyjny",
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Program",
                            name="programName",
                            value=self.operation_name,
                            read_only=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="3. Priorytet",
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Priorytet",
                            name="priorytetName",
                            value=self.priority_name,
                            read_only=True
                        )
                    ]
                )
            ]
        )
        self.save_part(part=part)

    def create_application_applicant_data(self):
        part = self.create_part(
            title="III. Dane wnioskodawcy",
            short_name="III. Dane wnioskodawcy",
            chapters=[
                self.section.applicant_name(number="1"),
                self.section.eligible_person_data(number="2"),
                self.section.responsible_person_data(number="3"),
                self.section.applicant_address(number="4", main_poland=True, main_foreign=True, contact_poland=True, contact_foreign=True),
                self.section.applicant_identification_data(number="5"),
                self.section.applicant_bank_data(number="6"),
                self.section.applicant_legal_information(number="7"),
                self.section.applicant_statistical_data(number="8"),
            ]
        )

        self.save_part(part=part)
