from classes.form_builder.form_builder_base import FormBuilderBase


class Part(FormBuilderBase):
    def __init__(self):
        super().__init__()

    def application_basic_data(self, data: dict):
        return self.create_part(
            title="I. Dane podstawowe",
            short_name="I. Dane podstawowe",
            chapters=[
                self.create_chapter(
                    title="1. Nazwa programu operacyjnego / priorytetu",
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Program",
                            name="programNamePartTwo",
                            read_only=True,
                            value=data["operation_name"]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Priorytet",
                            name="priorityNamePartTwo",
                            read_only=True,
                            value=data["priority_name"]
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Nazwa przedsięwzięcia, którego dotyczy wniosek",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="applicationTaskName",
                            validators=[
                                self.validator.length_validator(max_value=100)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="3. Rodzaj przedsięwzięcia określony w programie operacyjnym",
                    components=[
                        self.create_component(
                            component_type="radio",
                            name="projectType",
                            value=data['projectType']['options'][0] if len(data['projectType']['options']) == 1 else "",
                            read_only=True if len(data['projectType']['options']) == 1 else False,
                            options=data["projectType"]["options"]
                        )
                    ]
                ),
                self.create_chapter(
                    title="4. Poprzednie edycje przedsięwzięcia",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    label="Czy był składany wniosek na poprzednią edycję tego przedsięwzięcia",
                                    name="previousApplicationForProject",
                                    options=[
                                        "Tak",
                                        "Nie"
                                    ],
                                    validators=[
                                        self.validator.exact_validator(
                                            values=[
                                                "Tak",
                                                "Nie"
                                            ]
                                        )
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="previousApplicationForProject",
                                    values=[
                                        "Tak"
                                    ]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="Proszę podać numer wniosku nadany przez PISF",
                                    name="fiveDigitNumberOfApplication",
                                    required=True,
                                    validators=[
                                        self.validator.related_required_if_equal_validator(
                                            field_name="previousApplicationForProject",
                                            value="Tak"
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )

    def application_schedule_data(self):
        return self.create_part(
            title="VIII. Harmonogram realizacji przedsięwzięcia",
            short_name="VIII. Harmonogram",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Nazwa przedsięwzięcia",
                            name="projectNameRepeatSchedule",
                            read_only=True,
                            required=True,
                            calculation_rules=[
                                self.calculation_rule.copy_value(
                                    from_name="applicationTaskName"
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    multiple_forms_rules={
                        "minCount": 1,
                        "maxCount": 20
                    },
                    components=[
                        self.create_chapter(
                            class_list={
                                "main": [
                                    "dates"
                                ],
                                "sub": [
                                    "dates-item"
                                ]
                            },
                            components=[
                                self.create_component(
                                    component_type="date",
                                    label="Termin od",
                                    name="taskActionDateStart",
                                    validators=[
                                        self.validator.related_local_date_lte_validator(
                                            field_name="taskActionDateEnd",
                                            message="Termin rozpoczęcia działania musi być wcześniejszy niż termin jego zakończenia."
                                        )
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="date",
                                    label="Termin do",
                                    name="taskActionDateEnd",
                                    validators=[
                                        self.validator.related_local_date_gte_validator(
                                            field_name="taskActionDateStart",
                                            message="Termin zakończenia działania musi być późniejszy niż termin jego rozpoczęcia."
                                        )
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="textarea",
                                    label="Działanie",
                                    name="taskActionDesc",
                                    help_text="Krótki opis działania",
                                    class_list=[
                                        "full-width",
                                        "col-span-2"
                                    ],
                                    validators=[
                                        self.validator.length_validator(max_value=250)
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    class_list={
                        "main": [
                            "dates"
                        ],
                        "sub": [
                            "dates-item"
                        ]
                    },
                    components=[
                        self.create_component(
                            component_type="date",
                            label="Rozpoczęcie realizacji przedsięwzięcia",
                            name="projectCommencement",
                            read_only=True,
                            required=True,
                            calculation_rules=[
                                self.calculation_rule.first_date(
                                    field="taskActionDateStart"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="date",
                            label="Zakończenie realizacji przedsięwzięcia",
                            name="projectCompletion",
                            read_only=True,
                            required=True,
                            calculation_rules=[
                                self.calculation_rule.last_date(
                                    field="taskActionDateStart"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="date",
                            label="Termin rozliczenia z PISF",
                            name="settlementDeadline",
                            read_only=True,
                            required=True,
                            calculation_rules=[
                                self.calculation_rule.relate_to_last_date(
                                    field="projectCompletion",
                                    parameter=30
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Uwaga! <br /><small>Harmonogram przedsięwzięcia powinien uwzględniać etapy: <normal><br />1. przygotowawczy (np. zaproszenie uczestników, rekrutacja, rezerwacja noclegów itp.), <br />2. realizacji przedsięwzięcia (np. przeprowadzenie warsztatów, festiwal itp.), <br />3. zakończenie przedsięwzięcia (data zakończenia realizacji przedsięwzięcia (dzień, miesiąc, rok). <br />Prosimy o chronologiczne ułożenie wszystkich pozycji harmonogramu. </normal></small>"
                )
            ]
        )
