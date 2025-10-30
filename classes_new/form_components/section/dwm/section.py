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
