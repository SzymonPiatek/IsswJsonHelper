from classes.form_builder.departments.duk.application_builder import DUKApplicationBuilder


class DUKApplicationBuilder2026(DUKApplicationBuilder):
    YEAR = 2026

    def __init__(self):
        super().__init__()

    def create_application_metadata(self):
        part = self.create_part(
            title="Wniosek o dofinansowanie przedsięwzięcia realizowanego w ramach Programów Operacyjnych Polskiego Instytutu Sztuki Filmowej",
            short_name="I. Metadane wniosku",
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
                            label="Program",
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
                            label="Priorytet",
                            name="priorytetName",
                            value=self.priority_name,
                            read_only=True
                        )
                    ]
                )
            ]
        )
        self.save_part(part=part)

    def create_application_applicant_data(self):
        part = self.create_part(
            title="III. Dane wnioskodawcy",
            short_name="III. Dane wnioskodawcy",
            chapters=[
                self.section.applicant_name(number="1"),
                self.section.eligible_person_data(number="2"),
                self.section.responsible_person_data(number="3"),
                self.section.applicant_address(number="4", main_poland=True, main_foreign=True, contact_poland=True, contact_foreign=True),
                self.section.applicant_identification_data(number="5"),
                self.section.applicant_bank_data(number="6"),
                self.section.applicant_legal_information(number="7"),
                self.section.applicant_statistical_data(number="8"),
            ]
        )

        self.save_part(part=part)

    def create_application_sources_of_financing(self):
        sources_of_financing_chapters = {
            "a": [
                {
                    "section_title": "<normal>- wkład finansowy</normal>",
                    "name": "ownFinancial"
                },
                {
                    "section_title": "<normal>- wkład rzeczowy</normal>",
                    "name": "ownInKind"
                }
            ],
            "c": [
                {
                    "checkbox_title": "Czy występują środki z budżetów jednostek samorządu terytorialnego lub innych środków publicznych za wyjątkiem MKiDN?",
                    "checkbox_name": "isLocalGovernmentFunding",
                    "section_title": "<normal>c) z budżetów jednostek samorządu terytorialnego lub innych środków publicznych za wyjątkiem MKiDN </normal><br /><small>Uwaga! <normal>Odznaczenie powyższego checkboxa nie prowadzi do automatycznego usunięcia zawartych w tej sekcji informacji. Dane te nadal będą brane pod uwagę w obliczeniach finansowych i będą uwzględnione we wniosku. Jeżeli dane te nie są już potrzebne, prosimy o ich ręczne usunięcie. </small></normal>",
                    "section_name": "localGovernments",
                },
                {
                    "checkbox_title": "Czy występują środki MKiDN w ramach Programów Ministra?",
                    "checkbox_name": "isMinistryFunding",
                    "section_title": "<normal>d) ze środków MKiDN w ramach Programów Ministra </normal><br /><small>Uwaga! <normal>Odznaczenie powyższego checkboxa nie prowadzi do automatycznego usunięcia zawartych w tej sekcji informacji. Dane te nadal będą brane pod uwagę w obliczeniach finansowych i będą uwzględnione we wniosku. Jeżeli dane te nie są już potrzebne, prosimy o ich ręczne usunięcie. </small></normal>",
                    "section_name": "ministry",
                },
                {
                    "checkbox_title": "Czy występują środki od sponsorów lub innych podmiotów niezaliczanych do sektora finansów publicznych?",
                    "checkbox_name": "isOtherSponsorFunding",
                    "section_title": "<normal>e) od sponsorów lub innych podmiotów niezaliczanych do sektora finansów publicznych </normal><br /><small>Uwaga! <normal>Odznaczenie powyższego checkboxa nie prowadzi do automatycznego usunięcia zawartych w tej sekcji informacji. Dane te nadal będą brane pod uwagę w obliczeniach finansowych i będą uwzględnione we wniosku. Jeżeli dane te nie są już potrzebne, prosimy o ich ręczne usunięcie. </small></normal>",
                    "section_name": "otherSponsors",
                },
                {
                    "checkbox_title": "Czy występują środki zagraniczne, w tym europejskie?",
                    "checkbox_name": "isForeignFunding",
                    "section_title": "<normal>f) ze środków zagranicznych, w tym europejskich </normal><br /><small>Uwaga! <normal>Odznaczenie powyższego checkboxa nie prowadzi do automatycznego usunięcia zawartych w tej sekcji informacji. Dane te nadal będą brane pod uwagę w obliczeniach finansowych i będą uwzględnione we wniosku. Jeżeli dane te nie są już potrzebne, prosimy o ich ręczne usunięcie. </small></normal>",
                    "section_name": "foreign",
                }
            ]
        }

        part = self.create_part(
            title="V. Źródła finansowania",
            short_name="V. Źródła finansowania",
            chapters=[
                self.create_chapter(
                    title="1. Całkowity przewidywany koszt realizacji przedsięwzięcia",
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
                            mask="fund",
                            label="Kwota kosztu całkowitego",
                            name="totalProjectCost",
                            calculation_rules=[
                                self.calculation_rule.sum_inputs(
                                    fields=[
                                        "ownFundsSumAmount",
                                        "pisfSupportAmount",
                                        "localGovernmentsFundsSumAmount",
                                        "ministryFundsSumAmount",
                                        "otherSponsorsFundsSumAmount",
                                        "foreignFundsSumAmount"
                                    ]
                                )
                            ],
                            validators=[
                                self.validator.related_sum_validator(
                                    field_names=[
                                        "ownFundsSumAmount",
                                        "pisfSupportAmount",
                                        "localGovernmentsFundsSumAmount",
                                        "ministryFundsSumAmount",
                                        "otherSponsorsFundsSumAmount",
                                        "foreignFundsSumAmount"
                                    ]
                                )
                            ],
                            read_only=True,
                            unit="PLN"
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="Finansowanie ze źródeł publicznych razem",
                            name="publicSupportAltogether",
                            calculation_rules=[
                                self.calculation_rule.sum_inputs(
                                    fields=[
                                        "pisfSupportAmount",
                                        "localGovernmentsFundsSumAmount",
                                        "ministryFundsSumAmount"
                                    ]
                                )
                            ],
                            validators=[
                                self.validator.related_sum_validator(
                                    field_names=[
                                        "pisfSupportAmount",
                                        "localGovernmentsFundsSumAmount",
                                        "ministryFundsSumAmount"
                                    ]
                                ),
                                self.validator.related_fraction_gte_validator(
                                    field_name="totalProjectCost",
                                    ratio=0.9,
                                    message="Suma środków publicznych nie może przekroczyć 90% kosztu realizacji przedsięwzięcia."
                                )
                            ],
                            read_only=True,
                            unit="PLN"
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Wyszczególnienie źródeł finansowania",
                    components=[
                        self.create_chapter(
                            title="<normal>a) środki własne z podziałem na: wkład finansowy (np.: wpływy z biletów, ze sprzedaży publikacji, akredytacji, opłat uczestników itp.) i ewentualnie wyceniony wkład rzeczowy </normal>",
                            components=[
                                *[self.create_chapter(
                                    title=chapter["section_title"],
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
                                            mask="fund",
                                            label="Kwota",
                                            name=f"{chapter["name"]}FundsAmount",
                                            required=True,
                                            unit="PLN"
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Udział w koszcie całkowitym",
                                            name=f"{chapter["name"]}FundsShare",
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field=f"{chapter["name"]}FundsAmount",
                                                    divisor_field="totalProjectCost"
                                                )
                                            ],
                                            read_only=True,
                                            validators=[
                                                self.validator.related_share_validator(
                                                    dividend=f"{chapter["name"]}FundsAmount",
                                                    divisor="totalProjectCost"
                                                )
                                            ],
                                            required=True,
                                            mask="share",
                                            unit="%"
                                        )
                                    ]
                                ) for chapter in sources_of_financing_chapters["a"]],
                                self.create_chapter(
                                    title="<normal>Suma środków własnych</normal>",
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
                                            mask="fund",
                                            label="Kwota",
                                            name="ownFundsSumAmount",
                                            calculation_rules=[
                                                self.calculation_rule.sum_inputs(
                                                    fields=[
                                                        f"{chapter["name"]}FundsAmount" for chapter in sources_of_financing_chapters["a"]
                                                    ]
                                                )
                                            ],
                                            read_only=True,
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        f"{chapter["name"]}FundsAmount" for chapter in sources_of_financing_chapters["a"]
                                                    ]
                                                )
                                            ],
                                            unit="PLN"
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="<normal>b) ze środków PISF </normal>",
                            components=[
                                self.create_chapter(
                                    title="<normal>- dotacja PISF </normal>",
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
                                            mask="fund",
                                            label="Kwota",
                                            name="pisfSupportAmount",
                                            validators=[
                                                self.validator.related_fraction_gte_validator(
                                                    field_name="totalProjectCost",
                                                    ratio=0.9,
                                                    message="Dotacja PISF nie może przekroczyć 90% kosztu realizacji przedsięwzięcia."
                                                )
                                            ],
                                            required=True,
                                            unit="PLN"
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Udział w koszcie całkowitym",
                                            name="pisfSupportShare",
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field="pisfSupportAmount",
                                                    divisor_field="totalProjectCost"
                                                )
                                            ],
                                            read_only=True,
                                            validators=[
                                                self.validator.related_share_validator(
                                                    dividend="pisfSupportAmount",
                                                    divisor="totalProjectCost"
                                                )
                                            ],
                                            required=True,
                                            mask="share",
                                            unit="%"
                                        )
                                    ]
                                )
                            ]
                        ),
                        *[self.create_chapter(
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="checkbox",
                                            label=chapter["checkbox_title"],
                                            name=chapter["checkbox_name"]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name=chapter["checkbox_name"],
                                            values=[
                                                True
                                            ]
                                        )
                                    ],
                                    components=[
                                        self.create_chapter(
                                            title=chapter["section_title"],
                                            components=[
                                                self.create_chapter(
                                                    multiple_forms_rules={
                                                        "minCount": 1,
                                                        "maxCount": 20
                                                    },
                                                    components=[
                                                        self.create_chapter(
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
                                                                    label="Nazwa podmiotu finansującego",
                                                                    name=f"{chapter["section_name"]}Name",
                                                                    class_list=[
                                                                        "table-full"
                                                                    ],
                                                                    required=True,
                                                                    validators=[
                                                                        self.validator.related_required_if_equal_validator(
                                                                            field_name=chapter["checkbox_name"],
                                                                            value=True
                                                                        )
                                                                    ]
                                                                ),
                                                                self.create_component(
                                                                    component_type="text",
                                                                    mask="fund",
                                                                    label="Kwota",
                                                                    name=f"{chapter["section_name"]}FundingAmount",
                                                                    required=True,
                                                                    unit="PLN",
                                                                    validators=[
                                                                        self.validator.related_required_if_equal_validator(
                                                                            field_name=chapter["checkbox_name"],
                                                                            value=True
                                                                        )
                                                                    ]
                                                                ),
                                                                self.create_component(
                                                                    component_type="number",
                                                                    label="Udział w koszcie całkowitym",
                                                                    name=f"{chapter["section_name"]}FundingShare",
                                                                    calculation_rules=[
                                                                        self.calculation_rule.single_position_share_calculator(
                                                                            dividend_field=f"{chapter["section_name"]}FundingAmount",
                                                                            divisor_field="totalProjectCost"
                                                                        )
                                                                    ],
                                                                    read_only=True,
                                                                    required=True,
                                                                    unit="%",
                                                                    mask="share",
                                                                    validators=[
                                                                        self.validator.related_required_if_equal_validator(
                                                                            field_name=chapter["checkbox_name"],
                                                                            value=True
                                                                        )
                                                                    ]
                                                                )
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                self.create_chapter(
                                                    title="<normal>Łącznie</normal>",
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
                                                            mask="fund",
                                                            label="Kwota",
                                                            name=f"{chapter["section_name"]}FundsSumAmount",
                                                            calculation_rules=[
                                                                self.calculation_rule.dynamic_sum_inputs(
                                                                    fields=[
                                                                        f"{chapter["section_name"]}FundingAmount"
                                                                    ]
                                                                )
                                                            ],
                                                            read_only=True,
                                                            required=True,
                                                            unit="PLN"
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            label="Udział w koszcie całkowitym",
                                                            name=f"{chapter["section_name"]}FundsShare",
                                                            calculation_rules=[
                                                                self.calculation_rule.single_position_share_calculator(
                                                                    dividend_field=f"{chapter["section_name"]}FundsSumAmount",
                                                                    divisor_field="totalProjectCost"
                                                                )
                                                            ],
                                                            read_only=True,
                                                            required=True,
                                                            mask="share",
                                                            unit="%"
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ) for chapter in sources_of_financing_chapters["c"]]
                    ]
                )
            ]
        )
        self.save_part(part)
