from classes.helpers import int_to_roman
from .estimate_data import estimate_sections
from classes.form_builder.departments.duk._2026.estimate.application_estimate_builder import DUKApplicationEstimateBuilder
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

    def create_application_scope_of_project(self, number):
        part = self.create_part(
            title=f"{int_to_roman(number)}. Zakres przedsięwzięcia i jego charakterystyka",
            short_name=f"{int_to_roman(number)}. Zakres przedsięwzięcia",
            chapters=[
                self.create_chapter(
                    title="1. Zakres przedsięwzięcia i jego charakterystyka",
                    components=[
                        self.create_chapter(
                            title="Rodzaj planowanego przedsięwzięcia",
                            help_text="Np. kurs, warsztat, szkolenie itp.",
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
                                    component_type="date",
                                    label="Planowany termin realizacji od",
                                    name="plannedCompletionDateFrom",
                                    validators=[
                                        self.validator.related_date_lte_validator(
                                            field_name="plannedCompletionDateTo",
                                        )
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="date",
                                    label="Planowany termin raelizacji do",
                                    name="plannedCompletionDateTo",
                                    validators=[
                                        self.validator.related_date_gte_validator(
                                            field_name="plannedCompletionDateFrom",
                                        )
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    name="projectLocation",
                                    component_type="textarea",
                                    label="Miejsce realizacji przedsięwzięcia",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=3000
                                        )
                                    ],
                                    required=True,
                                    class_list=[
                                        "table-full"
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Opis przedsięwzięcia",
                            help_text="Tematyka, tryb, metody dydaktyczne, liczba godzin, modułów, bloków tematycznych.",
                            components=[
                                self.create_component(
                                    name="generalProjectDescription",
                                    component_type="textarea",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=3000
                                        )
                                    ],
                                    required=True,
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Idea i cel edukacyjny",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="educationalIdeaAndGoal",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=3000
                                        )
                                    ],
                                    required=True,
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Grupa docelowa",
                            help_text="Sposób rekrutacji i kryteria wyboru uczestników",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="targetGroup",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=3000
                                        )
                                    ],
                                    required=True,
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Liczba i zróżnicowanie struktury uczestników",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="numberAndDiversityOfParticipants",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=3000
                                        )
                                    ],
                                    required=True,
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Doświadczenie wnioskodawcy i kompetencje zespołu",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="applicantAndTeamExperience",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=3000
                                        )
                                    ],
                                    required=True
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Dostępność oferty edukacyjnej",
                            help_text="Podjęte działania w celu zapewnienia dostępności oferty kształcenia dla osób ze szczególnymi potrzebami oraz wspieranie inkluzywności.",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="projectAccessibility",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=3000
                                        )
                                    ],
                                    required=True
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Planowane efekty realizacji przedsięwzięcia",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="plannedEffectsOfProjectImplementation",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=3000
                                        )
                                    ],
                                    required=True
                                ),
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Podstawowe dane liczbowe i wskaźniki",
                    components=[
                        self.create_chapter(
                            title="<normal>1. Planowana liczba zajęć edukacyjnych</normal>",
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
                                    component_type="number",
                                    name="plannedNumberOfEducationalActivities",
                                    unit="szt."
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="<normal>2. Prognozowana liczba uczestników</normal>",
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
                                    component_type="number",
                                    name="estimatedNumberOfParticipantsPrimarySchools",
                                    unit="osoby",
                                    label="a) Uczniowie szkół podstawowych"
                                ),
                                self.create_component(
                                    component_type="number",
                                    name="estimatedNumberOfParticipantsSecondarySchools",
                                    unit="osoby",
                                    label="b) Uczniowie szkół ponadpodstawowych"
                                ),
                                self.create_component(
                                    component_type="number",
                                    name="estimatedNumberOfParticipantsAdults",
                                    unit="osoby",
                                    label="c) Dorośli"
                                ),
                                self.create_component(
                                    component_type="number",
                                    name="estimatedNumberOfParticipantsSeniors",
                                    unit="osoby",
                                    label="d) Seniorzy"
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="<normal>3. Planowana liczba szkół biorących udział w zajęciach</normal>",
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
                                    component_type="number",
                                    name="plannedNumberOfSchoolsParticipatingPrimarySchools",
                                    unit="szt.",
                                    label="a) Szkoły podstawowe"
                                ),
                                self.create_component(
                                    component_type="number",
                                    name="plannedNumberOfSchoolsParticipatingSecondarySchools",
                                    unit="szt.",
                                    label="b) Szkoły ponadpodstawowe"
                                )
                            ]
                        )
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
