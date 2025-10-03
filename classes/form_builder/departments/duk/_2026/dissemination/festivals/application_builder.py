from classes.form_builder.departments.duk._2026.dissemination.application_builder import DisseminationApplicationBuilder
from classes.form_builder.departments.duk._2026.dissemination.priority import FestivalsPriority
from classes.form_builder.departments.duk._2026.application_estimate_builder import DUKApplicationEstimateBuilder
from .estimate_data import estimate_sections
from classes.helpers import int_to_roman


class FestivalsApplicationBuilder(DisseminationApplicationBuilder, FestivalsPriority):
    FORM_ID = 9184

    def __init__(self):
        super().__init__()

        self.project_type = [
            "Organizacja festiwali filmowych o charakterze ogólnopolskim lub międzynarodowym, będących wydarzeniami cyklicznymi, obejmujących szeroki program filmowy, sekcje konkursowe oceniane przez jury oraz wydarzenia towarzyszące, takie jak spotkania z twórcami, panele dyskusyjne czy warsztaty."
        ]

        estimate_builder = DUKApplicationEstimateBuilder(estimate_sections=estimate_sections)
        self.estimate_chapters = [
            estimate_builder.generate_estimate()
        ]

        self.parts = [
            self.create_application_metadata,
            self.create_application_basic_data,
            self.create_application_applicant_data,
            self.create_application_scope_of_project,
            self.create_application_basic_number_data,
            self.create_application_sources_of_financing,
            self.create_application_statements,
            self.create_application_attachments,
            self.create_application_project_costs,
            self.create_application_schedule
        ]

    def create_application_scope_of_project(self, number: int):
        part = self.create_part(
            title=f"{int_to_roman(number)}. Zakres i charakterystyka przedsięwzięcia",
            short_name=f"{int_to_roman(number)}. Zakres przedsięwzięcia",
            chapters=[
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
                            component_type="date",
                            label="Termin od (otwarcie festiwalu)",
                            name="projectOpeningDatePointOne",
                            validators=[
                                self.validator.related_date_lte_validator(
                                    field_name="projectClosingDatePointOne",
                                    message="Data otwarcia festiwalu nie może być późniejsza niż data zamknięcia festiwalu."
                                )
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="date",
                            label="Termin do (zamknięcie festiwalu)",
                            name="projectClosingDatePointOne",
                            validators=[
                                self.validator.related_date_gte_validator(
                                    field_name="projectOpeningDatePointOne",
                                    message="Data zamknięcia festiwalu nie może być wcześniejszy niż data otwarcia festiwalu."
                                )
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            label="Miejscowość",
                            name="projectCity",
                            validators=[
                                self.validator.length_validator(max_value=100)
                            ],
                            required=True,
                            class_list=[
                                "table-full"
                            ]
                        ),
                        self.create_component(
                            component_type="text",
                            label="Miejsce realizacji projekcji i wydarzeń",
                            name="projectPlacesObjects",
                            validators=[
                                self.validator.length_validator(max_value=100)
                            ],
                            required=True,
                            class_list=[
                                "table-full"
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Cele strategiczne festiwalu",
                            name="strategicFestivalGoals",
                            validators=[
                                self.validator.length_validator(max_value=500)
                            ],
                            required=True,
                            class_list=[
                                "table-full"
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Profil artystyczny festiwalu",
                            name="artisticFestivalProfile",
                            validators=[
                                self.validator.length_validator(max_value=500)
                            ],
                            required=True,
                            class_list=[
                                "table-full"
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Program festiwalu",
                            name="festivalProgram",
                            validators=[
                                self.validator.length_validator(max_value=5000)
                            ],
                            required=True,
                            help_text="Repertuar, konkursy, sekcje, jury",
                            class_list=[
                                "table-full"
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            name="prizesAwarded",
                            label="Przyznane nagrody",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True,
                            class_list=[
                                "table-full"
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Wydarzenia towarzyszące",
                            name="accompanyingEvents",
                            validators=[
                                self.validator.length_validator(max_value=5000)
                            ],
                            required=True,
                            help_text="Np. spotkania z twórcami, warsztaty, retrospektywy, prelekcje",
                            class_list=[
                                "table-full"
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Doświadczenie wnioskodawcy i kompetencje zespołu",
                            name="applicantExperienceAndTeamCompetences",
                            validators=[
                                self.validator.length_validator(max_value=500)
                            ],
                            required=True,
                            class_list=[
                                "table-full"
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Promocja festiwalu",
                            name="festivalPromotion",
                            validators=[
                                self.validator.length_validator(max_value=500)
                            ],
                            required=True,
                            help_text="Plan promocji, działania marketingowe, współprace, partnerzy i patroni medialni",
                            class_list=[
                                "table-full"
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Dostępność wydarzenia",
                            name="eventAccessibility",
                            validators=[
                                self.validator.length_validator(max_value=500)
                            ],
                            required=True,
                            help_text="Działania podejmowane na rzecz osób ze szczególnymi potrzebami oraz wspieranie inkluzywności",
                            class_list=[
                                "table-full"
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Profil publiczności",
                            name="audienceProfile",
                            validators=[
                                self.validator.length_validator(max_value=500)
                            ],
                            required=True,
                            class_list=[
                                "table-full"
                            ]
                        ),
                        self.create_component(
                            component_type="radio",
                            label="Udział w przedsięwzięciach jest",
                            name="participationInVentureIs",
                            options=[
                                "bezpłatny",
                                "w większości bezpłatny",
                                "w większości płatny",
                                "płatny"
                            ],
                            required=True,
                            class_list=[
                                "table-full"
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Planowane efekty realizacji przedsięwzięcia",
                            name="plannedEffects",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True,
                            class_list=[
                                "table-full"
                            ]
                        )
                    ]
                )
            ]
        )

        self.save_part(part)

    def create_application_basic_number_data(self, number: int):
        part = self.create_part(
            title=f"{int_to_roman(number)}. Podstawowe dane liczbowe i wskaźniki",
            short_name=f"{int_to_roman(number)}. Dane liczbowe",
            chapters=[
                self.create_chapter(
                    title="Podstawowe dane liczbowe i wskaźniki",
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
                            component_type="number",
                            label="Filmy polskie i koprodukcje",
                            name="polishFilmsAndCoproductions"
                        ),
                        self.create_component(
                            component_type="number",
                            label="Filmy zagraniczne",
                            name="foreignFilms"
                        ),
                        self.create_component(
                            component_type="number",
                            label="Filmy z audiodeskrypcją",
                            name="audioDescriptionFilms",
                            class_list=[
                                "table-full"
                            ]
                        ),
                        self.create_component(
                            component_type="number",
                            label="Ogólna liczba seansów",
                            name="screeningNumberTotal"
                        ),
                        self.create_component(
                            component_type="number",
                            label="Liczba premier",
                            name="premieresNumber"
                        ),
                        self.create_component(
                            component_type="number",
                            label="Akredytacje płatne",
                            name="paidAccreditations"
                        ),
                        self.create_component(
                            component_type="number",
                            label="Akredytacje bezpłatne",
                            name="freeAccreditations"
                        ),
                        self.create_component(
                            component_type="number",
                            label="Liczba biletów",
                            name="ticketsNumber"
                        ),
                        self.create_component(
                            component_type="number",
                            label="Szacowana liczba widzów",
                            name="viewersEstimatedNumber"
                        ),
                    ]
                )
            ]
        )

        self.save_part(part)

    def create_application_sources_of_financing(self, number: int):
        sources_of_financing_chapters = {
            "c": [
                {
                    "checkbox_title": "Czy występują środki z budżetów jednostek samorządu terytorialnego lub innych środków publicznych za wyjątkiem MKiDN?",
                    "checkbox_name": "isLocalGovernmentFunding",
                    "section_title": "<normal>a) z budżetów jednostek samorządu terytorialnego lub innych środków publicznych za wyjątkiem MKiDN </normal><br /><small>Uwaga! <normal>Odznaczenie powyższego checkboxa nie prowadzi do automatycznego usunięcia zawartych w tej sekcji informacji. Dane te nadal będą brane pod uwagę w obliczeniach finansowych i będą uwzględnione we wniosku. Jeżeli dane te nie są już potrzebne, prosimy o ich ręczne usunięcie. </small></normal>",
                    "section_name": "localGovernments",
                },
                {
                    "checkbox_title": "Czy występują środki MKiDN w ramach Programów Ministra?",
                    "checkbox_name": "isMinistryFunding",
                    "section_title": "<normal>b) ze środków MKiDN w ramach Programów Ministra </normal><br /><small>Uwaga! <normal>Odznaczenie powyższego checkboxa nie prowadzi do automatycznego usunięcia zawartych w tej sekcji informacji. Dane te nadal będą brane pod uwagę w obliczeniach finansowych i będą uwzględnione we wniosku. Jeżeli dane te nie są już potrzebne, prosimy o ich ręczne usunięcie. </small></normal>",
                    "section_name": "ministry",
                },
                {
                    "checkbox_title": "Czy występują środki od sponsorów lub innych podmiotów niezaliczanych do sektora finansów publicznych?",
                    "checkbox_name": "isOtherSponsorFunding",
                    "section_title": "<normal>c) od sponsorów lub innych podmiotów niezaliczanych do sektora finansów publicznych </normal><br /><small>Uwaga! <normal>Odznaczenie powyższego checkboxa nie prowadzi do automatycznego usunięcia zawartych w tej sekcji informacji. Dane te nadal będą brane pod uwagę w obliczeniach finansowych i będą uwzględnione we wniosku. Jeżeli dane te nie są już potrzebne, prosimy o ich ręczne usunięcie. </small></normal>",
                    "section_name": "otherSponsors",
                },
                {
                    "checkbox_title": "Czy występują środki zagraniczne, w tym europejskie?",
                    "checkbox_name": "isForeignFunding",
                    "section_title": "<normal>d) ze środków zagranicznych, w tym europejskich </normal><br /><small>Uwaga! <normal>Odznaczenie powyższego checkboxa nie prowadzi do automatycznego usunięcia zawartych w tej sekcji informacji. Dane te nadal będą brane pod uwagę w obliczeniach finansowych i będą uwzględnione we wniosku. Jeżeli dane te nie są już potrzebne, prosimy o ich ręczne usunięcie. </small></normal>",
                    "section_name": "foreign",
                }
            ]
        }

        part = self.create_part(
            title=f"{int_to_roman(number)}. Źródła finansowania",
            short_name=f"{int_to_roman(number)}. Źródła finansowania",
            chapters=[
                self.create_chapter(
                    title="1. Podstawowe dane finansowe",
                    class_list={
                        "main": [
                            "table-1-3-narrow",
                            "grid",
                            "grid-cols-3"
                        ],
                        "sub": [
                            "table-1-3__col"
                        ]
                    },
                    components=[
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="Kwota całkowita",
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
                            label="Wnioskowana dotacja z PISF",
                            name="pisfSupportAmounRepeat",
                            calculation_rules=[
                                self.calculation_rule.copy_value(
                                    from_name="pisfSupportAmountInput"
                                )
                            ],
                            validators=[
                                self.validator.related_sum_validator(
                                    field_names=[
                                        "pisfSupportAmountInput",
                                    ]
                                )
                            ],
                            read_only=True,
                            unit="PLN"
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            label="Środki publiczne razem",
                            name="publicSupportAltogether",
                            read_only=True,
                            unit="PLN"
                        )
                    ]
                ),
                self.create_chapter(
                    components=[
                        self.create_chapter(
                            title="2. Wyszczególnienie źródeł finansowaniania",
                            components=[
                                self.create_chapter(
                                    title="<normal>1) Wkład własny</normal><br/><normal><small>Minimum 10% budżetu przedsięwzięcia. Wkład rzeczowy nie może być wyższy niż 50% całkowitego wkładu własnego.</small></normal>",
                                    class_list=[
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>1) Wkład własny</normal>",
                                    components=[
                                        self.create_chapter(
                                            title="<small>a) Wkład finansowy</small>",
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
                                                    name="ownFinancialFundsAmount",
                                                    label="Kwota",
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    mask="share",
                                                    name="ownFinancialFundsShare",
                                                    label="Udział w koszcie całkowitym",
                                                    calculation_rules=[
                                                        self.calculation_rule.share_calculator(
                                                            dividend_field="ownFinancialFundsAmount",
                                                            divisor_field="totalProjectCost"
                                                        )
                                                    ],
                                                    validators=[
                                                        self.validator.related_share_validator(
                                                            dividend="ownFinancialFundsAmount",
                                                            divisor="totalProjectCost"
                                                        )
                                                    ],
                                                    required=True,
                                                    read_only=True,
                                                    unit="%"
                                                )
                                            ]
                                        ),
                                        self.create_chapter(
                                            components=[
                                                self.create_component(
                                                    component_type="checkbox",
                                                    label="Należy zaznaczyć, jeśli częścią wkładu finansowego są wpływy z biletów, akredytacji itp.",
                                                    name="isTicketRevenues"
                                                )
                                            ]
                                        ),
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
                                            visibility_rules=[
                                                self.visibility_rule.depends_on_value(
                                                    field_name="isTicketRevenues",
                                                    values=[
                                                        True
                                                    ]
                                                )
                                            ],
                                            components=[
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    name="proceedsFromSales",
                                                    label="Wpływy ze sprzedaży",
                                                    validators=[
                                                        self.validator.related_fraction_lte_validator(
                                                            field_name="ownFinancialFundsAmount",
                                                            ratio=1
                                                        )
                                                    ],
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    mask="fund",
                                                    name="otherFinancialResources",
                                                    label="Pozostałe środki finansowe",
                                                    validators=[
                                                        self.validator.related_fraction_lte_validator(
                                                            field_name="ownFinancialFundsAmount",
                                                            ratio=1
                                                        )
                                                    ],
                                                    unit="PLN"
                                                )
                                            ]
                                        ),
                                        self.create_chapter(
                                            title="<small>b) Wkład rzeczowy</small>"
                                        ),
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
                                                    mask="fund",
                                                    name="ownInKindFundsAmount",
                                                    label="Kwota",
                                                    unit="PLN"
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    mask="share",
                                                    name="ownInKindFundsShare",
                                                    label="Udział w koszcie całkowitym",
                                                    calculation_rules=[
                                                        self.calculation_rule.share_calculator(
                                                            dividend_field="ownInKindFundsAmount",
                                                            divisor_field="totalProjectCost"
                                                        )
                                                    ],
                                                    validators=[
                                                        self.validator.related_share_validator(
                                                            dividend="ownInKindFundsAmount",
                                                            divisor="totalProjectCost"
                                                        )
                                                    ],
                                                    required=True,
                                                    read_only=True,
                                                    unit="%"
                                                )
                                            ]
                                        ),
                                        self.create_chapter(
                                            title="<small>Łączny wkład własny</small>",
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
                                                    name="ownFundsSumAmount",
                                                    read_only=True,
                                                    unit="PLN",
                                                    calculation_rules=[
                                                        self.calculation_rule.dynamic_sum_inputs(
                                                            fields=[
                                                                "ownFinancialFundsAmount",
                                                                "ownInKindFundsAmount"
                                                            ]
                                                        )
                                                    ],
                                                    validators=[
                                                        self.validator.related_sum_validator(
                                                            field_names=[
                                                                "ownFinancialFundsAmount",
                                                                "ownInKindFundsAmount"
                                                            ]
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>2) Dotacja PISF</normal>",
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
                                            label="Wnioskowana dotacja z PISF",
                                            name="pisfSupportAmountInput",
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
                                                    dividend_field="pisfSupportAmountInput",
                                                    divisor_field="totalProjectCost"
                                                )
                                            ],
                                            read_only=True,
                                            validators=[
                                                self.validator.related_share_validator(
                                                    dividend="pisfSupportAmountInput",
                                                    divisor="totalProjectCost"
                                                )
                                            ],
                                            required=True,
                                            mask="share",
                                            unit="%"
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>3) Pozostałe źródła finansowania</normal>",
                                    components=[
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
                    ]
                )
            ]
        )
        self.save_part(part)

    def create_application_statements(self, number: int):
        nature_of_project = [
            {
                "label": "krajowy",
                "name": "Domestic"
            },
            {
                "label": "międzynarodowy",
                "name": "International"
            },
            {
                "label": "ograniczony krąg odbiorców",
                "name": "LimitedAudience"
            },
            {
                "label": "ze względu na niską wartość komercyjną nie mogłoby się odbyć bez dofinansowania przez PISF",
                "name": "LowCommercialValue"
            },
            {
                "label": "lokalny",
                "name": "Local"
            }
        ]

        required_statements = [
            {
                "label": "Oświadczam, iż posiadam zasoby rzeczowe, finansowe i kadrowe niezbędne do realizacji zadania.",
                "name": "NecessaryResource"
            },
            {
                "label": "Oświadczam, iż nie zalegam z płatnościami na rzecz podmiotów publiczno-prawnych.",
                "name": "NotInArrears"
            },
            {
                "label": "Oświadczam, iż nie zachodzą przesłanki określone w art. 22 ust. 2 ustawy o kinematografii z dnia 30 czerwca 2005 r., które uniemożliwiają udzielenie dofinansowania.",
                "name": "ArticleTwentyTwo"
            },
            {
                "label": "W przypadku uzyskania dofinansowania, zobowiązuję się do uzupełnienia wniosku o niezbędne dokumenty w formie elektronicznej, weryfikujące dane i kwalifikowalność Wnioskodawcy (aktualny wypis z właściwego rejestru np. RIK, RIF – wystawiony nie wcześniej, niż trzy miesiące przed datą złożenia wniosku, statut, zaświadczenie o nadaniu numeru REGON, decyzję o nadaniu numeru NIP, umowę spółki cywilnej itp.), dokumenty potwierdzające uprawnienie do reprezentowania Wnioskodawcy (akt powołania, mianowania, pełnomocnictwo itp.) i dokumenty potwierdzające sposób reprezentacji (jeżeli z zapisów tych dokumentów wynika uprawnienie do reprezentowania Wnioskodawcy np. statut, umowa spółki cywilnej.",
                "name": "AllNecessaryDocuments"
            },
            {
                "label": "Oświadczenie Wnioskodawcy o braku powiązań z podmiotami sankcjonowanymi:\n\nW związku z wejściem w życie dnia 16 kwietnia 2022 roku ustawy z dnia 13 kwietnia 2022 roku o szczególnych rozwiązaniach w zakresie przeciwdziałania wspieraniu agresji na Ukrainę oraz służących ochronie bezpieczeństwa narodowego (Dz.U. z 2022 r. poz. 835) (dalej „Ustawa o przeciwdziałaniu wspieraniu agresji”), która uzupełnia pakiet wiążących Polskę środków ograniczających (sankcji) przyjętych na poziomie Unii Europejskiej oraz międzynarodowym, celem egzekwowania tychże sankcji,</br>\nWnioskodawca składa oświadczenia jak poniżej.</br>\n</br>\n§ 1</br>\n1. Beneficjent oświadcza, że, bezpośrednio lub pośrednio:</br>\na) nie wspiera agresji Federacji Rosyjskiej na Ukrainę rozpoczętą w dniu 24 lutego 2022 r.,</br>\nb) nie wspiera naruszeń praw człowieka lub represji wobec społeczeństwa obywatelskiego i opozycji demokratycznej lub których działalność stanowi inne poważne zagrożenie dla demokracji lub praworządności w Federacji Rosyjskiej lub na Białorusi,</br>\nc) nie jest bezpośrednio związany z osobami lub podmiotami, które nie spełniają kryteriów o których mowa w lit. a i b powyżej, w szczególności ze względu na powiązania o charakterze osobistym, organizacyjnym, gospodarczym lub finansowym, lub wobec których istnieje prawdopodobieństwo wykorzystania w tym celu dysponowanych przez nie takich środków finansowych, funduszy lub zasobów gospodarczych,</br>\nd) nie uchyla się od jakichkolwiek środków ograniczających (sankcji), nie narusza przepisów nakładających sankcje ani nie ułatwia innym podmiotom uchylania się od sankcji.</br>\n</br>\n2. Beneficjent oświadcza, że nie znajduje się na liście osób i podmiotów, wobec których są stosowane środki ograniczające (sankcje), o których mowa w art. 2 ustawy o przeciwdziałaniu wspieraniu agresji, a w szczególności:</br>\na) nie jest wymieniony w wykazach określonych w rozporządzeniu Rady (WE) nr 765/2006 z dnia 18 maja 2006 r. dotyczącego środków ograniczających w związku z sytuacją na Białorusi i udziałem Białorusi w agresji Rosji wobec Ukrainy (dalej jako „Rozporządzenie 765/2006”),</br>\nb) nie jest wymieniony w wykazach określonych w rozporządzeniu Rady (UE) nr 269/2014 z dnia 17 marca 2014 r. w sprawie środków ograniczających w odniesieniu do działań podważających integralność terytorialną, suwerenność i niezależność Ukrainy lub im zagrażających (dalej jako „Rozporządzenie 269/2014”),</br>\nc) wobec Beneficjenta nie została wydana decyzja w sprawie wpisu na listę osób i podmiotów, wobec których są stosowane środki w celu przeciwdziałania wspieraniu agresji Federacji Rosyjskiej na Ukrainę, z zastosowaniem środka w postaci wykluczenia z postępowania o udzielenie zamówienia publicznego lub konkursu prowadzonego na podstawie ustawy z dnia 11 września 2019 r. - Prawo zamówień publicznych,</br>\nd) Beneficjent nie jest umieszczony w wykazie cudzoziemców, których pobyt na terytorium Rzeczypospolitej Polskiej jest niepożądany, o którym mowa w art. 434 ustawy z dnia 12 grudnia 2013 r. o cudzoziemcach (dalej jako „Ustawa o cudzoziemcach”),</br>\ne) w stosunku do Beneficjenta członkiem organów, pracownikiem szczebla kierowniczego lub beneficjentem rzeczywistym, w rozumieniu ustawy z dnia 1 marca 2018 r. o przeciwdziałaniu praniu pieniędzy oraz finansowaniu terroryzmu, ani ich krewnym (przy czym na potrzeby niniejszego oświadczenia krewny, w odniesieniu do osoby fizycznej, oznacza jej małżonka, rodzeństwo, zstępnych i wstępnych) nie jest osoba znajdująca się na liście osób i podmiotów, wobec których są stosowane środki ograniczające, o której mowa w art. 2 ustawy o przeciwdziałaniu wspierania agresji, w szczególności nie znajduje się w wykazach określonych w Rozporządzeniu 765/2006, Rozporządzeniu 269/2014 lub art. 434 Ustawy o cudzoziemcach,</br>\nf) w stosunku do Beneficjenta jednostką dominującą w rozumieniu art. 3 ust. 1 pkt 37 ustawy z dnia 29 września 1994 r. o rachunkowości nie jest podmiot wymieniony w wykazach określonych w Rozporządzeniu 765/2006 i Rozporządzeniu 269/2014;</br>\ng) żaden z udziałów w kapitale zakładowym Beneficjenta nie jest własnością bezpośrednio lub pośrednio, ani nie został na nim ustanowiony zastaw ani użytkowanie na rzecz podmiotów wobec których są stosowane środki ograniczające (sankcje), o których mowa w niniejszym § 2, lub jakiegokolwiek podmiotu lub osoby, która korzysta z kapitału lub finansowania zapewnionego przez taki podmiot ani władz rosyjskich; przy czym na potrzeby niniejszego oświadczenia przez władze rosyjskie należy rozumieć Federację Rosyjską (i jej kraje związkowe), federalne i lokalne władze państwowe, państwowe jednostki organizacyjne i przedsiębiorstwa państwowe, instytucje publiczne, wszelkie spółki i podmioty bezpośrednio lub pośrednio kontrolowane przez wyżej wymienione oraz wszelkie podmioty powiązane z wyżej wymienionymi.</br>\n</br>\n3. Ponadto Beneficjent oświadcza, że nie znajduje się na liście osób i podmiotów, wobec których są stosowane środki ograniczające (sankcje) nałożone przez Organizację Narodów Zjednoczonych, państwo członkowskie Organizacji Narodów Zjednoczonych lub każdą inną organizację międzyrządową wprowadzone w związku z naruszeniem integralności terytorialnej Ukrainy i inwazją na Ukrainę (w tym również aneksją Krymu i konfliktem w regionie Donbasu) przeciwko Federacji Rosyjskiej, Białorusi, wskazanym osobom fizycznym i podmiotom.</br>\n</br>\n§ 2</br>\n1. Beneficjent przyjmuje do wiadomości, że oświadczenia Beneficjenta, o których mowa w § 1 powyżej, dotyczą środków ograniczających (sankcji), które obowiązują w dniu zawarcia Umowy i powinny pozostać prawdziwe przez cały okres obowiązywania Umowy.</br>\n2. Beneficjent zobowiązuje się monitorować swoje inwestycje, relacje biznesowe i działalność gospodarczą/zawodową w celu zapewnienia zgodności z wyżej wymienionymi oświadczeniami, przy jednoczesnym dochowaniu należytej staranności ogólnie wymaganej w relacjach biznesowych.</br>\n3. Beneficjent zobowiązuje się niezwłocznie poinformować Polski Instytut Sztuki Filmowej o każdej zmianie okoliczności, o których mowa w § 1 powyżej, które wystąpiły, powstały lub istniały przed dniem zawarcia Umowy, a których nie był świadomy, lub które wystąpiły, powstały lub zaistniały po zawarciu Umowy.</br>\n</br>\n§ 3</br>\n1. W przypadku nieprawdziwości któregokolwiek ze złożonych oświadczeń, o których mowa w § 1 powyżej, Polski Instytut Sztuki Filmowej jest uprawniony do wypowiedzenia Umowy w trybie natychmiastowym i żądania zwrotu przekazanych środków finansowych wraz z odsetkami ustawowymi za opóźnienie liczonymi od dnia przekazania środków, w terminie wskazanym przez Polski Instytut Sztuki Filmowej, jednak nie dłuższym niż 14 dni od dnia doręczenia wezwania zwrotu.</br>\n2. Bez uszczerbku dla postanowień ust. 1, w przypadku, w którym na skutek niepełnych, nierzetelnych lub nieprawdziwych oświadczeń Beneficjenta na Polski Instytut Sztuki Filmowej nałożona zostanie jakakolwiek kara administracyjna, Beneficjent zobowiązuje się do zwrotu - regresowo na wezwanie Polskiego Instytutu Sztuki Filmowej - całości pokrytych kar oraz wszelkich związanych z tym wydatków, włączając koszty postępowania sądowego, arbitrażowego, administracyjnego lub ugodowego oraz koszty pomocy prawnej.</br>",
                "name": "ApplicantsOfNoTies"
            }
        ]

        part = self.create_part(
            title=f"{int_to_roman(number)}. Oświadczenia",
            short_name=f"{int_to_roman(number)}. Oświadczenia",
            chapters=[
                self.create_chapter(
                    title="Oświadczenia Wnioskodawcy co do charakteru przedsięwzięcia",
                    components=[
                        *[self.create_component(
                            component_type="checkbox",
                            label=chapter["label"],
                            name=f"natureOfProject{chapter["name"]}"
                        ) for chapter in nature_of_project]
                    ]
                ),
                self.create_chapter(
                    title="Wymagane oświadczenia Wnioskodawcy",
                    components=[
                        *[self.create_component(
                            component_type="checkbox",
                            label=chapter["label"],
                            name=f"statement{chapter["name"]}",
                            required=True
                        ) for chapter in required_statements]
                    ]
                ),
                self.create_chapter(
                    title="Inne ważne informacje",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="otherImportantInformations",
                            validators=[
                                self.validator.length_validator(max_value=1800)
                            ],
                            required=True
                        )
                    ]
                )
            ]
        )

        self.save_part(part)

    def create_application_attachments(self, number: int):
        part = self.create_part(
            title=f"{int_to_roman(number)}. Załączniki",
            short_name=f"{int_to_roman(number)}. Załączniki",
            chapters=[
                self.create_chapter(
                    title="Obowiązkowe załączniki",
                    components=[
                        self.section.application_attachment.schedule_information()
                    ]
                ),
                self.section.application_attachment.other_attachments(),
                self.section.application_attachment.storage_of_blanks()
            ]
        )
        self.save_part(part)

    def create_application_schedule(self, number: int):
        part = self.create_part(
            title=f"{int_to_roman(number)}. Harmonogram realizacji zadania",
            short_name=f"{int_to_roman(number)}. Harmonogram",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Nazwa przedsięwzięcia",
                            name="projectNameRepeatSchedule",
                            read_only=True,
                            required=True,
                            calculation_rules=[
                                self.calculation_rule.copy_value(
                                    from_name="applicationTaskName"
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Uwaga!<br/>Harmonogram zadania powinien uwzględniać etapy: przygotowawczy (np. poszukiwania partnerów, zaproszenie uczestników, przygotowanie promocji wydarzenia itp.), realizacji zadania (np. wykonanie i/lub wysyłka materiałów promocyjnych, pokaz filmu na festiwalu) oraz podsumowania (ewaluacja i rozliczenie zadania – ostateczna data zakończenia realizacji zadania: dzień, miesiąc i rok). <br/>W zakresie każdego z tych etapów należy określić najważniejsze działania (tzw. „kamienie milowe” zadania) i terminy ich realizacji. <br/>- Harmonogram zadania powinien uwzględniać wszystkie działania wymienione w kosztorysie zadania.<br/>- Prosimy o chronologiczne ułożenie wszystkich pozycji harmonogramu.",
                    components=[]
                ),
                self.create_chapter(
                    multiple_forms_rules={
                        "minCount": 1,
                        "maxCount": 20
                    },
                    components=[
                        self.create_chapter(
                            title="Wydarzenie",
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
                                    component_type="date",
                                    label="Termin od",
                                    name="taskActionDateStart",
                                    validators=[
                                        self.validator.related_local_date_lte_validator(
                                            field_name="taskActionDateEnd",
                                            message="Termin rozpoczęcia działania musi być wcześniejszy niż termin jego zakończenia."
                                        )
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="date",
                                    label="Termin do",
                                    name="taskActionDateEnd",
                                    validators=[
                                        self.validator.related_local_date_gte_validator(
                                            field_name="taskActionDateStart",
                                            message="Termin zakończenia działania musi być późniejszy niż termin jego rozpoczęcia."
                                        )
                                    ],
                                    required=True
                                ),
                                self.create_component(
                                    component_type="textarea",
                                    label="Działanie",
                                    name="taskActionDesc",
                                    help_text="Krótki opis działania",
                                    class_list=[
                                        "table-full",
                                        "col-span-2"
                                    ],
                                    validators=[
                                        self.validator.length_validator(max_value=250)
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Podsumowanie",
                    class_list={
                        "main": [
                            "dates"
                        ],
                        "sub": [
                            "dates-item"
                        ]
                    },
                    components=[
                        self.create_component(
                            component_type="date",
                            label="Rozpoczęcie realizacji przedsięwzięcia",
                            name="projectCommencement",
                            read_only=True,
                            required=True,
                            calculation_rules=[
                                self.calculation_rule.first_date(
                                    field="taskActionDateStart"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="date",
                            label="Zakończenie realizacji przedsięwzięcia",
                            name="projectCompletion",
                            read_only=True,
                            required=True,
                            calculation_rules=[
                                self.calculation_rule.last_date(
                                    field="taskActionDateStart"
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="date",
                            label="Termin rozliczenia z PISF",
                            name="settlementDeadline",
                            read_only=True,
                            required=True,
                            calculation_rules=[
                                self.calculation_rule.relate_to_last_date(
                                    field="projectCompletion",
                                    parameter=30
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        self.save_part(part)
