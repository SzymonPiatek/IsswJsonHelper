from classes_new.forms._2026.duk.development.application_builder import \
    DevelopmentOperationalProgramApplicationFormBuilder
from classes_new.forms._2026.duk.pisf_structure import ModernizationPriority
from classes_new.forms._2026.duk.estimate.application_estimate_builder import DUKApplicationEstimateBuilder
from .estimate_data import estimate_sections


class ModernizationPriorityApplicationFormBuilder(DevelopmentOperationalProgramApplicationFormBuilder):
    def __init__(self):
        super().__init__(
            priority=ModernizationPriority()
        )

        self.form_id = self.set_ids(
            local_id=26,
            uat_id=None
        )

        self.project_type = [
            "Współfinansowanie zakupu i modernizacji wyposażenia do prowadzenia lub rozpoczęcia działalności kinowej, w tym sprzętu umożliwiającego odbiór filmów przez osoby ze szczególnymi potrzebami."
        ]

        estimate_builder = DUKApplicationEstimateBuilder(estimate_sections=estimate_sections)
        self.estimate_chapters = [
            estimate_builder.generate_estimate()
        ]
