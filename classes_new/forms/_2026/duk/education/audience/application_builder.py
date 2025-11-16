from .estimate_data import estimate_sections
from classes_new.forms._2026.duk.education.application_builder import EducationOperationalProgramApplicationFormBuilder
from classes_new.forms._2026.duk.pisf_structure import AudiencePriority
from classes_new.forms._2026.duk.estimate.application_estimate_builder import DUKApplicationEstimateBuilder


class AudiencePriorityApplicationFormBuilder(EducationOperationalProgramApplicationFormBuilder):
    def __init__(self):
        super().__init__(
            priority=AudiencePriority()
        )

        self.form_id = self.set_ids(
            local_id=16407,
            uat_id=None
        )

        # Variables
        self.project_type = [
            "Zajęcia edukacyjne połączone z projekcją filmu o wysokich walorach artystycznych, dotyczące analizy prezentowanego utworu, jego miejsca w historii kinematografii polskiej i/lub światowej, estetyki filmowej i zastosowanych środków wyrazu oraz społecznych funkcji filmu, organizowane w kinach lub innych salach przygotowanych do projekcji filmu",
            "Zajęcia i warsztaty wzbogacone materiałami dydaktycznymi o wysokiej wartości merytorycznej, rozwijające wiedzę o filmie oraz umiejętności twórcze i analityczne uczestników",
            "Inne działania realizujące cele Priorytetu IV"
        ]
        self.is_only_one_application_grant_usage = True

        # Estimate
        estimate_builder = DUKApplicationEstimateBuilder(estimate_sections=estimate_sections)
        self.estimate_chapters = [
            estimate_builder.generate_estimate()
        ]

    def create_application_scope_of_project(self, number):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Zakres przedsięwzięcia i jego charakterystyka",
            short_name=f"{self.helpers.int_to_roman(number)}. Zakres przedsięwzięcia",
            chapters=[
                self.create_chapter(
                    title="Nazwa przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="applicationTaskNameRepeatPage4",
                            read_only=True,
                            calculation_rules=[
                                self.calculation_rule.copy_value(
                                    from_name="applicationTaskName"
                                )
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="1. Termin i miejsce realizacji przedsięwzięcia",
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
                            label="Termin od",
                            name="projectOpeningDatePointOne",
                            validators=[
                                self.validator.related_date_lte_validator(
                                    field_name="projectClosingDatePointOne",
                                )
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="date",
                            label="Termin do",
                            name="projectClosingDatePointOne",
                            validators=[
                                self.validator.related_date_gte_validator(
                                    field_name="projectOpeningDatePointOne",
                                )
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Miejscowość",
                            name="projectCity",
                            validators=[
                                self.validator.length_validator(max_value=100)
                            ],
                            required=True,
                            class_list=[
                                "table-full"
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Miejsce realizacji przedsięwzięcia",
                            name="projectPlacesObjects",
                            required=True,
                            validators=[
                                self.validator.length_validator(max_value=100)
                            ],
                            class_list=[
                                "table-full"
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Zakres przedsięwzięcia i jego charakterystyka",
                    components=[
                        self.create_chapter(
                            title="Idea i cel edukacyjny",
                            help_text="Idea, wartość dydaktyczna przedsięwzięcia i główne cele edukacyjne.",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="educationalIdeaAndGoal",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=5000
                                        )
                                    ],
                                    required=True,
                                ),
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
                                            max_value=5000
                                        )
                                    ],
                                    required=True,
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Liczba i zróżnicowanie struktury uczestników",
                            help_text="Analiza struktury i zróżnicowania adresatów oferty edukacyjnej.",
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
                            help_text="Doświadczenie wnioskodawcy w działalności edukacyjnej oraz kompetencje zespołu zaangażowanego w realizację przedsięwzięcia.",
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
                            help_text="Spodziewane efekty realizacji przedsięwzięcia w ujęciu jakościowym.",
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
                            title="<normal>Planowana liczba zajęć edukacyjnych</normal>",
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
                            title="<normal>Prognozowana liczba uczestników</normal>",
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
                                    name="estimatedNumberOfParticipantsKindergarten",
                                    unit="os.",
                                    label="a) Dzieci w wieku przeszkolnym"
                                ),
                                self.create_component(
                                    component_type="number",
                                    name="estimatedNumberOfParticipantsPrimarySchools",
                                    unit="os.",
                                    label="b) Uczniowie szkół podstawowych"
                                ),
                                self.create_component(
                                    component_type="number",
                                    name="estimatedNumberOfParticipantsSecondarySchools",
                                    unit="os.",
                                    label="c) Uczniowie szkół ponadpodstawowych"
                                ),
                                self.create_component(
                                    component_type="number",
                                    name="estimatedNumberOfParticipantsAdults",
                                    unit="os.",
                                    label="d) Dorośli"
                                ),
                                self.create_component(
                                    component_type="number",
                                    name="estimatedNumberOfParticipantsSeniors",
                                    unit="os.",
                                    label="e) Seniorzy"
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="<normal>Planowana liczba szkół biorących udział w zajęciach</normal>",
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
            title=f"{self.helpers.int_to_roman(number)}. Załączniki",
            short_name=f"{self.helpers.int_to_roman(number)}. Załączniki",
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
                    title="5. Szczegółowy wykaz kin, w których prowadzone będą zajęcia",
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
