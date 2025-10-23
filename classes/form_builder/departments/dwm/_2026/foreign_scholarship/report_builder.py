from ..report_builder import DWMReportBuilder2026
from ..priority import ForeignScholarshipPriority


class ForeignScholarshipReportBuilder(DWMReportBuilder2026, ForeignScholarshipPriority):
    FORM_ID = 63

    def __init__(self):
        super().__init__()

        self.intro_text = [
            "Raport końcowy",
            "<small>z wykonania przedsięwzięcia realizowanego w ramach Programu Operacyjnego \"Promocja polskiej twórczości filmowej za granicą\"</small> <br> Priorytet II \"Stypendia Zagraniczne\""
        ]

    def create_report_basic_data(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Dane podstawowe",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="instruction",
                            value="<h4 style='color: red';>UWAGA!</h4>Przed wypełnieniem raportu bardzo prosimy o zapoznanie się z <a target='_blank' rel='noopener noreferrer' href='https://isswstorage.blob.core.windows.net/django-files/instrukcja_POVPR2-raport.pdf.pdf' style='font-weight: bold; text-decoration: underline;'>INSTRUKCJĄ</a>",
                            read_only=True,
                            class_list=[
                                "displayNoneFrontend"
                            ]
                        )
                    ]
                ),
                self.section.report_basic_data.project_implementation_period(number="A"),
                self.section.report_basic_data.agreement_and_annex(number="B"),
                self.create_chapter(
                    title=f"C. Nazwa i adres Stypendysty",
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
                            value="Nazwa Stypendysty",
                            class_list=[
                                "displayNoneFrontend"
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Nazwa Stypendysty",
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
                            value="Adres Stypendysty",
                            class_list=[
                                "displayNoneFrontend"
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Adres Stypendysty",
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
                            ]
                        )
                    ]
                )
            ]
        )

        self.save_part(part)

    def create_report_expenditure_exacution(self, number: int):
        cost_types = [
            {
                "name": "accreditation",
                "label": "Koszty akredytacji"
            },
            {
                "name": "accommodation",
                "label": "Koszty noclegu"
            },
            {
                "name": "transportation",
                "label": "Koszty transportu"
            },
            {
                "name": "participation",
                "label": "Koszty uczestnictwa w warsztatach (jeśli dotyczy)"
            }
        ]

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
                            required=True,
                            options=[
                                "Wnioskodawca jest osobą fizyczną, dlatego kwoty zamieszczone w kosztorysie wniosku to KWOTY BRUTTO"
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
                                *[self.create_chapter(
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
                                        self.create_component(
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
                                        ),
                                        self.create_component(
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
                                        ),
                                        self.create_component(
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
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Bieżący okres sprawozdawczy: koszt całkowity",
                                            name=f"{cost["name"]}CostActualTotal",
                                            unit="PLN",
                                            class_list=[
                                                "no-label"
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Bieżący okres sprawozdawczy: w tym dofinansowanie z PISF",
                                            name=f"{cost["name"]}CostActualSupportPisf",
                                            unit="PLN",
                                            class_list=[
                                                "no-label"
                                            ]
                                        ),
                                    ]
                                ) for cost in cost_types],
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
                                                    fields=[f"{cost["name"]}CostTotal" for cost in cost_types]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[f"{cost["name"]}CostTotal" for cost in cost_types]
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
                                                    fields=[f"{cost["name"]}CostRequestPisf" for cost in cost_types]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[f"{cost["name"]}CostRequestPisf" for cost in cost_types]
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
                        self.section.report_expenditure_exacution.cost_estimate_by_source_of_financing_foreign_scholarship()
                    ]
                ),
                self.section.report_expenditure_exacution.list_of_bills_and_invoices_foreign_scholarship()
            ]
        )

        self.save_part(part)
