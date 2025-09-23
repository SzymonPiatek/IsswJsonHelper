from .priority import PromotionPriority
from ..report_builder import DWMReportBuilder2026


class PromotionReportBuilder(DWMReportBuilder2026, PromotionPriority):
    FORM_ID = 9226

    def __init__(self):
        super().__init__()

    def create_report_base(self):
        self.create_base(
            intro_text=[
                "Raport końcowy",
                "<small>z wykonania przedsięwzięcia realizowanego w ramach Programu Operacyjnego \"Promocja polskiej twórczości filmowej za granicą\"</small> <br> Priorytet I \"Promocja polskiej twórczości filmowej za granicą\""
            ]
        )

    def create_report_basic_data(self):
        part = self.create_part(
            title="I. Dane podstawowe",
            short_name="I. Dane podstawowe",
            chapters=[
                self.section.report_basic_data.project_implementation_period(number="A"),
                self.section.report_basic_data.agreement_and_annex(number="B"),
                self.section.report_basic_data.grantee_name_and_address(number="C")
            ]
        )

        self.save_part(part)
