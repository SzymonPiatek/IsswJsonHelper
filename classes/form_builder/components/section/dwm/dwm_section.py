from classes.form_builder.components.section.section import Section
from .application_financial_data import ApplicationFinancialData
from .application_name_data import ApplicationNameData
from .application_schedule import ApplicationSchedule


class DWMSection(Section):
    def __init__(self):
        super().__init__()

        self.application_schedule = ApplicationSchedule()
        self.application_name_data = ApplicationNameData()
        self.application_financial_data = ApplicationFinancialData()
