from classes.form_builder.duk.education.application_builder import EducationApplicationBuilder


class CinemasApplicationBuilder(EducationApplicationBuilder):
    PRIORITY_NAME = 'IV. Edukacja w kinach'
    PRIORITY_NUM = 4

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'cinemas'

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
        chapter_02 = self.create_chapter(
            title=""
        )

        chapter_02['components'] = [
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
        ],

        part['chapters'] = [
            chapter_01,
            self.load_json(path=attachments_data_path / 'document_confirming_represent_applicant.json'),
            self.load_json(path=attachments_data_path / 'schedule_information.json'),
            chapter_02,
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
                    "cykliczne zajęcia edukacyjne połączone z projekcją filmu o wysokich walorach artystycznych, dotyczące analizy prezentowanego utworu, jego miejsca w historii kinematografii polskiej i/lub światowej, estetyki filmowej i zastosowanych środków wyrazu oraz społecznych funkcji filmu, organizowane w kinach studyjnych, prowadzone w trakcie roku szkolnego",
                    "inne działania realizujące cele Priorytetu V"
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
