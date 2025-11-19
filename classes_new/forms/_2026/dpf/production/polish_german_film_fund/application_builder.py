from classes_new.forms._2026.dpf.production.application_builder import \
    ProductionOperationalProgramApplicationFormBuilder
from classes_new.forms._2026.dpf.pisf_structure import PolishGermanFilmFundPriority


class PolishGermanFilmFundPriorityApplicationFormBuilder(ProductionOperationalProgramApplicationFormBuilder):
    def __init__(self):
        super().__init__(
            priority=PolishGermanFilmFundPriority()
        )

        self.form_id = self.set_ids(
            local_id=16444,
            uat_id=None
        )
