from classes_new.form_components.section.dpf.application_additional_data import ApplicationAdditionalData
from classes_new.form_components.section.dpf.application_applicant_data import ApplicationApplicantData
from classes_new.form_components.section.dpf.application_attachments import ApplicationAttachments
from classes_new.form_components.section.dpf.application_basic_data import ApplicationBasicData
from classes_new.form_components.section.dpf.application_completion_date_data import ApplicationCompletionDateData
from classes_new.form_components.section.dpf.application_financial_data import ApplicationFinancialData
from classes_new.form_components.section.dpf.application_information_data import ApplicationInformationData
from classes_new.form_components.section.dpf.application_metadata import ApplicationMetadata
from classes_new.form_components.section.dpf.application_statements import ApplicationStatements
from classes_new.form_components.section.section import Section


class DPFSection(Section):
    def __init__(self):
        super().__init__()

        self.application_metadata = ApplicationMetadata()
        self.application_basic_data = ApplicationBasicData()
        self.application_applicant_data = ApplicationApplicantData()
        self.application_information_data = ApplicationInformationData()
        self.application_completion_date_data = ApplicationCompletionDateData()
        self.application_financial_data = ApplicationFinancialData()
        self.application_additional_data = ApplicationAdditionalData()
        self.application_attachments = ApplicationAttachments()
        self.application_statements = ApplicationStatements()
