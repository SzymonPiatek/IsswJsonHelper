from classes_new.forms._2026.dpf.production.application_builder import \
    ProductionOperationalProgramApplicationFormBuilder
from classes_new.forms._2026.dpf.pisf_structure import FeaturedFilmProductionPriority


class FeaturedFilmProductionPriorityApplicationFormBuilder(ProductionOperationalProgramApplicationFormBuilder):
    def __init__(self):
        super().__init__(
            priority=FeaturedFilmProductionPriority()
        )

        self.form_id = self.set_ids(
            local_id=16439,
            uat_id=None
        )
