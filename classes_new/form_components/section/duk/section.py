from classes_new.form_components.section.section import Section
from classes_new.form_components.section.duk.application.application_applicant_data import ApplicationApplicantData
from classes_new.form_components.section.duk.application.application_attachment import ApplicationAttachment
from classes_new.form_components.section.duk.application.application_scope_of_project import ApplicationScopeOfProject


class DUKSection(Section):
    def __init__(self, names=None):
        super().__init__(names=names)

        self.application_attachment = ApplicationAttachment(names=self.names)
        self.application_scope_of_project = ApplicationScopeOfProject(names=self.names)
        self.application_applicant_data = ApplicationApplicantData(names=self.names)
