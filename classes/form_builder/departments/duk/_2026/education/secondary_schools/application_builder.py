from .estimate_data import estimate_sections
from classes.form_builder.departments.duk._2026.estimate.application_estimate_builder import DUKApplicationEstimateBuilder
from ..priority import SecondarySchoolsPriority
from ..application_builder import EducationApplicationBuilder


class SecondarySchoolsApplicationBuilder(EducationApplicationBuilder, SecondarySchoolsPriority):
    FORM_ID = 17

    def __init__(self):
        super().__init__()

        self.project_type = [
            "Programy edukacyjne wchodzące w skład edukacji ciągłej.",
            "Kształcenie w kierunku zdobycia zawodów związanych z potrzebami współczesnego rynku audiowizualnego.",
            "Praktyki zawodowe."
        ]

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
                    title="1. Zakres przedsięwzięcia i jego charakterystyka",
                    components=[
                        self.create_chapter(
                            title="Opis przedsięwzięcia",
                            help_text="Profil kształcenia, forma realizacji zajęć dydaktycznych, metody i techniki nauczania itp.",
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
                                            max_value=3000
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
                                            max_value=3000
                                        )
                                    ],
                                    required=True
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Liczba i zróżnicowanie struktury studentów",
                            help_text="Analiza struktury i zróżnicowania adresatów oferty edukacyjnej.",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="numberAndDiversityOfStudents",
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
                            title="Profil absolwenta",
                            help_text="Umiejętności lub kompetencje zawodowe nabywane przez uczniów.",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="graduateProfile",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=3000
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
                                            unit="osoby"
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
                                            unit="osoby"
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
                                            unit="osoby"
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
                                                    unit="osoby"
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
