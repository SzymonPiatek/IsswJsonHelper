from .estimate_data import estimate_sections
from classes.form_builder.departments.duk._2026.application_estimate_builder import DUKApplicationEstimateBuilder
from ..priority import HigherSchoolsPriority
from ..application_builder import EducationApplicationBuilder


class HigherSchoolsApplicationBuilder(EducationApplicationBuilder, HigherSchoolsPriority):
    FORM_ID = 9180

    def __init__(self):
        super().__init__()

        self.project_type = [
            "Programy edukacyjne wchodzące w skład edukacji ciągłej.",
            "Realizacja szkolnych i pozaszkolnych filmów krótko- i średniometrażowych.",
            "Kształcenie zawodowe i podnoszenie kompetencji poprzez organizację studiów podyplomowych.",
            "Inne działania realizujące cele Priorytetu I."
        ]

        estimate_builder = DUKApplicationEstimateBuilder(estimate_sections=estimate_sections)
        self.estimate_chapters = [
            estimate_builder.generate_estimate()
        ]

    def create_application_attachments(self, number):
        pass

    def create_application_schedule(self, number):
        pass
