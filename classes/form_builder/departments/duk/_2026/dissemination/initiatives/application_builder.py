from classes.form_builder.departments.duk._2026.dissemination.application_builder import DisseminationApplicationBuilder
from .estimate_data import estimate_sections_pt124, estimate_sections_pt3
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
            "Inne działania realizujące cele Priorytetu II."
        ]

        estimate_builder_pt124 = DUKApplicationEstimateBuilder(
            estimate_sections=estimate_sections_pt124,
            after_name="pt124"
        )
        estimate_builder_pt3 = DUKApplicationEstimateBuilder(
            estimate_sections=estimate_sections_pt3,
            after_name="pt3"
        )
        self.estimate_chapters = [
            self.create_chapter(
                visibility_rules=[
                    self.visibility_rule.depends_on_value(
                        field_name="projectType",
                        values=[
                            "Organizacja przeglądów, konkursów, wystaw i innych wydarzeń filmowych promujących sztukę filmową.",
                            "Organizacja kongresów, konferencji, sympozjów i inne działania edukacyjne pogłębiające wiedzę o filmie.",
                            "Inne działania realizujące cele Priorytetu II."
                        ]
                    )
                ],
                components=[
                    estimate_builder_pt124.generate_estimate(),
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
                    estimate_builder_pt3.generate_estimate(),
                ]
            )
        ]

    def create_application_scope_of_project(self, number):
        pass

    def create_application_attachments(self, number):
        pass

    def create_application_statements(self, number):
        pass

    def create_application_schedule(self, number):
        pass
