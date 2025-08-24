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
