from classes.form_builder.duk.dissemination.application_builder import DisseminationApplicationBuilder


class ReconstructionApplicationBuilder(DisseminationApplicationBuilder):
    PRIORITY_NAME = 'IV. Rekonstrukcja cyfrowa'
    PRIORITY_NUM = 4

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'reconstruction'

    def create_application_scope_of_project(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'scope_of_the_project.json')
        self.save_part(part)

    def create_application_attachments(self):
        part = self.create_part(
            title="VI. Załączniki",
            short_name="VI. Załączniki"
        )

        attachments_data_path = self.department_data_path / '_pages' / 'application_attachments'

        chapter_01 = self.create_chapter(
            title="Obowiązkowe załączniki"
        )
        chapter_01['components'] = [
            self.load_json(path=attachments_data_path / 'document_confirming_represent_applicant.json'),
            self.load_json(path=attachments_data_path / 'schedule_information.json'),
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

        part['chapters'] = [
            chapter_01,
            self.load_json(path=attachments_data_path / 'other_attachments.json'),
            self.load_json(path=attachments_data_path / 'storage_of_blanks.json'),
        ]
        self.save_part(part)

    def generate(self):
        self.create_application_base()

        # Metadane wniosku
        self.create_application_metadata()

        # I. Dane podstawowe
        self.create_application_basic_data(data={
            'projectType': {
                'options': [
                    "Rekonstrukcja cyfrowa i digitalizacja filmów polskich oraz ich przygotowanie do rozpowszechniania",
                    "Systemowe przedsięwzięcia, mające na celu zabezpieczenie materiałów filmowych"
                ]
            }
        })

        # II. Dane wnioskodawcy
        self.create_application_applicant_data()

        # III. Zakres przedsięwzięcia
        self.create_application_scope_of_project()

        # IV. Źródła finansowania
        self.create_application_sources_of_financing()

        # V. Oświadczenia
        self.create_application_statements()

        # VI. Załączniki
        self.create_application_attachments()

        # VII. Kosztorys przedsięwzięcia

        # VIII. Harmonogram
        self.create_application_schedule()

        self.save_output()
