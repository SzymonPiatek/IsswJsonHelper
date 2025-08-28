from classes.form_builder.duk.dissemination.application_builder import DisseminationApplicationBuilder
from classes.form_builder.duk.application_builder import DUKApplicationBuilder
from classes.form_builder.duk.dissemination.reconstruction.estimate_data import estimate_sections


class ReconstructionApplicationBuilder(DisseminationApplicationBuilder):
    PRIORITY_NAME = 'IV. Rekonstrukcja cyfrowa'
    PRIORITY_NUM = 4
    FORM_ID = 9187

    def __init__(self):
        super().__init__()

        self.estimate_sections = estimate_sections

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
                            title="",
                            components=[
                                self.create_component(
                                    component_type='file',
                                    label="Dokument zaświadczający o posiadaniu praw do digitalizacji/rekonstrukcji filmu",
                                    name="attachmentDigitalizationRights",
                                    required=True
                                ),
                                self.create_component(
                                    component_type='file',
                                    label="Diagnoza stanu technicznego taśmy światłoczułej, w przypadku filmów fabularnych przeprowadzona przez Filmotekę Narodową – Instytut Audiowizualny (w przypadku braku wymaganego dokumentu Wnioskodawca zobowiązany jest do dołączenia oświadczenia, w którym zobowiązuje się do dostarczenia dokumentu)",
                                    name="attachmentTechnicalCondition",
                                    required=True
                                ),
                                self.create_component(
                                    component_type='file',
                                    label="Umowa między Wnioskodawcą a właścicielem praw do digitalizowanego filmu/filmów",
                                    name="attachmentOwnerContract",
                                    required=True
                                ),
                            ]
                        ),
                    ]
                ),
                self.section.application_attachment.other_attachments(),
                self.section.application_attachment.storage_of_blanks()
            ]
        )

        self.save_part(part)

    def create_application_scope_of_project(self):
        pass
