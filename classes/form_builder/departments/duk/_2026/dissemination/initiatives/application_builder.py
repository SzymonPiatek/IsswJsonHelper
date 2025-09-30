from classes.form_builder.departments.duk._2026.dissemination.application_builder import DisseminationApplicationBuilder
from .estimate_data import estimate_sections_pt_123, estimate_sections_pt_4
from classes.form_builder.departments.duk._2026.application_estimate_builder import DUKApplicationEstimateBuilder
from classes.form_builder.departments.duk._2026.dissemination.priority import InitiativesPriority


class InitiativesApplicationBuilder(DisseminationApplicationBuilder, InitiativesPriority):
    FORM_ID = 9185

    def __init__(self):
        super().__init__()

        self.project_type = [
            "Organizacja przeglądów, konkursów, wystaw i innych wydarzeń filmowych promujących sztukę filmową.",
            "Organizacja kongresów, konferencji, sympozjów i inne działania edukacyjne pogłębiające wiedzę o filmie.",
            "Działalność Sieci Kin Studyjnych.",
            "Inne działania realizujące cele priorytetu."
        ]

        estimate_builder_pt123 = DUKApplicationEstimateBuilder(
            estimate_sections=estimate_sections_pt_123,
            after_name="pt123"
        )
        estimate_builder_pt4 = DUKApplicationEstimateBuilder(
            estimate_sections=estimate_sections_pt_4,
            after_name="pt4"
        )
        self.estimate_chapters = [
            self.create_chapter(
                visibility_rules=[
                    self.visibility_rule.depends_on_value(
                        field_name="projectType",
                        values=[
                            "Organizacja przeglądów, konkursów, wystaw i innych wydarzeń filmowych promujących sztukę filmową.",
                            "Organizacja kongresów, konferencji, sympozjów i inne działania edukacyjne pogłębiające wiedzę o filmie.",
                            "Inne działania realizujące cele priorytetu."
                        ]
                    )
                ],
                components=[
                    estimate_builder_pt123.generate_estimate(),
                ]
            ),
            self.create_chapter(
                visibility_rules=[
                    self.visibility_rule.depends_on_value(
                        field_name="projectType",
                        values=[
                            "Działalność Sieci Kin Studyjnych."
                        ]
                    )
                ],
                components=[
                    estimate_builder_pt4.generate_estimate(),
                ]
            )
        ]

    def create_application_scope_of_project(self):
        pass

    def create_application_attachments(self):
        pass

    def create_application_statements(self):
        pass

    def create_application_schedule(self):
        pass
