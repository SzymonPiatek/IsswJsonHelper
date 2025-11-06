from classes_new.forms._2026.dpf.production.application_builder import \
    ProductionOperationalProgramApplicationFormBuilder
from classes_new.forms._2026.dpf.pisf_structure import ScreenplayScholarshipPriority


class ScreenplayScholarshipPriorityApplicationFormBuilder(ProductionOperationalProgramApplicationFormBuilder):
    def __init__(self):
        super().__init__(
            priority=ScreenplayScholarshipPriority()
        )

        self.form_id = self.set_ids(
            local_id=16416,
            uat_id=2830
        )

        self.task_type = "Stypendium scenariuszowe"
