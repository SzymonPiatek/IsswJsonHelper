from classes.form_builder.application_builder import ApplicationBuilder
from classes.form_builder.duk.application_estimate_builder import DUKApplicationEstimateBuilder
from classes.form_builder.additional.decorators import not_implemented_func
from classes.form_builder.components.section.duk_section import DUKSection


class DUKApplicationBuilder(ApplicationBuilder):
    DEPARTMENT_NAME = 'DUK'

    def __init__(self):
        super().__init__()

        self.department_data_path = self.application_data_path / 'duk'
        self.program_data_path = None
        self.priority_data_path = None
        self.estimate_sections = []
        self.section = DUKSection()

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
        part = self.part.application_basic_data(
            data={
                **data,
                "operation_name": self.operation_name,
                "priority_name": self.priority_name,
            }
        )
        self.save_part(part)

    def create_application_applicant_data(self):
        part = self.create_part(
            title="II. Dane wnioskodawcy",
            short_name="II. Dane wnioskodawcy",
            chapters=[
                self.section.applicant_name(number="1"),
                self.section.eligible_person_data(number="2"),
                self.section.responsible_person_data(number="3"),
                self.section.applicant_address(number="4", main_poland=True, contact_poland=True, main_foreign=False, contact_foreign=False),
                self.section.applicant_identification_data(number="5"),
                self.section.applicant_bank_data(number="6", poland=True, foreign=True),
                self.section.applicant_legal_information(number="7"),
                self.section.applicant_statistical_data(number="8")
            ]
        )
        self.save_part(part)

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

    @not_implemented_func
    def create_application_scope_of_project(self):
        pass

    def create_application_statements(self):
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
            title="V. Oświadczenia",
            short_name="V. Oświadczenia",
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
                    title="Inne ważne informacje - zdaniem Wnioskodawcy ważne dla wykazania celowości przedsięwzięcia",
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

    def create_application_attachments(self):
        part = self.create_part(
            title="VI. Załączniki",
            short_name="VI. Załączniki",
            chapters=[
                self.create_chapter(
                    title="Obowiązkowe załączniki",
                    components=[
                        self.section.application_attachment.document_confirming_represent_applicant(),
                        self.section.application_attachment.schedule_information()
                    ]
                ),
                self.section.application_attachment.other_attachments(),
                self.section.application_attachment.storage_of_blanks()
            ]
        )
        self.save_part(part)

    def create_application_schedule(self):
        part = self.part.application_schedule_data()
        self.save_part(part)

    def create_application_project_costs(self):
        estimate = DUKApplicationEstimateBuilder(
            estimate_sections=self.estimate_sections
        )
        part = estimate.generate()

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
