from classes.form_builder.duk.development.application_builder import DevelopmentApplicationBuilder
from classes.form_builder.duk.application_builder import DUKApplicationBuilder


class ModernizationApplicationBuilder(DevelopmentApplicationBuilder):
    PRIORITY_NAME = 'I. Modernizacja kin'
    PRIORITY_NUM = 1

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'modernization'

    def create_application_basic_data(self, **kwargs):
        data = {
            'projectType': {
                'options': [
                    "Współfinansowanie zakupu i modernizacji wyposażenia do prowadzenia lub rozpoczęcia działalności kinowej, w tym sprzętu umożliwiającego odbiór filmów przez osoby ze szczególnymi potrzebami",
                    "Inne działania realizujące cele Priorytetu I"
                ]
            }
        }
        DUKApplicationBuilder.create_application_basic_data(self=self, data=data)

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
