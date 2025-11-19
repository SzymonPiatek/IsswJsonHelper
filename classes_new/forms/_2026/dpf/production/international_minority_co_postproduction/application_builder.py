from classes_new.forms._2026.dpf.production.application_builder import \
    ProductionOperationalProgramApplicationFormBuilder
from classes_new.forms._2026.dpf.pisf_structure import InternationalMinorityCoPostproductionPriority


class InternationalMinorityCoPostproductionPriorityApplicationFormBuilder(ProductionOperationalProgramApplicationFormBuilder):
    def __init__(self):
        super().__init__(
            priority=InternationalMinorityCoPostproductionPriority()
        )

        self.form_id = self.set_ids(
            local_id=16442,
            uat_id=None
        )
