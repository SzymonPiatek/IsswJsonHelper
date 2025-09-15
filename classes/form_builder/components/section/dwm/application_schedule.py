from classes.form_builder.form_builder_base import FormBuilderBase


class ApplicationSchedule(FormBuilderBase):
    def __init__(self):
        super().__init__()

    def task_action_dates(self):
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
