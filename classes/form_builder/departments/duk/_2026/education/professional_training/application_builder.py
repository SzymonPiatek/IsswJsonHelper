from .estimate_data import estimate_sections
from classes.form_builder.departments.duk._2026.application_estimate_builder import DUKApplicationEstimateBuilder
from ..priority import ProfessionalTrainingPriority
from ..application_builder import EducationApplicationBuilder


class ProfessionalTrainingApplicationBuilder(EducationApplicationBuilder, ProfessionalTrainingPriority):
    FORM_ID = 9182

    def __init__(self):
        super().__init__()

        self.project_type = [
            ""
        ]

        estimate_builder = DUKApplicationEstimateBuilder(estimate_sections=estimate_sections)
        self.estimate_chapters = [
            estimate_builder.generate_estimate()
        ]

    def create_application_scope_of_project(self):
        pass

    def create_application_attachments(self):
        pass

    def create_application_statements(self):
        pass

    def create_application_schedule(self):
        pass
