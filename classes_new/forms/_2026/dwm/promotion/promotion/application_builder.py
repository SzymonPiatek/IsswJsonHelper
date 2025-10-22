from classes_new.forms._2026.dwm.promotion.application_builder import PromotionOperationalProgramApplicationFormBuilder
from classes_new.forms._2026.dwm.pisf_structure import PromotionPriority


class PromotionPriorityApplicationFormBuilder(PromotionOperationalProgramApplicationFormBuilder):
    def __init__(self):
        super().__init__()

        self.form_id = self.set_ids(
            local_id=16406,
            uat_id=2803
        )

        self.priority = PromotionPriority()
