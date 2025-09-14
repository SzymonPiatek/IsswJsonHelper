from classes.form_builder.additional.decorators import not_implemented_func
from classes.form_builder.application_builder import ApplicationBuilder
from classes.form_builder.components.component.dpf_component import DPFComponent
from classes.form_builder.components.section.dpf.dpf_section import DPFSection


class DPFApplicationBuilder(ApplicationBuilder):
    DEPARTMENT_NAME = 'DPF'
    OPERATION_NAME = 'I. Produkcja filmowa'
    OPERATION_NUM = 1

    def __init__(self):
        super().__init__()

        self.department_data_path = self.application_data_path / 'dpf'
        self.priority_data_path = None
        self.section = DPFSection()
        self.component = DPFComponent()

    def create_application_metadata(self, task_type: str):
        part = self.create_part(
            title="Wniosek o dofinansowanie w ramach Programów Operacyjnych Polskiego Instytutu Sztuki Filmowej",
            short_name="Metadane wniosku",
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
                            name="priorityName",
                            value=self.priority_name,
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
                            value=task_type,
                            read_only=True
                        )
                    ]
                )
            ]
        )

        self.save_part(part)

    @not_implemented_func
    def create_application_basic_data(self):
        pass

    def create_application_applicant_data(self):
        part = self.create_part(
            title="II. Dane wnioskodawcy",
            short_name="II. Dane wnioskodawcy",
            chapters=[
                self.section.applicant_name(number="1"),
                self.section.applicant_type(number="2"),
                self.section.eligible_person_data(number="3"),
                self.section.eligible_person_attachments(number="4"),
                self.section.responsible_person_data(number="5"),
                self.section.applicant_address(number="6"),
                self.section.applicant_identification_data(number="7"),
                self.section.applicant_bank_data(number="8"),
                self.section.applicant_legal_information(number="9"),
                self.section.applicant_statistical_data(number="10"),
            ]
        )

        self.save_part(part=part)

    @not_implemented_func
    def create_application_information_data(self):
        pass

    @not_implemented_func
    def create_application_completion_date_data(self, **kwargs):
        pass

    def create_application_financial_data(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_financial_data.json')
        self.save_part(part=part)

    def create_application_additional_data(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_additional_data.json')
        self.save_part(part=part)

    @not_implemented_func
    def create_application_attachments(self):
        pass

    def create_application_statements(self):
        part = self.create_part(
            title="VIII. Oświadczenia",
            short_name="VIII. Oświadczenia",
            chapters=[
                self.section.application_statements.applicant_statements(),
                self.section.application_statements.producer_statements(),
                self.section.application_statements.script_statements(),
                self.section.application_statements.storage_of_blank_public_documents()
            ]
        )

        self.save_part(part)

    def generate(self):
        self.create_application_base()

        # Metadane wniosku
        self.create_application_metadata(task_type='Produkcja filmowa')

        # I. Dane podstawowe
        self.create_application_basic_data()

        # II. Dane wnioskodawcy
        self.create_application_applicant_data()

        # III. Informacje
        self.create_application_information_data()

        # IV. Termin realizacji
        self.create_application_completion_date_data()

        # V. Dane finansowe
        self.create_application_financial_data()

        # VI. Dane dodatkowe
        self.create_application_additional_data()

        # VII. Załączniki
        self.create_application_attachments()

        # VIII. Oświadczenia
        self.create_application_statements()

        self.save_output()
