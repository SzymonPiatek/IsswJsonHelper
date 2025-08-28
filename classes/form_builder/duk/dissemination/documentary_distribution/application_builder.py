from classes.form_builder.duk.dissemination.application_builder import DisseminationApplicationBuilder
from classes.form_builder.duk.application_builder import DUKApplicationBuilder
from classes.form_builder.duk.dissemination.documentary_distribution.estimate_data import estimate_sections


class DocumentaryDistributionApplicationBuilder(DisseminationApplicationBuilder):
    PRIORITY_NAME = 'VI. Dystrybucja filmów dokumentalnych'
    PRIORITY_NUM = 6
    FORM_ID = 9189

    def __init__(self):
        super().__init__()

        self.estimate_sections = estimate_sections

    def create_application_basic_data(self, **kwargs):
        data = {
            'projectType': {
                'options': [
                    "Dystrybucja kinowa pełnometrażowych filmów dokumentalnych na terenie Polski"
                ]
            }
        }
        DUKApplicationBuilder.create_application_basic_data(self=self, data=data)

    def create_application_attachments(self):
        part = self.create_part(
            title="VI. Załączniki",
            short_name="VI. Załączniki",
            chapters=[
                self.create_chapter(
                    title="Obowiązkowe załączniki",
                    components=[
                        self.section.application_attachment.document_confirming_represent_applicant(),
                        self.section.application_attachment.schedule_information(),
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type='file',
                                    label="Umowa potwierdzająca prawa do dystrybucji filmu, zawierająca w szczególności postanowienia w zakresie przeniesienia praw albo udzielenia licencji wyłącznej na polu eksploatacji publicznego wyświetlania w kinach",
                                    name="agreementConfirmingRights",
                                    required=True
                                ),
                                self.create_component(
                                    component_type='file',
                                    label="Podział przychodów i zysków z dystrybucji, o ile umowa potwierdzająca prawa do dystrybucji nie zawiera wyżej wymienionych informacji",
                                    name="divisionRevenuesAndProfits",
                                    required=True
                                )
                            ]
                        )
                    ]
                ),
                self.section.application_attachment.other_attachments(),
                self.section.application_attachment.storage_of_blanks()
            ]
        )
        self.save_part(part)

    def create_application_scope_of_project(self):
        pass
