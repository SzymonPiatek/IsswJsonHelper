from classes.form_components.section.section import Section


class ApplicationApplicantData(Section):
    def __init__(self):
        super().__init__()

    def pisf_transfer_currency(self, number: str):
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

    def identification_numbers(self, number: str):
        return self.create_chapter(
            title=f"{number}. Numery identyfikacyjne",
            components=[
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
                            label="Numer PESEL",
                            name="applicantPesel",
                            required=True,
                            validators=[
                                self.validator.pesel_validator()
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Właściwy urząd skarbowy",
                            name="applicantTaxOffice",
                            required=True
                        )
                    ]
                ),
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
                            label="Numer PESEL",
                            name="applicantForeignPesel",
                            required=True,
                            validators=[
                                self.validator.pesel_validator()
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Właściwy urząd skarbowy",
                            name="applicantForeignTaxOffice",
                            required=True
                        )
                    ]
                )
            ]
        )
