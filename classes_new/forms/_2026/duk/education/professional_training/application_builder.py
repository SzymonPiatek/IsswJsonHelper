from .estimate_data import estimate_sections_pt124, estimate_sections_pt3
from classes_new.forms._2026.duk.education.application_builder import EducationOperationalProgramApplicationFormBuilder
from classes_new.forms._2026.duk.pisf_structure import ProfessionalTrainingPriority
from classes_new.forms._2026.duk.estimate.application_estimate_builder import DUKApplicationEstimateBuilder


class ProfessionalTrainingPriorityApplicationFormBuilder(EducationOperationalProgramApplicationFormBuilder):
    def __init__(self):
        super().__init__(
            priority=ProfessionalTrainingPriority()
        )

        self.form_id = self.set_ids(
            local_id=16406,
            uat_id=None
        )

        # Variables
        self.project_type = [
            "Podnoszenie kwalifikacji i kompetencji zawodowych przedstawicieli wszystkich grup zawodowych sektora audiowizualnego poprzez organizację szkoleń, warsztatów, kursów oraz innych form doskonalenia zawodowego, w tym programów długoterminowych.",
            "Kształcenie w kierunku zdobycia dodatkowych umiejętności i zawodów związanych z potrzebami współczesnego rynku audiowizualnego.",
            "Organizacja kursów nauki języków obcych dla przedstawicieli zawodów filmowych.",
            "Inne działania, realizujące cele Priorytetu III."
        ]

        # Estimate
        estimate_builder_pt124 = DUKApplicationEstimateBuilder(
            estimate_sections=estimate_sections_pt124,
            after_name="pt124"
        )
        estimate_builder_pt3 = DUKApplicationEstimateBuilder(
            estimate_sections=estimate_sections_pt3,
            after_name="pt3"
        )
        self.estimate_chapters = [
            self.create_chapter(
                visibility_rules=[
                    self.visibility_rule.depends_on_value(
                        field_name="projectType",
                        values=[
                            "Podnoszenie kwalifikacji i kompetencji zawodowych przedstawicieli wszystkich grup zawodowych sektora audiowizualnego poprzez organizację szkoleń, warsztatów, kursów oraz innych form doskonalenia zawodowego, w tym programów długoterminowych.",
                            "Kształcenie w kierunku zdobycia dodatkowych umiejętności i zawodów związanych z potrzebami współczesnego rynku audiowizualnego.",
                            "Inne działania, realizujące cele Priorytetu III."
                        ]
                    )
                ],
                components=[
                    estimate_builder_pt124.generate_estimate(),
                ]
            ),
            self.create_chapter(
                visibility_rules=[
                    self.visibility_rule.depends_on_value(
                        field_name="projectType",
                        values=[
                            "Organizacja kursów nauki języków obcych dla przedstawicieli zawodów filmowych."
                        ]
                    )
                ],
                components=[
                    estimate_builder_pt3.generate_estimate(),
                ]
            )
        ]

    def create_application_scope_of_project(self, number):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Zakres przedsięwzięcia i jego charakterystyka",
            short_name=f"{self.helpers.int_to_roman(number)}. Zakres przedsięwzięcia",
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
                                    component_type='textarea',
                                    name="plannedProjectType",
                                    validators=[
                                        self.validator.length_validator(max_value=100)
                                    ],
                                    required=True,
                                    class_list=[
                                        "table-full"
                                    ]
                                ),
                                self.create_component(
                                    name="projectLocation",
                                    component_type="textarea",
                                    label="Miejsce realizacji przedsięwzięcia",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=100
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
                                            max_value=2000
                                        )
                                    ],
                                    required=True,
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Idea i cel edukacyjny",
                            help_text="Istota i wartość dydaktyczna przedsięwzięcia.",
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
                            title="Analiza potrzeb rynku pracy",
                            help_text="Wpływ proponowanej oferty edukacyjnej na rozwój naukowy z uwzględnieniem praktycznych wymagań rynku pracy.",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="marketLaborAnalysis",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=1500
                                        )
                                    ],
                                    required=True,
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Grupa docelowa",
                            help_text="Sposób rekrutacji i kryteria wyboru uczestników.",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="targetGroup",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=1000
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
                                            max_value=1000
                                        )
                                    ],
                                    required=True,
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Doświadczenie wnioskodawcy i kompetencje zespołu",
                            help_text="W tym udział specjalistów w realizacji przedsięwzięcia.",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="applicantAndTeamExperience",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=1500
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
                                            max_value=1000
                                        )
                                    ],
                                    required=True
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Planowane efekty realizacji przedsięwzięcia",
                            help_text="Spodziewane efekty w ujęciu jakościowym.",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="plannedEffects",
                                    validators=[
                                        self.validator.length_validator(max_value=1000)
                                    ],
                                    required=True,
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Podstawowe dane liczbowe i prognozowane wskaźniki",
                    components=[
                        self.create_chapter(
                            title="Liczba prognozowanych wydarzeń, liczba uczestników oraz wpływy ze sprzedaży",
                            components=[
                                self.create_chapter(
                                    title="<normal>a) Szkolenia</normal>",
                                    class_list={
                                        "main": [
                                            "table-1-3-narrow",
                                            "grid",
                                            "grid-cols-3"
                                        ],
                                        "sub": [
                                            "table-1-3__col"
                                        ]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="number",
                                            label="Liczba wydarzeń",
                                            name="eventsNumberTraining",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Liczba osób",
                                            name="peopleNumberTraining",
                                            unit="os."
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            name="forecastedSalesRevenuesTraining",
                                            label="Koszt jednostkowy",
                                            unit="PLN"
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>b) Warsztaty</normal>",
                                    class_list={
                                        "main": [
                                            "table-1-3-narrow",
                                            "grid",
                                            "grid-cols-3"
                                        ],
                                        "sub": [
                                            "table-1-3__col"
                                        ]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="number",
                                            label="Liczba wydarzeń",
                                            name="eventsNumberWorkshops",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Liczba osób",
                                            name="peopleNumberWorkshops",
                                            unit="os."
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            name="forecastedSalesRevenuesWorkshops",
                                            label="Koszt jednostkowy",
                                            unit="PLN"
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>c) Kursy</normal>",
                                    class_list={
                                        "main": [
                                            "table-1-3-narrow",
                                            "grid",
                                            "grid-cols-3"
                                        ],
                                        "sub": [
                                            "table-1-3__col"
                                        ]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="number",
                                            label="Liczba wydarzeń",
                                            name="eventsNumberCourses",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Liczba osób",
                                            name="peopleNumberCourses",
                                            unit="os."
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            name="forecastedSalesRevenuesCourses",
                                            label="Koszt jednostkowy",
                                            unit="PLN"
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>d) Inne</normal>",
                                    components=[
                                        self.create_chapter(
                                            components=[
                                                self.create_component(
                                                    component_type="text",
                                                    label="Rodzaj",
                                                    name="otherEventType",
                                                    class_list=[
                                                        "table-full"
                                                    ]
                                                ),
                                            ]
                                        ),
                                        self.create_chapter(
                                            class_list={
                                                "main": [
                                                    "table-1-3-narrow",
                                                    "grid",
                                                    "grid-cols-3"
                                                ],
                                                "sub": [
                                                    "table-1-3__col"
                                                ]
                                            },
                                            components=[
                                                self.create_component(
                                                    component_type="number",
                                                    label="Liczba wydarzeń",
                                                    name="eventsNumberOther",
                                                    unit="szt."
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Liczba osób",
                                                    name="peopleNumberOther",
                                                    unit="os."
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    name="forecastedSalesRevenuesOther",
                                                    label="Koszt jednostkowy",
                                                    unit="PLN"
                                                )
                                            ]
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
