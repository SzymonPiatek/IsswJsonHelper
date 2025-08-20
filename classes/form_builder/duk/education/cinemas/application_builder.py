from classes.form_builder.duk.education.application_builder import EducationApplicationBuilder
from classes.form_builder.duk.application_builder import DUKApplicationBuilder


class CinemasApplicationBuilder(EducationApplicationBuilder):
    PRIORITY_NAME = 'IV. Edukacja w kinach'
    PRIORITY_NUM = 4
    FORM_ID = 9183

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'cinemas'

    def create_application_basic_data(self, **kwargs):
        data = {
            'projectType': {
                'options': [
                    "cykliczne zajęcia edukacyjne połączone z projekcją filmu o wysokich walorach artystycznych, dotyczące analizy prezentowanego utworu, jego miejsca w historii kinematografii polskiej i/lub światowej, estetyki filmowej i zastosowanych środków wyrazu oraz społecznych funkcji filmu, organizowane w kinach studyjnych, prowadzone w trakcie roku szkolnego",
                    "inne działania realizujące cele Priorytetu V"
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
                            label="Lista filmów pokazywanych podczas zajęć",
                            name="movieListAttachment",
                            validators=[
                                {
                                    "name": "RequiredValidator"
                                }
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type='file',
                            label="Lista szkół biorących udział w przedsięwzięciu (nazwa, adres)",
                            name="schoolsParticipatingAttachment",
                            validators=[
                                {
                                    "name": "RequiredValidator"
                                }
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type='file',
                            label="Program edukacyjny, w tym materiały dydaktyczne",
                            name="educationMaterialsAttachment",
                            validators=[
                                {
                                    "name": "RequiredValidator"
                                }
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type='file',
                            label="Lista prelegentów/edukatorów oraz ich biogramy",
                            name="speakersListAttachment",
                            validators=[
                                {
                                    "name": "RequiredValidator"
                                }
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type='file',
                            label="Szczegółowy wykaz kin studyjnych, w których prowadzone będą zajęcia",
                            name="cinemaListAttachment",
                            validators=[
                                {
                                    "name": "RequiredValidator"
                                }
                            ],
                            required=True
                        )
                    ]
                ),
                self.load_json(path=attachments_data_path / 'other_attachments.json'),
                self.load_json(path=attachments_data_path / 'storage_of_blanks.json'),
            ]
        )

        self.save_part(part)
