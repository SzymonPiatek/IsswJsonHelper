from classes_new.form_components.section.dwm.report.report_expenditure_exacution import ReportExpenditureExecution
from classes_new.form_components.section.section import Section


class DWMSection(Section):
    def __init__(self):
        super().__init__()

        self.report_expenditure_exacution = ReportExpenditureExecution()

    def pisf_transfer_currency(
            self,
            number: int | str
    ):
        return self.create_chapter(
            title=f"{number}. Waluta, z której dotacja PISF ma zostać przelana na w/w konto",
            components=[
                self.create_chapter(
                    title="Uwaga, rozliczenie przedsięwzięcia musi zostać przedstawione w walucie PLN",
                    class_list={
                        "main": [
                            "table-1-2",
                            "grid",
                            "grid-cols-2"
                        ],
                        "sub": [
                            "table-1-2__col"
                        ]
                    },
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Waluta, w której dotacja PISF ma zostać przelana na w/w konto",
                            name="applicantCurrency",
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Waluta rozliczenia",
                            name="applicantCurrencySettlement",
                            read_only=True,
                            value="PLN"
                        )
                    ]
                )
            ]
        )

    def applicant_bank_data(
            self,
            number: int | str,
            poland: bool = True,
            foreign: bool = True,
            is_promotion: bool = False,
    ):
        chapter = self.create_chapter(
            title=f"{number}. Nazwa i numer rachunku bankowego",
            components=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="bankAccountInfo",
                            value="WAŻNE: Wszystkie koszty dotyczące danego przedsięwzięcia powinny być ponoszone z rachunku bankowego wskazanego we Wniosku o dofinansowanie, jak również wszystkie wpłaty od podmiotów współfinansujących dane przedsięwzięcie powinny być dokonywane na rachunek bankowy wskazany we Wniosku o dofinansowanie." if is_promotion else "WAŻNE: Wszystkie koszty dotyczące danego przedsięwzięcia powinny być ponoszone z rachunku bankowego wskazanego we Wniosku o ustanowienie stypendium, jak również wszystkie wpłaty od podmiotów współfinansujących dane przedsięwzięcie powinny być dokonywane na rachunek bankowy wskazany we Wniosku o ustanowienie stypendium. Ponadto rachunek bankowy nie może być rachunkiem firmowym."
                        )
                    ]
                )
            ]
        )

        if poland:
            chapter["components"].append(
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="applicantResidence",
                            values=[
                                "w Polsce"
                            ]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Nazwa banku",
                            name="applicantBank",
                            required=True,
                            validators=[
                                self.validator.related_required_if_equal_validator(
                                    field_name="applicantResidence",
                                    value="w Polsce"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            mask="bankAccount",
                            label="Numer konta bankowego",
                            name="applicantBankAccountNum",
                            validators=[
                                self.validator.length_validator(
                                    min_value=26,
                                    max_value=26
                                ),
                                self.validator.related_required_if_equal_validator(
                                    field_name="applicantResidence",
                                    value="w Polsce"
                                )
                            ],
                            required=True
                        )
                    ]
                )
            )
        if foreign:
            chapter["components"].append(
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="applicantResidence",
                            values=[
                                "za granicą"
                            ]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Nazwa banku",
                            name="applicantForeignBank",
                            required=True,
                            validators=[
                                self.validator.related_required_if_equal_validator(
                                    field_name="applicantResidence",
                                    value="za granicą"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Międzynarodowy Numer Rachunku Bankowego (IBAN)",
                            name="applicantIban",
                            mask="ibanAccount",
                            required=True,
                            validators=[
                                self.validator.iban_validator(),
                                self.validator.related_required_if_equal_validator(
                                    field_name="applicantResidence",
                                    value="za granicą"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Kod SWIFT banku",
                            name="applicantForeignBankSwift",
                            validators=[
                                self.validator.swift_validator(),
                                self.validator.related_required_if_equal_validator(
                                    field_name="applicantResidence",
                                    value="za granicą"
                                )
                            ],
                            required=True
                        )
                    ]
                )
            )

        return chapter
