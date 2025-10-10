from classes.helpers import int_to_roman
from .estimate_data import estimate_sections
from classes.form_builder.departments.duk._2026.application_estimate_builder import DUKApplicationEstimateBuilder
from ..priority import AudiencePriority
from ..application_builder import EducationApplicationBuilder


class AudienceApplicationBuilder(EducationApplicationBuilder, AudiencePriority):
    FORM_ID = 19

    def __init__(self):
        super().__init__()

        self.project_type = [
            "Cykliczne zajęcia edukacyjne połączone z projekcją filmu o wysokich walorach artystycznych, dotyczące analizy prezentowanego utworu, jego miejsca w historii kinematografii polskiej i/lub światowej, estetyki filmowej i zastosowanych środków wyrazu oraz społecznych funkcji filmu, organizowane w kinach lub innych salach przygotowanych do projekcji filmu.",
            "Niecykliczne zajęcia, warsztaty wzbogacone materiałami dydaktycznymi o wysokiej wartości merytorycznej, zgodne z obowiązującą podstawą programową nauczania.",
            "Inne działania realizujące cele Priorytetu IV."
        ]

        estimate_builder = DUKApplicationEstimateBuilder(estimate_sections=estimate_sections)
        self.estimate_chapters = [
            estimate_builder.generate_estimate()
        ]

        self.is_basic_number_data = True

    def create_application_scope_of_project(self, number):
        part = self.create_part(
            title=f"{int_to_roman(number)}. Zakres przedsięwzięcia i jego charakterystyka",
            short_name=f"{int_to_roman(number)}. Zakres przedsięwzięcia",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            label="Miejsce realizacji przedsięwzięcia",
                            name="projectLocation",
                            component_type="textarea",
                            validators=[
                                self.validator.length_validator(
                                    max_value=3000
                                )
                            ],
                            required=True
                        ),
                        self.create_component(
                            label="Opis ogólny przedsięwzięcia",
                            name="generalProjectDescription",
                            component_type="textarea",
                            validators=[
                                self.validator.length_validator(
                                    max_value=3000
                                )
                            ],
                            required=True,
                            help_text="Cel i zakres merytoryczny, zastosowane technologie, sposób realizacji przedsięwzięcia, promocja."
                        ),
                        self.create_component(
                            component_type="textarea",
                            name="offerEducationalValue",
                            label="Wartość edukacyjna przedsięwzięcia",
                            validators=[
                                self.validator.length_validator(
                                    max_value=3000
                                )
                            ],
                            required=True,
                            help_text="W tym ciągłość realizacji oraz wartość edukacyjna przedsięwzięcia."
                        ),
                        self.create_component(
                            component_type="textarea",
                            name="skillsAcquiredByStudents",
                            label="Praktyczne umiejętności nabywane przez uczestników",
                            validators=[
                                self.validator.length_validator(
                                    max_value=3000
                                )
                            ],
                            required=True,
                        ),
                        self.create_component(
                            component_type="textarea",
                            name="numberAndDiversityOfStudents",
                            label="Liczba i zróżnicowanie struktury studentów",
                            validators=[
                                self.validator.length_validator(
                                    max_value=3000
                                )
                            ],
                            required=True,
                        ),
                        self.create_component(
                            component_type="textarea",
                            name="plannedImplementationAndEvaluationEffects",
                            label="Planowane efekty realizacji przedsięwzięcia oraz jego ewaluacja",
                            validators=[
                                self.validator.length_validator(
                                    max_value=3000
                                )
                            ],
                            required=True,
                        ),
                        self.create_component(
                            component_type="textarea",
                            name="applicantAndTeamExperience",
                            label="Doświadczenie wnioskodawcy i kompetencje zespołu",
                            help_text="Proszę o wyszczególnienie przedsięwzięć z zakresu kinematografii realizowanych przez wnioskodawcę w ostatnich 2 latach.",
                            validators=[
                                self.validator.length_validator(
                                    max_value=3000
                                )
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="textarea",
                            name="projectAccessibility",
                            label="Dostępność przedsięwzięcia",
                            help_text="Działania podejmowane na rzecz osób ze szczególnymi potrzebami oraz wspierania inkluzywności.",
                            validators=[
                                self.validator.length_validator(
                                    max_value=3000
                                )
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Czy przedsięwzięcie, na które składany jest wniosek jest powiązane z innymi przedsięwzięciami, o dofinansowanie których ubiega się Wnioskodawca w bieżącym roku z innych programów operacyjnych PISF? Jeżeli tak, proszę podać nazwę przedsięwzięcia, program oraz wnioskowaną kwotę dofinansowania",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    name="wasSubmittedBefore",
                                    options=["Tak", "Nie"],
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="wasSubmittedBefore",
                                    values=["Tak"])
                            ],
                            multiple_forms_rules={"minCount": 1, "maxCount": 20},
                            components=[
                                self.create_chapter(
                                    class_list=["grid", "grid-cols-3"],
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            label="Nazwa przedsięwzięcia",
                                            name="otherProjectName"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Program operacyjny",
                                            name="programmeName"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Wnioskowana kwota",
                                            name="otherProjectFundingAmount",
                                            unit="PLN",
                                            mask="fund"
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )

        self.save_part(part)

    def create_application_basic_number_data(self, number):
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

        part = self.create_part(
            title=f"{int_to_roman(number)}. Podstawowe dane liczbowe i wskaźniki",
            short_name=f"{int_to_roman(number)}. Dane liczbowe",
            chapters=[
                self.create_chapter(
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
                )
            ]
        )
        self.save_part(part)

    def create_application_attachments(self, number):
        part = self.create_part(
            title=f"{int_to_roman(number)}. Załączniki",
            short_name=f"{int_to_roman(number)}. Załączniki",
            chapters=[
                self.create_chapter(
                    title="Obowiązkowe załączniki",
                    components=[
                        self.section.application_attachment.document_confirming_represent_applicant(),
                        self.section.application_attachment.schedule_information()
                    ]
                ),
                self.create_chapter(
                    title="1. Lista filmów pokazywanych podczas zajęć",
                    components=[
                        self.create_component(
                            component_type="file",
                            name="movieListAttachment",
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Lista szkół biorących udział w przedsięwzięciu (nazwa, adres)",
                    components=[
                        self.create_component(
                            component_type="file",
                            name="schoolsParticipatingAttachment",
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="3. Program edukacyjny, w tym materiały dydaktyczne",
                    components=[
                        self.create_component(
                            component_type="file",
                            name="educationMaterialsAttachment",
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="4. Lista prelegentów/edukatorów oraz ich biogramy",
                    components=[
                        self.create_component(
                            component_type="file",
                            name="cinemaListAttachment",
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="5. Szczegółowy wykaz kin studyjnych,w których prowadzone będą zajęcia",
                    components=[
                        self.create_component(
                            component_type="file",
                            name="detailedListOfCinemas",
                            required=True
                        )
                    ]
                ),
                self.section.application_attachment.other_attachments(),
                self.section.application_attachment.storage_of_blanks()
            ]
        )
        self.save_part(part)
