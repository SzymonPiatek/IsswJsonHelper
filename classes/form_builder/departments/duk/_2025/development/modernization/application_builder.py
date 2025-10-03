from classes.form_builder.departments.duk._2025.development.application_builder import DevelopmentApplicationBuilder
from classes.form_builder.departments.duk.application_builder import DUKApplicationBuilder
from classes.form_builder.departments.duk._2025.development.modernization.estimate_data import estimate_sections


class ModernizationApplicationBuilder(DevelopmentApplicationBuilder):
    PRIORITY_NAME = 'I. Modernizacja kin'
    PRIORITY_NUM = 1
    FORM_ID = 9190

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'modernization'
        self.estimate_sections = estimate_sections

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
            short_name="VI. Załączniki",
            chapters=[
                self.create_chapter(
                    title="Obowiązkowe załączniki",
                    components=[
                        self.section.application_attachment.document_confirming_represent_applicant(),
                        self.section.application_attachment.schedule_information(),
                        self.section.application_attachment.right_to_property(),
                        self.section.application_attachment.building_permit(),
                        self.section.application_attachment.investment_cost_estimate()
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
                        self.section.application_scope_of_project.cinema_detailed_infomration_years_functioning(),
                        self.section.application_scope_of_project.characteristics_of_cinema_halls(),
                        self.section.application_scope_of_project.cinema_projectors_information()
                    ]
                ),
                self.section.application_scope_of_project.information_about_location(),
                self.create_chapter(
                    title="4. Informacje o działalności prowadzonej w kinie w okresie 12 miesięcy do dnia złożenia wniosku",
                    components=[
                        self.section.application_scope_of_project.cinema_activities_information_12_months_period_from_submission(),
                        self.section.application_scope_of_project.cinema_additional_activities(),
                        self.section.application_scope_of_project.cinema_education_programs_info(),
                        self.section.application_scope_of_project.cinema_avg_ticket_price(),
                        self.section.application_scope_of_project.cinema_cooperation_with_other_cinemas(),
                        self.section.application_scope_of_project.cinema_webpage(),
                        self.section.application_scope_of_project.cinema_online_ticketing(),
                        self.section.application_scope_of_project.cinema_key_events_last_year()
                    ]
                ),
                self.section.application_scope_of_project.project_description(),
                self.section.application_scope_of_project.cinema_project_relation_to_other_fundings()
            ]
        )
        self.save_part(part)
