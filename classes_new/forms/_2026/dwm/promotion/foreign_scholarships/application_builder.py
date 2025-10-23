from classes_new.forms._2026.dwm.pisf_structure import ForeignScholarshipsPriority
from classes_new.forms._2026.dwm.promotion.application_builder import PromotionOperationalProgramApplicationFormBuilder


class ForeignPriorityApplicationFormBuilder(PromotionOperationalProgramApplicationFormBuilder):
    def __init__(self):
        super().__init__()

        self.form_id = self.set_ids(
            local_id=0,
            uat_id=0
        )

        self.priority = ForeignScholarshipsPriority()
