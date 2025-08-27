from classes.form_builder.duk.development.application_builder import DevelopmentApplicationBuilder
from classes.form_builder.duk.application_builder import DUKApplicationBuilder
from classes.form_builder.duk.development.digitalization.estimate_data import estimate_sections


class DigitalizationApplicationBuilder(DevelopmentApplicationBuilder):
    PRIORITY_NAME = 'II. Cyfryzacja kin'
    PRIORITY_NUM = 2
    FORM_ID = 9191

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'digitalization'
        self.estimate_sections = estimate_sections

    def create_application_basic_data(self, **kwargs):
        data = {
            'projectType': {
                'options': [
                    "Współfinansowanie zakupu sprzętu do projekcji cyfrowych o minimalnej rozdzielczości 2K w standardzie DCI"
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
        priority_attachments_data_path = self.priority_data_path / '_pages' / 'application_attachments'

        chapter_01 = self.create_chapter(
            title="Obowiązkowe załączniki"
        )
        chapter_02 = self.create_chapter(
            title=""
        )
        chapter_02["components"] = [
            self.create_component(
                component_type='file',
                label="Poświadczenie posiadania finansowego wkładu własnego (np. opinia bankowa o rachunku firmy, wyciąg z konta, umowa z podmiotem współfinansującym)",
                name="attachmentBankOpinion",
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
            self.load_json(path=priority_attachments_data_path / 'attachment_room_pics.json'),
            self.load_json(path=priority_attachments_data_path / 'attachment_right_to_property.json'),
            self.load_json(path=priority_attachments_data_path / 'attachment_deminimis_statement.json'),
            self.load_json(path=attachments_data_path / 'other_attachments.json'),
            self.load_json(path=attachments_data_path / 'storage_of_blanks.json'),
        ]
        self.save_part(part)
