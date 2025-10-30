from classes_new.form_components.section.section import Section


class ReportExpenditureExecution(Section):
    def __init__(self):
        super().__init__()

    def invoice_section(self, is_promotion_priority: bool = False):
        lp_invoice_number = self.create_component(
            component_type="textarea",
            label="Lp.",
            name="lp-number-invoice",
            class_list=[
                "displayNoneFrontend",
                "no-label"
            ],
            read_only=True,
            calculation_rules=[
                self.calculation_rule.row_number()
            ]
        )
        cost_expenditure_desc = self.create_component(
            component_type="textarea",
            label="Nazwa i opis wydatku",
            name="costExpenditureDesc",
            validators=[
                self.validator.length_validator(
                    max_value=200
                )
            ],
            required=True,
            class_list=[
                "col-span-11",
                "text-bold",
                "no-label",
                "text-left"
            ]
        )
        accounting_doc_type_num = self.create_component(
            component_type="textarea",
            label="Rodzaj i numer dokumentu księgowego",
            name="accountingDocTypeNum",
            validators=[
                self.validator.length_validator(
                    max_value=150
                )
            ],
            required=True,
            class_list=[
                "table-invoice__full",
                "no-label",
                "col-start-2"
            ]
        )

        cost_estimate_item_num = self.create_component(
            component_type="text",
            label="Numer pozycji kosztorysu",
            name="costEstimateItemNum",
            validators=[
                self.validator.length_validator(
                    max_value=10
                )
            ],
            required=True,
            class_list=[
                "no-label",
                "table-1-2"
            ]
        )
        accounting_doc_date_issued = self.create_component(
            component_type="date",
            label="Data wystawienia",
            name="accountingDocDateIssued",
            validators=[
                self.validator.related_date_gte_validator(
                    field_name="taskDateStart",
                    message="Data wystawienia nie może być wcześniejsza niż data wpłynięcia wniosku."
                ),
                self.validator.related_date_lte_validator(
                    field_name="taskDateEnd",
                    message="Data wystawienia nie może być późniejsza niż data zakończenia przedsięwzięcia"
                )
            ],
            required=True,
            class_list=[
                "no-label"
            ]
        )
        cost_payment_date = self.create_component(
            component_type="date",
            label="Data zapłaty",
            name="costPaymentDate",
            validators=[
                self.validator.related_date_gte_validator(
                    field_name="taskDateStart",
                    message="Data zapłaty nie może być wcześniejsza niż data wpłynięcia wniosku."
                ),
                self.validator.related_date_lte_validator(
                    field_name="taskDateEnd",
                    message="Data zapłaty nie może być późniejsza niż data zakończenia przedsięwzięcia"
                )
            ],
            required=True,
            class_list=[
                "no-label"
            ]
        )
        cost_currency = self.create_component(
            component_type="currency",
            label="Waluta",
            name="costCurrency",
            class_list=[
                "no-label",
                "table-1-2"
            ],
            required=True
        )
        cost_currency_nbp_exch_rate = self.create_component(
            component_type="number",
            label="Kurs średni NBP",
            name="costCurrencyNbpExchRate",
            calculation_rules=[
                self.calculation_rule.get_nbp_currency(
                    date_field="accountingDocDateIssued",
                    currency_field="costCurrency",
                )
            ],
            read_only=True,
            class_list=[
                "no-label",
                "table-1-2"
            ] if is_promotion_priority else [
                "no-label"
            ]
        )
        cost_currency_actual_rate = self.create_component(
            component_type="number",
            label="Kurs faktyczny",
            name="costCurrencyActualRate",
            class_list=[
                "no-label"
            ]
        )
        choosen_rate = self.create_component(
            component_type="number",
            name="choosenRate",
            class_list=[
                "no-label",
                "displayNoneFrontend",
                "displayNonePDF"
            ],
            read_only=True,
            calculation_rules=[
                self.calculation_rule.conditional_copy_value(
                    field_name_local="isActualRate",
                    condition={
                        "containValues": ["true"]
                    },
                    correct_field_name_local="costCurrencyActualRate",
                    incorrect_field_name_local="costCurrencyNbpExchRate"
                )
            ]
        )
        is_actual_rate = self.create_component(
            component_type="checkbox",
            label="Użyj kursu faktycznego",
            name="isActualRate",
            class_list=[
                "no-label"
            ]
        )
        cost_in_currency = self.create_component(
            component_type="text",
            mask="fund",
            label="Kwota całkowita w walucie obcej",
            name="costInCurrency",
            class_list=[
                "no-label",
                "table-1-2"
            ] if is_promotion_priority else [
                "no-label"
            ]
        )
        cost_in_pln = self.create_component(
            component_type="text",
            mask="fund",
            label="Kwota całkowita w PLN",
            name="costInPln",
            class_list=[
                "no-label"
            ],
            read_only=True,
            calculation_rules=[
                self.calculation_rule.local_multiply_inputs(
                    fields=[
                        "costInCurrency",
                        "costCurrencyNbpExchRate"
                    ]
                ) if is_promotion_priority else self.calculation_rule.local_multiply_inputs(
                    fields=[
                        "costInCurrency",
                        "choosenRate"
                    ]
                )
            ],
            validators=[
                self.validator.related_local_multiplication_validator(
                    field_names=[
                        "costInCurrency",
                        "costCurrencyNbpExchRate"
                    ]
                ) if is_promotion_priority else self.validator.related_local_multiplication_validator(
                    field_names=[
                        "costInCurrency",
                        "choosenRate"
                    ]
                )
            ],
            unit="PLN"
        )
        cost_in_pln_pisf = self.create_component(
            component_type="text",
            mask="fund",
            label="W tym ze środków pochodzących z dofinansowania PISF w PLN",
            name="costInPlnPisf",
            required=True,
            class_list=[
                "no-label"
            ],
            unit="PLN"
        )

        if is_promotion_priority:
            chapter = self.create_chapter(
                title="Faktura/rachunek",
                class_list={
                    "sub": [
                        "table-invoice__col",
                    ],
                    "main": [
                        "table-invoice",
                        "grid",
                        "grid-cols-12",
                    ]
                },
                components=[
                    lp_invoice_number,
                    cost_expenditure_desc,
                    accounting_doc_type_num,
                    cost_estimate_item_num,
                    accounting_doc_date_issued,
                    cost_payment_date,
                    cost_currency,
                    cost_currency_nbp_exch_rate,
                    cost_in_currency,
                    cost_in_pln,
                    cost_in_pln_pisf
                ],
            )
        else:
            chapter = self.create_chapter(
                title="Faktura/rachunek",
                class_list={
                    "main": []
                },
                components=[
                    self.create_chapter(
                        components=[
                            lp_invoice_number,
                            cost_expenditure_desc,
                            accounting_doc_type_num,
                        ]
                    ),
                    self.create_chapter(
                        class_list={
                            "main": [
                                "table-1-2"
                            ],
                            "sub": [
                                "table-1-2__col"
                            ]
                        },
                        components=[
                            self.create_chapter(
                                components=[
                                    cost_estimate_item_num
                                ]
                            ),
                            self.create_chapter(
                                class_list={
                                    "main": [
                                        "table-1-2"
                                    ],
                                    "sub": [
                                        "table-1-2__col"
                                    ]
                                },
                                components=[
                                    accounting_doc_date_issued,
                                    cost_payment_date
                                ]
                            ),
                            self.create_chapter(
                                components=[
                                    cost_currency
                                ]
                            ),
                            self.create_chapter(
                                class_list={
                                    "main": [
                                        "table-1-2"
                                    ],
                                    "sub": [
                                        "table-1-2__col"
                                    ]
                                },
                                components=[
                                    cost_currency_nbp_exch_rate,
                                    cost_currency_actual_rate
                                ]
                            ),
                            self.create_chapter(
                                class_list={
                                    "main": [
                                        "table-1-2"
                                    ],
                                    "sub": [
                                        "table-1-2__col"
                                    ]
                                },
                                components=[
                                    is_actual_rate,
                                    cost_in_currency
                                ]
                            ),
                            self.create_chapter(
                                class_list={
                                    "main": [
                                        "table-1-2"
                                    ],
                                    "sub": [
                                        "table-1-2__col"
                                    ]
                                },
                                components=[
                                    choosen_rate,
                                    cost_in_pln,
                                    cost_in_pln_pisf
                                ]
                            )
                        ]
                    )
                ]
            )

        return chapter

    def invoice_section_headers(self, is_promotion_priority: bool = False):
        return self.create_chapter(
            class_list=[
                "grid",
                "grid-cols-12",
                "table-header"
            ],
            components=[
                self.create_component(
                    component_type="header",
                    name="invoiceTotalCost",
                    value="Kwota całkowita",
                    class_list=[
                        "text-center",
                        "col-start-9",
                        "col-span-2",
                        "displayNoneFrontend"
                    ]
                ),
                self.create_component(
                    component_type="header",
                    name="invoicePISFRefund",
                    value="W tym z dofinansowania PISF",
                    class_list=[
                        "text-center",
                        "col-start-11",
                        "col-span-2",
                        "displayNoneFrontend"
                    ]
                ),
                self.create_component(
                    component_type="header",
                    name="invoiceLp",
                    value="Lp.",
                    class_list=[
                        "text-center",
                        "displayNoneFrontend"
                    ]
                ),
                self.create_component(
                    component_type="header",
                    name="invoiceNumber",
                    value="Nr i nazwa dokumentu księgowego",
                    class_list=[
                        "text-center",
                        "displayNoneFrontend"
                    ]
                ),
                self.create_component(
                    component_type="header",
                    name="invoicePositionNumber",
                    value="Nr pozycji kosztorysu",
                    class_list=[
                        "text-center",
                        "displayNoneFrontend"
                    ]
                ),
                self.create_component(
                    component_type="header",
                    name="invoiceIssuedDate",
                    value="Data wystawienia",
                    class_list=[
                        "text-center",
                        "displayNoneFrontend"
                    ]
                ),
                self.create_component(
                    component_type="header",
                    name="invoicePaymentDate",
                    value="Data zapłaty",
                    class_list=[
                        "text-center",
                        "displayNoneFrontend"
                    ]
                ),
                self.create_component(
                    component_type="header",
                    name="invoiceDesc",
                    value="Waluta",
                    class_list=[
                        "text-center",
                        "displayNoneFrontend"
                    ]
                ),
                self.create_component(
                    component_type="header",
                    name="invoicePriceNBP",
                    value="Średni kurs NBP",
                    class_list=[
                        "text-center",
                        "displayNoneFrontend"
                    ]
                ),
                self.create_component(
                    component_type="header",
                    name="totalInvoiceOtherCurrency",
                    value="W walucie obcej",
                    class_list=[
                        "text-center",
                        "displayNoneFrontend"
                    ]
                ),
                self.create_component(
                    component_type="header",
                    name="totalInvoicePLN",
                    value="PLN",
                    class_list=[
                        "text-center",
                        "displayNoneFrontend"
                    ]
                ),
                self.create_component(
                    component_type="header",
                    name="supportInvoiceOtherCurrency",
                    value="W walucie obcej",
                    class_list=[
                        "text-center",
                        "displayNoneFrontend"
                    ]
                ),
                self.create_component(
                    component_type="header",
                    name="supportInvoicePLN",
                    value="PLN",
                    class_list=[
                        "text-center",
                        "displayNoneFrontend"
                    ]
                ),
            ]
        )
