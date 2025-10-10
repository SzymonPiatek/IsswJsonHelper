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
                    "checkbox_title": "Czy występują środki z budżetów jednostek samorządu terytorialnego lub innych środków publicznych za wyjątkiem Ministerstwa Kultury i Dziedzictwa Narodowego?",
                    "checkbox_name": "isLocalGovernmentFunding",
                    "section_title": "<normal>a) z budżetów jednostek samorządu terytorialnego lub innych środków publicznych za wyjątkiem Ministerstwa Kultury i Dziedzictwa Narodowego </normal><br /><small>Uwaga! <normal>Odznaczenie powyższego checkboxa nie prowadzi do automatycznego usunięcia zawartych w tej sekcji informacji. Dane te nadal będą brane pod uwagę w obliczeniach finansowych i będą uwzględnione we wniosku. Jeżeli dane te nie są już potrzebne, prosimy o ich ręczne usunięcie. </small></normal>",
                    "section_name": "localGovernments",
                },
                {
                    "checkbox_title": "Czy występują środki Ministerstwa Kultury i Dziedzictwa Narodowego w ramach Programów Ministra?",
                    "checkbox_name": "isMinistryFunding",
                    "section_title": "<normal>b) ze środków Ministerstwa Kultury i Dziedzictwa Narodowego w ramach Programów Ministra </normal><br /><small>Uwaga! <normal>Odznaczenie powyższego checkboxa nie prowadzi do automatycznego usunięcia zawartych w tej sekcji informacji. Dane te nadal będą brane pod uwagę w obliczeniach finansowych i będą uwzględnione we wniosku. Jeżeli dane te nie są już potrzebne, prosimy o ich ręczne usunięcie. </small></normal>",
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
                                                    component_type="text",
                                                    mask="fund",
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
                                                    component_type="text",
                                                    mask="fund",
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
                                            component_type="text",
                                            mask="fund",
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
                                                                                    component_type="text",
                                                                                    mask="fund",
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
                                                                            component_type="text",
                                                                            mask="fund",
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
                                )
                            ]
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
