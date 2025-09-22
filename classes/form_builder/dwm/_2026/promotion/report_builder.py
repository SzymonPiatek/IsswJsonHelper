from ..report_builder import DWMReportBuilder2026


class PromotionReportBuilder(DWMReportBuilder2026):
    PRIORITY_NAME = 'I. Promocja polskiej twórczości filmowej za granicą'
    PRIORITY_NUM = 1
    FORM_ID = 9226

    def __init__(self):
        super().__init__()
