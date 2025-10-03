from .estimate_data import estimate_sections_pt124, estimate_sections_pt3
from classes.form_builder.departments.duk._2026.application_estimate_builder import DUKApplicationEstimateBuilder
from ..priority import ProfessionalTrainingPriority
from ..application_builder import EducationApplicationBuilder


class ProfessionalTrainingApplicationBuilder(EducationApplicationBuilder, ProfessionalTrainingPriority):
    FORM_ID = 9182

    def __init__(self):
        super().__init__()

        self.project_type = [
            "Podnoszenie kwalifikacji i kompetencji zawodowych przedstawicieli wszystkich grup zawodowych sektora audiowizualnego poprzez organizację szkoleń, warsztatów, kursów oraz innych form doskonalenia zawodowego, w tym programów długoterminowych.",
            "Kształcenie w kierunku zdobycia dodatkowych umiejętności i zawodów związanych z potrzebami współczesnego rynku audiowizualnego.",
            "Organizacja kursów nauki języków obcych dla przedstawicieli zawodów filmowych.",
            "Inne działania, realizujące cele Priorytetu III."
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
                            "Podnoszenie kwalifikacji i kompetencji zawodowych przedstawicieli wszystkich grup zawodowych sektora audiowizualnego poprzez organizację szkoleń, warsztatów, kursów oraz innych form doskonalenia zawodowego, w tym programów długoterminowych.",
                            "Kształcenie w kierunku zdobycia dodatkowych umiejętności i zawodów związanych z potrzebami współczesnego rynku audiowizualnego.",
                            "Inne działania, realizujące cele Priorytetu III."
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
                            "Organizacja kursów nauki języków obcych dla przedstawicieli zawodów filmowych."
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
