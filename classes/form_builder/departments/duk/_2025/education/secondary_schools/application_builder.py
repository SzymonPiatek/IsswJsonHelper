from classes.form_builder.departments.duk._2025.education.application_builder import EducationApplicationBuilder
from classes.form_builder.departments.duk.application_builder import DUKApplicationBuilder
from classes.form_builder.departments.duk._2025.education.secondary_schools.estimate_data import estimate_sections


class SecondarySchoolsApplicationBuilder(EducationApplicationBuilder):
    PRIORITY_NAME = 'II. Edukacja w szkołach średnich i zawodowych'
    PRIORITY_NUM = 2
    FORM_ID = 9181

    def __init__(self):
        super().__init__()

        self.estimate_sections = estimate_sections
        self.basic_number_data = self.create_application_basic_number_data()


    def create_application_basic_data(self, **kwargs):
        data = {
            'projectType': {
                'options': [
                    "programy edukacyjne wchodzące w skład edukacji ciągłej",
                    "kształcenie w kierunku zdobycia zawodów związanych z potrzebami współczesnego rynku audiowizualnego",
                    "inne działania realizujące cele Priorytetu II",
                ]
            }
        }
        DUKApplicationBuilder.create_application_basic_data(self, data=data)

    def create_application_basic_number_data(self):
        return self.create_chapter(
            title="2. Podstawowe dane liczbowe i prognozowane wskaźniki",
            components=[
                self.create_chapter(
                    title="1. Prognozowana liczba studentów",
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
                    title="2. Średnia wysokość czesnego w rozrachunku rocznym",
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
                            component_type="text",
                            mask="fund",
                            label="Studia stacjonarne",
                            name="averageTuitionFeeFullTimeStudies",
                            unit="PLN"
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="Studia niestacjonarne",
                            name="averageTuitionFeePartTimeStudies",
                            unit="PLN"
                        )
                    ]
                ),
                self.create_chapter(
                    title="3. Średni koszt kształcenia studenta w rozrachunku rocznym",
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
                            component_type="text",
                            mask="fund",
                            label="Studia stacjonarne",
                            name="averageCostOfEducatingStudentFullTimeStudies",
                            unit="PLN"
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="Studia niestacjonarne",
                            name="averageCostOfEducatingStudentPartTimeStudies",
                            unit="PLN"
                        )
                    ]
                ),
                self.create_chapter(
                    title="4. Liczba wyprodukowanych filmów",
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

    def create_application_scope_of_project(self, number):
        part = self.create_part(
            title=f"{int_to_roman(number)}. Zakres przedsięwzięcia i jego charakterystyka",
            short_name=f"{int_to_roman(number)}. Zakres przedsięwzięcia",
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
                            help_text="Umiejętności lub kompetencje zawodowe nabywane przez studentów",
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
                )
            ]
        )

        if self.basic_number_data:
            part["chapters"].append(self.basic_number_data)

        self.save_part(part)
