from classes.form_components.component.component import Component
from .application_attachments import ApplicationAttachments
from .application_statements import ApplicationStatements


class DPFComponent(Component):
    def __init__(self):
        super().__init__()

        self.application_statements = ApplicationStatements()
        self.application_attachments = ApplicationAttachments()
