from classes.form_builder.duk.development.application_builder import DevelopmentApplicationBuilder


class ModernizationApplicationBuilder(DevelopmentApplicationBuilder):
    PRIORITY_NAME = 'I. Modernizacja kin'
    PRIORITY_NUM = 1

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'modernization'

    def create_application_scope_of_project(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'scope_of_the_project.json')
        self.save_part(part)

    def create_application_attachments(self):
        part = self.create_part(
            title="VI. Załączniki",
            short_name="VI. Załączniki"
        )

        attachments_data_path = self.department_data_path / '_pages' / 'application_attachments'
        priority_attachments_data_path = self.priority_data_path / '_pages' / 'application_attachments'

        chapter_01 = self.create_chapter(
            title="Obowiązkowe załączniki"
        )

        part['chapters'] = [
            chapter_01,
            self.load_json(path=attachments_data_path / 'document_confirming_represent_applicant.json'),
            self.load_json(path=attachments_data_path / 'schedule_information.json'),
            self.load_json(path=priority_attachments_data_path / 'attachment_right_to_property.json'),
            self.load_json(path=priority_attachments_data_path / 'attachment_building_permit.json'),
            self.load_json(path=priority_attachments_data_path / 'attachment_investment_cost_estimate.json'),
            self.load_json(path=attachments_data_path / 'other_attachments.json'),
            self.load_json(path=attachments_data_path / 'storage_of_blanks.json'),
        ]
        self.save_part(part)

    def generate(self):
        self.create_application_base()

        # Metadane wniosku
        self.create_application_metadata()

        # I. Dane podstawowe
        self.create_application_basic_data(data={
            'projectType': {
                'options': [
                    "Współfinansowanie zakupu i modernizacji wyposażenia do prowadzenia lub rozpoczęcia działalności kinowej, w tym sprzętu umożliwiającego odbiór filmów przez osoby ze szczególnymi potrzebami",
                    "Inne działania realizujące cele Priorytetu I"
                ]
            }
        })

        # II. Dane wnioskodawcy
        self.create_application_applicant_data()

        # III. Zakres przedsięwzięcia
        self.create_application_scope_of_project()

        # IV. Źródła finansowania
        self.create_application_sources_of_financing()

        # V. Oświadczenia
        self.create_application_statements()

        # VI. Załączniki
        self.create_application_attachments()

        # VII. Kosztorys przedsięwzięcia

        # VIII. Harmonogram
        self.create_application_schedule()

        self.save_output()
