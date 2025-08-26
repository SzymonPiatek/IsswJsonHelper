from classes.form_builder.duk.education.application_builder import EducationApplicationBuilder
from classes.form_builder.duk.application_builder import DUKApplicationBuilder


class SecondarySchoolsApplicationBuilder(EducationApplicationBuilder):
    PRIORITY_NAME = 'II. Edukacja w szkołach średnich i zawodowych'
    PRIORITY_NUM = 2
    FORM_ID = 9181

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'professional_training'

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

    def create_application_scope_of_project(self):
        basic_data_chapters = [
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
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "programy edukacyjne wchodzące w skład edukacji ciągłej",
                                        "kształcenie w kierunku zdobycia zawodów związanych z potrzebami współczesnego rynku audiowizualnego"
                                    ]
                                )
                            ],
                            components=[
                                self.create_chapter(
                                    title="<normal>1. Liczba studentów (studia stacjonarne)</normal>",
                                    components=[
                                        self.create_component(
                                            component_type="number",
                                            label="Liczba uczniów",
                                            name="studentsCount",
                                            unit="osoby"
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>2. Średnia wysokość czesnego (w rozrachunku rocznym, studia stacjonarne)</normal>",
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            label="Studia stacjonarne",
                                            name="averageTuitionFeesPerAnnum",
                                            mask="fund",
                                            unit="PLN"
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>3. Średni koszt kształcenia ucznia (w roku i w tys. zł, studia stacjonarne)</normal>",
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            label="Studia stacjonarne",
                                            name="averagePupilCostOfEducationPerYear",
                                            validators=[
                                                self.validator.range_validator(min_value=1000)
                                            ],
                                            mask="fund",
                                            unit="PLN"
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
                                        "inne działania realizujące cele Priorytetu II"
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
                                                    unit="szt."
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Bieżąca edycja (planowane wielkości)",
                                                    name=f"{chapter["name"]}CurrentEditionPkt4",
                                                    unit="szt."
                                                )
                                            ]
                                        ) for chapter in basic_data_chapters],
                                        self.create_chapter(
                                            title="<normal>- innych</normal>",
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
                                                            unit="szt."
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Bieżąca edycja (planowane wielkości)",
                                                            name="otherCurrentEditionPkt4",
                                                            unit="szt."
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
                                                    name="otherPastEditionPkt4Sum",
                                                    unit="szt.",
                                                    read_only=True,
                                                    validators=[
                                                        self.validator.related_sum_validator(
                                                            field_names=[
                                                                *[f"{chapter["name"]}PastEditionPkt4" for chapter in basic_data_chapters],
                                                                "otherPastEditionPkt4"
                                                            ]
                                                        )
                                                    ],
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                *[f"{chapter["name"]}PastEditionPkt4" for chapter in basic_data_chapters],
                                                                "otherPastEditionPkt4"
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Bieżąca edycja (planowane wielkości)",
                                                    name="otherCurrentEditionPkt4Sum",
                                                    unit="szt.",
                                                    read_only=True,
                                                    validators=[
                                                        self.validator.related_sum_validator(
                                                            field_names=[
                                                                *[f"{chapter["name"]}CurentEditionPkt4" for chapter in basic_data_chapters],
                                                                "otherCurrentEditionPkt4"
                                                            ]
                                                        )
                                                    ],
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                *[f"{chapter["name"]}CurentEditionPkt4" for chapter in basic_data_chapters],
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
                                                    unit="os."
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Bieżąca edycja (planowane wielkości)",
                                                    name=f"{chapter["name"]}ParticipantsCurrentEditionPkt4",
                                                    unit="os."
                                                )
                                            ]
                                        ) for chapter in basic_data_chapters],
                                        self.create_chapter(
                                            title="<normal>- innych</normal>",
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
                                                            unit="os."
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Bieżąca edycja (planowane wielkości)",
                                                            name="otherParticipantsCurrentEditionPkt4",
                                                            unit="os."
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
                                                    unit="os.",
                                                    read_only=True,
                                                    validators=[
                                                        self.validator.related_sum_validator(
                                                            field_names=[
                                                                *[f"{chapter["name"]}ParticipantsPastEditionPkt4" for chapter in basic_data_chapters],
                                                                "otherParticipantsPastEditionPkt4"
                                                            ]
                                                        )
                                                    ],
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                *[f"{chapter["name"]}ParticipantsPastEditionPkt4" for chapter in basic_data_chapters],
                                                                "otherParticipantsPastEditionPkt4"
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Bieżąca edycja (planowane wielkości)",
                                                    name="participantsSumCurrentEditionPkt4",
                                                    unit="os.",
                                                    read_only=True,
                                                    validators=[
                                                        self.validator.related_sum_validator(
                                                            field_names=[
                                                                *[f"{chapter["name"]}ParticipantsPastEditionPkt4" for chapter in basic_data_chapters],
                                                                "otherParticipantsPastEditionPkt4"
                                                            ]
                                                        )
                                                    ],
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                *[f"{chapter["name"]}ParticipantsCurrentEditionPkt4" for chapter in basic_data_chapters],
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
                                                    mask="fund",
                                                    label="Suma: poprzednia edycja",
                                                    name=f"{chapter["name"]}IncomePastEditionPkt4",
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Koszt jednostkowy: poprzednia edycja",
                                                    name=f"{chapter["name"]}CostPastEditionPkt4",
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Suma: bieżąca edycja (planowane wielkości)",
                                                    name=f"{chapter["name"]}IncomeCurrentEditionPkt4",
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Koszt jednostkowy: bieżąca edycja",
                                                    name=f"{chapter["name"]}CostCurrentEditionPkt4",
                                                    unit="PLN"
                                                )
                                            ]
                                        ) for chapter in basic_data_chapters],
                                        self.create_chapter(
                                            title="<normal>- innych</normal>",
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
                                                            component_type="text",
                                                            mask="fund",
                                                            label="Suma: poprzednia edycja",
                                                            name="otherIncomePastEditionPkt4",
                                                            unit="PLN"
                                                        ),
                                                        self.create_component(
                                                            component_type="text",
                                                            mask="fund",
                                                            label="Koszt jednostkowy: poprzednia edycja",
                                                            name="otherCostPastEditionPkt4",
                                                            unit="PLN"
                                                        ),
                                                        self.create_component(
                                                            component_type="text",
                                                            mask="fund",
                                                            label="Suma: bieżąca edycja (planowane wielkości)",
                                                            name="otherIncomeCurrentEditionPkt4",
                                                            unit="PLN"
                                                        ),
                                                        self.create_component(
                                                            component_type="text",
                                                            mask="fund",
                                                            label="Koszt jednostkowy: bieżąca edycja",
                                                            name="otherCostCurrentEditionPkt4",
                                                            unit="PLN"
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
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Suma: poprzednia edycja",
                                                    name="sumIncomePastEditionPkt4",
                                                    unit="PLN",
                                                    read_only=True,
                                                    validators=[
                                                        self.validator.related_sum_validator(
                                                            field_names=[
                                                                *[f"{chapter["name"]}IncomePastEditionPkt4" for chapter in basic_data_chapters],
                                                                "otherIncomePastEditionPkt4"
                                                            ]
                                                        )
                                                    ],
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                *[f"{chapter["name"]}IncomePastEditionPkt4" for chapter in basic_data_chapters],
                                                                "otherIncomePastEditionPkt4"
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Koszt jednostkowy: poprzednia edycja",
                                                    name="sumCostPastEditionPkt4",
                                                    unit="PLN",
                                                    read_only=True,
                                                    validators=[
                                                        self.validator.related_sum_validator(
                                                            field_names=[
                                                                *[f"{chapter["name"]}CostPastEditionPkt4" for chapter in basic_data_chapters],
                                                                "otherCostPastEditionPkt4"
                                                            ]
                                                        )
                                                    ],
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                *[f"{chapter["name"]}CostPastEditionPkt4" for chapter in basic_data_chapters],
                                                                "otherCostPastEditionPkt4"
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Suma: bieżąca edycja (planowane wielkości)",
                                                    name="sumIncomeCurrentEditionPkt4",
                                                    unit="PLN",
                                                    read_only=True,
                                                    validators=[
                                                        self.validator.related_sum_validator(
                                                            field_names=[
                                                                *[f"{chapter["name"]}IncomeCurrentEditionPkt4" for chapter in basic_data_chapters],
                                                                "otherIncomeCurrentEditionPkt4"
                                                            ]
                                                        )
                                                    ],
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                *[f"{chapter["name"]}IncomeCurrentEditionPkt4" for chapter in basic_data_chapters],
                                                                "otherIncomeCurrentEditionPkt4"
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Koszt jednostkowy: bieżąca edycja",
                                                    name="sumCostCurrentEditionPkt4",
                                                    unit="PLN",
                                                    read_only=True,
                                                    validators=[
                                                        self.validator.related_sum_validator(
                                                            field_names=[
                                                                *[f"{chapter["name"]}CostCurrentEditionPkt4" for chapter in basic_data_chapters],
                                                                "otherCostCurrentEditionPkt4"
                                                            ]
                                                        )
                                                    ],
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                *[f"{chapter["name"]}CostCurrentEditionPkt4" for chapter in basic_data_chapters],
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
        }

        EducationApplicationBuilder.create_application_scope_of_project(
            self, data=data
        )
