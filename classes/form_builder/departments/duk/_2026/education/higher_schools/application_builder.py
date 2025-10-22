from .estimate_data import estimate_sections
from classes.form_builder.departments.duk._2026.estimate.application_estimate_builder import DUKApplicationEstimateBuilder
from ..priority import HigherSchoolsPriority
from ..application_builder import EducationApplicationBuilder


class HigherSchoolsApplicationBuilder(EducationApplicationBuilder, HigherSchoolsPriority):
    FORM_ID = 16

    def __init__(self):
        super().__init__()

        self.project_type = [
            "Programy edukacyjne wchodzące w skład edukacji ciągłej.",
            "Realizacja szkolnych i pozaszkolnych filmów krótko- i średniometrażowych.",
            "Kształcenie zawodowe i podnoszenie kompetencji poprzez organizację studiów podyplomowych.",
            "Inne działania realizujące cele Priorytetu I."
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
                                            max_value=2000
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
                                            max_value=1500
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
                            title="Liczba i zróżnicowanie struktury studentów",
                            help_text="Analiza struktury i zróżnicowania adresatów oferty edukacyjnej.",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="numberAndDiversityOfStudents",
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
                            title="Profil absolwenta",
                            help_text="Umiejętności lub kompetencje zawodowe nabywane przez studentów",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="graduateProfile",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=1000
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
                            title="Prognozowana liczba studentów",
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
                                    label="Studia stacjonarne",
                                    name="estimatedNumberOfStudentsFullTimeStudies",
                                    unit="osoby"
                                ),
                                self.create_component(
                                    component_type="number",
                                    label="Studia niestacjonarne",
                                    name="estimatedNumberOfStudentsPartTimeStudies",
                                    unit="osoby"
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Liczba wyprodukowanych filmów",
                            components=[
                                self.create_chapter(
                                    title="<normal>a) Filmy fabularne</normal>",
                                    class_list={
                                        "main": ["table-1-2", "grid", "grid-cols-2"],
                                        "sub": ["table-1-2__col"]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="number",
                                            label="Studia stacjonarne",
                                            name="producedFilmsFabFullTimeStudies",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Studia niestacjonarne",
                                            name="producedFilmsFabPartTimeStudies",
                                            unit="szt."
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>b) Filmy dokumentalne</normal>",
                                    class_list={
                                        "main": ["table-1-2", "grid", "grid-cols-2"],
                                        "sub": ["table-1-2__col"]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="number",
                                            label="Studia stacjonarne",
                                            name="producedFilmsDocFullTimeStudies",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Studia niestacjonarne",
                                            name="producedFilmsDocPartTimeStudies",
                                            unit="szt."
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>c) Filmy animowane</normal>",
                                    class_list={
                                        "main": ["table-1-2", "grid", "grid-cols-2"],
                                        "sub": ["table-1-2__col"]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="number",
                                            label="Studia stacjonarne",
                                            name="producedFilmsAniFullTimeStudies",
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Studia niestacjonarne",
                                            name="producedFilmsAniPartTimeStudies",
                                            unit="szt."
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
