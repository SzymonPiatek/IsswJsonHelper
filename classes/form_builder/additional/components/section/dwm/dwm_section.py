from classes.form_builder.additional.components.section.dwm.report.report_basic_data import ReportBasicData
from classes.form_builder.additional.components.section.section import Section
from classes.form_builder.additional.components.section.dwm.application.application_applicant_data import ApplicationApplicantData
from classes.form_builder.additional.components.section.dwm.application.application_financial_data import ApplicationFinancialData
from classes.form_builder.additional.components.section.dwm.application.application_name_data import ApplicationNameData
from classes.form_builder.additional.components.section.dwm.application.application_schedule import ApplicationSchedule


class DWMSection(Section):
    def __init__(self):
        super().__init__()

        # APPLICATION
        self.application_schedule = ApplicationSchedule()
        self.application_name_data = ApplicationNameData()
        self.application_financial_data = ApplicationFinancialData()
        self.application_applicant_data = ApplicationApplicantData()

        # REPORT
        self.report_basic_data = ReportBasicData()

