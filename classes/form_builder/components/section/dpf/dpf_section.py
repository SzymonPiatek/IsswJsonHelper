from classes.form_builder.components.section.section import Section
from .application_basic_data import ApplicationBasicData
from .application_statements import ApplicationStatements
from .application_attachments import ApplicationAttachments
from .application_information_data import ApplicationInformationData
from .application_completion_date_data import ApplicationCompletionDateData
from .application_additional_data import ApplicationAdditionalData


class DPFSection(Section):
    def __init__(self):
        super().__init__()

        self.application_basic_data = ApplicationBasicData()
        self.application_statements = ApplicationStatements()
        self.application_attachments = ApplicationAttachments()
        self.application_information_data = ApplicationInformationData()
        self.application_completion_date_data = ApplicationCompletionDateData()
        self.application_additional_data = ApplicationAdditionalData()
