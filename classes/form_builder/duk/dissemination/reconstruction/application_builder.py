from classes.form_builder.duk.dissemination.application_builder import DisseminationApplicationBuilder
from classes.form_builder.duk.application_builder import DUKApplicationBuilder


class ReconstructionApplicationBuilder(DisseminationApplicationBuilder):
    PRIORITY_NAME = 'IV. Rekonstrukcja cyfrowa'
    PRIORITY_NUM = 4
    FORM_ID = 9187

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'reconstruction'

    def create_application_basic_data(self, **kwargs):
        data = {
            'projectType': {
                'options': [
                    "Rekonstrukcja cyfrowa i digitalizacja filmów polskich oraz ich przygotowanie do rozpowszechniania",
                    "Systemowe przedsięwzięcia, mające na celu zabezpieczenie materiałów filmowych"
                ]
            }
        }
        DUKApplicationBuilder.create_application_basic_data(self=self, data=data)

    def create_application_attachments(self):
        attachments_data_path = self.department_data_path / '_pages' / 'application_attachments'

        part = self.create_part(
            title="VI. Załączniki",
            short_name="VI. Załączniki",
            chapters=[
                self.create_chapter(
                    title="Obowiązkowe załączniki"
                ),
                self.load_json(path=attachments_data_path / 'document_confirming_represent_applicant.json'),
                self.load_json(path=attachments_data_path / 'schedule_information.json'),
                self.create_chapter(
                    title="",
                    components=[
                        self.create_component(
                            component_type='file',
                            label="Dokument zaświadczający o posiadaniu praw do digitalizacji/rekonstrukcji filmu",
                            name="attachmentDigitalizationRights",
                            validators=[
                                {
                                    "name": "RequiredValidator"
                                }
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type='file',
                            label="Diagnoza stanu technicznego taśmy światłoczułej, w przypadku filmów fabularnych przeprowadzona przez Filmotekę Narodową – Instytut Audiowizualny (w przypadku braku wymaganego dokumentu Wnioskodawca zobowiązany jest do dołączenia oświadczenia, w którym zobowiązuje się do dostarczenia dokumentu)",
                            name="attachmentTechnicalCondition",
                            validators=[
                                {
                                    "name": "RequiredValidator"
                                }
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type='file',
                            label="Umowa między Wnioskodawcą a właścicielem praw do digitalizowanego filmu/filmów",
                            name="attachmentOwnerContract",
                            validators=[
                                {
                                    "name": "RequiredValidator"
                                }
                            ],
                            required=True
                        ),
                    ]
                ),
                self.load_json(path=attachments_data_path / 'other_attachments.json'),
                self.load_json(path=attachments_data_path / 'storage_of_blanks.json'),
            ]
        )

        self.save_part(part)
