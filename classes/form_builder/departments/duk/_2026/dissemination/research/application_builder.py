from classes.form_builder.departments.duk._2026.dissemination.application_builder import DisseminationApplicationBuilder
from .estimate_data import estimate_sections
from classes.form_builder.departments.duk._2026.application_estimate_builder import DUKApplicationEstimateBuilder
from ..priority import ResearchPriority


class ResearchApplicationBuilder(DisseminationApplicationBuilder, ResearchPriority):
    FORM_ID = 9188

    def __init__(self):
        super().__init__()

        self.estimate_sections = estimate_sections
        self.project_type = [
            ""
        ]

    def create_application_scope_of_project(self):
        pass

    def create_application_attachments(self):
        pass

    def create_application_statements(self):
        pass

    def create_application_schedule(self):
        pass

    def create_application_project_costs(self):
        estimate_builder = DUKApplicationEstimateBuilder(
            estimate_sections=self.estimate_sections,
        )

        part = self.create_part(
            title="VIII. Kosztorys przedsięwzięcia",
            short_name="VIII. Kosztorys przedsięwzięcia",
            chapters=[
                estimate_builder.generate_estimate_top(),
                self.create_chapter(
                    title="Koszty z podziałem na źródło finansowania",
                    components=[
                        estimate_builder.generate_estimate_headers(),
                        estimate_builder.generate_estimate(),
                    ]
                ),
                estimate_builder.generate_estimate_bottom()
            ]
        )

        self.save_part(part=part)

