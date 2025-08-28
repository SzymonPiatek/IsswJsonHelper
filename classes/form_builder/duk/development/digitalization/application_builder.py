from classes.form_builder.duk.development.application_builder import DevelopmentApplicationBuilder
from classes.form_builder.duk.application_builder import DUKApplicationBuilder
from classes.form_builder.duk.development.digitalization.estimate_data import estimate_sections


class DigitalizationApplicationBuilder(DevelopmentApplicationBuilder):
    PRIORITY_NAME = 'II. Cyfryzacja kin'
    PRIORITY_NUM = 2
    FORM_ID = 9191

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'digitalization'
        self.estimate_sections = estimate_sections

    def create_application_basic_data(self, **kwargs):
        data = {
            'projectType': {
                'options': [
                    "Współfinansowanie zakupu sprzętu do projekcji cyfrowych o minimalnej rozdzielczości 2K w standardzie DCI"
                ]
            }
        }
        DUKApplicationBuilder.create_application_basic_data(self=self, data=data)

    def create_application_attachments(self):
        part = self.create_part(
            title="VI. Załączniki",
            short_name="VI. Załączniki",
            chapters=[
                self.create_chapter(
                    title="Obowiązkowe załączniki",
                    components=[
                        self.section.application_attachment.document_confirming_represent_applicant(),
                        self.section.application_attachment.schedule_information(),
                        self.section.application_attachment.financial_contribution_confirmation(),
                        self.section.application_attachment.room_pics(),
                        self.section.application_attachment.right_to_property(),
                        self.section.application_attachment.deminimis_statement(),
                    ]
                ),
                self.section.application_attachment.other_attachments(),
                self.section.application_attachment.storage_of_blanks()
            ]
        )
        self.save_part(part)

    def create_application_scope_of_project(self):
        part = self.create_part(
            title="III. Zakres przedsięwzięcia",
            short_name="III. Zakres przedsięwzięcia",
            chapters=[
                self.section.application_scope_of_project.project_implementation_place(),
                self.create_chapter(
                    title="2. Informacje szczegółowe o kinie",
                    components=[
                        self.section.application_scope_of_project.cinema_detailed_information_basic_data(),
                        self.section.application_scope_of_project.characteristics_of_cinema_halls(),
                        self.section.application_scope_of_project.number_of_seats_in_room_for_digitization(),
                        self.section.application_scope_of_project.cinema_projectors_information(),
                        self.section.application_scope_of_project.information_about_sound_in_room_for_digitization()
                    ]
                ),
                self.section.application_scope_of_project.information_about_location()
            ]
        )

        self.save_part(part)
