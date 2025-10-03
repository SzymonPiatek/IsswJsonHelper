from classes.form_builder.departments.duk._2025.education.application_builder import EducationApplicationBuilder
from classes.form_builder.departments.duk.application_builder import DUKApplicationBuilder
from classes.form_builder.departments.duk._2025.education.professional_training.estimate_data import estimate_sections_pt1235, \
    estimate_sections_pt4
from classes.form_builder.departments.duk.application_estimate_builder import DUKApplicationEstimateBuilder


class ProfessionalTrainingApplicationBuilder(EducationApplicationBuilder):
    PRIORITY_NAME = 'III. Edukacja i kształcenie profesjonalne'
    PRIORITY_NUM = 3
    FORM_ID = 9182

    def __init__(self):
        super().__init__()

    def create_application_basic_data(self, **kwargs):
        data = {
            'projectType': {
                'options': [
                    "kształcenie zawodowe i podnoszenie kompetencji poprzez organizację szkoleń zawodowych, warsztatów, kursów i innych przedsięwzięć lub programów długoterminowych",
                    "edukacja dotycząca historii filmu polskiego i światowego, estetyki filmowej i środków wyrazu oraz społecznych funkcji filmu",
                    "projekty edukacyjne dla przedstawicieli wszystkich grup zawodowych, pracujących na potrzeby polskiej kinematografii",
                    "organizacja kursów nauki języków obcych dla przedstawicieli zawodów filmowych",
                    "inne działania realizujące cele Priorytetu V",
                    "inne działania realizujące cele Priorytetu III",
                ]
            }
        }
        DUKApplicationBuilder.create_application_basic_data(self=self, data=data)

    def create_application_scope_of_project(self):
        last_chapter = self.section.application_scope_of_project.cinema_project_relation_to_other_fundings()
        last_chapter[
            "title"] = "Czy przedsięwzięcie, na które składany jest wniosek jest powiązane z innymi przedsięwzięciami, o dofinansowanie których ubiega się wnioskodawca w bieżącym roku z innych programów operacyjnych PISF? Jeżeli tak, proszę podać nazwę przedsięwzięcia, program oraz wnioskowaną kwotę dofinansowania"

        chapters_data = [
            {
                "label": "szkoleń",
                "name": "Trainings"
            },
            {
                "label": "warsztatów",
                "name": "Workshops"
            },
            {
                "label": "kursów",
                "name": "Courses"
            }
        ]

        data = {
            "chapters": [
                self.create_chapter(
                    title="7. Podstawowe dane liczbowe na temat bieżącej i poprzedniej edycji",
                    components=[
                        self.create_chapter(
                            title="<normal>1. Liczba wydarzeń w ramach realizowanego przedsięwzięcia (pola obowiązkowe do wypełnienia):</normal>",
                            class_list={"sub": ["table-1-2-top"]},
                            components=[
                                *[
                                    self.create_chapter(
                                        title=f"<small>- {chapter["label"]}</small>",
                                        class_list={
                                            "main": ["table-1-2", "grid", "grid-cols-2"],
                                            "sub": ["table-1-2__col"]
                                        },
                                        components=[
                                            self.create_component(
                                                component_type="number",
                                                label="Poprzednia edycja przedsięwzięcia",
                                                name=f"numberOfEvents{chapter["name"]}PreviousEdition",
                                                unit="szt.",
                                                value=0
                                            ),
                                            self.create_component(
                                                component_type="number",
                                                label="Bieżąca edycja przedsięwzięcia (przewidywane wielkości)",
                                                name=f"numberOfEvents{chapter["name"]}CurrentEdition",
                                                unit="szt.",
                                                value=0
                                            )
                                        ]
                                    )
                                    for chapter in chapters_data
                                ],
                                self.create_chapter(
                                    title="<small>- inne</small>",
                                    multiple_forms_rules={"minCount": 1, "maxCount": 20},
                                    components=[
                                        self.create_chapter(
                                            components=[
                                                self.create_chapter(
                                                    components=[
                                                        self.create_component(
                                                            component_type="text",
                                                            label="Rodzaj",
                                                            name="numberOfEventsOtherKind"
                                                        )
                                                    ]
                                                ),
                                                self.create_chapter(
                                                    class_list={
                                                        "main": ["table-1-2", "grid", "grid-cols-2"],
                                                        "sub": ["table-1-2__col"]
                                                    },
                                                    components=[
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Poprzednia edycja przedsięwzięcia",
                                                            name="numberOfEventsOtherPreviousEdition",
                                                            unit="szt.",
                                                            value=0
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Bieżąca edycja przedsięwzięcia (przewidywane wielkości)",
                                                            name="numberOfEventsOtherCurrentEdition",
                                                            unit="szt.",
                                                            value=0
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>Suma</normal>",
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
                                            label="Poprzednia edycja przedsięwzięcia",
                                            name="numerOfEventsPreviousEditionSum",
                                            read_only=True,
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        *[f"numberOfEvents{chapter["name"]}PreviousEdition" for chapter in chapters_data],
                                                        "numberOfEventsOtherPreviousEdition"
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        *[f"numberOfEvents{chapter["name"]}PreviousEdition" for chapter in chapters_data],
                                                        "numberOfEventsOtherPreviousEdition"
                                                    ]
                                                )
                                            ],
                                            unit="szt."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Bieżąca edycja przedsięwzięcia (przewidywane wielkości)",
                                            name="numberOfEventsCurrentEditionSum",
                                            read_only=True,
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        *[f"numberOfEvents{chapter["name"]}CurrentEdition" for chapter in chapters_data],
                                                        "numberOfEventsOtherCurrentEdition"
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        *[f"numberOfEvents{chapter["name"]}CurrentEdition" for chapter in chapters_data],
                                                        "numberOfEventsOtherCurrentEdition"
                                                    ]
                                                )
                                            ],
                                            unit="szt."
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="<normal>2. Liczba uczestników w ramach realizowanego przedsięwzięcia:</normal>",
                            class_list={"sub": ["table-1-2-top"]},
                            components=[
                                *[
                                    self.create_chapter(
                                        title=f"<small>- {chapter["label"]}</small>",
                                        class_list={
                                            "main": ["table-1-2", "grid", "grid-cols-2"],
                                            "sub": ["table-1-2__col"]
                                        },
                                        components=[
                                            self.create_component(
                                                component_type="number",
                                                label="Poprzednia edycja przedsięwzięcia",
                                                name=f"participantsCountPreviousEdition{chapter["name"]}",
                                                unit="os."
                                            ),
                                            self.create_component(
                                                component_type="number",
                                                label="Bieżąca edycja przedsięwzięcia (przewidywane wielkości)",
                                                name=f"participantsCountCurrentEdition{chapter["name"]}",
                                                unit="os."
                                            )
                                        ]
                                    )
                                    for chapter in chapters_data
                                ],
                                self.create_chapter(
                                    title="<small>- inne</small>",
                                    multiple_forms_rules={"minCount": 1, "maxCount": 20},
                                    components=[
                                        self.create_chapter(
                                            components=[
                                                self.create_chapter(
                                                    components=[
                                                        self.create_component(
                                                            component_type="text",
                                                            label="Rodzaj",
                                                            name="participantsCountOtherKind",
                                                            validators=[
                                                                self.validator.length_validator(
                                                                    max_value=100
                                                                )
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                self.create_chapter(
                                                    class_list={
                                                        "main": ["table-1-2", "grid", "grid-cols-2"],
                                                        "sub": ["table-1-2__col"]
                                                    },
                                                    components=[
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Poprzednia edycja przedsięwzięcia",
                                                            name="participantsCountPreviousEditionOther",
                                                            unit="os."
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Bieżąca edycja przedsięwzięcia (przewidywane wielkości)",
                                                            name="participantsCountCurrentEditionOther",
                                                            unit="os."
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>Suma</normal>",
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
                                            label="Poprzednia edycja przedsięwzięcia",
                                            name="participantsCountCurrentEditionSum",
                                            read_only=True,
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        *[f"participantsCountPreviousEdition{chapter["name"]}" for chapter in chapters_data],
                                                        "participantsCountPreviousEditionOther"
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        *[f"participantsCountPreviousEdition{chapter["name"]}" for chapter in chapters_data],
                                                        "participantsCountPreviousEditionOther"
                                                    ]
                                                )
                                            ],
                                            unit="os."
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="<normal>3. Wpływy ze sprzedaży:</normal>",
                            class_list={
                                "main": ["w-full"],
                                "sub": ["table-4-top"]
                            },
                            components=[
                                *[
                                    self.create_chapter(
                                        title=f"<small>- {chapter["label"]}</small>",
                                        class_list={
                                            "main": ["table-4", "grid", "grid-cols-4"],
                                            "sub": ["table-4__col"]
                                        },
                                        components=[
                                            self.create_component(
                                                component_type="text",
                                                label="Poprzednia edycja przedsięwzięcia",
                                                name=f"proceedsOfSalePreviousEdition{chapter["name"]}",
                                                unit="PLN",
                                                mask="fund"
                                            ),
                                            self.create_component(
                                                component_type="text",
                                                label="Koszt jednostkowy",
                                                name=f"proceedsOfSalePreviousEdition{chapter["name"]}UnitCost",
                                                unit="PLN",
                                                mask="fund"
                                            ),
                                            self.create_component(
                                                component_type="text",
                                                label="Bieżąca edycja przedsięwzięcia (przewidywane wielkości)",
                                                name=f"proceedsOfSaleCurrentEdition{chapter["name"]}",
                                                unit="PLN",
                                                mask="fund"
                                            ),
                                            self.create_component(
                                                component_type="text",
                                                label="Koszt jednostkowy",
                                                name=f"proceedsOfSaleCurrentEdition{chapter["name"]}UnitCost",
                                                unit="PLN",
                                                mask="fund"
                                            )
                                        ]
                                    )
                                    for chapter in chapters_data
                                ],
                                self.create_chapter(
                                    title="<small>- inne</small>",
                                    multiple_forms_rules={"minCount": 1, "maxCount": 20},
                                    components=[
                                        self.create_chapter(
                                            components=[
                                                self.create_chapter(
                                                    components=[
                                                        self.create_component(
                                                            component_type="text",
                                                            label="Rodzaj",
                                                            name="proceedsOfSalePreviousEditionKind"
                                                        )
                                                    ]
                                                ),
                                                self.create_chapter(
                                                    class_list={
                                                        "main": ["table-4", "grid", "grid-cols-4"],
                                                        "sub": ["table-4__col"]
                                                    },
                                                    components=[
                                                        self.create_component(
                                                            component_type="text",
                                                            label="Poprzednia edycja przedsięwzięcia",
                                                            name="proceedsOfSalePreviousEditionOther",
                                                            unit="PLN",
                                                            mask="fund"
                                                        ),
                                                        self.create_component(
                                                            component_type="text",
                                                            label="Koszt jednostkowy",
                                                            name="proceedsOfSalePreviousEditionOtherUnitCost",
                                                            unit="PLN",
                                                            mask="fund"
                                                        ),
                                                        self.create_component(
                                                            component_type="text",
                                                            label="Bieżąca edycja przedsięwzięcia (przewidywane wielkości)",
                                                            name="proceedsOfSaleCurrentEditionOther",
                                                            unit="PLN",
                                                            mask="fund"
                                                        ),
                                                        self.create_component(
                                                            component_type="text",
                                                            label="Koszt jednostkowy",
                                                            name="proceedsOfSaleCurrentEditionOtherUnitCost",
                                                            unit="PLN",
                                                            mask="fund"
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>Suma</normal>",
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
                                            label="Poprzednia edycja przedsięwzięcia",
                                            name="proceedsOfSalePreviousSum",
                                            read_only=True,
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        *[f"proceedsOfSalePreviousEdition{chapter["name"]}" for chapter in chapters_data],
                                                        "proceedsOfSalePreviousEditionOther"
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        *[f"proceedsOfSalePreviousEdition{chapter["name"]}" for chapter in chapters_data],
                                                        "proceedsOfSalePreviousEditionOther"
                                                    ]
                                                )
                                            ],
                                            unit="PLN"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Koszt jednostkowy",
                                            name="proceedsOfSalePreviousEditionSumUnitCost",
                                            read_only=True,
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        *[f"proceedsOfSalePreviousEdition{chapter["name"]}UnitCost" for chapter in chapters_data],
                                                        "proceedsOfSalePreviousEditionOtherUnitCost"
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        *[f"proceedsOfSaleCurrentEdition{chapter["name"]}UnitCost" for chapter in chapters_data],
                                                        "proceedsOfSaleCurrentEditionOtherUnitCost"
                                                    ]
                                                )
                                            ],
                                            unit="PLN"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Bieżąca edycja przedsięwzięcia (przewidywane wielkości)",
                                            name="proceedsOfSaleCurrentSum",
                                            read_only=True,
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        *[f"proceedsOfSaleCurrentEdition{chapter["name"]}" for chapter in chapters_data],
                                                        "proceedsOfSaleCurrentEditionOther"
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        *[f"proceedsOfSaleCurrentEdition{chapter["name"]}" for chapter in chapters_data],
                                                        "proceedsOfSaleCurrentEditionOther"
                                                    ]
                                                )
                                            ],
                                            unit="PLN"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Koszt jednostkowy",
                                            name="proceedsOfSaleCurrentEditionSumUnitCost",
                                            read_only=True,
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        *[f"proceedsOfSaleCurrentEdition{chapter["name"]}UnitCost" for chapter in chapters_data],
                                                        "proceedsOfSaleCurrentEditionOtherUnitCost"
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        *[f"proceedsOfSaleCurrentEdition{chapter["name"]}UnitCost" for chapter in chapters_data],
                                                        "proceedsOfSaleCurrentEditionOtherUnitCost"
                                                    ]
                                                )
                                            ],
                                            unit="PLN"
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                last_chapter
            ]
        }

        EducationApplicationBuilder.create_application_scope_of_project(
            self, data=data
        )

    def create_application_project_costs(self):
        estimate_pt1235 = DUKApplicationEstimateBuilder(
            estimate_sections=estimate_sections_pt1235,
            after_name="Pt1235"
        )
        estimate_pt4 = DUKApplicationEstimateBuilder(
            estimate_sections=estimate_sections_pt4,
            after_name="Pt4"
        )

        part = self.create_part(
            title="VII. Kosztorys przedsięwzięcia",
            short_name="VII. Kosztorys przedsięwzięcia",
            chapters=[
                estimate_pt1235.generate_estimate_top(),
                estimate_pt1235.generate_estimate_headers(),
                self.create_chapter(
                    components=[
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "kształcenie zawodowe i podnoszenie kompetencji poprzez organizację szkoleń zawodowych, warsztatów, kursów i innych przedsięwzięć lub programów długoterminowych",
                                        "edukacja dotycząca historii filmu polskiego i światowego, estetyki filmowej i środków wyrazu oraz społecznych funkcji filmu",
                                        "projekty edukacyjne dla przedstawicieli wszystkich grup zawodowych, pracujących na potrzeby polskiej kinematografii",
                                        "inne działania realizujące cele Priorytetu III"
                                    ]
                                )
                            ],
                            components=[
                                estimate_pt1235.generate_estimate(),
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "organizacja kursów nauki języków obcych dla przedstawicieli zawodów filmowych"
                                    ]
                                )
                            ],
                            components=[
                                estimate_pt4.generate_estimate(),
                            ]
                        )
                    ]
                ),
                estimate_pt1235.generate_estimate_bottom()
            ]
        )

        self.save_part(part=part)
