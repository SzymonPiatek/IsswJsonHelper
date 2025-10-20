from ..report_builder import DWMReportBuilder2026
from ..priority import PromotionPriority


class PromotionReportBuilder(DWMReportBuilder2026, PromotionPriority):
    FORM_ID = 62

    def __init__(self):
        super().__init__()

        self.intro_text = [
                "Raport końcowy",
                "<small>z wykonania przedsięwzięcia realizowanego w ramach Programu Operacyjnego \"Promocja polskiej twórczości filmowej za granicą\"</small> <br> Priorytet I \"Promocja polskiej twórczości filmowej za granicą\""
        ]

    def create_report_basic_data(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Dane podstawowe",
            chapters=[
                self.section.report_basic_data.project_implementation_period(number="A"),
                self.section.report_basic_data.agreement_and_annex(number="B"),
                self.section.report_basic_data.grantee_name_and_address(number="C")
            ]
        )

        self.save_part(part)

    def create_report_general_data(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Informacje ogólne",
            chapters=[
                self.create_chapter(
                    class_list=[
                        "grid",
                        "grid-cols-3",
                        "no-title"
                    ],
                    components=[
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
                            name="taskCompletionInfo",
                            value="2. Stopień realizacji przedsięwzięcia na dzień złożenia raportu",
                            class_list=[
                                "displayNoneFrontend"
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="2. Stopień realizacji przedsięwzięcia na dzień złożenia raportu",
                            name="taskCompletionInfo",
                            validators=[
                                self.validator.length_validator(max_value=10000)
                            ],
                            required=True,
                            class_list=[
                                "no-label",
                                "col-span-2",
                                "text-left"
                            ]
                        ),
                        self.create_component(
                            component_type="header",
                            name="taskImplementationDesc",
                            value="3. Szczegółowy opis wykonania przedsięwzięcia",
                            class_list=[
                                "displayNoneFrontend"
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="3. Szczegółowy opis wykonania przedsięwzięcia",
                            name="taskImplementationDesc",
                            validators=[
                                self.validator.length_validator(max_value=20000)
                            ],
                            required=True,
                            class_list=[
                                "no-label",
                                "col-span-2",
                                "text-left"
                            ]
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
                    ]
                )
            ]
        )

        self.save_part(part)

    def create_report_expenditure_exacution(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Sprawozdanie z wykonania wydatków",
            class_list=[
                "full-width-grid"
            ],
            chapters=[
                self.section.report_expenditure_exacution.grantee_vat_declaration(),
                self.create_chapter(
                    class_list={
                        "sub": [
                            "table-4-top"
                        ]
                    },
                    components=[
                        self.section.report_expenditure_exacution.expenses_information_incurred_in_implementing_the_project(),
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
                        ),
                        self.section.report_expenditure_exacution.cost_estimate_by_source_of_financing()
                    ]
                ),
                self.section.report_expenditure_exacution.list_of_bills_and_invoices()
            ]
        )

        self.save_part(part)
