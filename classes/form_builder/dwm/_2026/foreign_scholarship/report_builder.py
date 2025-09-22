from ..report_builder import DWMReportBuilder2026


class ForeignScholarshipReportBuilder(DWMReportBuilder2026):
    PRIORITY_NAME = 'II. Stypendia zagraniczne'
    PRIORITY_NUM = 2
    FORM_ID = 9227

    def __init__(self):
        super().__init__()
