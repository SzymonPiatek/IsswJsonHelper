from classes.form_builder.duk.dissemination.application_builder import DisseminationApplicationBuilder
from classes.form_builder.duk.application_builder import DUKApplicationBuilder


class DocumentaryDistributionApplicationBuilder(DisseminationApplicationBuilder):
    PRIORITY_NAME = 'VI. Dystrybucja filmów dokumentalnych'
    PRIORITY_NUM = 6
    FORM_ID = 2601

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'documentary_distribution'

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
            short_name="VI. Załączniki"
        )

        attachments_data_path = self.department_data_path / '_pages' / 'application_attachments'

        chapter_01 = self.create_chapter(
            title="Obowiązkowe załączniki"
        )
        chapter_02 = self.create_chapter(
            title=""
        )

        chapter_02['components'] = [
            self.create_component(
                component_type='file',
                label="Umowa potwierdzająca prawa do dystrybucji filmu, zawierająca w szczególności postanowienia w zakresie przeniesienia praw albo udzielenia licencji wyłącznej na polu eksploatacji publicznego wyświetlania w kinach",
                name="agreementConfirmingRights",
                validators=[
                    {
                        "name": "RequiredValidator"
                    }
                ],
                required=True
            ),
            self.create_component(
                component_type='file',
                label="Podział przychodów i zysków z dystrybucji, o ile umowa potwierdzająca prawa do dystrybucji nie zawiera wyżej wymienionych informacji",
                name="divisionRevenuesAndProfits",
                validators=[
                    {
                        "name": "RequiredValidator"
                    }
                ],
                required=True
            )
        ]

        part['chapters'] = [
            chapter_01,
            self.load_json(path=attachments_data_path / 'document_confirming_represent_applicant.json'),
            self.load_json(path=attachments_data_path / 'schedule_information.json'),
            chapter_02,
            self.load_json(path=attachments_data_path / 'other_attachments.json'),
            self.load_json(path=attachments_data_path / 'storage_of_blanks.json'),
        ]
        self.save_part(part)
