from classes.form_builder.dwm.report_builder import DWMReportBuilder


class DWMReportBuilder2026(DWMReportBuilder):
    YEAR = 2026

    def __init__(self):
        super().__init__()

    def create_report_base(self):
        self.create_base(
            intro_text=[
                "Raport końcowy",
                "<small>z wykonania przedsięwzięcia realizowanego w ramach Programu Operacyjnego \"Promocja polskiej twórczości filmowej za granicą\"</small> <br> Priorytet I \"Promocja polskiej twórczości filmowej za granicą\""
            ]
        )

    def create_report_basic_data(self):
        part = self.create_part(
            title="I. Dane podstawowe",
            short_name="I. Dane podstawowe",
            chapters=[
                self.create_chapter(
                    title="A. Okres realizacji przedsięwzięcia",
                    class_list={
                        "main": [
                            "table-1-2",
                            "grid",
                            "grid-cols-6",
                            "no-title"
                        ],
                        "sub": [
                            "table-1-2__col"
                        ]
                    },
                    components=[
                        self.create_component(
                            component_type="header",
                            name="taskDateStart",
                            value="Data wpłynięcia wniosku",
                            class_list=[
                                "col-start-3",
                                "text-right",
                                "displayNoneFrontend"
                            ]
                        ),
                        self.create_component(
                            component_type="date",
                            label="Data wpłynięcia wniosku",
                            name="taskDateStart",
                            read_only=True,
                            required=True,
                            copyFrom="$submitted_at",
                            class_list=[
                                "no-label"
                            ]
                        ),
                        self.create_component(
                            component_type="header",
                            name="taskDateEnd",
                            value="Data zakończenia przedsięwzięcia",
                            class_list=[
                                "text-right",
                                "displayNoneFrontend"
                            ]
                        ),
                        self.create_component(
                            component_type="date",
                            label="Data zakończenia przedsięwzięcia",
                            name="taskDateEnd",
                            read_only=True,
                            required=True,
                            copyFrom="$submitted_at",
                            class_list=[
                                "no-label"
                            ]
                        ),
                    ]
                ),
                self.create_chapter(
                    components=[
                        self.create_chapter(
                            title="B. Umowa",
                            class_list={
                                "main": [
                                    "table-1-2",
                                    "grid",
                                    "grid-cols-6",
                                    "no-title"
                                ],
                                "sub": [
                                    "table-1-2__col"
                                ]
                            },
                            components=[
                                self.create_component(
                                    component_type="header",
                                    name="contractNum",
                                    value="Numer umowy",
                                    class_list=[
                                        "col-start-3",
                                        "text-right",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Numer umowy",
                                    name="contractNum",
                                    copyFrom="$jrwa",
                                    read_only=True,
                                    required=True,
                                    validators=[
                                        self.validator.length_validator(max_value=16)
                                    ],
                                    class_list=[
                                        "no-label"
                                    ]
                                ),
                                self.create_component(
                                    component_type="header",
                                    name="contractDate",
                                    value="Data zawarcia umowy",
                                    class_list=[
                                        "text-right",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="date",
                                    label="Data zawarcia umowy",
                                    name="contractDate",
                                    required=True,
                                    class_list=[
                                        "no-label"
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            class_list={
                                "main": [
                                    "grid",
                                    "grid-cols-6",
                                    "no-title"
                                ]
                            },
                            components=[
                                self.create_component(
                                    component_type="header",
                                    name="addAnnex",
                                    value="Czy umowa była aneksowana?",
                                    class_list=[
                                        "col-span-2",
                                        "col-start-3",
                                        "text-right",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="checkbox",
                                    label="Czy umow była aneksowana",
                                    name="addAnnex",
                                    class_list=[
                                        "no-label"
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="addAnnex",
                                    values=[True]
                                )
                            ],
                            multiple_forms_rules={
                                "minCount": 1,
                                "maxCount": 10,
                            },
                            components=[
                                self.create_chapter(
                                    class_list={
                                        "main": [
                                            "table-1-2",
                                            "grid",
                                            "grid-cols-6",
                                            "no-title"
                                        ],
                                        "sub": [
                                            "table-1-2__col"
                                        ]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="header",
                                            name="contractAnnexNum",
                                            value="Numer aneksu",
                                            class_list=[
                                                "col-span-2",
                                                "col-start-2",
                                                "text-right",
                                                "displayNoneFrontend"
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Numer aneksu",
                                            name="contractAnnexNum",
                                            validators=[
                                                self.validator.length_validator(max_value=3)
                                            ],
                                            class_list=[
                                                "no-label"
                                            ],
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="header",
                                            name="contractAnnexDate",
                                            value="Data zawarcia aneksu",
                                            class_list=[
                                                "text-right",
                                                "displayNoneFrontend"
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="date",
                                            label="Data zawarcia aneksu",
                                            name="contractAnnexDate",
                                            class_list=[
                                                "no-label"
                                            ],
                                            required=True
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="C. Nazwa i adres Beneficjenta",
                    class_list=[
                        "no-title",
                        "grid",
                        "grid-cols-5",
                        "no-title"
                    ],
                    components=[
                        self.create_component(
                            component_type="header",
                            name="granteeFullName",
                            value="Nazwa Beneficjenta",
                            class_list=[
                                "displayNoneFrontend"
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Nazwa Beneficjenta",
                            copyFrom="applicantName",
                            required=True,
                            read_only=True,
                            class_list=[
                                "no-label",
                                "col-span-4",
                                "text-left"
                            ],
                            name="granteeFullName"
                        ),
                        self.create_component(
                            component_type="header",
                            name="granteeFullAddress",
                            value="Adres Beneficjenta",
                            class_list=[
                                "displayNoneFrontend"
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Adres Beneficjenta",
                            name="granteeFullAddress",
                            validators=[
                                self.validator.length_validator(max_value=400)
                            ],
                            required=True,
                            class_list=[
                                "no-label",
                                "col-span-4",
                                "text-left"
                            ]
                        )
                    ]
                )
            ]
        )

        self.save_part(part)

    def create_report_general_data(self):
        pass

    def create_report_expenditure_exacution(self):
        pass

    def create_report_additional_information(self):
        pass

