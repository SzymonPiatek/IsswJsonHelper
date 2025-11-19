from classes_new.form_components.section.dpf.application.application_additional_data import ApplicationAdditionalData
from classes_new.form_components.section.dpf.application.application_applicant_data import ApplicationApplicantData
from classes_new.form_components.section.dpf.application.application_attachments import ApplicationAttachments
from classes_new.form_components.section.dpf.application.application_basic_data import ApplicationBasicData
from classes_new.form_components.section.dpf.application.application_completion_date_data import ApplicationCompletionDateData
from classes_new.form_components.section.dpf.application.application_financial_data import ApplicationFinancialData
from classes_new.form_components.section.dpf.application.application_information_data import ApplicationInformationData
from classes_new.form_components.section.dpf.application.application_metadata import ApplicationMetadata
from classes_new.form_components.section.dpf.application.application_statements import ApplicationStatements
from classes_new.form_components.section.section import Section


class DPFSection(Section):
    def __init__(self, names=None):
        super().__init__(names=names)

        self.application_metadata = ApplicationMetadata(names=self.names)
        self.application_basic_data = ApplicationBasicData(names=self.names)
        self.application_applicant_data = ApplicationApplicantData(names=self.names)
        self.application_information_data = ApplicationInformationData(names=self.names)
        self.application_completion_date_data = ApplicationCompletionDateData(names=self.names)
        self.application_financial_data = ApplicationFinancialData(names=self.names)
        self.application_additional_data = ApplicationAdditionalData(names=self.names)
        self.application_attachments = ApplicationAttachments(names=self.names)
        self.application_statements = ApplicationStatements(names=self.names)
