from classes.form_builder.duk.education.application_builder import EducationApplicationBuilder
from classes.form_builder.duk.application_builder import DUKApplicationBuilder
from classes.form_builder.estimate_builder.duk.application_estimate_builder import DUKApplicationEstimateBuilder
from classes.form_builder.duk.education.postgraduate_schools.estimate_data import estimate_sections


class PostgraduateSchoolsApplicationBuilder(EducationApplicationBuilder):
    PRIORITY_NAME = 'I. Szkoły wyższe i podyplomowe'
    PRIORITY_NUM = 1
    FORM_ID = 9180

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'postgraduate_schools'

    def create_application_basic_data(self, **kwargs):
        data = {
            'projectType': {
                'options': [
                    "programy edukacyjne wchodzące w skład edukacji ciągłej",
                    "realizacja szkolnych i pozaszkolnych filmów krótko- i średniometrażowych",
                    "kształcenie zawodowe i podnoszenie kompetencji poprzez organizację studiów podyplomowych",
                    "inne działania realizujące cele Priorytetu I"
                ]
            }
        }
        DUKApplicationBuilder.create_application_basic_data(self=self, data=data)

    def create_application_project_costs(self):
        estimate = DUKApplicationEstimateBuilder(
            estimate_sections=estimate_sections
        )

        part = estimate.generate()

        self.save_part(part=part)

    def create_application_scope_of_project(self):
        produced_films_chapters = [
            {
                "section_title": "fabularnych",
                "name": "Feature"
            },
            {
                "section_title": "dokumentalnych",
                "name": "Documentary"
            },
            {
                "section_title": "animowanych",
                "name": "Animated"
            }
        ]

        implemented_project_events = [
            {
                "section_title": "szkoleń",
                "name": "trainings"
            },
            {
                "section_title": "warsztatów",
                "name": "workshops"
            },
            {
                "section_title": "kursów",
                "name": "courses"
            }
        ]

        data = {
            "chapters": [
                self.create_chapter(
                    title="7. Podstawowe dane liczbowe na temat bieżącej i poprzedniej edycji",
                    components=[
                        self.create_chapter(
                            class_list={
                                "main": [
                                    "w-full"
                                ],
                                "sub": [
                                    "table-4-top"
                                ]
                            },
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "programy edukacyjne wchodzące w skład edukacji ciągłej",
                                        "realizacja szkolnych i pozaszkolnych filmów krótko- i średniometrażowych",
                                        "kształcenie zawodowe i podnoszenie kompetencji poprzez organizację studiów podyplomowych"
                                    ]
                                )
                            ],
                            components=[
                                self.create_chapter(
                                    title="<normal>1. Liczba studentów</normal>",
                                    class_list={
                                        "main": [
                                            "table-4",
                                            "grid",
                                            "grid-cols-4"
                                        ],
                                        "sub": [
                                            "table-4__col"
                                        ]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="number",
                                            label="Studia stacjonarne / Rok poprzedni",
                                            name="fullTimeStudiesPreviousYearStudentsCount",
                                            unit="osoby"
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Studia stacjonarne / Rok bieżący",
                                            name="fullTimeStudiesCurrentYearStudentsCount",
                                            unit="osoby",
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Studia niestacjonarne / Rok poprzedni",
                                            name="partTimeStudiesPreviousYearStudentsCount",
                                            unit="osoby",
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Studia niestacjonarne / Rok bieżący",
                                            name="partTimeStudiesCurrentYearStudentsCount",
                                            unit="osoby",
                                            required=True,
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>2. Średnia wysokość czesnego (w rozrachunku rocznym)</normal>",
                                    class_list={
                                        "main": [
                                            "table-4",
                                            "grid",
                                            "grid-cols-4"
                                        ],
                                        "sub": [
                                            "table-4__col"
                                        ]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Studia stacjonarne / Rok poprzedni",
                                            name="fullTimeStudiesPreviousYearAverageTuition",
                                            unit="PLN"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Studia stacjonarne / Rok bieżący",
                                            name="fullTimeStudiesCurrentYearAverageTuition",
                                            unit="PLN",
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Studia niestacjonarne / Rok poprzedni",
                                            name="partTimeStudiesPreviousYearAverageTuition",
                                            unit="PLN",
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Studia niestacjonarne / Rok bieżący",
                                            name="partTimeStudiesCurrentYearAverageTuition",
                                            unit="PLN",
                                            required=True,
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>3. Średni koszt kształcenia studenta (w roku i w tys. zł)</normal>",
                                    class_list={
                                        "main": [
                                            "table-4",
                                            "grid",
                                            "grid-cols-4"
                                        ],
                                        "sub": [
                                            "table-4__col"
                                        ]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Studia stacjonarne / Rok poprzedni",
                                            name="fullTimeStudiesPreviousYearAverageEducationCostPerStudent",
                                            unit="tys. PLN",
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Studia stacjonarne / Rok bieżący",
                                            name="fullTimeStudiesCurrentYearAverageEducationCostPerStudent",
                                            unit="tys. PLN",
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Studia niestacjonarne / Rok poprzedni",
                                            name="partTimeStudiesPreviousYearAverageEducationCostPerStudent",
                                            unit="tys. PLN",
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Studia niestacjonarne / Rok bieżący",
                                            name="partTimeStudiesCurrentYearAverageEducationCostPerStudent",
                                            unit="tys. PLN",
                                            required=True,
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>4. Liczba wyprodukowanych filmów: </normal>",
                                    components=[
                                        subchapter
                                        for chapter in produced_films_chapters
                                        for subchapter in [
                                            self.create_chapter(
                                                title=f"<small>- liczba filmów {chapter["section_title"]}</small>",
                                                class_list={
                                                    "main": [
                                                        "table-4",
                                                        "grid",
                                                        "grid-cols-4"
                                                    ],
                                                    "sub": [
                                                        "table-4__col"
                                                    ]
                                                },
                                                components=[
                                                    self.create_component(
                                                        component_type="number",
                                                        label="Studia stacjonarne / Rok poprzedni",
                                                        name=f"fullTimeStudiesPreviousEdition{chapter["name"]}FilmCount",
                                                        unit="szt.",
                                                    ),
                                                    self.create_component(
                                                        component_type="number",
                                                        label="Studia stacjonarne / Rok bieżący",
                                                        name=f"fullTimeStudiesCurrentEdition{chapter["name"]}FilmCount",
                                                        unit="szt.",
                                                        required=True
                                                    ),
                                                    self.create_component(
                                                        component_type="number",
                                                        label="Studia niestacjonarne / Rok poprzedni",
                                                        name=f"partTimeStudiesPreviousEdition{chapter["name"]}FilmCount",
                                                        unit="szt.",
                                                    ),
                                                    self.create_component(
                                                        component_type="number",
                                                        label="Studia niestacjonarne / Rok bieżący",
                                                        name=f"partTimeStudiesCurrentEdition{chapter["name"]}FilmCount",
                                                        unit="szt.",
                                                        required=True,
                                                    )
                                                ]
                                            ),
                                            self.create_chapter(
                                                title=f"<small>- liczba minut filmów {chapter["section_title"]}</small>",
                                                class_list={
                                                    "main": [
                                                        "table-4",
                                                        "grid",
                                                        "grid-cols-4"
                                                    ],
                                                    "sub": [
                                                        "table-4__col"
                                                    ]
                                                },
                                                components=[
                                                    self.create_component(
                                                        component_type="number",
                                                        label="Studia stacjonarne / Rok poprzedni",
                                                        name=f"fullTimeStudiesPreviousEdition{chapter["name"]}FilmMinutes",
                                                        unit="min.",
                                                    ),
                                                    self.create_component(
                                                        component_type="number",
                                                        label="Studia stacjonarne / Rok bieżący",
                                                        name=f"fullTimeStudiesCurrentEdition{chapter["name"]}FilmMinutes",
                                                        unit="min.",
                                                        required=True
                                                    ),
                                                    self.create_component(
                                                        component_type="number",
                                                        label="Studia niestacjonarne / Rok poprzedni",
                                                        name=f"partTimeStudiesPreviousEdition{chapter["name"]}FilmMinutes",
                                                        unit="min.",
                                                    ),
                                                    self.create_component(
                                                        component_type="number",
                                                        label="Studia niestacjonarne / Rok bieżący",
                                                        name=f"partTimeStudiesCurrentEdition{chapter["name"]}FilmMinutes",
                                                        unit="min.",
                                                        required=True,
                                                    )
                                                ]
                                            )
                                        ]
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>Inne</normal>",
                                    is_multiple_forms=True,
                                    multiple_forms_rules={
                                        "minCount": 1,
                                        "maxCount": 20
                                    },
                                    components=[
                                        self.create_chapter(
                                            components=[
                                                self.create_chapter(
                                                    components=[
                                                        self.create_component(
                                                            component_type="text",
                                                            label="Rodzaj",
                                                            name="otherFilmsKind",
                                                            validators=[
                                                                self.validator.length_validator(max_value=100)
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                self.create_chapter(
                                                    title="<small>- liczba filmów</small>",
                                                    class_list={
                                                        "main": [
                                                            "table-4",
                                                            "grid",
                                                            "grid-cols-4"
                                                        ],
                                                        "sub": [
                                                            "table-4__col"
                                                        ]
                                                    },
                                                    components=[
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Studia stacjonarne / Rok poprzedni",
                                                            name="fullTimeStudiesPreviousEditionOtherFilmCount",
                                                            unit="szt.",
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Studia stacjonarne / Rok bieżący",
                                                            name="fullTimeStudiesCurrentEditionOtherFilmCount",
                                                            unit="szt.",
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Studia niestacjonarne / Rok poprzedni",
                                                            name="partTimeStudiesPreviousEditionOtherFilmCount",
                                                            unit="szt.",
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Studia niestacjonarne / Rok bieżący",
                                                            name="partTimeStudiesCurrentEditionOtherFilmCount",
                                                            unit="szt.",
                                                        )
                                                    ]
                                                ),
                                                self.create_chapter(
                                                    title="<small>- liczba minut</small>",
                                                    class_list={
                                                        "main": [
                                                            "table-4",
                                                            "grid",
                                                            "grid-cols-4"
                                                        ],
                                                        "sub": [
                                                            "table-4__col"
                                                        ]
                                                    },
                                                    components=[
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Studia stacjonarne / Rok poprzedni",
                                                            name="fullTimeStudiesPreviousEditionOtherFilmMinutes",
                                                            unit="min.",
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Studia stacjonarne / Rok bieżący",
                                                            name="fullTimeStudiesCurrentEditionOtherFilmMinutes",
                                                            unit="min.",
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Studia niestacjonarne / Rok poprzedni",
                                                            name="partTimeStudiesPreviousEditionOtherFilmMinutes",
                                                            unit="min.",
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Studia niestacjonarne / Rok bieżący",
                                                            name="partTimeStudiesCurrentEditionOtherFilmMinutes",
                                                            unit="min.",
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="SUMA",
                                    components=[
                                        self.create_chapter(
                                            title="<small>- suma filmów</small>",
                                            class_list={
                                                "main": [
                                                    "table-4",
                                                    "grid",
                                                    "grid-cols-4"
                                                ],
                                                "sub": [
                                                    "table-4__col"
                                                ]
                                            },
                                            components=[
                                                self.create_chapter(
                                                    title="<small>- suma filmów</small>",
                                                    class_list={
                                                        "main": [
                                                            "table-4",
                                                            "grid",
                                                            "grid-cols-4"
                                                        ],
                                                        "sub": [
                                                            "table-4__col"
                                                        ]
                                                    },
                                                    components=[
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Studia stacjonarne / Rok poprzedni",
                                                            name="fullTimeStudiesPreviousEditionOtherFilmCountSum",
                                                            unit="szt.",
                                                            read_only=True,
                                                            calculation_rules=[
                                                                self.calculation_rule.dynamic_sum_inputs(
                                                                    fields=[
                                                                        "fullTimeStudiesPreviousEditionFeatureFilmCount",
                                                                        "fullTimeStudiesPreviousEditionDocumentaryFilmCount",
                                                                        "fullTimeStudiesPreviousEditionAnimatedFilmCount",
                                                                        "fullTimeStudiesPreviousEditionOtherFilmCount"
                                                                    ]
                                                                )
                                                            ],
                                                            validators=[
                                                                self.validator.related_sum_validator(
                                                                    field_names=[
                                                                        "fullTimeStudiesPreviousEditionFeatureFilmCount",
                                                                        "fullTimeStudiesPreviousEditionDocumentaryFilmCount",
                                                                        "fullTimeStudiesPreviousEditionAnimatedFilmCount",
                                                                        "fullTimeStudiesPreviousEditionOtherFilmCount"
                                                                    ]
                                                                )
                                                            ]
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Studia stacjonarne / Rok bieżący",
                                                            name="fullTimeStudiesCurrentEditionOtherFilmCountSum",
                                                            unit="szt.",
                                                            read_only=True,
                                                            calculation_rules=[
                                                                self.calculation_rule.dynamic_sum_inputs(
                                                                    fields=[
                                                                        "fullTimeStudiesCurrentEditionFeatureFilmCount",
                                                                        "fullTimeStudiesCurrentEditionDocumentaryFilmCount",
                                                                        "fullTimeStudiesCurrentEditionAnimatedFilmCount",
                                                                        "fullTimeStudiesCurrentEditionOtherFilmCount"
                                                                    ]
                                                                )
                                                            ],
                                                            validators=[
                                                                self.validator.related_sum_validator(
                                                                    field_names=[
                                                                        "fullTimeStudiesCurrentEditionFeatureFilmCount",
                                                                        "fullTimeStudiesCurrentEditionDocumentaryFilmCount",
                                                                        "fullTimeStudiesCurrentEditionAnimatedFilmCount",
                                                                        "fullTimeStudiesCurrentEditionOtherFilmCount"
                                                                    ]
                                                                )
                                                            ]
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Studia niestacjonarne / Rok poprzedni",
                                                            name="partTimeStudiesPreviousEditionOtherFilmCountSum",
                                                            unit="szt.",
                                                            read_only=True,
                                                            calculation_rules=[
                                                                self.calculation_rule.dynamic_sum_inputs(
                                                                    fields=[
                                                                        "partTimeStudiesPreviousEditionFeatureFilmCount",
                                                                        "partTimeStudiesPreviousDocumentaryFeatureFilmCount",
                                                                        "partTimeStudiesPreviousEditionAnimatedFilmCount",
                                                                        "partTimeStudiesPreviousEditionOtherFilmCount"
                                                                    ]
                                                                )
                                                            ],
                                                            validators=[
                                                                self.validator.related_sum_validator(
                                                                    field_names=[
                                                                        "partTimeStudiesPreviousEditionFeatureFilmCount",
                                                                        "partTimeStudiesPreviousDocumentaryFeatureFilmCount",
                                                                        "partTimeStudiesPreviousEditionAnimatedFilmCount",
                                                                        "partTimeStudiesPreviousEditionOtherFilmCount"
                                                                    ]
                                                                )
                                                            ]
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Studia niestacjonarne / Rok bieżący",
                                                            name="partTimeStudiesCurrentEditionOtherFilmCountSum",
                                                            unit="szt.",
                                                            read_only=True,
                                                            calculation_rules=[
                                                                self.calculation_rule.dynamic_sum_inputs(
                                                                    fields=[
                                                                        "partTimeStudiesCurrentEditionFeatureFilmCount",
                                                                        "partTimeStudiesCurrentEditionDocumentaryFilmCount",
                                                                        "partTimeStudiesCurrentEditionAnimatedFilmCount",
                                                                        "partTimeStudiesCurrentEditionOtherFilmCount"
                                                                    ]
                                                                )
                                                            ],
                                                            validators=[
                                                                self.validator.related_sum_validator(
                                                                    field_names=[
                                                                        "partTimeStudiesCurrentEditionFeatureFilmCount",
                                                                        "partTimeStudiesCurrentEditionDocumentaryFilmCount",
                                                                        "partTimeStudiesCurrentEditionAnimatedFilmCount",
                                                                        "partTimeStudiesCurrentEditionOtherFilmCount"
                                                                    ]
                                                                )
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                self.create_chapter(
                                                    title="<small>- suma minut</small>",
                                                    class_list={
                                                        "main": [
                                                            "table-4",
                                                            "grid",
                                                            "grid-cols-4"
                                                        ],
                                                        "sub": [
                                                            "table-4__col"
                                                        ]
                                                    },
                                                    components=[
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Studia stacjonarne / Rok poprzedni",
                                                            name="fullTimeStudiesPreviousEditionOtherFilmMinutesSum",
                                                            unit="min.",
                                                            read_only=True,
                                                            calculation_rules=[
                                                                self.calculation_rule.dynamic_sum_inputs(
                                                                    fields=[
                                                                        "fullTimeStudiesPreviousEditionFeatureFilmMinutes",
                                                                        "fullTimeStudiesPreviousEditionDocumentaryFilmMinutes",
                                                                        "fullTimeStudiesPreviousEditionAnimatedFilmMinutes",
                                                                        "fullTimeStudiesPreviousEditionOtherFilmMinutes"
                                                                    ]
                                                                )
                                                            ],
                                                            validators=[
                                                                self.validator.related_sum_validator(
                                                                    field_names=[
                                                                        "fullTimeStudiesPreviousEditionFeatureFilmMinutes",
                                                                        "fullTimeStudiesPreviousEditionDocumentaryFilmMinutes",
                                                                        "fullTimeStudiesPreviousEditionAnimatedFilmMinutes",
                                                                        "fullTimeStudiesPreviousEditionOtherFilmMinutes"
                                                                    ]
                                                                )
                                                            ]
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Studia stacjonarne / Rok bieżący",
                                                            name="fullTimeStudiesCurrentEditionOtherFilmMinutesSum",
                                                            unit="min.",
                                                            read_only=True,
                                                            calculation_rules=[
                                                                self.calculation_rule.dynamic_sum_inputs(
                                                                    fields=[
                                                                        "fullTimeStudiesCurrentEditionFeatureFilmMinutes",
                                                                        "fullTimeStudiesCurrentEditionDocumentaryFilmMinutes",
                                                                        "fullTimeStudiesCurrentEditionAnimatedFilmMinutes",
                                                                        "fullTimeStudiesCurrentEditionOtherFilmMinutes"
                                                                    ]
                                                                )
                                                            ],
                                                            validators=[
                                                                self.validator.related_sum_validator(
                                                                    field_names=[
                                                                        "fullTimeStudiesCurrentEditionFeatureFilmMinutes",
                                                                        "fullTimeStudiesCurrentEditionDocumentaryFilmMinutes",
                                                                        "fullTimeStudiesCurrentEditionAnimatedFilmMinutes",
                                                                        "fullTimeStudiesCurrentEditionOtherFilmMinutes"
                                                                    ]
                                                                )
                                                            ]
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Studia niestacjonarne / Rok poprzedni",
                                                            name="partTimeStudiesPreviousEditionOtherFilmMinutesSum",
                                                            unit="min.",
                                                            read_only=True,
                                                            calculation_rules=[
                                                                self.calculation_rule.dynamic_sum_inputs(
                                                                    fields=[
                                                                        "partTimeStudiesPreviousEditionFeatureFilmMinutes",
                                                                        "partTimeStudiesPreviousEditionDocumentaryFilmMinutes",
                                                                        "partTimeStudiesPreviousEditionAnimatedFilmMinutes",
                                                                        "partTimeStudiesPreviousEditionOtherFilmMinutes"
                                                                    ]
                                                                )
                                                            ],
                                                            validators=[
                                                                self.validator.related_sum_validator(
                                                                    field_names=[
                                                                        "partTimeStudiesPreviousEditionFeatureFilmMinutes",
                                                                        "partTimeStudiesPreviousEditionDocumentaryFilmMinutes",
                                                                        "partTimeStudiesPreviousEditionAnimatedFilmMinutes",
                                                                        "partTimeStudiesPreviousEditionOtherFilmMinutes"
                                                                    ]
                                                                )
                                                            ]
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Studia niestacjonarne / Rok bieżący",
                                                            name="partTimeStudiesCurrentEditionOtherFilmMinutesSum",
                                                            unit="min.",
                                                            read_only=True,
                                                            calculation_rules=[
                                                                self.calculation_rule.dynamic_sum_inputs(
                                                                    fields=[
                                                                        "partTimeStudiesPreviousEditionFeatureFilmMinutes",
                                                                        "partTimeStudiesPreviousEditionDocumentaryFilmMinutes",
                                                                        "partTimeStudiesPreviousEditionAnimatedFilmMinutes",
                                                                        "partTimeStudiesPreviousEditionOtherFilmMinutes"
                                                                    ]
                                                                )
                                                            ],
                                                            validators=[
                                                                self.validator.related_sum_validator(
                                                                    field_names=[
                                                                        "partTimeStudiesPreviousEditionFeatureFilmMinutes",
                                                                        "partTimeStudiesPreviousEditionDocumentaryFilmMinutes",
                                                                        "partTimeStudiesPreviousEditionAnimatedFilmMinutes",
                                                                        "partTimeStudiesPreviousEditionOtherFilmMinutes"
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
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "inne działania realizujące cele Priorytetu I"
                                    ]
                                )
                            ],
                            components=[
                                self.create_chapter(
                                    title="<normal>1. Liczba wydarzeń w ramach realizowanego przedsięwzięcia</normal>",
                                    components=[
                                        *[self.create_chapter(
                                            title=f"<normal>- {chapter["section_title"]}</normal>",
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
                                                    label="Poprzednia edycja",
                                                    name=f"{chapter["name"]}PastEditionPkt4",
                                                    unit="szt.",
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Bieżąca edycja (planowane wielkości)",
                                                    name=f"{chapter["name"]}CurrentEditionPkt4",
                                                    unit="szt.",
                                                )
                                            ]
                                        ) for chapter in implemented_project_events],
                                        self.create_chapter(
                                            title="<normal>- innych</normal>",
                                            is_multiple_forms=True,
                                            multiple_forms_rules={
                                                "minCount": 1,
                                                "maxCount": 25
                                            },
                                            components=[
                                                self.create_chapter(
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
                                                            label="Poprzednia edycja",
                                                            name="otherPastEditionPkt4",
                                                            unit="szt.",
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Bieżąca edycja (planowane wielkości)",
                                                            name="otherCurrentEditionPkt4",
                                                            unit="szt.",
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_chapter(
                                            title="<normal>SUMA</normal>",
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
                                                    label="Poprzednia edycja",
                                                    name="eventsSumPastEditionPkt4",
                                                    read_only=True,
                                                    unit="szt.",
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                *[f"{chapter["name"]}PastEditionPkt4" for chapter in implemented_project_events],
                                                                "otherPastEditionPkt4"
                                                            ]
                                                        )
                                                    ],
                                                    validators=[
                                                        self.validator.related_sum_validator(
                                                            field_names=[
                                                                *[f"{chapter["name"]}PastEditionPkt4" for chapter in implemented_project_events],
                                                                "otherPastEditionPkt4"
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Bieżąca edycja (planowane wielkości)",
                                                    name="eventsSumCurrentEditionPkt4",
                                                    read_only=True,
                                                    unit="szt.",
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                *[f"{chapter["name"]}CurrentEditionPkt4" for chapter in implemented_project_events],
                                                                "otherCurrentEditionPkt4"
                                                            ]
                                                        )
                                                    ],
                                                    validators=[
                                                        self.validator.related_sum_validator(
                                                            field_names=[
                                                                *[f"{chapter["name"]}CurrentEditionPkt4" for chapter in implemented_project_events],
                                                                "otherCurrentEditionPkt4"
                                                            ]
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>2. Liczba uczestników w ramach realizowanego przedsięwzięcia</normal>",
                                    components=[
                                        *[self.create_chapter(
                                            title=f"<normal>- {chapter["section_title"]}</normal>",
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
                                                    label="Poprzednia edycja",
                                                    name=f"{chapter["name"]}ParticipantsPastEditionPkt4",
                                                    unit="os.",
                                                    validators=[
                                                        self.validator.range_validator(min_value=0)
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Bieżąca edycja (planowane wielkości)",
                                                    name=f"{chapter["name"]}ParticipantsCurrentEditionPkt4",
                                                    unit="os.",
                                                    validators=[
                                                        self.validator.range_validator(min_value=0)
                                                    ]
                                                )
                                            ]
                                        ) for chapter in implemented_project_events],
                                        self.create_chapter(
                                            title="<normal>- innych</normal>",
                                            is_multiple_forms=True,
                                            multiple_forms_rules={
                                                "minCount": 1,
                                                "maxCount": 25
                                            },
                                            components=[
                                                self.create_chapter(
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
                                                            label="Poprzednia edycja",
                                                            name="otherParticipantsPastEditionPkt4",
                                                            unit="os.",
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Bieżąca edycja (planowane wielkości)",
                                                            name="otherParticipantsCurrentEditionPkt4",
                                                            unit="os.",
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_chapter(
                                            title="<normal>SUMA</normal>",
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
                                                    label="Poprzednia edycja",
                                                    name="participantsSumPastEditionPkt4",
                                                    read_only=True,
                                                    unit="os.",
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                *[f"{chapter["name"]}ParticipantsPastEditionPkt4" for chapter in implemented_project_events],
                                                                "otherParticipantsPastEditionPkt4"
                                                            ]
                                                        )
                                                    ],
                                                    validators=[
                                                        self.validator.related_sum_validator(
                                                            field_names=[
                                                                *[f"{chapter["name"]}ParticipantsPastEditionPkt4" for chapter in implemented_project_events],
                                                                "otherParticipantsPastEditionPkt4"
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Bieżąca edycja (planowane wielkości)",
                                                    name="participantsSumCurrentEditionPkt4",
                                                    read_only=True,
                                                    unit="os.",
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                *[f"{chapter["name"]}ParticipantsCurrentEditionPkt4" for chapter in implemented_project_events],
                                                                "otherParticipantsCurrentEditionPkt4"
                                                            ]
                                                        )
                                                    ],
                                                    validators=[
                                                        self.validator.related_sum_validator(
                                                            field_names=[
                                                                *[f"{chapter["name"]}ParticipantsCurrentEditionPkt4" for chapter in implemented_project_events],
                                                                "otherParticipantsCurrentEditionPkt4"
                                                            ]
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>3. Wpływy ze sprzedaży</normal>",
                                    class_list={
                                        "main": [
                                            "w-full"
                                        ],
                                        "sub": [
                                            "table-4-top",
                                            "w-full-sub"
                                        ]
                                    },
                                    components=[
                                        *[self.create_chapter(
                                            title=f"<normal>- {chapter["section_title"]}</normal>",
                                            class_list={
                                                "main": [
                                                    "table-4",
                                                    "grid",
                                                    "grid-cols-4"
                                                ],
                                                "sub": [
                                                    "table-4__col"
                                                ]
                                            },
                                            components=[
                                                self.create_component(
                                                    component_type="text",
                                                    label="Suma: poprzednia edycja",
                                                    name=f"{chapter["name"]}IncomePastEditionPkt4",
                                                    unit="PLN",
                                                    mask="fund"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    label="Koszt jednostkowy: poprzednia edycja",
                                                    name=f"{chapter["name"]}CostPastEditionPkt4",
                                                    unit="PLN",
                                                    mask="fund"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    label="Suma: bieżąca edycja (planowane wielkości)",
                                                    name=f"{chapter["name"]}IncomeCurrentEditionPkt4",
                                                    unit="PLN",
                                                    mask="fund"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    label="Koszt jednostkowy: bieżąca edycja (planowane wielkości)",
                                                    name=f"{chapter["name"]}CostCurrentEditionPkt4",
                                                    unit="PLN",
                                                    mask="fund"
                                                )
                                            ]
                                        ) for chapter in implemented_project_events],
                                        self.create_chapter(
                                            title="<normal>- innych</normal>",
                                            is_multiple_forms=True,
                                            multiple_forms_rules={
                                                "minCount": 1,
                                                "maxCount": 25
                                            },
                                            components=[
                                                self.create_chapter(
                                                    class_list={
                                                        "main": [
                                                            "table-4",
                                                            "grid",
                                                            "grid-cols-4"
                                                        ],
                                                        "sub": [
                                                            "table-4__col"
                                                        ]
                                                    },
                                                    components=[
                                                        self.create_component(
                                                            component_type="text",
                                                            label="Suma: poprzednia edycja",
                                                            name="otherIncomePastEditionPkt4",
                                                            unit="PLN",
                                                            mask="fund"
                                                        ),
                                                        self.create_component(
                                                            component_type="text",
                                                            label="Koszt jednostkowy: poprzednia edycja",
                                                            name="otherCostPastEditionPkt4",
                                                            unit="PLN",
                                                            mask="fund"
                                                        ),
                                                        self.create_component(
                                                            component_type="text",
                                                            label="Suma: bieżąca edycja (planowane wielkości)",
                                                            name="otherIncomeCurrentEditionPkt4",
                                                            unit="PLN",
                                                            mask="fund"
                                                        ),
                                                        self.create_component(
                                                            component_type="text",
                                                            label="Koszt jednostkowy: bieżąca edycja (planowane wielkości)",
                                                            name="otherCostCurrentEditionPkt4",
                                                            unit="PLN",
                                                            mask="fund"
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_chapter(
                                            title="<normal>SUMA</normal>",
                                            class_list={
                                                "main": [
                                                    "table-4",
                                                    "grid",
                                                    "grid-cols-4"
                                                ],
                                                "sub": [
                                                    "table-4__col"
                                                ]
                                            },
                                            components=[
                                                self.create_component(
                                                    component_type="text",
                                                    label="Suma: poprzednia edycja",
                                                    name="sumIncomePastEditionPkt4",
                                                    unit="PLN",
                                                    mask="fund",
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                *[f"{chapter["name"]}IncomePastEditionPkt4" for chapter in implemented_project_events],
                                                                "otherIncomePastEditionPkt4"
                                                            ]
                                                        )
                                                    ],
                                                    validators=[
                                                        self.validator.related_sum_validator(
                                                            field_names=[
                                                                *[f"{chapter["name"]}IncomePastEditionPkt4" for chapter in implemented_project_events],
                                                                "otherIncomePastEditionPkt4"
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    label="Koszt jednostkowy: poprzednia edycja",
                                                    name="sumCostPastEditionPkt4",
                                                    unit="PLN",
                                                    mask="fund",
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                *[f"{chapter["name"]}CostPastEditionPkt4" for chapter in implemented_project_events],
                                                                "otherCostPastEditionPkt4"
                                                            ]
                                                        )
                                                    ],
                                                    validators=[
                                                        self.validator.related_sum_validator(
                                                            field_names=[
                                                                *[f"{chapter["name"]}CostPastEditionPkt4" for chapter in implemented_project_events],
                                                                "otherCostPastEditionPkt4"
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    label="Suma: bieżąca edycja (planowane wielkości)",
                                                    name="sumIncomeCurrentEditionPkt4",
                                                    unit="PLN",
                                                    mask="fund",
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                *[f"{chapter["name"]}IncomeCurrentEditionPkt4" for chapter in implemented_project_events],
                                                                "otherIncomeCurrentEditionPkt4"
                                                            ]
                                                        )
                                                    ],
                                                    validators=[
                                                        self.validator.related_sum_validator(
                                                            field_names=[
                                                                *[f"{chapter["name"]}IncomeCurrentEditionPkt4" for chapter in implemented_project_events],
                                                                "otherIncomeCurrentEditionPkt4"
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    label="Koszt jednostkowy: bieżąca edycja (planowane wielkości)",
                                                    name="sumCostCurrentEditionPkt4",
                                                    unit="PLN",
                                                    mask="fund",
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                *[f"{chapter["name"]}CostCurrentEditionPkt4" for chapter in implemented_project_events],
                                                                "otherCostCurrentEditionPkt4"
                                                            ]
                                                        )
                                                    ],
                                                    validators=[
                                                        self.validator.related_sum_validator(
                                                            field_names=[
                                                                *[f"{chapter["name"]}CostCurrentEditionPkt4" for chapter in implemented_project_events],
                                                                "otherCostCurrentEditionPkt4"
                                                            ]
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Czy przedsięwzięcie, na które składany jest wniosek jest powiązane z innymi przedsięwzięciami, o dofinansowanie których ubiega się wnioskodawca w bieżącym roku z innych programów operacyjnych PISF? Jeżeli tak, proszę podać nazwę przedsięwzięcia, program oraz wnioskowaną kwotę dofinansowania",
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="radio",
                                            name="wasSubmittedBefore",
                                            options=[
                                                "Tak",
                                                "Nie"
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="wasSubmittedBefore",
                                            values=[
                                                "Tak"
                                            ]
                                        )
                                    ],
                                    is_multiple_forms=True,
                                    multiple_forms_rules={
                                        "minCount": 1,
                                        "maxCount": 20
                                    },
                                    components=[
                                        self.create_chapter(
                                            class_list=[
                                                "grid",
                                                "grid-cols-3"
                                            ],
                                            components=[
                                                self.create_component(
                                                    component_type="text",
                                                    label="Nazwa przedsięwzięcia",
                                                    name="otherProjectName",
                                                    required=True,
                                                    validators=[
                                                        self.validator.related_required_if_equal_validator(
                                                            field_name="wasSubmittedBefore",
                                                            value="Tak"
                                                        )
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    label="Program operacyjny",
                                                    name="programmeName",
                                                    required=True,
                                                    validators=[
                                                        self.validator.related_required_if_equal_validator(
                                                            field_name="wasSubmittedBefore",
                                                            value="Tak"
                                                        )
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Wnioskowana kwota",
                                                    name="otherProjectFundingAmount",
                                                    required=True,
                                                    validators=[
                                                        self.validator.related_required_if_equal_validator(
                                                            field_name="wasSubmittedBefore",
                                                            value="Tak"
                                                        )
                                                    ],
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
        }

        EducationApplicationBuilder.create_application_scope_of_project(self, data=data)
