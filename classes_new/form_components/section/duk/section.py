from classes_new.form_components.section.section import Section
from classes_new.form_components.section.duk.application.application_applicant_data import ApplicationApplicantData
from classes_new.form_components.section.duk.application.application_attachment import ApplicationAttachment
from classes_new.form_components.section.duk.application.application_scope_of_project import ApplicationScopeOfProject


class DUKSection(Section):
    def __init__(self):
        super().__init__()

        self.application_attachment = ApplicationAttachment()
        self.application_scope_of_project = ApplicationScopeOfProject()
        self.application_applicant_data = ApplicationApplicantData()
