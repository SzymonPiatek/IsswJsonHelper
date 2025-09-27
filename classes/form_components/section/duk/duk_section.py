from classes.form_components.section.section import Section
from .application_attachment import ApplicationAttachment
from .application_scope_of_project import ApplicationScopeOfProject


class DUKSection(Section):
    def __init__(self):
        super().__init__()

        self.application_attachment = ApplicationAttachment()
        self.application_scope_of_project = ApplicationScopeOfProject()
