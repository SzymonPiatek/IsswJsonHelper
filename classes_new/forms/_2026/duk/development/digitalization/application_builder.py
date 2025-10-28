from classes_new.forms._2026.duk.development.application_builder import DevelopmentOperationalProgramApplicationFormBuilder
from classes_new.forms._2026.duk.pisf_structure import DigitalizationPriority
from classes_new.forms._2026.duk.estimate.application_estimate_builder import DUKApplicationEstimateBuilder
from .estimate_data import estimate_sections


class DigitalizationPriorityApplicationFormBuilder(DevelopmentOperationalProgramApplicationFormBuilder):
    def __init__(self):
        super().__init__(
            priority=DigitalizationPriority()
        )

        self.form_id = self.set_ids(
            local_id=27,
            uat_id=None
        )

        # Variables
        self.project_type = [
            "Współfinansowanie zakupu sprzętu do projekcji cyfrowych o minimalnej rozdzielczości 2K w standardzie DCI."
        ]

        # Estimate
        estimate_builder = DUKApplicationEstimateBuilder(estimate_sections=estimate_sections)
        self.estimate_chapters = [
            estimate_builder.generate_estimate()
        ]
