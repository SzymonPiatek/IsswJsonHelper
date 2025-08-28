from classes.form_builder.duk.education.application_builder import EducationApplicationBuilder
from classes.form_builder.duk.application_builder import DUKApplicationBuilder
from classes.form_builder.duk.education.cinemas.estimate_data import estimate_sections


class CinemasApplicationBuilder(EducationApplicationBuilder):
    PRIORITY_NAME = 'IV. Edukacja w kinach'
    PRIORITY_NUM = 4
    FORM_ID = 9183

    def __init__(self):
        super().__init__()

        self.estimate_sections = estimate_sections

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
                                    label="Lista filmów pokazywanych podczas zajęć",
                                    name="movieListAttachment",
                                    required=True
                                ),
                                self.create_component(
                                    component_type='file',
                                    label="Lista szkół biorących udział w przedsięwzięciu (nazwa, adres)",
                                    name="schoolsParticipatingAttachment",
                                    required=True
                                ),
                                self.create_component(
                                    component_type='file',
                                    label="Program edukacyjny, w tym materiały dydaktyczne",
                                    name="educationMaterialsAttachment",
                                    required=True
                                ),
                                self.create_component(
                                    component_type='file',
                                    label="Lista prelegentów/edukatorów oraz ich biogramy",
                                    name="speakersListAttachment",
                                    required=True
                                ),
                                self.create_component(
                                    component_type='file',
                                    label="Szczegółowy wykaz kin studyjnych, w których prowadzone będą zajęcia",
                                    name="cinemaListAttachment",
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
        basic_number_data_chapters = [
            {
                "section_title": "1. Liczba zajęć edukacyjnych",
                "name": "educationalActivities",
                "unit": "szt."
            },
            {
                "section_title": "2. Liczba uczestników (uczniów szkół podstawowych)",
                "name": "primarySchoolPupils",
                "unit": "os."
            },
            {
                "section_title": "3. Liczba uczestników (uczniów szkół ponadpodstawowych)",
                "name": "secondarySchoolPupils",
                "unit": "os."
            },
            {
                "section_title": "4. Liczba szkół podstawowych uczestniczących w przedsięwzięciu",
                "name": "primarySchools",
                "unit": "szt."
            },
            {
                "section_title": "5. Liczba szkół ponadpodstawowych uczestniczących w przedsięwzięciu",
                "name": "secondarySchools",
                "unit": "szt."
            }
        ]

        last_chapter = self.section.application_scope_of_project.cinema_project_relation_to_other_fundings()
        last_chapter["title"] = "Czy przedsięwzięcie, na które składany jest wniosek jest powiązane z innymi przedsięwzięciami, o dofinansowanie których ubiega się wnioskodawca w bieżącym roku z innych programów operacyjnych PISF? Jeżeli tak, proszę podać nazwę przedsięwzięcia, program oraz wnioskowaną kwotę dofinansowania"

        data = {
            "chapters": [
                self.create_chapter(
                    title="7. Podstawowe dane liczbowe na temat bieżącej i poprzedniej edycji",
                    class_list={
                        "sub": [
                            "table-1-2-top"
                        ]
                    },
                    components=[
                        *[self.create_chapter(
                            title=f"<normal>{chapter["section_title"]}</normal>",
                            class_list={
                                "main": [
                                    "table-1-2",
                                    "grid",
                                    "grid-cols-2"
                                ],
                                "sub": [
                                    "table-1-2__col"
                                ]
                            },
                            components=[
                                self.create_component(
                                    component_type='number',
                                    label="Poprzednia edycja przedsięwzięcia",
                                    unit=chapter["unit"],
                                    name=f'{chapter["name"]}CountPreviousEdition'
                                ),
                                self.create_component(
                                    component_type='number',
                                    label="Bieżąca edycja przedsięwzięcia (przewidywane wielkości)",
                                    unit=chapter["unit"],
                                    name=f'{chapter["name"]}CountCurrentEdition'
                                )
                            ]
                        ) for chapter in basic_number_data_chapters]
                    ]
                ),
                last_chapter
            ],
            "project_detailed_description_chapters": [
                {
                    "section_title": "Wartość merytoryczna przedsięwzięcia, w tym ciągłość realizacji przedsięwzięcia oraz wartość edukacyjna",
                    "name": "scopeAndValueOfContent"
                },
                {
                    "section_title": "Planowane efekty realizacji przedsięwzięcia oraz jego ewaluacja",
                    "name": "plannedResultsOfProject"
                }
            ]
        }

        EducationApplicationBuilder.create_application_scope_of_project(
            self, data=data
        )
