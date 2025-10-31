from classes_new.form_builder.form_builder import ReportFormBuilder
from classes_new.form_components.section.dwm.section import DWMSection


class DWMDepartmentReportFormBuilder(ReportFormBuilder):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.parts = [
            self.create_report_basic_data,
            self.create_report_general_data,
            self.create_report_expenditure_exacution,
            self.create_report_additional_information
        ]

        self.section = DWMSection()
        self.is_promotion_priority: bool = False
        self.statements: list[dict] = []
        self.grantee_vat_declaration: list[str] = []

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
                                    "grid-cols-8",
                                    "no-title"
                                ]
                            },
                            components=[
                                self.create_component(
                                    component_type="checkbox",
                                    label="Czy umowa była aneksowana?",
                                    name="addAnnex",
                                    class_list=[
                                        "col-start-4",
                                        "no-label"
                                    ]
                                ),
                                self.create_component(
                                    component_type="header",
                                    name="addAnnex",
                                    value="Czy umowa była aneksowana?",
                                    class_list=[
                                        "col-span-4",
                                        "text-left",
                                        "displayNoneFrontend"
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
                            value=f"{'Nazwa Beneficjenta' if self.is_promotion_priority else 'Imię i nazwisko Stypendysty'}",
                            class_list=[
                                "displayNoneFrontend"
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            label=f"{'Nazwa Beneficjenta' if self.is_promotion_priority else 'Imię i nazwisko Stypendysty'}",
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

    def create_report_expenditure_exacution(self, number: int):
        cost_types = [
            {
                "name": "accreditation",
                "label": "Koszty akredytacji",
                "isEstimate": True
            },
            {
                "name": "accommodation",
                "label": "Koszty noclegu",
                "isEstimate": True
            },
            {
                "name": "transportation",
                "label": "Koszty transportu",
                "isEstimate": True
            },
            {
                "name": "participation",
                "label": "Koszty uczestnictwa w warsztatach (jeśli dotyczy)",
                "isEstimate": True
            }
        ]

        # TODO
        second_cost_types = [
            {
                "name": "costsProvidedByEventOrganizer",
                "label": "Koszty zapewnione przez organizatora wydarzenia",
                "isEstimate": False
            }
        ]

        def return_cost_types_section(cost: dict):
            cost_type = self.create_component(
                component_type="textarea",
                label="Rodzaj kosztów",
                name=f"{cost["name"]}Costs",
                value=cost["label"],
                read_only=True,
                class_list=[
                    "no-label",
                    "col-span-2",
                    "text-left",
                    "displayNoneFrontend"
                ]
            )
            estimate_cost_total = self.create_component(
                component_type="text",
                mask="fund",
                label="Preliminarz: koszt całkowity",
                name=f"{cost["name"]}CostTotal",
                read_only=True,
                copy_from=f"{cost["name"]}CostTotal",
                unit="PLN",
                class_list=[
                    "no-label"
                ]
            )
            estimate_cost_pisf = self.create_component(
                component_type="text",
                mask="fund",
                label="Preliminarz: wniosek o dotację PISF",
                name=f"{cost["name"]}CostRequestPisf",
                read_only=True,
                copy_from=f"{cost["name"]}CostRequestPisf",
                unit="PLN",
                class_list=[
                    "no-label"
                ]
            )
            actual_cost_total = self.create_component(
                component_type="text",
                mask="fund",
                label="Bieżący okres sprawozdawczy: koszt całkowity",
                name=f"{cost["name"]}CostActualTotal",
                unit="PLN",
                class_list=[
                    "no-label"
                ] if cost.get("isEstimate", False) else [
                    "no-label",
                    "col-start-5"
                ]
            )

            actual_cost_pisf = self.create_component(
                component_type="text",
                mask="fund",
                label="Bieżący okres sprawozdawczy: w tym dofinansowanie z PISF",
                name=f"{cost["name"]}CostActualSupportPisf",
                unit="PLN",
                class_list=[
                    "no-label"
                ]
            )

            chapter = self.create_chapter(
                title=cost["label"],
                class_list={
                    "main": [
                        "table-4",
                        "grid",
                        "grid-cols-6",
                        "no-title",
                        "chapter-bg-red"
                    ],
                    "sub": [
                        "table-4-2__col"
                    ]
                },
                components=[
                    cost_type
                ]
            )

            if cost.get("isEstimate", False):
                chapter["components"].extend([
                    estimate_cost_total,
                    estimate_cost_pisf,
                ])

            chapter["components"].extend([
                actual_cost_total,
                actual_cost_pisf
            ])

            return chapter

        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Sprawozdanie z wykonania wydatków",
            class_list=[
                "full-width-grid"
            ],
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="radio",
                            name="granteeVatDeclaration",
                            copy_from="applicantVatDeclaration",
                            read_only=True,
                            required=True,
                            options=self.grantee_vat_declaration
                        )
                    ]
                ),
                self.create_chapter(
                    title="A. Informacja o wydatkach poniesionych przy wykonaniu przedsięwzięcia",
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
                            label="Całkowity koszt realizacji przedsięwzięcia",
                            name="reportingCostsTotal",
                            calculation_rules=[
                                self.calculation_rule.copy_value(
                                    from_name="costActualTotalSum"
                                )
                            ],
                            validators=[
                                self.validator.related_sum_validator(
                                    field_names=[
                                        "budgetTotalCurrentSumAmount"
                                    ]
                                )
                            ],
                            read_only=True,
                            unit="PLN",
                            class_list=[
                                "userInput-bg-red",
                                "default-margin",
                                "label-center"
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="w tym koszty pokryte ze środków PISF",
                            name="reportingCostsPisfSupport",
                            calculation_rules=[
                                self.calculation_rule.copy_value(
                                    from_name="costActualSupportPisfSum"
                                )
                            ],
                            read_only=True,
                            unit="PLN",
                            class_list=[
                                "default-margin",
                                "label-center"
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="w tym środki własne",
                            name="reportingCostsOwnFunds",
                            calculation_rules=[
                                self.calculation_rule.copy_value(
                                    from_name="budgetInputOwnFundsCurrentAmount"
                                )
                            ],
                            read_only=True,
                            unit="PLN",
                            class_list=[
                                "default-margin",
                                "label-center"
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="w tym inne środki",
                            name="reportingCostsOtherFunds",
                            calculation_rules=[
                                self.calculation_rule.copy_value(
                                    from_name="budgetInputAllPartnersCurrentAmount"
                                )
                            ],
                            validators=[
                                self.validator.related_sum_validator(
                                    field_names=[
                                        "budgetInputAllPartnersCurrentAmount"
                                    ]
                                )
                            ],
                            read_only=True,
                            unit="PLN",
                            class_list=[
                                "default-margin",
                                "label-center"
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="1. Kosztorys ze względu na rodzaj kosztów",
                    class_list={
                        "sub": [
                            "table-invoice-top"
                        ]
                    },
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="header",
                                    name="budget",
                                    value="Zestawienie to stanowi porównanie kosztów planowanych z faktycznie poniesionymi. Należy w nim uwzględnić wszystkie pozycje, które figurowały w kosztorysie załączonym do umowy. Jeżeli Beneficjent wykorzystał dotację PISF inaczej, niż było to planowane (np. dokonał pewnych przesunięć między pozycjami kosztorysu w ramach przyznanej kwoty dofinansowania), konieczne jest wystosowanie przezeń specjalnego pisma, w którym opisze i wyjaśni zaistniałe różnice i zwróci się z prośbą o ich akceptację. <br><br><a target='_blank' rel='noopener noreferrer' href='https://wnioski.pisf.pl/programy-operacyjne/dokumenty-do-pobrania/promocja-polskiego-kina'>Wzór pisma wyjaśniającego zmiany w wykorzystaniu środków pochodzących z dofinansowania</a>"
                                )
                            ]
                        ),
                        self.create_chapter(
                            class_list=[
                                "grid",
                                "grid-cols-12",
                                "table-header"
                            ],
                            components=[
                                self.create_component(
                                    component_type="header",
                                    name="plannedCost",
                                    value="Koszt planowany",
                                    class_list=[
                                        "col-start-5",
                                        "col-span-4",
                                        "text-center",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="header",
                                    name="alreadySpent",
                                    value="Koszt poniesiony",
                                    class_list=[
                                        "col-span-4",
                                        "text-center",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="header",
                                    name="costTypeLp",
                                    value="Lp.",
                                    class_list=[
                                        "text-center",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="header",
                                    name="costType",
                                    value="Rodzaj kosztów",
                                    class_list=[
                                        "col-span-3",
                                        "text-center",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="header",
                                    name="overallFromPISF",
                                    value="Ogółem",
                                    class_list=[
                                        "col-span-2",
                                        "text-center",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="header",
                                    name="fromPISF",
                                    value="Z dotacji PISF",
                                    class_list=[
                                        "col-span-2",
                                        "text-center",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="header",
                                    name="overallFromDonation",
                                    value="Ogółem",
                                    class_list=[
                                        "col-span-2",
                                        "text-center",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="header",
                                    name="fromDonation",
                                    value="Z dotacji PISF",
                                    class_list=[
                                        "col-span-2",
                                        "text-center",
                                        "displayNoneFrontend"
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            is_paginated=True,
                            multiple_forms_rules={
                                "minCount": 1,
                                "maxCount": 60
                            },
                            class_list={
                                "sub": [
                                    "table-invoice-top"
                                ],
                                "main": [
                                    "no-title",
                                    "swappable-bg",
                                    "lp-table"
                                ]
                            },
                            components=[
                                self.create_chapter(
                                    title="Koszt",
                                    class_list={
                                        "sub": [
                                            "table-invoice__col"
                                        ],
                                        "main": [
                                            "table-invoice",
                                            "grid",
                                            "grid-cols-12"
                                        ]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="textarea",
                                            name="lp-number-costs",
                                            class_list=[
                                                "displayNoneFrontend",
                                                "lp-number"
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="textarea",
                                            label="Rodzaj kosztów",
                                            name="costType",
                                            help_text="Wpisz rodzaj kosztu zgodnie z kosztorysem załączonym do umowy.",
                                            copy_from="costType",
                                            validators=[
                                                self.validator.length_validator(max_value=200)
                                            ],
                                            class_list=[
                                                "no-label",
                                                "col-span-3",
                                                "text-left"
                                            ],
                                            read_only=True
                                        ),
                                        self.create_component(
                                            component_type="textarea",
                                            name="costTypeEmpty",
                                            class_list=[
                                                "no-label",
                                                "col-span-3",
                                                "text-left",
                                                "displayNoneFrontend",
                                                "displayNonePDF"
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Preliminarz: koszt całkowity",
                                            name="costTotal",
                                            help_text="Wpisz wartość kosztu zgodnie z kosztorysem załączonym do umowy.",
                                            copy_from="costTotal",
                                            unit="PLN",
                                            class_list=[
                                                "no-label",
                                                "col-span-2",
                                            ],
                                            read_only=True
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Preliminarz: wniosek o dotację PISF",
                                            name="costRequestPisf",
                                            help_text="Wpisz wysokość dotacji PISF zgodnie z kosztorysem załączonym do umowy.",
                                            copy_from="costRequestPisf",
                                            unit="PLN",
                                            class_list=[
                                                "no-label",
                                                "col-span-2",
                                            ],
                                            read_only=True
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Bieżący okres sprawozdawczy: koszt całkowity",
                                            name="costActualTotal",
                                            help_text="Wpisz wartość rzeczywiście poniesionych wydatków.",
                                            unit="PLN",
                                            class_list=[
                                                "no-label",
                                                "col-span-2",
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Bieżący okres sprawozdawczy: wniosek o dotację PISF",
                                            name="costActualSupportPisf",
                                            help_text="Wpisz wysokość dofinansowania PISF w kwocie poniesionego wydatku.",
                                            unit="PLN",
                                            class_list=[
                                                "no-label",
                                                "col-span-2",
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Razem",
                            class_list={
                                "main": [
                                    "table-4",
                                    "grid",
                                    "grid-cols-12",
                                    "no-title"
                                ],
                                "sub": [
                                    "table-4__col"
                                ]
                            },
                            components=[
                                self.create_component(
                                    component_type="header",
                                    name="total",
                                    value="Łącznie",
                                    class_list=[
                                        "col-start-4",
                                        "text-right",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Preliminarz: koszt całkowty",
                                    name="costTotalSum",
                                    read_only=True,
                                    calculation_rules=[
                                        self.calculation_rule.dynamic_sum_inputs(
                                            fields="costTotal"
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_sum_validator(
                                            field_names=[
                                                "costTotal"
                                            ]
                                        )
                                    ],
                                    unit="PLN",
                                    class_list=[
                                        "no-label",
                                        "col-span-2"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Preliminarz: wniosek o dotację PISF",
                                    name="costRequestPisfSum",
                                    read_only=True,
                                    calculation_rules=[
                                        self.calculation_rule.dynamic_sum_inputs(
                                            fields="costRequestPisf"
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_sum_validator(
                                            field_names=[
                                                "costRequestPisf"
                                            ]
                                        )
                                    ],
                                    unit="PLN",
                                    class_list=[
                                        "no-label",
                                        "col-span-2"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Bieżący okres sprawozdawczy: koszt całkowty",
                                    name="costActualTotalSum",
                                    read_only=True,
                                    calculation_rules=[
                                        self.calculation_rule.dynamic_sum_inputs(
                                            fields="costActualTotal"
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_sum_validator(
                                            field_names=[
                                                "costActualTotal"
                                            ]
                                        )
                                    ],
                                    unit="PLN",
                                    class_list=[
                                        "no-label",
                                        "col-span-2"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Bieżący okres sprawozdawczy: wniosek o dotację PISF",
                                    name="costActualSupportPisfSum",
                                    read_only=True,
                                    calculation_rules=[
                                        self.calculation_rule.dynamic_sum_inputs(
                                            fields="costActualSupportPisf"
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_sum_validator(
                                            field_names=[
                                                "costActualSupportPisf"
                                            ]
                                        )
                                    ],
                                    unit="PLN",
                                    class_list=[
                                        "no-label",
                                        "col-span-2"
                                    ]
                                )
                            ]
                        )
                    ]
                ) if self.is_promotion_priority else self.create_chapter(
                    title="1. Kosztorys ze względu na rodzaj kosztów",
                    class_list={
                        "sub": [
                            "table-invoice-top"
                        ]
                    },
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="header",
                                    name="budget",
                                    value="Zestawienie to stanowi porównanie kosztów planowanych z faktycznie poniesionymi. Należy w nim uwzględnić wszystkie pozycje, które figurowały w kosztorysie załączonym do umowy. Jeżeli Stypendysta wykorzystał dotację PISF inaczej, niż było to planowane (np. dokonał pewnych przesunięć między pozycjami kosztorysu w ramach przyznanej kwoty dofinansowania), konieczne jest wystosowanie przezeń specjalnego pisma, w którym opisze i wyjaśni zaistniałe różnice i zwróci się z prośbą o ich akceptację. <br><br><a target='_blank' rel='noopener noreferrer' href='https://wnioski.pisf.pl/programy-operacyjne/dokumenty-do-pobrania/promocja-polskiego-kina'>Wzór pisma wyjaśniającego zmiany w wykorzystaniu środków pochodzących z dofinansowania</a>"
                                )
                            ]
                        ),
                        self.create_chapter(
                            class_list=[
                                "grid",
                                "grid-cols-12",
                                "table-header"
                            ],
                            components=[
                                self.create_component(
                                    component_type="header",
                                    name="plannedCost",
                                    value="Koszt planowany",
                                    class_list=[
                                        "col-start-5",
                                        "col-span-4",
                                        "text-center",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="header",
                                    name="alreadySpent",
                                    value="Koszt poniesiony",
                                    class_list=[
                                        "col-span-4",
                                        "text-center",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="header",
                                    name="costTypeLp",
                                    value="Lp.",
                                    class_list=[
                                        "text-center",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="header",
                                    name="costType",
                                    value="Rodzaj kosztów",
                                    class_list=[
                                        "col-span-3",
                                        "text-center",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="header",
                                    name="overallFromPISF",
                                    value="Ogółem",
                                    class_list=[
                                        "col-span-2",
                                        "text-center",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="header",
                                    name="fromPISF",
                                    value="Z dotacji PISF",
                                    class_list=[
                                        "col-span-2",
                                        "text-center",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="header",
                                    name="overallFromDonation",
                                    value="Ogółem",
                                    class_list=[
                                        "col-span-2",
                                        "text-center",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="header",
                                    name="fromDonation",
                                    value="Z dotacji PISF",
                                    class_list=[
                                        "col-span-2",
                                        "text-center",
                                        "displayNoneFrontend"
                                    ]
                                )
                            ]
                        ),
                        *[return_cost_types_section(cost) for cost in cost_types],
                        self.create_chapter(
                            title="Razem",
                            class_list={
                                "main": [
                                    "table-4",
                                    "grid",
                                    "grid-cols-12",
                                    "no-title"
                                ],
                                "sub": [
                                    "table-4__col"
                                ]
                            },
                            components=[
                                self.create_component(
                                    component_type="header",
                                    name="total",
                                    value="Łącznie",
                                    class_list=[
                                        "col-start-4",
                                        "text-right",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Preliminarz: koszt całkowty",
                                    name="costTotalSum",
                                    read_only=True,
                                    calculation_rules=[
                                        self.calculation_rule.dynamic_sum_inputs(
                                            fields=[f"{cost["name"]}CostTotal" for cost in cost_types if cost.get("isEstimate", False)]
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_sum_validator(
                                            field_names=[f"{cost["name"]}CostTotal" for cost in cost_types if cost.get("isEstimate", False)]
                                        )
                                    ],
                                    unit="PLN",
                                    class_list=[
                                        "no-label",
                                        "col-span-2"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Preliminarz: wniosek o dotację PISF",
                                    name="costRequestPisfSum",
                                    read_only=True,
                                    calculation_rules=[
                                        self.calculation_rule.dynamic_sum_inputs(
                                            fields=[f"{cost["name"]}CostRequestPisf" for cost in cost_types if cost.get("isEstimate", False)]
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_sum_validator(
                                            field_names=[f"{cost["name"]}CostRequestPisf" for cost in cost_types if cost.get("isEstimate", False)]
                                        )
                                    ],
                                    unit="PLN",
                                    class_list=[
                                        "no-label",
                                        "col-span-2"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Bieżący okres sprawozdawczy: koszt całkowty",
                                    name="costActualTotalSum",
                                    read_only=True,
                                    calculation_rules=[
                                        self.calculation_rule.dynamic_sum_inputs(
                                            fields=[f"{cost["name"]}CostActualTotal" for cost in cost_types]
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_sum_validator(
                                            field_names=[f"{cost["name"]}CostActualTotal" for cost in cost_types]
                                        )
                                    ],
                                    unit="PLN",
                                    class_list=[
                                        "no-label",
                                        "col-span-2"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Bieżący okres sprawozdawczy: wniosek o dotację PISF",
                                    name="costActualSupportPisfSum",
                                    read_only=True,
                                    calculation_rules=[
                                        self.calculation_rule.dynamic_sum_inputs(
                                            fields=[f"{cost["name"]}CostActualSupportPisf" for cost in cost_types]
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_sum_validator(
                                            field_names=[f"{cost["name"]}CostActualSupportPisf" for cost in cost_types]
                                        )
                                    ],
                                    unit="PLN",
                                    class_list=[
                                        "no-label",
                                        "col-span-2"
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Kosztorys ze względu na źródło finansowania",
                    class_list={
                        "sub": [
                            "table-invoice-top"
                        ]
                    },
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="header",
                                    name="description",
                                    value=f"Zestawienie to stanowi porównanie kosztów planowanych z faktycznie poniesionymi. Uwaga: procentowy wkład dotacji PISF w finalnym budżecie przedsięwzięcia nie może przekroczyć wkładu zakładanego (określonego w umowie). Jeżeli faktycznie poniesiony koszt całkowity przedsięwzięcia okazał się niższy od planowanego lub {'Stypendysta' if not self.is_promotion_priority else 'Beneficjent'} nie wykorzystał całej dotacji, należy dokonać zwrotu na rachunek PISF i dostarczyć wraz z raportem potwierdzenie przelewu. Nr rachunku PISF: Banku Gospodarstwa Krajowego {'Stypendyści' if not self.is_promotion_priority else 'Beneficjenci'} krajowi: 91 1130 1017 0020 1234 1320 0016, {'Stypendyści' if not self.is_promotion_priority else 'Beneficjenci'} zagraniczni: PL 91 1130 1017 0020 1234 1320 0016 SWIFT: GOSKPLPW."
                                )
                            ]
                        ),
                        self.create_chapter(
                            class_list=[
                                "grid",
                                "grid-cols-12",
                                "table-header"
                            ],
                            components=[
                                self.create_component(
                                    component_type="header",
                                    name="plannedCostSecond",
                                    value="Koszt planowany",
                                    class_list=[
                                        "col-start-5",
                                        "col-span-4",
                                        "text-center",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="header",
                                    name="alreadySpentSecond",
                                    value="Koszt poniesiony",
                                    class_list=[
                                        "col-span-4",
                                        "text-center",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="header",
                                    name="costTypeSecond",
                                    value="Źródło finansowania",
                                    class_list=[
                                        "col-span-4",
                                        "text-center",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="header",
                                    name="plannedPln",
                                    value="PLN",
                                    class_list=[
                                        "col-span-2",
                                        "text-center",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="header",
                                    name="plannedShare",
                                    value="%",
                                    class_list=[
                                        "col-span-2",
                                        "text-center",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="header",
                                    name="actualPln",
                                    value="PLN",
                                    class_list=[
                                        "col-span-2",
                                        "text-center",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="header",
                                    name="actualShare",
                                    value="%",
                                    class_list=[
                                        "col-span-2",
                                        "text-center",
                                        "displayNoneFrontend"
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Koszty pokryte z dofinansowania PISF",
                            class_list={
                                "main": [
                                    "table-4",
                                    "grid",
                                    "grid-cols-6",
                                    "no-title",
                                    "chapter-bg-red"
                                ],
                                "sub": [
                                    "table-4__col"
                                ]
                            },
                            components=[
                                self.create_component(
                                    component_type="header",
                                    name="costPISF",
                                    value="Koszty pokryte z dofinansowania PISF",
                                    class_list=[
                                        "col-span-2",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Preliminarz",
                                    name="budgetInputPisfSupportAmount",
                                    read_only=True,
                                    copy_from="costRequestPisfSum",
                                    unit="PLN",
                                    class_list=[
                                        "no-label"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Preliminarz: udział w całym budżecie",
                                    name="budgetInputPisfSupportShare",
                                    read_only=True,
                                    copy_from="costRequestPisfSumShare",
                                    unit="%",
                                    class_list=[
                                        "no-label"
                                    ],
                                    calculation_rules=[
                                        self.calculation_rule.share_calculator(
                                            dividend_field="budgetInputPisfSupportAmount",
                                            divisor_field="reportingCostsTotal"
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_share_validator(
                                            dividend="budgetInputPisfSupportAmount",
                                            divisor="reportingCostsTotal"
                                        )
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Koszty bieżące",
                                    name="budgetInputPisfSupportCurrentAmount",
                                    calculation_rules=[
                                        self.calculation_rule.copy_value(
                                            from_name="costActualSupportPisfSum"
                                        )
                                    ],
                                    read_only=True,
                                    unit="PLN",
                                    class_list=[
                                        "no-label"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Koszty bieżące: udział w całym budżecie",
                                    name="budgetInputPisfSupportCurrentShare",
                                    read_only=True,
                                    unit="%",
                                    class_list=[
                                        "no-label"
                                    ],
                                    calculation_rules=[
                                        self.calculation_rule.share_calculator(
                                            dividend_field="budgetInputPisfSupportCurrentAmount",
                                            divisor_field="reportingCostsTotal"
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_share_validator(
                                            dividend="budgetInputPisfSupportCurrentAmount",
                                            divisor="reportingCostsTotal"
                                        ),
                                        self.validator.range_validator(
                                            max_value=100,
                                            message="Procentowy wkład dotacji PISF w finalnym budżecie przedsięwzięcia nie może przekroczyć wkładu zakładanego (określonego w umowie)."
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Środki własne",
                            class_list={
                                "main": [
                                    "table-4",
                                    "grid",
                                    "grid-cols-6",
                                    "no-title",
                                    "chapter-bg-grey"
                                ],
                                "sub": [
                                    "table-4__col"
                                ]
                            },
                            components=[
                                self.create_component(
                                    component_type="header",
                                    name="ownFunds",
                                    value="Środki własne",
                                    class_list=[
                                        "col-span-2",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Preliminarz",
                                    name="budgetInputOwnFundsAmount",
                                    read_only=True,
                                    copy_from="costOwnFundsSum",
                                    unit="PLN",
                                    class_list=[
                                        "no-label"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Preliminarz: udział w całym budżecie",
                                    name="budgetInputOwnFundsShare",
                                    read_only=True,
                                    calculation_rules=[
                                        self.calculation_rule.share_calculator(
                                            dividend_field="budgetInputOwnFundsAmount",
                                            divisor_field="reportingCostsTotal"
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_share_validator(
                                            dividend="budgetInputOwnFundsAmount",
                                            divisor="reportingCostsTotal"
                                        )
                                    ],
                                    unit="%",
                                    class_list=[
                                        "no-label"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Koszty bieżące",
                                    name="budgetInputOwnFundsCurrentAmount",
                                    unit="PLN",
                                    class_list=[
                                        "no-label"
                                    ],
                                    validators=[
                                        self.validator.related_fraction_lte_validator(
                                            field_name="costActualTotalSum",
                                            ratio=0.1,
                                            message="Minimalny wkład własny wnioskodawcy powinien wynosić 10% całości budżetu przedsięwzięcia."
                                        )
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Koszty bieżące: udział w całym budżecie",
                                    name="budgetInputOwnFundsCurrentShare",
                                    read_only=True,
                                    unit="%",
                                    class_list=[
                                        "no-label"
                                    ],
                                    calculation_rules=[
                                        self.calculation_rule.share_calculator(
                                            dividend_field="budgetInputOwnFundsCurrentAmount",
                                            divisor_field="reportingCostsTotal"
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_share_validator(
                                            dividend="budgetInputOwnFundsCurrentAmount",
                                            divisor="reportingCostsTotal"
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Środki partnerów prywatnych i publicznych łacznie",
                            class_list={
                                "main": [
                                    "table-4",
                                    "grid",
                                    "grid-cols-6",
                                    "no-title",
                                    "chapter-bg-grey"
                                ],
                                "sub": [
                                    "table-4__col"
                                ]
                            },
                            components=[
                                self.create_component(
                                    component_type="header",
                                    name="otherPartners",
                                    value="Środki partnerów prywatnych i publicznych łącznie",
                                    class_list=[
                                        "col-span-2",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Preliminarz",
                                    name="budgetInputAllPartnersAmount",
                                    read_only=True,
                                    unit="PLN",
                                    class_list=[
                                        "no-label"
                                    ],
                                    calculation_rules=[
                                        self.calculation_rule.dynamic_sum_inputs(
                                            fields=[
                                                "budgetInputPartnersSponsorsAmount",
                                                "budgetInputPublicSourcesAmount"
                                            ]
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_sum_validator(
                                            field_names=[
                                                "budgetInputPartnersSponsorsAmount",
                                                "budgetInputPublicSourcesAmount"
                                            ]
                                        )
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Preliminarz: udział w całym budżecie",
                                    name="budgetInputAllPartnersShare",
                                    read_only=True,
                                    calculation_rules=[
                                        self.calculation_rule.share_calculator(
                                            dividend_field="budgetInputAllPartnersAmount",
                                            divisor_field="reportingCostsTotal"
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_share_validator(
                                            dividend="budgetInputAllPartnersAmount",
                                            divisor="reportingCostsTotal"
                                        )
                                    ],
                                    unit="%",
                                    class_list=[
                                        "no-label"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Koszty bieżące",
                                    name="budgetInputAllPartnersCurrentAmount",
                                    unit="PLN",
                                    class_list=[
                                        "no-label"
                                    ],
                                    read_only=True,
                                    calculation_rules=[
                                        self.calculation_rule.dynamic_sum_inputs(
                                            fields=[
                                                "budgetInputPartnersSponsorsCurrentAmount",
                                                "budgetInputPublicSourcesCurrentAmount"
                                            ]
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_sum_validator(
                                            field_names=[
                                                "budgetInputPartnersSponsorsCurrentAmount",
                                                "budgetInputPublicSourcesCurrentAmount"
                                            ]
                                        )
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Koszty bieżące: udział w całym budżecie",
                                    name="budgetInputAllPartnersCurrentShare",
                                    read_only=True,
                                    unit="%",
                                    class_list=[
                                        "no-label"
                                    ],
                                    calculation_rules=[
                                        self.calculation_rule.share_calculator(
                                            dividend_field="budgetInputAllPartnersCurrentAmount",
                                            divisor_field="reportingCostsTotal"
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_share_validator(
                                            dividend="budgetInputAllPartnersCurrentAmount",
                                            divisor="reportingCostsTotal"
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Środki innych partnerów/sponsorów",
                            class_list={
                                "sub": [
                                    "table-4-top"
                                ],
                                "main": [
                                    "no-title",
                                    "chapter-bg-grey"
                                ]
                            },
                            components=[
                                self.create_chapter(
                                    title="Razem",
                                    class_list={
                                        "main": [
                                            "table-4",
                                            "grid",
                                            "grid-cols-6",
                                            "no-title"
                                        ],
                                        "sub": [
                                            "table-4__col"
                                        ]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="header",
                                            name="totalPartnersSponsors",
                                            value="Środki innych partnerów/sponsorów łącznie",
                                            class_list=[
                                                "col-span-2",
                                                "displayNoneFrontend"
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Preliminarz",
                                            name="budgetInputPartnersSponsorsAmount",
                                            read_only=True,
                                            unit="PLN",
                                            class_list=[
                                                "no-label"
                                            ],
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        "budgetInputPartnerSponsorAmount"
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        "budgetInputPartnerSponsorAmount"
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Preliminarz: udział w całym budżecie",
                                            name="budgetInputPartnersSponsorsShare",
                                            read_only=True,
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field="budgetInputPartnersSponsorsAmount",
                                                    divisor_field="reportingCostsTotal"
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_share_validator(
                                                    dividend="budgetInputPartnersSponsorsAmount",
                                                    divisor="reportingCostsTotal"
                                                )
                                            ],
                                            unit="%",
                                            class_list=[
                                                "no-label"
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Koszty bieżące",
                                            name="budgetInputPartnersSponsorsCurrentAmount",
                                            unit="PLN",
                                            class_list=[
                                                "no-label"
                                            ],
                                            read_only=True,
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        "budgetInputPartnerSponsorCurrentAmount"
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        "budgetInputPartnerSponsorCurrentAmount"
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Koszty bieżące: udział w całym budżecie",
                                            name="budgetInputPartnersSponsorsCurrentShare",
                                            read_only=True,
                                            unit="%",
                                            class_list=[
                                                "no-label"
                                            ],
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field="budgetInputPartnersSponsorsCurrentAmount",
                                                    divisor_field="reportingCostsTotal"
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_share_validator(
                                                    dividend="budgetInputPartnersSponsorsCurrentAmount",
                                                    divisor="reportingCostsTotal"
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    is_paginated=True,
                                    multiple_forms_rules={
                                        "minCount": 1,
                                        "maxCount": 20
                                    },
                                    class_list={
                                        "sub": [
                                            "table-4-top"
                                        ]
                                    },
                                    components=[
                                        self.create_chapter(
                                            title="Partner lub sponsor",
                                            class_list={
                                                "main": [
                                                    "table-4",
                                                    "table-invoice",
                                                    "grid",
                                                    "grid-cols-6",
                                                ],
                                                "sub": [
                                                    "table-4-2__col"
                                                ]
                                            },
                                            components=[
                                                self.create_component(
                                                    component_type="text",
                                                    label="Nazwa partnera lub sponsora",
                                                    name="partnerSponsorName",
                                                    validators=[
                                                        self.validator.length_validator(max_value=100)
                                                    ],
                                                    class_list=[
                                                        "col-start-2",
                                                        "no-label"
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Preliminarz",
                                                    name="budgetInputPartnerSponsorAmount",
                                                    read_only=True,
                                                    unit="PLN",
                                                    class_list=[
                                                        "no-label"
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Preliminarz: udział w całym budżecie",
                                                    name="budgetInputPartnerSponsorShare",
                                                    read_only=True,
                                                    calculation_rules=[
                                                        self.calculation_rule.share_calculator(
                                                            dividend_field="budgetInputPartnerSponsorAmount",
                                                            divisor_field="reportingCostsTotal"
                                                        )
                                                    ],
                                                    validators=[
                                                        self.validator.related_share_validator(
                                                            dividend="budgetInputPartnerSponsorAmount",
                                                            divisor="reportingCostsTotal"
                                                        )
                                                    ],
                                                    unit="%",
                                                    class_list=[
                                                        "no-label"
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Koszty bieżące",
                                                    name="budgetInputPartnerSponsorCurrentAmount",
                                                    unit="PLN",
                                                    class_list=[
                                                        "no-label"
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Koszty bieżące: udział w całym budżecie",
                                                    name="budgetInputPartnerSponsorCurrentShare",
                                                    read_only=True,
                                                    unit="%",
                                                    class_list=[
                                                        "no-label"
                                                    ],
                                                    calculation_rules=[
                                                        self.calculation_rule.share_calculator(
                                                            dividend_field="budgetInputPartnerSponsorCurrentAmount",
                                                            divisor_field="reportingCostsTotal"
                                                        )
                                                    ],
                                                    validators=[
                                                        self.validator.related_share_validator(
                                                            dividend="budgetInputPartnerSponsorCurrentAmount",
                                                            divisor="reportingCostsTotal"
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
                            title="Pozostałe źródła publiczne",
                            class_list={
                                "sub": [
                                    "table-4-top"
                                ],
                                "main": [
                                    "no-title",
                                    "chapter-bg-grey"
                                ]
                            },
                            components=[
                                self.create_chapter(
                                    title="Razem",
                                    class_list={
                                        "main": [
                                            "table-4",
                                            "grid",
                                            "grid-cols-6",
                                            "no-title"
                                        ],
                                        "sub": [
                                            "table-4__col"
                                        ]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="header",
                                            name="totalPublicSources",
                                            value="Pozostałe źródła publiczne łącznie",
                                            class_list=[
                                                "col-span-2",
                                                "displayNoneFrontend"
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Preliminarz",
                                            name="budgetInputPublicSourcesAmount",
                                            read_only=True,
                                            unit="PLN",
                                            class_list=[
                                                "no-label"
                                            ],
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        "budgetInputPublicSourceAmount"
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        "budgetInputPublicSourceAmount"
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Preliminarz: udział w całym budżecie",
                                            name="budgetInputPublicSourcesShare",
                                            read_only=True,
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field="budgetInputPublicSourcesAmount",
                                                    divisor_field="reportingCostsTotal"
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_share_validator(
                                                    dividend="budgetInputPublicSourcesAmount",
                                                    divisor="reportingCostsTotal"
                                                )
                                            ],
                                            unit="%",
                                            class_list=[
                                                "no-label"
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Koszty bieżące",
                                            name="budgetInputPublicSourcesCurrentAmount",
                                            unit="PLN",
                                            class_list=[
                                                "no-label"
                                            ],
                                            read_only=True,
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        "budgetInputPublicSourceCurrentAmount"
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        "budgetInputPublicSourceCurrentAmount"
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Koszty bieżące: udział w całym budżecie",
                                            name="budgetInputPublicSourcesCurrentShare",
                                            read_only=True,
                                            unit="%",
                                            class_list=[
                                                "no-label"
                                            ],
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field="budgetInputPublicSourcesCurrentAmount",
                                                    divisor_field="reportingCostsTotal"
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_share_validator(
                                                    dividend="budgetInputPublicSourcesCurrentAmount",
                                                    divisor="reportingCostsTotal"
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    is_paginated=True,
                                    multiple_forms_rules={
                                        "minCount": 1,
                                        "maxCount": 20
                                    },
                                    class_list={
                                        "sub": [
                                            "table-4-top"
                                        ]
                                    },
                                    components=[
                                        self.create_chapter(
                                            title="Źródła publiczne",
                                            class_list={
                                                "main": [
                                                    "table-4",
                                                    "table-invoice",
                                                    "grid",
                                                    "grid-cols-6",
                                                ],
                                                "sub": [
                                                    "table-4-2__col"
                                                ]
                                            },
                                            components=[
                                                self.create_component(
                                                    component_type="text",
                                                    label="Nazwa partnera lub sponsora",
                                                    name="publicSourceName",
                                                    validators=[
                                                        self.validator.length_validator(max_value=100)
                                                    ],
                                                    class_list=[
                                                        "col-start-2",
                                                        "no-label"
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Preliminarz",
                                                    name="budgetInputPublicSourceAmount",
                                                    read_only=True,
                                                    unit="PLN",
                                                    class_list=[
                                                        "no-label"
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Preliminarz: udział w całym budżecie",
                                                    name="budgetInputPublicSourceShare",
                                                    read_only=True,
                                                    calculation_rules=[
                                                        self.calculation_rule.share_calculator(
                                                            dividend_field="budgetInputPublicSourceAmount",
                                                            divisor_field="reportingCostsTotal"
                                                        )
                                                    ],
                                                    validators=[
                                                        self.validator.related_share_validator(
                                                            dividend="budgetInputPublicSourceAmount",
                                                            divisor="reportingCostsTotal"
                                                        )
                                                    ],
                                                    unit="%",
                                                    class_list=[
                                                        "no-label"
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Koszty bieżące",
                                                    name="budgetInputPublicSourceCurrentAmount",
                                                    unit="PLN",
                                                    class_list=[
                                                        "no-label"
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    label="Koszty bieżące: udział w całym budżecie",
                                                    name="budgetInputPublicSourceCurrentShare",
                                                    read_only=True,
                                                    unit="%",
                                                    class_list=[
                                                        "no-label"
                                                    ],
                                                    calculation_rules=[
                                                        self.calculation_rule.share_calculator(
                                                            dividend_field="budgetInputPublicSourceCurrentAmount",
                                                            divisor_field="reportingCostsTotal"
                                                        )
                                                    ],
                                                    validators=[
                                                        self.validator.related_share_validator(
                                                            dividend="budgetInputPublicSourceCurrentAmount",
                                                            divisor="reportingCostsTotal"
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
                            title="Źródła finansowania ogółem",
                            class_list={
                                "main": [
                                    "table-4",
                                    "grid",
                                    "grid-cols-6",
                                    "no-title",
                                    "chapter-bg-grey"
                                ],
                                "sub": [
                                    "table-4__col"
                                ]
                            },
                            components=[
                                self.create_component(
                                    component_type="header",
                                    name="fundingSourcesOverall",
                                    value="Źródła finansowania ogółem",
                                    class_list=[
                                        "col-span-2",
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Preliminarz",
                                    name="budgetTotalSumAmount",
                                    read_only=True,
                                    unit="PLN",
                                    class_list=[
                                        "no-label"
                                    ],
                                    calculation_rules=[
                                        self.calculation_rule.dynamic_sum_inputs(
                                            fields=[
                                                "budgetInputPisfSupportAmount",
                                                "budgetInputOwnFundsAmount",
                                                "budgetInputAllPartnersAmount"
                                            ]
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_sum_validator(
                                            field_names=[
                                                "budgetInputPisfSupportAmount",
                                                "budgetInputOwnFundsAmount",
                                                "budgetInputAllPartnersAmount"
                                            ]
                                        ),
                                        self.validator.related_sum_validator(
                                            field_names=[
                                                "costTotalSum"
                                            ]
                                        )
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Preliminarz: udział w całym budżecie",
                                    name="budgetTotalSumShare",
                                    read_only=True,
                                    calculation_rules=[
                                        self.calculation_rule.share_calculator(
                                            dividend_field="budgetTotalSumAmount",
                                            divisor_field="budgetTotalSumAmount"
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_share_validator(
                                            dividend="budgetTotalSumAmount",
                                            divisor="budgetTotalSumAmount"
                                        )
                                    ],
                                    unit="%",
                                    class_list=[
                                        "no-label"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Koszty bieżące",
                                    name="budgetTotalCurrentSumAmount",
                                    unit="PLN",
                                    class_list=[
                                        "no-label"
                                    ],
                                    read_only=True,
                                    calculation_rules=[
                                        self.calculation_rule.dynamic_sum_inputs(
                                            fields=[
                                                "budgetInputPisfSupportCurrentAmount",
                                                "budgetInputOwnFundsCurrentAmount",
                                                "budgetInputAllPartnersCurrentAmount"
                                            ]
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_sum_validator(
                                            field_names=[
                                                "budgetInputPisfSupportCurrentAmount",
                                                "budgetInputOwnFundsCurrentAmount",
                                                "budgetInputAllPartnersCurrentAmount"
                                            ]
                                        ),
                                        self.validator.related_sum_validator(
                                            field_names=[
                                                "costActualTotalSum"
                                            ]
                                        )
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Koszty bieżące: udział w całym budżecie",
                                    name="budgetTotalCurrentSumShare",
                                    read_only=True,
                                    unit="%",
                                    class_list=[
                                        "no-label"
                                    ],
                                    calculation_rules=[
                                        self.calculation_rule.share_calculator(
                                            dividend_field="budgetTotalCurrentSumAmount",
                                            divisor_field="reportingCostsTotal"
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_share_validator(
                                            dividend="budgetTotalCurrentSumAmount",
                                            divisor="reportingCostsTotal"
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="header",
                                    name="budgetComments",
                                    value="Wyjaśnienie dotyczące różnic pomiędzy kosztem planowanym a poniesionym",
                                    class_list=[
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="textarea",
                                    label="Uwagi",
                                    name="budgetComments",
                                    validators=[
                                        self.validator.length_validator(max_value=10000)
                                    ],
                                    class_list=[
                                        "no-label"
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="B. Zestawienie faktur/rachunków",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="header",
                                    name="invoiceDescription",
                                    value="Zestawienie to spis wszystkich faktur/rachunków/biletów, które dotyczą przedsięwzięcia i zostały pokryte z dofinansowania PISF. Spis zawierać powinien: rodzaj dokumentu (faktura/rachunek), nr faktury/rachunku (w przypadku rachunku należy podać jego nr i datę oraz podać nr i datę umowy, której dotyczy), datę wystawienia dokumentu, nazwę wydatku (rodzaj towaru/usługi), wysokość wydatkowanej kwoty ze wskazaniem części, w jakiej została ona pokryta z dofinansowania PISF. Uwaga: Każda z faktur/rachunków opłaconych z otrzymanego dofinansowania powinna być opatrzona na odwrocie pieczęcią Beneficjenta oraz zawierać sporządzony w sposób trwały opis zawierający informacje: z jakich środków wydatkowana kwota została pokryta oraz jakie było przeznaczenie zakupionych towarów, usług lub innego rodzaju opłaconej należności. Informacja ta powinna być podpisana przez osobę odpowiedzialną za sprawy dotyczące rozliczeń finansowych Beneficjenta. Do raportu nie załącza się faktur/rachunków, które należy przechowywać zgodnie z obowiązującymi przepisami i udostępniać podczas przeprowadzanych czynności kontrolnych. W przypadku faktur za akredytacje, noclegi, bilety lub umów o dzieło należy podać imię i nazwisko osoby, której dotyczy pozycja. Z dotacji PISF mogą zostać pokryte dokumenty księgowe wystawione od momentu złożenia wniosku o dofinansowanie PISF (w wersji elektronicznej) do zakończenia przedsięwzięcia określonego w harmonogramie stanowiącym załącznik nr 1/1A do Umowy. Przeliczeń z waluty obcej na PLN należy dokonywać dla każdej pozycji osobno, wg średniego kursu NBP z dnia poprzedzającego dzień wystawienia faktury. Uwzględnić należy wartość przelicznika do 4. miejsca po przecinku, a otrzymaną wartość w PLN – zaokrąglić do 2. miejsca po przecinku. Kolejność wpisywania faktur powinna być taka sama jak kolejność pozycji kosztorysu."
                                ) if self.is_promotion_priority else self.create_component(
                                    component_type="header",
                                    name="invoiceDescription",
                                    value="Zestawienie to spis wszystkich faktur/rachunków/biletów, które dotyczą przedsięwzięcia i zostały pokryte z dofinansowania PISF. Spis zawierać powinien: rodzaj dokumentu (faktura/rachunek), nr faktury/rachunku (w przypadku rachunku należy podać jego nr i datę oraz podać nr i datę umowy, której dotyczy), datę wystawienia dokumentu, nazwę wydatku (rodzaj towaru/usługi), wysokość wydatkowanej kwoty ze wskazaniem części, w jakiej została ona pokryta z dofinansowania PISF. Uwaga: Każda z faktur/rachunków opłaconych z otrzymanego dofinansowania powinna być podpisana na odwrocie przez Stypendystę oraz zawierać sporządzony w sposób trwały opis zawierający informacje: z jakich środków wydatkowana kwota została pokryta oraz jakie było przeznaczenie zakupionych towarów, usług lub innego rodzaju opłaconej należności. Informacja ta powinna być podpisana przez osobę odpowiedzialną za sprawy dotyczące rozliczeń finansowych Stypendysty. W przypadku faktur za akredytacje, noclegi i bilety należy podać imię i nazwisko osoby, której dotyczy pozycja. Z dotacji PISF mogą zostać pokryte dokumenty księgowe wystawione od momentu złożenia wniosku o dofinansowanie PISF (w wersji elektronicznej) do zakończenia przedsięwzięcia określonego w harmonogramie stanowiącym załącznik nr 1/1A do Umowy. Przeliczeń z waluty obcej na PLN należy dokonywać dla każdej pozycji osobno, wg średniego kursu NBP z dnia poprzedzającego dzień wystawienia faktury (w przypadku płatności gotówką) lub kursu faktycznego wynikającego z przedstawionych dokumentów finansowo-księgowych. Uwzględnić należy wartość przelicznika do 4. miejsca po przecinku, a otrzymaną wartość w PLN – zaokrąglić do 2. miejsca po przecinku. Kolejność wpisywania faktur powinna być taka sama jak kolejność pozycji kosztorysu."
                                )
                            ]
                        ),
                        self.section.report_expenditure_exacution.invoice_section_headers(is_promotion_priority=self.is_promotion_priority),
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 1,
                                "maxCount": 60
                            },
                            is_paginated=True,
                            class_list={
                                "main": [
                                    "no-title",
                                    "swappable-bg",
                                ]
                            },
                            components=[
                                self.section.report_expenditure_exacution.invoice_section(is_promotion_priority=self.is_promotion_priority, is_multi=True)
                            ]
                        ),
                        self.create_chapter(
                            title="Łącznie PLN",
                            class_list={
                                "main": [
                                    "table-2-sum",
                                    "grid",
                                    "grid-cols-4",
                                    "no-title"
                                ],
                                "sub": [
                                    "table-2-sum__col"
                                ]
                            },
                            components=[
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Suma wydatków w PLN",
                                    name="costInPlnTotalSum",
                                    calculation_rules=[
                                        self.calculation_rule.dynamic_sum_inputs(
                                            fields=[
                                                "costInPln"
                                            ]
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_sum_validator(
                                            field_names=[
                                                "costInPln"
                                            ]
                                        )
                                    ],
                                    read_only=True,
                                    unit="PLN",
                                    class_list=[
                                        "default-margin",
                                        "col-start-3",
                                        "userInput-border"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="W tym z dofinansowania PISF w PLN",
                                    name="costInPlnPisfTogether",
                                    calculation_rules=[
                                        self.calculation_rule.dynamic_sum_inputs(
                                            fields=[
                                                "costInPlnPisf"
                                            ]
                                        )
                                    ],
                                    validators=[
                                        self.validator.related_sum_validator(
                                            field_names=[
                                                "costInPlnPisf"
                                            ]
                                        ),
                                        self.validator.related_sum_validator(
                                            field_names=[
                                                "reportingCostsPisfSupport"
                                            ]
                                        )
                                    ],
                                    read_only=True,
                                    unit="PLN",
                                    class_list=[
                                        "default-margin",
                                        "userInput-border"
                                    ]
                                )
                            ]
                        )
                    ]
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
                                    value="Do raportu należy załączyć dokumenty finansowo-księgowe potwierdzające wydatkowania kosztów poniesionych z udzielonego dofinansowania w postaci faktur (WAŻNE: faktury muszą być wystawione na Stypendystę jako osobę fizyczną) oraz biletów (jeśli z przyczyn obiektywnie niezależnych od Stypendysty niemożliwe jest otrzymanie faktury) wraz z potwierdzeniem wykonania przelewów z rachunku bankowego Stypendysty." if not self.is_promotion_priority else "Do raportu należy załączyć ewentualny raport medialny, ulotki, plakaty oraz inne materiały promocyjne i informacyjne.",
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
                                  value=checkbox["label"],
                                  class_list=[
                                      "col-span-9",
                                      "text-left",
                                      "displayNoneFrontend"
                                  ]
                              )
                          ]],
                        self.create_component(
                            component_type="text",
                            label=f"PODPIS {'BENEFICJENTA' if self.is_promotion_priority else 'STYPENDYSTY'}:",
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
