from classes.form_factory.form_factory import FormFactory


class ApplicationSchedule(FormFactory):
    def __init__(self):
        super().__init__()

    def task_action_dates(self):
        return self.create_chapter(
            multiple_forms_rules={
                "minCount": 3,
                "maxCount": 20
            },
            components=[
                self.create_chapter(
                    title="Etap",
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
                            name=f"taskActionDateStart",
                            required=True,
                            validators=[
                                self.validator.related_local_date_lte_validator(
                                    field_name="taskActionDateEnd",
                                    message="Data początkowa musi być wcześniejsza od daty końcowej"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="date",
                            label="Termin do",
                            name=f"taskActionDateEnd",
                            required=True,
                            validators=[
                                self.validator.related_local_date_gte_validator(
                                    field_name="taskActionDateStart",
                                    message="Data końcowa musi być późniejsza od daty początkowej"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Działanie",
                            name=f"taskActionDesc",
                            help_text="Krótki opis działania",
                            validators=[
                                self.validator.length_validator(max_value=500)
                            ],
                            required=True,
                            class_list=[
                                "table-full",
                                "col-span-2"
                            ]
                        )
                    ]
                )
            ]
        )

    def task_action_dates_final(self):
        return self.create_chapter(
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
                    label="Zakończenie realizacji przedsięwzięcia",
                    name="taskActionCompletionDate",
                    read_only=True,
                    calculation_rules=[
                        self.calculation_rule.last_date(field="taskActionDateEnd")
                    ],
                    required=True
                ),
                self.create_component(
                    component_type="date",
                    label="Maksymalny termin złożenia raportu końcowego do PISF",
                    name="taskActionSettlingDate",
                    read_only=True,
                    calculation_rules=[
                        self.calculation_rule.relate_to_last_date(
                            field="taskActionDateEnd",
                            parameter=30
                        )
                    ],
                    required=True
                )
            ]
        )
