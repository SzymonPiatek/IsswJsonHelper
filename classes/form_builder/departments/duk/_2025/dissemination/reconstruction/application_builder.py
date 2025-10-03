from classes.form_builder.departments.duk._2025.dissemination.application_builder import DisseminationApplicationBuilder
from classes.form_builder.departments.duk.application_builder import DUKApplicationBuilder
from classes.form_builder.departments.duk._2025.dissemination.reconstruction.estimate_data import estimate_sections


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
        part = self.create_part(
            title="III. Zakres przedsięwzięcia i jego charakterystyka",
            short_name="III. Zakres przedsięwięcia",
            chapters=[
                self.create_chapter(
                    title="Miejsce realizacji i rodzaj organizowanego przedsięwzięcia",
                    components=[
                        self.create_chapter(
                            components=[
                                self.component.project_location()
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Cel i zakres merytoryczny przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="projectGoalAndScope",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Dotychczasowe doświadczenia Wnioskodawcy w działaniach będących przedmiotem przedsięwzięcia. </br><normal>Proszę o wyszczególnienie przedsięwzięć z zakresu kinematografii realizowanych przez Wnioskodawcę w ostatnich 2 latach, o budżecie przekraczającym 50 000 zł</normal>",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="granteeExperience",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Partnerzy, eksperci i specjaliści zaangażowani w przedsięwzięcie i ich dotychczasowy dorobek w tym zakresie (z wyszczególnieniem stopni i tytułów naukowych oraz afiliacji instytucjonalnych)",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="projectCooperators",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True
                        )
                    ]
                ),
            ]
        )
        self.save_part(part)
