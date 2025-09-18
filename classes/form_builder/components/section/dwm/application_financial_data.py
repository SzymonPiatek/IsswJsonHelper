from classes.form_builder.components.section.section import Section


class ApplicationFinancialData(Section):
    def __init__(self):
        super().__init__()

    def other_partners_funding(self, number: str):
        return self.create_chapter(
            title=f"{number}. Środki innych partnerów/sponsorów (wyłącznie udokumentowane deklaracjami i listami intencyjnymi)",
            class_list={
                "main": [
                    "table-2-top"
                ]
            },
            components=[
                self.create_chapter(
                    multiple_forms_rules={
                        "minCount": 1,
                        "maxCount": 20
                    },
                    class_list={
                        "main": [
                            "table-2-multiple"
                        ]
                    },
                    components=[
                        self.create_chapter(
                            title="Podmiot finansujący",
                            class_list={
                                "main": [
                                    "table-2",
                                    "grid",
                                    "grid-cols-2"
                                ],
                                "sub": [
                                    "table-2__col"
                                ]
                            },
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    label="Nazwa podmiotu finansującego",
                                    name="otherPartnersSponsorsName",
                                    class_list=[
                                        "table-2__col--textarea"
                                    ],
                                    validators=[
                                        self.validator.length_validator(max_value=200)
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Kwota",
                                    name="otherPartnersSponsorsAmount",
                                    class_list=[
                                        "table-2__col--text"
                                    ],
                                    unit="PLN"
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Razem",
                    class_list={
                        "main": [
                            "summary"
                        ]
                    },
                    components=[
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            name="otherPartnersSponsorsAmountSum",
                            read_only=True,
                            calculation_rules=[
                                self.calculation_rule.dynamic_sum_inputs(
                                    fields=[
                                        "otherPartnersSponsorsAmount"
                                    ]
                                )
                            ],
                            validators=[
                                self.validator.related_sum_validator(
                                    field_names=[
                                        "otherPartnersSponsorsAmount"
                                    ]
                                )
                            ],
                            unit="PLN"
                        )
                    ]
                )
            ]
        )

    def other_public_funding(self, number: str):
        return self.create_chapter(
            title=f"{number}. Pozostałe źródła publiczne (wyłącznie udokumentowane deklaracjami i listami intencyjnymi)",
            class_list={
                "main": [
                    "table-2-top"
                ]
            },
            components=[
                self.create_chapter(
                    multiple_forms_rules={
                        "minCount": 1,
                        "maxCount": 20
                    },
                    class_list={
                        "main": [
                            "table-2-multiple"
                        ]
                    },
                    components=[
                        self.create_chapter(
                            title="Podmiot publiczny",
                            class_list={
                                "main": [
                                    "table-2",
                                    "grid",
                                    "grid-cols-2"
                                ],
                                "sub": [
                                    "table-2__col"
                                ]
                            },
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    label="Nazwa podmiotu publicznego",
                                    name="otherSourcesName",
                                    class_list=[
                                        "table-2__col--textarea"
                                    ],
                                    validators=[
                                        self.validator.length_validator(max_value=200)
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Kwota",
                                    name="otherSourcesAmount",
                                    class_list=[
                                        "table-2__col--text"
                                    ],
                                    unit="PLN"
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Razem",
                    class_list={
                        "main": [
                            "summary"
                        ]
                    },
                    components=[
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            name="otherSourcesAmountSum",
                            read_only=True,
                            calculation_rules=[
                                self.calculation_rule.dynamic_sum_inputs(
                                    fields=[
                                        "otherSourcesAmount"
                                    ]
                                )
                            ],
                            validators=[
                                self.validator.related_sum_validator(
                                    field_names=[
                                        "otherSourcesAmount"
                                    ]
                                )
                            ],
                            unit="PLN"
                        )
                    ]
                )
            ]
        )
