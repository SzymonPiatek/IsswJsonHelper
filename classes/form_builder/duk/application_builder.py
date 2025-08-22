from classes.form_builder.application_builder import ApplicationBuilder


class DUKApplicationBuilder(ApplicationBuilder):
    DEPARTMENT_NAME = 'DUK'

    def __init__(self):
        super().__init__()

        self.department_data_path = self.application_data_path / 'duk'
        self.program_data_path = None
        self.priority_data_path = None

    def create_application_metadata(self):
        part = self.create_part(
            title="Wniosek o dofinansowanie przedsięwzięcia realizowanego w ramach Programów Operacyjnych Polskiego Instytutu Sztuki Filmowej",
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

    def create_application_basic_data(self, data):
        part = self.create_part(
            title="I. Dane podstawowe",
            short_name="I. Dane podstawowe",
            chapters=[
                self.create_chapter(
                    title="1. Nazwa programu operacyjnego / priorytetu",
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Program",
                            name="programNamePartTwo",
                            read_only=True,
                            value=self.operation_name
                        ),
                        self.create_component(
                            component_type="text",
                            label="Priorytet",
                            name="priorityNamePartTwo",
                            read_only=True,
                            value=self.priority_name
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Nazwa przedsięwzięcia, którego dotyczy wniosek",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="applicationTaskName",
                            validators=[
                                self.validator.length_validator(max_value=100)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="3. Rodzaj przedsięwzięcia określony w programie operacyjnym",
                    components=[
                        self.create_component(
                            component_type="radio",
                            name="projectType",
                            value=data['projectType']['options'][0] if len(data['projectType']['options']) == 1 else "",
                            read_only=True if len(data['projectType']['options']) == 1 else False,
                            options=data["projectType"]["options"]
                        )
                    ]
                ),
                self.create_chapter(
                    title="4. Poprzednie edycje przedsięwzięcia",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    label="Czy był składany wniosek na poprzednią edycję tego przedsięwzięcia",
                                    name="previousApplicationForProject",
                                    options=[
                                        "Tak",
                                        "Nie"
                                    ],
                                    validators=[
                                        self.validator.exact_validator(
                                            values=[
                                                "Tak",
                                                "Nie"
                                            ]
                                        )
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="previousApplicationForProject",
                                    values=[
                                        "Tak"
                                    ]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="Proszę podać numer wniosku nadany przez PISF",
                                    name="fiveDigitNumberOfApplication",
                                    required=True,
                                    validators=[
                                        self.validator.related_required_if_equal_validator(
                                            field_name="previousApplicationForProject",
                                            value="Tak"
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        self.save_part(part=part)

    def create_application_applicant_data(self):
        part = self.create_part(
            title="II. Dane wnioskodawcy",
            short_name="II. Dane wnioskodawcy"
        )

        self.create_part_by_sections(
            part=part,
            sections=[
                {
                    "path": self.department_data_path / '_pages' / 'application_applicant_data' / 'applicant_full_name.json',
                    "data": {
                        "number": "1"
                    }
                },
                {
                    "path": self.application_data_path / '_pages' / 'application_applicant_data' / 'eligible_person.json',
                    "data": {
                        "number": "2"
                    }
                },
                {
                    "path": self.application_data_path / '_pages' / 'application_applicant_data' / 'responsible_person.json',
                    "data": {
                        "number": "3"
                    }
                },
                {
                    "path": self.application_data_path / '_pages' / 'application_applicant_data' / 'applicant_main_address.json',
                    "data": {
                        "number": "4",
                        "applicantResidence": {
                            "options": [
                                "w Polsce"
                            ]
                        }
                    }
                },
                {
                    "path": self.application_data_path / '_pages' / 'application_applicant_data' / 'applicant_contact_address.json',
                    "data": {
                        "number": "5",
                        "applicantContactResidence": {
                            "options": [
                                "w Polsce"
                            ]
                        }
                    }
                },
                {
                    "path": self.application_data_path / '_pages' / 'application_applicant_data' / 'applicant_identification_data.json',
                    "data": {
                        "number": "6"
                    }
                },
                {
                    "path": self.application_data_path / '_pages' / 'application_applicant_data' / 'bank_data.json',
                    "data": {
                        "number": "7"
                    }
                },
                {
                    "path": self.application_data_path / '_pages' / 'application_applicant_data' / 'legal_information.json',
                    "data": {
                        "number": "8"
                    }
                },
                {
                    "path": self.application_data_path / '_pages' / 'application_applicant_data' / 'statistical_data.json',
                    "data": {
                        "number": "9"
                    }
                },
            ]
        )

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
            title="IV. Źródła finansowania",
            short_name="IV. Źródła finansowania",
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
                                                    is_multiple_forms=True,
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
                ),
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="headerBudgetWarning",
                            value="Uwaga: W przypadku innych kosztów niż ujętych w wykazie kosztów kwalifikowanych powyżej, PISF może wskazać konkretne pozycje w budżecie przedsięwzięcia, które mogą zostać pokryte z przyznanego dofinansowania."
                        )
                    ]
                )
            ]
        )
        self.save_part(part)

    def create_application_scope_of_project(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'scope_of_the_project.json')
        self.save_part(part)

    def create_application_statements(self):
        part = self.load_json(path=self.department_data_path / '_pages' / 'application_statements.json')
        self.save_part(part)

    def create_application_attachments(self):
        part = self.create_part(
            title="VI. Załączniki",
            short_name="VI. Załączniki"
        )

        attachments_data_path = self.department_data_path / '_pages' / 'application_attachments'

        chapter_01 = self.create_chapter(
            title="Obowiązkowe załączniki"
        )

        part['chapters'] = [
            chapter_01,
            self.load_json(path=attachments_data_path / 'document_confirming_represent_applicant.json'),
            self.load_json(path=attachments_data_path / 'schedule_information.json'),
            self.load_json(path=attachments_data_path / 'other_attachments.json'),
            self.load_json(path=attachments_data_path / 'storage_of_blanks.json'),
        ]
        self.save_part(part)

    def create_application_schedule(self):
        part = self.load_json(path=self.department_data_path / '_pages' / 'application_schedule.json')
        self.save_part(part)

    def create_application_project_costs(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_project_costs.json')
        self.save_part(part=part)

    def generate(self):
        # Base
        self.create_application_base()

        # Metadane wniosku
        self.create_application_metadata()

        # I. Dane podstawowe
        self.create_application_basic_data()

        # II. Dane wnioskodawcy
        self.create_application_applicant_data()

        # III. Zakres przedsięwzięcia
        self.create_application_scope_of_project()

        # IV. Źródła finansowania
        self.create_application_sources_of_financing()

        # V. Oświaczenia
        self.create_application_statements()

        # VI. Załączniki
        self.create_application_attachments()

        # VII. Kosztorys przedsięwzięcia
        self.create_application_project_costs()

        # VIII. Harmonogram
        self.create_application_schedule()

        # Zapis
        self.save_output()
