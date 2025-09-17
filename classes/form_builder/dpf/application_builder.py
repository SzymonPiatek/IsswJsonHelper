from classes.form_builder.additional.decorators import not_implemented_func
from classes.form_builder.application_builder import ApplicationBuilder
from classes.form_builder.components.component.dpf.dpf_component import DPFComponent
from classes.form_builder.components.section.dpf.dpf_section import DPFSection


class DPFApplicationBuilder(ApplicationBuilder):
    DEPARTMENT_NAME = 'DPF'
    OPERATION_NAME = 'I. Produkcja filmowa'
    OPERATION_NUM = "i"

    def __init__(self):
        super().__init__()

        self.department_data_path = self.application_data_path / 'dpf'
        self.priority_data_path = None
        self.section = DPFSection()
        self.component = DPFComponent()

        self.task_type = "Produkcja filmowa"

    def create_application_metadata(self):
        part = self.create_part(
            title="Wniosek o dofinansowanie w ramach Programów Operacyjnych Polskiego Instytutu Sztuki Filmowej",
            short_name="Metadane wniosku",
            chapters=[
                self.create_chapter(
                    title="1. Tryb naboru",
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Nr sesji i rok",
                            name="sessionYear",
                            value=f"Sesja {self.session}/{self.year}",
                            read_only=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Program operacyjny",
                    components=[
                        self.create_component(
                            component_type="text",
                            name="programName",
                            value=self.operation_name,
                            read_only=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="3. Priorytet",
                    components=[
                        self.create_component(
                            component_type="text",
                            name="priorityName",
                            value=self.priority_name,
                            read_only=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="4. Zakres przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="text",
                            name="taskType",
                            value=self.task_type,
                            read_only=True
                        )
                    ]
                )
            ]
        )

        self.save_part(part)

    @not_implemented_func
    def create_application_basic_data(self):
        pass

    def create_application_applicant_data(self):
        part = self.create_part(
            title="II. Dane wnioskodawcy",
            short_name="II. Dane wnioskodawcy",
            chapters=[
                self.section.applicant_name(number="1"),
                self.section.applicant_type(number="2"),
                self.section.eligible_person_data(number="3"),
                self.section.eligible_person_attachments(number="4"),
                self.section.responsible_person_data(number="5"),
                self.section.applicant_address(number="6"),
                self.section.applicant_identification_data(number="7"),
                self.section.applicant_bank_data(number="8"),
                self.section.applicant_legal_information(number="9"),
                self.section.applicant_statistical_data(number="10"),
            ]
        )

        self.save_part(part=part)

    @not_implemented_func
    def create_application_information_data(self):
        pass

    @not_implemented_func
    def create_application_completion_date_data(self):
        pass

    @not_implemented_func
    def create_application_financial_data(self):
        pass

    def create_application_additional_data(self):
        part = self.create_part(
            title="VI. Dane dodatkowe",
            short_name="VI. Dane dodatkowe",
            chapters=[
                self.create_chapter(
                    title="Czy przedsięwzięcie było wcześniej ocenianie w PISF?",
                    components=[
                        self.create_component(
                            component_type="select",
                            name="isProjectRatedInPisf",
                            options=[
                                "Tak",
                                "Nie"
                            ],
                            required=True,
                        )
                    ]
                ),
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="isProjectRatedInPisf",
                            values=["Tak"]
                        )
                    ],
                    components=[
                        self.create_chapter(
                            title="Na etapie",
                            components=[
                                self.create_component(
                                    component_type="checkbox",
                                    label=comp["label"],
                                    name=comp["name"],
                                ) for comp in [
                                    {
                                        "label": "Stypendium scenariuszowe",
                                        "name": "scriptScholarshipStage"
                                    },
                                    {
                                        "label": "Dewelopmentu scenariuszowe",
                                        "name": "scriptDevelopmentStage"
                                    },
                                    {
                                        "label": "Rozwoju projektu",
                                        "name": "projectDevelopmentStage"
                                    },
                                    {
                                        "label": "Produkcji",
                                        "name": "productionStage"
                                    },
                                    {
                                        "label": "W ramach systemu wsparcia finansowego produkcji audiowizualnej tzw. Zachęt",
                                        "name": "financialSupportSystemStage"
                                    },
                                    {
                                        "label": "Inne dotyczące projektu w innym Programie Operacyjnym PISF",
                                        "name": "otherStage"
                                    }
                                ]
                            ]
                        ),
                        # Stypendium sceniurszowe
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="scriptScholarshipStage",
                                    values=[True]
                                )
                            ],
                            components=[
                                self.create_chapter(
                                    title="Na etapie stypendium scenariuszowego",
                                    components=[
                                        self.create_component(
                                            component_type="select",
                                            label="Decyzja Dyrektora",
                                            name="scriptScholarshipDirectorDecision",
                                            options=[
                                                "Pozytywna",
                                                "Negatywna"
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="scriptScholarshipDirectorDecision",
                                            values=["Pozytywna"]
                                        )
                                    ],
                                    components=[
                                        self.create_chapter(
                                            title="Autorzy scenariusza",
                                            multiple_forms_rules={
                                                "minCount": 1,
                                                "maxCount": 20
                                            },
                                            components=[
                                                self.create_chapter(
                                                    class_list=[
                                                        "grid",
                                                        "grid-cols-2"
                                                    ],
                                                    components=[
                                                        self.create_component(
                                                            component_type="text",
                                                            label="Imię",
                                                            name="scriptwriterName"
                                                        ),
                                                        self.create_component(
                                                            component_type="text",
                                                            label="Nazwisko",
                                                            name="scriptwriterSurname"
                                                        ),
                                                        self.create_component(
                                                            component_type="text",
                                                            mask="fund",
                                                            label="Kwota",
                                                            name="scriptwriterPLNAmount",
                                                            unit="PLN"
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Udział procentowy",
                                                            name="scriptwriterPercentage",
                                                            unit="%"
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_chapter(
                                            class_list=[
                                                "grid",
                                                "grid-cols-4"
                                            ],
                                            components=[
                                                self.create_component(
                                                    component_type="number",
                                                    label="Suma udziałów",
                                                    name="scriptwriterTotalShares",
                                                    help_text="Suma udziałów musi być równa 100%.",
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=["scriptwriterPercentage"]
                                                        )
                                                    ],
                                                    validators=[
                                                        self.validator.range_validator(
                                                            min_value=100,
                                                            max_value=100,
                                                            message="Suma udziałów musi być równa 100%."
                                                        )
                                                    ],
                                                    read_only=True,
                                                    required=True,
                                                    class_list=[
                                                        "col-start-1",
                                                        "col-end-2"
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                *self.section.application_additional_data.create_section_with_positive_and_negative_decision(
                                    name="scriptScholarship"
                                )
                            ]
                        ),
                        # Dewelopment scenariuszowy
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="scriptDevelopmentStage",
                                    values=[True]
                                )
                            ],
                            components=[
                                self.create_chapter(
                                    title="Na etapie dewelopmentu scenariuszowego",
                                    components=[
                                        self.create_component(
                                            component_type="select",
                                            label="Decyzja Dyrektora",
                                            name="scriptDevelopmentDirectorDecision",
                                            options=[
                                                "Pozytywna",
                                                "Negatywna"
                                            ]
                                        )
                                    ]
                                ),
                                *self.section.application_additional_data.create_section_with_positive_and_negative_decision(
                                    name="scriptDevelopment"
                                )
                            ]
                        ),
                        # Rozwój projektu
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectDevelopmentStage",
                                    values=[True]
                                )
                            ],
                            components=[
                                self.create_chapter(
                                    title="Na etapie rozwoju projektu",
                                    components=[
                                        self.create_component(
                                            component_type="select",
                                            label="Decyzja Dyrektora",
                                            name="projectDevelopmentDirectorDecision",
                                            options=[
                                                "Pozytywna",
                                                "Negatywna"
                                            ]
                                        )
                                    ]
                                ),
                                *self.section.application_additional_data.create_section_with_positive_and_negative_decision(
                                    name="projectDevelopment"
                                )
                            ]
                        ),
                        # Produkcja
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="productionStage",
                                    values=[True]
                                )
                            ],
                            components=[
                                self.create_chapter(
                                    title="Na etapie rozwoju projektu",
                                    components=[
                                        self.create_component(
                                            component_type="select",
                                            label="Decyzja Dyrektora",
                                            name="productionDirectorDecision",
                                            options=[
                                                "Pozytywna",
                                                "Negatywna"
                                            ]
                                        )
                                    ]
                                ),
                                *self.section.application_additional_data.create_section_with_positive_and_negative_decision(
                                    name="production"
                                )
                            ]
                        ),
                        # Zachęty
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="financialSupportSystemStage",
                                    values=[True]
                                )
                            ],
                            components=[
                                self.create_chapter(
                                    title="W ramach systemu wsparcia finansowego produkcji audiowizualnej tzw. Zachęt",
                                    components=[
                                        self.create_component(
                                            component_type="select",
                                            label="Czy projekt otrzymał wsparcie finansowe?",
                                            name="projectReceiveFinancialSupportStage",
                                            options=[
                                                "Tak",
                                                "Nie"
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="Projekt posiada",
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="projectReceiveFinancialSupportStage",
                                            values=["Tak"]
                                        )
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="checkbox",
                                            label="podpisaną umowę",
                                            name="projectSignedContract"
                                        ),
                                        self.create_component(
                                            component_type="checkbox",
                                            label="wniosek z decyzją pozytywną",
                                            name="projectPositiveDecision"
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="Umowa",
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="projectSignedContract",
                                            values=[True]
                                        )
                                    ],
                                    class_list=[
                                        "grid",
                                        "grid-cols-3"
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            label="Numer umowy",
                                            name="contractNumber"
                                        ),
                                        self.create_component(
                                            component_type="date",
                                            label="Data zawarcia umowy",
                                            name="contractConclusionDate"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Przyznana kwota wsparcia",
                                            name="contactSupportAmount"
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="Wniosek",
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="projectPositiveDecision",
                                            values=[True]
                                        )
                                    ],
                                    class_list=[
                                        "grid",
                                        "grid-cols-3"
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            label="Numer wniosku",
                                            name="applicationNumber"
                                        ),
                                        self.create_component(
                                            component_type="date",
                                            label="Data wydania decyzji",
                                            name="applicationDecisionDate",
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Przyznana kwota wsparcia",
                                            name="applicationSupportAmount"
                                        )
                                    ]
                                )
                            ]
                        ),
                        # Inne
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="otherStage",
                                    values=[True]
                                )
                            ],
                            components=[
                                self.create_chapter(
                                    title="Inne dotyczące projektu w innym Programie Operacyjnym PISF",
                                    components=[
                                        self.create_component(
                                            component_type="select",
                                            label="Decyzja Dyrektora",
                                            name="otherDirectorDecision",
                                            options=[
                                                "Pozytywna",
                                                "Negatywna"
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="otherDirectorDecision",
                                            values=["Pozytywna"]
                                        )
                                    ],
                                    class_list=[
                                        "grid",
                                        "grid-cols-2"
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            label="Nazwa Programu Operacyjnego",
                                            name="otherOperationalProgramName"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Nazwa priorytetu",
                                            name="otherPriorityName"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Tytuł projektu",
                                            name="otherPriorityTitle"
                                        ),
                                        self.create_component(
                                            component_type="date",
                                            label="Data decyzji",
                                            name="otherDecisionDate",
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Kwota dotacji w PLN",
                                            name="otherSubsidyAmount",
                                            unit="PLN"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Numer umowy (jeśli dotyczy)",
                                            name="otherContractNumber"
                                        ),
                                        self.create_component(
                                            component_type="textarea",
                                            label="Uwagi",
                                            name="otherComments",
                                            class_list=[
                                                "col-span-2"
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Wykaz wniosków podmiotu w PISF",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_chapter(
                                    title=chapter["title"],
                                    components=[
                                        self.create_chapter(
                                            components=[
                                                self.create_component(
                                                    component_type="checkbox",
                                                    label="Nie dotyczy",
                                                    name=f"notApplicable{chapter["name"]}"
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name=f"notApplicable{chapter["name"]}",
                                            values=[False]
                                        )
                                    ],
                                    multiple_forms_rules={
                                        "minCount": 1,
                                        "maxCount": 30
                                    },
                                    components=[
                                        self.create_chapter(
                                            class_list=[
                                                "grid",
                                                "grid-cols-3"
                                            ],
                                            components=[
                                                self.create_component(
                                                    component_type="select",
                                                    label="Priorytet",
                                                    name=f"entityApplicationsListPriority{chapter["name"]}",
                                                    options=[
                                                        "rozwój projektu animowanego",
                                                        "rozwój projektu fabularnego",
                                                        "rozwój projektu dokumentalnego",
                                                        "development scenariuszowy filmu animowanego",
                                                        "development scenariuszowy filmu fabularnego",
                                                        "development scenariuszowy filmu dokumentalnego",
                                                        "produkcja filmu animowanego",
                                                        "produkcja filmu fabularnego",
                                                        "produkcja filmu dokumentalnego"
                                                    ],
                                                    required=True,
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    label="Reżyser",
                                                    name=f"entityApplicationsListDirector{chapter["name"]}",
                                                    validators=[
                                                        self.validator.length_validator(
                                                            max_value=100
                                                        )
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    label="Tytuł",
                                                    name=f"entityApplicationsListTitle{chapter["name"]}",
                                                    validators=[
                                                        self.validator.length_validator(
                                                            max_value=100
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ) for chapter in [
                            {
                                "title": "Wnioski składane do PO Produkcja filmowa w bieżącej sesji",
                                "name": "CurrentSession"
                            },
                            {
                                "title": "Wykaz aktualnych promes (filmy przed umową z PISF)",
                                "name": "CurrentPromises"
                            },
                            {
                                "title": "Wykaz filmów w produkcji z umową na dofinansowanie PISF",
                                "name": "CurrentProductionContracts"
                            },
                            {
                                "title": "Projekty w realizacji z dofinansowaniem PISF w zakresie rozwoju projektu",
                                "name": "CurrentProjectDevelopment"
                            },
                            {
                                "title": "Wnioski dotyczące rozwoju projektu z poprzednich sesji, oczekujące na decyzję Dyrektora PISF",
                                "name": "PreviousProjectDevelopment"
                            },
                            {
                                "title": "Wnioski dotyczące produkcji filmowej z poprzednich sesji, oczekujące na decyzję Dyrektora PISF",
                                "name": "PreviousSessionProduction"
                            }
                        ]
                    ]
                )
            ]
        )

        self.save_part(part=part)

    @not_implemented_func
    def create_application_attachments(self):
        pass

    def create_application_statements(self):
        part = self.create_part(
            title="VIII. Oświadczenia",
            short_name="VIII. Oświadczenia",
            chapters=[
                self.section.application_statements.applicant_statements(),
                self.section.application_statements.producer_statements(),
                self.section.application_statements.script_statements(),
                self.section.application_statements.storage_of_blank_public_documents()
            ]
        )

        self.save_part(part)

    def generate(self):
        self.create_application_base()

        # Metadane wniosku
        self.create_application_metadata()

        # I. Dane podstawowe
        self.create_application_basic_data()

        # II. Dane wnioskodawcy
        self.create_application_applicant_data()

        # III. Informacje
        self.create_application_information_data()

        # IV. Termin realizacji
        self.create_application_completion_date_data()

        # V. Dane finansowe
        self.create_application_financial_data()

        # VI. Dane dodatkowe
        self.create_application_additional_data()

        # VII. Załączniki
        self.create_application_attachments()

        # VIII. Oświadczenia
        self.create_application_statements()

        self.save_output()
