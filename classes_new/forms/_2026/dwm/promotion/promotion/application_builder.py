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

        self.requested_support_type = [
            "Organizowanie promocyjnych kampanii lub stoisk na międzynarodowych targach, festiwalach oraz innych wydarzeniach branżowych z udziałem polskich twórców filmowych, związanych z polską twórczością filmową zgodnie z ust. 2 pkt 1",
            "Organizowanie promocyjnych kampanii lub stoisk na międzynarodowych targach, festiwalach oraz innych wydarzeniach branżowych z udziałem polskich twórców filmowych, związanych z polską twórczością filmową zgodnie z ust. 2 pkt 2",
            "Organizowanie albo współorganizowanie poza granicami Polski wydarzeń promujących dorobek polskich twórców filmowych oraz polską twórczość filmową, w tym przeglądów, retrospektyw, wystaw, konferencji zgodnie z ust. 2 pkt 3",
            "Organizowanie albo współorganizowanie w Polsce wizyt, spotkań zagranicznych inwestorów, producentów i twórców filmowych, które służą rozwojowi koprodukcji, usług filmowych oraz dystrybucji polskiej twórczości filmowej za granicą zgodnie z ust. 2 pkt 4",
            "Organizowanie albo współorganizowanie z partnerami zagranicznymi wydarzeń dla przedstawicieli branży filmowej w formie szkoleń, warsztatów, prezentacji zgodnie z ust. 2 pkt 5"
        ]
        self.is_promotion_priority = True
