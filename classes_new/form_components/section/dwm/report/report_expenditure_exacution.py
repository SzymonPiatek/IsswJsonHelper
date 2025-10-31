from classes_new.form_components.section.section import Section


class ReportExpenditureExecution(Section):
    def __init__(self):
        super().__init__()

    def invoice_section_headers_promotion(self):
        return self.create_chapter(
            class_list=[
                "grid",
                "grid-cols-15",
                "table-header"
            ],
            components=[
                self.create_component(
                    component_type="header",
                    name="invoiceNumber",
                    value="Nr i nazwa dokument księgowego",
                    class_list=[
                        "displayNoneFrontend",
                        "text-left",
                        "col-span-8",
                        "col-start-2"
                    ]
                ),
                self.create_component(
                    component_type="header",
                    name="invoiceTotalCost",
                    value="Kwota całkowita",
                    class_list=[
                        "text-center",
                        "col-span-4",
                        "displayNoneFrontend"
                    ]
                ),
                self.create_component(
                    component_type="header",
                    name="invoicePISFRefund",
                    value="W tym z dofinansowania PISF",
                    class_list=[
                        "text-center",
                        "displayNoneFrontend",
                        "col-span-2"
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
                        "displayNoneFrontend",
                        "col-span-2"
                    ]
                ),
                self.create_component(
                    component_type="header",
                    name="invoicePaymentDate",
                    value="Data zapłaty",
                    class_list=[
                        "text-center",
                        "displayNoneFrontend",
                        "col-span-2"
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
                        "displayNoneFrontend",
                        "col-span-2"
                    ]
                ),
                self.create_component(
                    component_type="header",
                    name="totalInvoiceOtherCurrency",
                    value="W walucie obcej",
                    class_list=[
                        "text-center",
                        "displayNoneFrontend",
                        "col-span-2"
                    ]
                ),
                self.create_component(
                    component_type="header",
                    name="totalInvoicePLN",
                    value="PLN",
                    class_list=[
                        "text-center",
                        "displayNoneFrontend",
                        "col-span-2"
                    ]
                ),
                self.create_component(
                    component_type="header",
                    name="supportInvoicePLN",
                    value="PLN",
                    class_list=[
                        "text-center",
                        "displayNoneFrontend",
                        "col-span-2"
                    ]
                ),
            ]
        )

    def invoice_section_promotion(self):
        return self.create_chapter(
            title="Faktura/rachunek",
            class_list={
                "sub": [
                    "table-invoice__col"
                ],
                "main": [
                    "table-invoice",
                    "grid",
                    "grid-cols-15",
                ]
            },
            components=[
                self.create_component(
                    component_type="textarea",
                    label="Lp.",
                    name="lp-number-invoice",
                    class_list=[
                        "displayNoneFrontend",
                        "no-label"
                    ],
                    calculation_rules=[
                        self.calculation_rule.row_number()
                    ]
                ),
                self.create_component(
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
                        "col-span-14",
                        "text-bold",
                        "no-label",
                        "text-left"
                    ]
                ),
                self.create_component(
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
                        "col-start-2",
                        "col-span-14",
                        "text-left"
                    ]
                ),
                self.create_component(
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
                        "table-1-2",
                        "col-start-2"
                    ]
                ),
                self.create_component(
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
                        "no-label",
                        "col-span-2"
                    ]
                ),
                self.create_component(
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
                        "no-label",
                        "col-span-2"
                    ]
                ),
                self.create_component(
                    component_type="currency",
                    label="Waluta",
                    name="costCurrency",
                    class_list=[
                        "no-label",
                        "table-1-2"
                    ],
                    required=True
                ),
                self.create_component(
                    component_type="number",
                    label="Kurs średni NBP",
                    name="costCurrencyNbpExchRate",
                    calculation_rules=[
                        self.calculation_rule.get_nbp_currency(
                            date_field="accountingDocDateIssued",
                            currency_field="costCurrency",
                        )
                    ],
                    validators=[
                        self.validator.length_validator(
                            max_value=20
                        )
                    ],
                    read_only=True,
                    class_list=[
                        "no-label",
                        "table-1-2",
                        "col-span-2"
                    ]
                ),
                self.create_component(
                    component_type="text",
                    mask="fund",
                    label="Kwota całkowita w walucie obcej",
                    name="costInCurrency",
                    class_list=[
                        "no-label",
                        "table-1-2",
                        "col-span-2"
                    ]
                ),
                self.create_component(
                    component_type="text",
                    mask="fund",
                    label="Kwota całkowita w PLN",
                    name="costInPln",
                    class_list=[
                        "no-label",
                        "col-span-2"
                    ],
                    read_only=True,
                    calculation_rules=[
                        self.calculation_rule.local_multiply_inputs(
                            fields=[
                                "costInCurrency",
                                "costCurrencyNbpExchRate"
                            ]
                        )
                    ],
                    validators=[
                        self.validator.related_local_multiplication_validator(
                            field_names=[
                                "costInCurrency",
                                "costCurrencyNbpExchRate"
                            ]
                        )
                    ],
                    unit="PLN"
                ),
                self.create_component(
                    component_type="text",
                    mask="fund",
                    label="W tym ze środków pochodzących z dofinansowania PISF w PLN",
                    name="costInPlnPisf",
                    required=True,
                    class_list=[
                        "no-label",
                        "col-span-2"
                    ],
                    unit="PLN"
                )
            ]
        )

    def invoice_section_headers_foreign(self):
        return self.create_chapter(
            class_list=[
                "grid",
                "grid-cols-16",
                "table-header"
            ],
            components=[
                self.create_component(
                    component_type="header",
                    name="invoiceNumber",
                    value="Nr i nazwa dokument księgowego",
                    class_list=[
                        "displayNoneFrontend",
                        "text-left",
                        "col-span-9",
                        "col-start-2"
                    ]
                ),
                self.create_component(
                    component_type="header",
                    name="invoiceTotalCost",
                    value="Kwota całkowita",
                    class_list=[
                        "text-center",
                        "col-span-4",
                        "displayNoneFrontend"
                    ]
                ),
                self.create_component(
                    component_type="header",
                    name="invoicePISFRefund",
                    value="W tym z dofinansowania PISF",
                    class_list=[
                        "text-center",
                        "displayNoneFrontend",
                        "col-span-2"
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
                        "displayNoneFrontend",
                        "col-span-2"
                    ]
                ),
                self.create_component(
                    component_type="header",
                    name="invoicePaymentDate",
                    value="Data zapłaty",
                    class_list=[
                        "text-center",
                        "displayNoneFrontend",
                        "col-span-2"
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
                    name="isActaulRate",
                    value="Kurs faktyczny",
                    class_list=[
                        "text-center",
                        "displayNoneFrontend"
                    ]
                ),
                self.create_component(
                    component_type="header",
                    name="invoicePriceNBP",
                    value="Średni kurs NBP / kurs faktyczny",
                    class_list=[
                        "text-center",
                        "displayNoneFrontend",
                        "col-span-2"
                    ]
                ),
                self.create_component(
                    component_type="header",
                    name="totalInvoiceOtherCurrency",
                    value="W walucie obcej",
                    class_list=[
                        "text-center",
                        "displayNoneFrontend",
                        "col-span-2"
                    ]
                ),
                self.create_component(
                    component_type="header",
                    name="totalInvoicePLN",
                    value="PLN",
                    class_list=[
                        "text-center",
                        "displayNoneFrontend",
                        "col-span-2"
                    ]
                ),
                self.create_component(
                    component_type="header",
                    name="supportInvoicePLN",
                    value="PLN",
                    class_list=[
                        "text-center",
                        "displayNoneFrontend",
                        "col-span-2"
                    ]
                ),
            ]
        )

    def invoice_section_foreign(self, is_multi: bool = False):
        class_list = {
            "sub": [
                "new_table_4__col"
            ],
            "main": [
                "new_table",
                "grid",
                "grid-cols-16"
            ]
        }

        if is_multi:
            class_list["main"].append("padding__0_1")

        return self.create_chapter(
            title="Faktura/rachunek",
            class_list=class_list,
            components=[
                self.create_chapter(
                    class_list=[
                        "displayNoneFrontend"
                    ],
                    components=[
                        self.create_component(
                            component_type="textarea",
                            label="Lp.",
                            name="lp-number-invoice",
                            class_list=[
                                "no-label"
                            ],
                            read_only=True,
                            calculation_rules=[
                                self.calculation_rule.row_number()
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    class_list={
                        "main": [
                            "col-span-15",
                            "new_table_4__4-4"
                        ]
                    },
                    components=[
                        self.create_component(
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
                                "no-label",
                                "text-left"
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    class_list={
                        "main": [
                            "col-start-2",
                            "col-span-15",
                            "new_table_4__4-4"
                        ]
                    },
                    components=[
                        self.create_component(
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
                                "no-label"
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    class_list={
                        "main": [
                            "col-start-2",
                            "new_table_4__2-4"
                        ]
                    },
                    components=[
                        self.create_component(
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
                                "no-label"
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    class_list=[
                        "col-span-2"
                    ],
                    components=[
                        self.create_component(
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
                    ]
                ),
                self.create_chapter(
                    class_list=[
                        "col-span-2"
                    ],
                    components=[
                        self.create_component(
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
                    ]
                ),
                self.create_chapter(
                    class_list={
                        "main": [
                            "new_table_4__2-4",
                        ],
                    },
                    components=[
                        self.create_component(
                            component_type="currency",
                            label="Waluta",
                            name="costCurrency",
                            class_list=[
                                "no-label"
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Użyj kursu faktycznego",
                            name="isActualRate",
                            class_list=[
                                "no-label"
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    class_list={
                        "main": [
                            "col-span-2"
                        ]
                    },
                    components=[
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.local_equals_value(
                                    field_name="isActualRate",
                                    values=[False]
                                )
                            ],
                            components=[
                                self.create_component(
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
                                        "displayNonePDF"
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.local_equals_value(
                                    field_name="isActualRate",
                                    values=[True]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="number",
                                    label="Kurs faktyczny",
                                    name="costCurrencyActualRate",
                                    class_list=[
                                        "no-label",
                                        "displayNonePDF"
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            class_list=[
                                "displayNoneFrontend"
                            ],
                            components=[
                                self.create_component(
                                    component_type="number",
                                    name="choosenRate",
                                    class_list=[
                                        "no-label"
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
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    class_list={
                        "main": [
                            "col-span-2",
                            "new_table_4__2-4"
                        ]
                    },
                    components=[
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="Kwota całkowita w walucie obcej",
                            name="costInCurrency",
                            class_list=[
                                "no-label"
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    class_list=[
                        "col-span-2"
                    ],
                    components=[
                        self.create_component(
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
                                        "choosenRate"
                                    ]
                                )
                            ],
                            validators=[
                                self.validator.related_local_multiplication_validator(
                                    field_names=[
                                        "costInCurrency",
                                        "choosenRate"
                                    ]
                                )
                            ],
                            unit="PLN"
                        )
                    ]
                ),
                self.create_chapter(
                    class_list=[
                        "col-span-2"
                    ],
                    components=[
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="W tym ze środków pochodzących z dofinansowania PISF w PLN",
                            name="costInPlnPisf",
                            required=True,
                            class_list=[
                                "no-label",
                                "col-span-2"
                            ],
                            unit="PLN"
                        )
                    ]
                )
            ]
        )

    def invoice_section(self, is_promotion_priority: bool = False, is_multi: bool = False):
        if is_promotion_priority:
            return self.invoice_section_promotion()
        else:
            return self.invoice_section_foreign(is_multi=is_multi)

    def invoice_section_headers(self, is_promotion_priority: bool = False):
        if is_promotion_priority:
            return self.invoice_section_headers_promotion()
        else:
            return self.invoice_section_headers_foreign()
