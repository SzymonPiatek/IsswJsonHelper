from classes_new.form_builder.form_builder import ReportFormBuilder
from classes_new.form_components.section.dwm.section import DWMSection


class DWMDepartmentReportFormBuilder(ReportFormBuilder):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.parts = []

        self.section = DWMSection()
        self.is_promotion_priority: bool = False
        self.statements: list[dict] = []

    def create_report_basic_data(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Dane podstawowe",
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
                            copy_from="$submitted_at",
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
                            copy_from="$submitted_at",
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
                                    copy_from="$jrwa",
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
                                    label="Czy umowa była aneksowana?",
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
                            class_list=[
                                "swappable-bg"
                            ],
                            components=[
                                self.create_chapter(
                                    title="Aneks",
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
                            value=f"Nazwa {'Beneficjenta' if self.is_promotion_priority else 'Stypendysty'}",
                            class_list=[
                                "displayNoneFrontend"
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            label=f"Nazwa {'Beneficjenta' if self.is_promotion_priority else 'Stypendysty'}",
                            copy_from="applicantName",
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
                            value=f"Adres {'Beneficjenta' if self.is_promotion_priority else 'Stypendysty'}",
                            class_list=[
                                "displayNoneFrontend"
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            label=f"Adres {'Beneficjenta' if self.is_promotion_priority else 'Stypendysty'}",
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

    def create_report_general_data(self, number: int):
        components = [
            self.create_component(
                component_type="header",
                name="taskName",
                value="1. Nazwa przedsięwzięcia",
                class_list=[
                    "displayNoneFrontend"
                ]
            ),
            self.create_component(
                component_type="textarea",
                label="1. Nazwa przedsięwzięcia",
                name="taskName",
                required=True,
                validators=[
                    self.validator.length_validator(max_value=600)
                ],
                copy_from="applicationTaskName",
                read_only=True,
                class_list=[
                    "no-label",
                    "col-span-2",
                    "text-left"
                ]
            ),
            self.create_component(
                component_type="header",
                name="taskImplementationDesc",
                value="2. Szczegółowy opis wykonania przedsięwzięcia",
                class_list=[
                    "displayNoneFrontend"
                ]
            ),
            self.create_component(
                component_type="textarea",
                label="2. Szczegółowy opis wykonania przedsięwzięcia",
                name="taskImplementationDesc",
                validators=[
                    self.validator.length_validator(max_value=20000)
                ],
                required=True,
                class_list=[
                    "no-label",
                    "col-span-2",
                    "text-left"
                ],
            )
        ]

        if self.is_promotion_priority:
            components.extend([
                self.create_component(
                    component_type="header",
                    name="taskCompletionInfo",
                    value="3. Stopień realizacji przedsięwzięcia na dzień złożenia raportu",
                    class_list=[
                        "displayNoneFrontend"
                    ],
                ),
                self.create_component(
                    component_type="textarea",
                    label="3. Stopień realizacji przedsięwzięcia na dzień złożenia raportu",
                    name="taskCompletionInfo",
                    validators=[
                        self.validator.length_validator(max_value=10000)
                    ],
                    required=True,
                    class_list=[
                        "no-label",
                        "col-span-2",
                        "text-left"
                    ],
                ),
                self.create_component(
                    component_type="header",
                    name="taskImplementationByPartnersDesc",
                    value="4. Opis działań partnerów w ramach realizacji przedsięwzięcia ze szczególnym uwzględnieniem organów administracji publicznej",
                    class_list=[
                        "displayNoneFrontend"
                    ]
                ),
                self.create_component(
                    component_type="textarea",
                    name="taskImplementationByPartnersDesc",
                    label="4. Opis działań partnerów w ramach realizacji przedsięwzięcia ze szczególnym uwzględnieniem organów administracji publicznej",
                    validators=[
                        self.validator.length_validator(max_value=10000)
                    ],
                    required=True,
                    class_list=[
                        "no-label",
                        "col-span-2",
                        "text-left"
                    ]
                )
            ])

        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Informacje ogólne",
            chapters=[
                self.create_chapter(
                    class_list=[
                        "grid",
                        "grid-cols-3",
                        "no-title"
                    ],
                    components=components
                )
            ]
        )

        self.save_part(part)

    def create_report_additional_information(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Dodatkowe informacje",
            chapters=[
                self.create_chapter(
                    class_list=[
                        "grid",
                        "grid-cols-4",
                    ],
                    components=[
                        self.create_component(
                            component_type="header",
                            value="Dodatkowe informacje",
                            name="additionalGeneralComments",
                            class_list=[
                                "displayNoneFrontend"
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Dodatkowe informacje",
                            name="additionalGeneralComments",
                            validators=[
                                self.validator.length_validator(max_value=10000)
                            ],
                            class_list=[
                                "no-label",
                                "col-span-3",
                                "text-left"
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="header",
                                    value="Do raportu należy załączyć ewentualny raport medialny, ulotki, plakaty oraz inne materiały promocyjne i informacyjne.",
                                    name="attachmentsDesc"
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Informacja o załącznikach",
                            class_list=[
                                "grid",
                                "grid-cols-4",
                                "no-title"
                            ],
                            components=[
                                self.create_component(
                                    component_type="header",
                                    value="Informacja o załącznikach",
                                    name="attachmentsInfo",
                                    class_list=[
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="textarea",
                                    name="attachmentsInfo",
                                    validators=[
                                        self.validator.length_validator(max_value=20000)
                                    ],
                                    class_list=[
                                        "col-span-3",
                                        "text-left"
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Lista załączników",
                            components=[
                                self.create_chapter(
                                    multiple_forms_rules={
                                        "minCount": 1,
                                        "maxCount": 20
                                    },
                                    class_list={
                                        "main": [
                                            "swappable-bg",
                                        ]
                                    },
                                    components=[
                                        self.create_chapter(
                                            title="Załącznik",
                                            class_list=[
                                                "no-title",
                                            ],
                                            components=[
                                                self.create_component(
                                                    component_type="file",
                                                    name="reportAttachment"
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
                    title="Oświadczenia",
                    class_list=[
                        "no-title",
                        "grid",
                        "grid-cols-10"
                    ],
                    components=[
                        *[comp
                          for checkbox in self.statements
                          for comp in [
                              self.create_component(
                                  component_type="checkbox",
                                  label=checkbox["label"],
                                  name=checkbox["name"],
                                  required=True,
                                  class_list=[
                                      "no-label",
                                      "text-center"
                                  ]
                              ),
                              self.create_component(
                                  component_type="header",
                                  name=checkbox["name"],
                                  class_list=[
                                      "col-span-9",
                                      "text-left",
                                      "displayNoneFrontend"
                                  ]
                              )
                          ]],
                        self.create_component(
                            component_type="text",
                            label=f"PODPIS {'BENEFICJENTA' if self.is_promotion_priority else 'STYPENDSTY'}:",
                            name="reportSignature",
                            class_list=[
                                "col-start-7",
                                "col-span-4",
                                "text-center",
                                "report-signature",
                                "displayNoneFrontend"
                            ]
                        )
                    ]
                )
            ]
        )

        self.save_part(part)

