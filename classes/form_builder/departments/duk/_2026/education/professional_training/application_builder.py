from classes.helpers import int_to_roman
from .estimate_data import estimate_sections_pt124, estimate_sections_pt3
from classes.form_builder.departments.duk._2026.application_estimate_builder import DUKApplicationEstimateBuilder
from ..priority import ProfessionalTrainingPriority
from ..application_builder import EducationApplicationBuilder


class ProfessionalTrainingApplicationBuilder(EducationApplicationBuilder, ProfessionalTrainingPriority):
    FORM_ID = 18

    def __init__(self):
        super().__init__()

        self.project_type = [
            "Podnoszenie kwalifikacji i kompetencji zawodowych przedstawicieli wszystkich grup zawodowych sektora audiowizualnego poprzez organizację szkoleń, warsztatów, kursów oraz innych form doskonalenia zawodowego, w tym programów długoterminowych.",
            "Kształcenie w kierunku zdobycia dodatkowych umiejętności i zawodów związanych z potrzebami współczesnego rynku audiowizualnego.",
            "Organizacja kursów nauki języków obcych dla przedstawicieli zawodów filmowych.",
            "Inne działania, realizujące cele Priorytetu III."
        ]

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

        self.is_basic_number_data = True

    def create_application_basic_number_data(self, number):
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

        part = self.create_part(
            title=f"{int_to_roman(number)}. Podstawowe dane liczbowe i wskaźniki",
            short_name=f"{int_to_roman(number)}. Dane liczbowe",
            chapters=[
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
                            components=[
                                self.create_chapter(
                                    multiple_forms_rules={"minCount": 1, "maxCount": 20},
                                    components=[
                                        self.create_chapter(
                                            title="Pozycja",
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
                            components=[
                                self.create_chapter(
                                    multiple_forms_rules={"minCount": 1, "maxCount": 20},
                                    components=[
                                        self.create_chapter(
                                            title="Pozycja",
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
                            components=[
                                self.create_chapter(
                                    multiple_forms_rules={"minCount": 1, "maxCount": 20},
                                    components=[
                                        self.create_chapter(
                                            title="Pozycja",
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
        )
        self.save_part(part)
