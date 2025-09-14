from classes.form_builder.components.section.section import Section
from classes.form_builder.components.section.dpf.application_basic_data import ApplicationBasicData
from classes.form_builder.components.section.dpf.application_statements import ApplicationStatements
from classes.form_builder.components.section.dpf.application_attachments import ApplicationAttachments
from classes.form_builder.components.section.dpf.application_information_data import ApplicationInformationData
from classes.form_builder.components.section.dpf.application_completion_date_data import ApplicationCompletionDateData


class DPFSection(Section):
    def __init__(self):
        super().__init__()

        self.application_basic_data = ApplicationBasicData()
        self.application_statements = ApplicationStatements()
        self.application_attachments = ApplicationAttachments()
        self.application_information_data = ApplicationInformationData()
        self.application_completion_date_data = ApplicationCompletionDateData()
