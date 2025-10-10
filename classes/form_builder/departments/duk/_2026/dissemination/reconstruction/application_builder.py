from classes.form_builder.departments.duk._2026.dissemination.application_builder import DisseminationApplicationBuilder
from .estimate_data import estimate_sections
from classes.form_builder.departments.duk._2026.application_estimate_builder import DUKApplicationEstimateBuilder
from ..priority import ReconstructionPriority


class ReconstructionApplicationBuilder(DisseminationApplicationBuilder, ReconstructionPriority):
    FORM_ID = 9187

    def __init__(self):
        super().__init__()

        self.project_type = [
            "Rekonstrukcja cyfrowa i digitalizacja filmów polskich oraz ich przygotowanie do rozpowszechniania.",
            "Systemowe przedsięwzięcia, mające na celu zabezpieczenie materiałów filmowych."
        ]

        estimate_builder = DUKApplicationEstimateBuilder(estimate_sections=estimate_sections)
        self.estimate_chapters = [
            estimate_builder.generate_estimate()
        ]

    def create_application_scope_of_project(self, number):
        pass

    def create_application_attachments(self, number):
        pass

    def create_application_schedule(self, number):
        pass
