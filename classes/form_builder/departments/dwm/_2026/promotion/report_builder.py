from .priority import PromotionPriority
from ..report_builder import DWMReportBuilder2026


class PromotionReportBuilder(DWMReportBuilder2026, PromotionPriority):
    FORM_ID = 9226

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
                self.section.report_basic_data.project_implementation_period(number="A"),
                self.section.report_basic_data.agreement_and_annex(number="B"),
                self.section.report_basic_data.grantee_name_and_address(number="C")
            ]
        )

        self.save_part(part)

    def create_report_general_data(self):
        part = self.create_part(
            title="II. Informacje ogólne",
            short_name="II. Informacje ogólne",
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

    def create_report_expenditure_exacution(self):
        part = self.create_part(
            title="III. Sprawozdanie z wykonania wydatków",
            short_name="III. Sprawozdanie z wykonania wydatków",
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
                            options=[
                                "Wnioskodawca JEST płatnikiem VAT, dlatego kwoty zamieszczone w kosztach planowanego przedsięwzięcia we wniosku to KWOTY NETTO",
                                "Wnioskodawca NIE JEST płatnikiem VAT, dlatego kwoty zamieszczone w kosztorysie wniosku to KWOTY BRUTTO"
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    class_list={
                        "sub": [
                            "table-4-top"
                        ]
                    },
                    components=[
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
                                                "reportingCostsPisfSupport",
                                                "reportingCostsOwnFunds",
                                                "reportingCostsOtherFunds"
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
                                        #     TODO
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
                                            value="Zestawienie to stanowi porównanie kosztów planowanych z faktycznie poniesionymi. Uwaga: procentowy wkład dotacji PISF w finalnym budżecie przedsięwzięcia nie może przekroczyć wkładu zakładanego (określonego w umowie). Jeżeli faktycznie poniesiony koszt całkowity przedsięwzięcia okazał się niższy od planowanego lub Beneficjent nie wykorzystał całej dotacji, należy dokonać zwrotu na rachunek PISF i dostarczyć wraz z raportem potwierdzenie przelewu. Nr rachunku PISF: Banku Gospodarstwa Krajowego Beneficjenci krajowi: 91 1130 1017 0020 1234 1320 0016, Beneficjenci zagraniczni: PL 91 1130 1017 0020 1234 1320 0016 SWIFT: GOSKPLPW."
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
                                            component_type="number",
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
                                            component_type="number",
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
                                            component_type="number",
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
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="number",
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
                                                ),
                                                self.validator.related_fraction_lte_validator(
                                                    field_name="reportingCostsTotal",
                                                    ratio=0.1,
                                                    message="Minimalny wkład własny wnioskodawcy powinien wynosić 10% całości budżetu przedsięwzięcia."
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
                                            component_type="number",
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
                                            component_type="number",
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
                                )
                            ]
                        )
                    ]
                )
            ]
        )

        self.save_part(part)

    def create_report_additional_information(self):
        part = self.create_part(
            title="IV. Dodatkowe informacje",
            short_name="IV. Dodatkowe informacje",
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
                            multiple_forms_rules={
                                "minCount": 1,
                                "maxCount": 20
                            },
                            class_list=[
                                "swappable-bg"
                            ],
                            components=[
                                self.create_chapter(
                                    title="Załącznik",
                                    class_list=[
                                        "no-title"
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
                          for checkbox in [
                              {
                                  "label": "Od daty zawarcia umowy nie zmienił się status prawny Beneficjenta.",
                                  "name": "statementLegalStatusUnchanged"
                              },
                              {
                                  "label": "Wszystkie podane w niniejszym raporcie informacje są zgodne z aktualnym stanem prawnym i faktycznym.",
                                  "name": "statementDeclaredInformationUptodate"
                              },
                              {
                                  "label": "Przedstawiciele Instytutu dokonujący weryfikacji mogą dokonać poprawy oczywistych omyłek pisarskich i rachunkowych w raporcie końcowym, zawiadamiając o tym Beneficjenta.",
                                  "name": "statementInstituteMayCorrectObviousErrors"
                              },
                              {
                                  "label": "Oświadczam, że zestawienie faktur (rachunków) obejmuje wyłącznie koszty ujęte w ewidencji księgowej podmiotu realizującego przedsięwzięcie.",
                                  "name": "statementInvoicesIncludeOnlyRecordedCosts"
                              },
                              {
                                  "label": "Oświadczam, że wszystkie kwoty wymienione w zestawieniu faktur (rachunków) zostały faktycznie poniesione.",
                                  "name": "statementAllInvoiceAmountsActuallyIncurred"
                              },
                              {
                                  "label": "Oświadczam, że wszystkie płatności, w tym podatki i świadczenia od wynagrodzeń zostały uregulowane do dnia zakończenia zadania, o którym mowa w § ………… zawartej umowy z PISF.",
                                  "name": "statementAllPaymentsSettledByProjectEnd"
                              },
                              {
                                  "label": "Oświadczam, że w całkowitym koszcie przedsięwzięcia nie został uwzględniony podatek od towarów i usług (VAT) podlegający odzyskaniu lub rozliczeniu w deklaracjach składanych do Urzędu Skarbowego.",
                                  "name": "statementNoRecoverableVATIncluded"
                              },
                              {
                                  "label": "Oświadczam, że nie toczą się przeciwko mnie żadne postępowania sądowe oraz nie posiadam żadnych tytułów egzekucyjnych wydanych przez komornika.",
                                  "name": "statementNoLegalProceedingsOrEnforcements"
                              }
                          ]
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
                            label="PODPIS BENEFICJENTA:",
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
