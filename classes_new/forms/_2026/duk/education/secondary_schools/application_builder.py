from .estimate_data import estimate_sections
from classes_new.forms._2026.duk.education.application_builder import EducationOperationalProgramApplicationFormBuilder
from classes_new.forms._2026.duk.pisf_structure import SecondarySchoolsPriority
from classes_new.forms._2026.duk.estimate.application_estimate_builder import DUKApplicationEstimateBuilder


class SecondarySchoolsPriorityApplicationFormBuilder(EducationOperationalProgramApplicationFormBuilder):
    def __init__(self):
        super().__init__(
            priority=SecondarySchoolsPriority()
        )

        self.form_id = self.set_ids(
            local_id=16405,
            uat_id=None
        )

        # Variables
        self.project_type = [
            "Programy edukacyjne wchodzące w skład edukacji ciągłej",
            "Kształcenie w kierunku zdobycia zawodów związanych z potrzebami współczesnego rynku audiowizualnego",
            "Organizacja praktyk zawodowych dla uczniów"
        ]

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
                    title="1. Zakres przedsięwzięcia i jego charakterystyka",
                    components=[
                        self.create_chapter(
                            title="Opis przedsięwzięcia",
                            help_text="Organizacyjny aspekt realizacji przedsięwzięcia z określeniem profilu kształcenia, formy zajęć oraz metod dydaktycznych.",
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
                            title="Program nauczania i wartość merytoryczna oferty dydaktycznej",
                            help_text="Ogólny charakter programu nauczania ukierunkowany na realizację celów i osiąganie zakładanych efektów kształcenia, bez uszczegółowienia treści poszczególnych zajęć.",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="offerEducationalValue",
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
                            title="Analiza potrzeb rynku pracy",
                            help_text="Wpływ proponowanej oferty edukacyjnej na rozwój naukowy z uwzględnieniem praktycznych wymagań rynku pracy.",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="laborMarketAnalysis",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=2000
                                        )
                                    ],
                                    required=True,
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Doświadczenie wnioskodawcy i kompetencje zespołu",
                            help_text="Doświadczenie wnioskodawcy w prowadzeniu działalności edukacyjnej oraz kompetencje zespołu zaangażowanego w realizację przedsięwzięcia.",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="applicantAndTeamExperience",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=2000
                                        )
                                    ],
                                    required=True
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Liczba i zróżnicowanie struktury uczniów",
                            help_text="Liczba uczniów z uwzględnieniem profilu, roku nauki, trybem itp.",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="numberAndDiversityOfStudents",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=2000
                                        )
                                    ],
                                    required=True,
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
                                            max_value=2000
                                        )
                                    ],
                                    required=True
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Profil absolwenta",
                            help_text="Umiejętności lub kompetencje zawodowe nabywane przez uczniów w toku kształcenia.",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="graduateProfile",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=2000
                                        )
                                    ],
                                    required=True,
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Podstawowe dane liczbowe i prognozowane wskaźniki",
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
                            label="Prognozowana liczba kursów i warsztatów",
                            name="estimatedCourcesAndWorkshops"
                        ),
                        self.create_component(
                            component_type="number",
                            label="Prognozowana liczba uczestników",
                            name="estimatedParticipants"
                        ),
                        self.create_component(
                            component_type="number",
                            label="Prognozowana liczba zrealizowanych etiud i innych ćwiczeń filmowych",
                            name="estimatedCompletedShortFilms"
                        )
                    ]
                )
            ]
        )

        self.save_part(part)
