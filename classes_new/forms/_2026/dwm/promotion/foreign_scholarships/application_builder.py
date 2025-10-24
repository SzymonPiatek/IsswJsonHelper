from classes_new.forms._2026.dwm.pisf_structure import ForeignScholarshipsPriority
from classes_new.forms._2026.dwm.promotion.application_builder import PromotionOperationalProgramApplicationFormBuilder


class ForeignPriorityApplicationFormBuilder(PromotionOperationalProgramApplicationFormBuilder):
    def __init__(self):
        super().__init__(
            priority=ForeignScholarshipsPriority()
        )

        self.form_id = self.set_ids(
            local_id=16410,
            uat_id=2823
        )

        self.grantee_vat_declaration = [
            "Wnioskodawca jest osobą fizyczną, dlatego kwoty zamieszczone w kosztorysie wniosku to KWOTY BRUTTO"
        ]

    def create_application_applicant_achievements_data(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Dotychczasowy dorobek i doświadczenie Wnioskodawcy w dziedzinie, której wniosek dotyczy",
            short_name=f"{self.helpers.int_to_roman(number)}. Dorobek Wnioskodawcy",
            chapters=[
                self.create_chapter(
                    title="CV Wnioskodawcy",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="applicantCv",
                            validators=[
                                self.validator.length_validator(max_value=10000)
                            ],
                            help_text="Należy podać filmografię z informacją o pełnionej funkcji w projekcie oraz ew. nagrody filmu lub/i nagrody dla Wnioskodawcy.",
                            required=True
                        )
                    ]
                )
            ]
        )
        self.save_part(part=part)

    def create_application_description_of_the_project_data(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Opis zaplanowanego przedsięwzięcia",
            short_name=f"{self.helpers.int_to_roman(number)}. Opis przedsięwzięcia",
            chapters=[
                self.create_chapter(
                    title="Opis przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="plannedTaskDesc",
                            validators=[
                                self.validator.length_validator(max_value=20000)
                            ],
                            help_text="Należy podać opis, charakter wydarzenia oraz cel uczestnictwa Wnioskodawcy.",
                            required=True
                        )
                    ]
                )
            ]
        )
        self.save_part(part=part)

    def create_application_other_information_data(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Inne informacje",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="textarea",
                            label="1. Synopsis filmu / opis projektu",
                            name="movieProjectSynopsis",
                            validators=[
                                self.validator.length_validator(max_value=20000)
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="2. Link do filmu",
                            name="movieLink",
                            validators=[
                                self.validator.length_validator(max_value=1800)
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="3. Plan promocji",
                            name="moviePromotionPlan",
                            validators=[
                                self.validator.length_validator(max_value=20000)
                            ],
                            required=True
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="4. Festiwale, warsztaty, pitchingi w których film / projekt dotychczas wziął udział",
                            name="movieFestivalsShown",
                            validators=[
                                self.validator.length_validator(max_value=20000)
                            ],
                            required=True,
                            help_text="Podaj informacje na temat wydarzeń, w których film już wziął udział."
                        )
                    ]
                )
            ]
        )
        self.save_part(part=part)

    def create_application_statements(self, number: int):
        components_data = [
            {
                "label": "1. Oświadczam, iż nie zalegam z płatnościami na rzecz podmiotów publiczno-prawnych.",
                "name": "statementNoPublicLiabilities"
            },
            {
                "label": "2. Oświadczam, iż nie zachodzą przesłanki określone w art. 22 ust. 2 Ustawy u kinematografii, które uniemożliwiają udzielenie dofinansowania przez Polski Instytut Sztuki Filmowej.",
                "name": "statementEligibleForFunding"
            },
            {
                "label": "3. Oświadczam, iż spełniam warunki do otrzymania dofinansowania określone w Ustawie o kinematografii, Rozporządzeniu Ministra Kultury w sprawie udzielenia przez PISF dofinansowania przedsięwzięć z zakresu kinematografii oraz Programie Operacyjnym V - Promocja polskiej twórczości filmowej za granicą.",
                "name": "statementMeetConditions"
            },
            {
                "label": "4. Oświadczam, że zapoznałem się z treścią i zasadami dofinansowania w ramach <a href='https://pisf.pl/wp-content/uploads/2024/12/Programy-Operacyjne-PISF-na-rok-2025.pdf' target=\"_blank\">V Programu Operacyjnego, Priorytet II: Stypendia zagraniczne Polskiego Instytutu Sztuki Filmowej na rok 2025</a>",
                "name": "applicantsStatementOfDeclareRead"
            },
            {
                "label": "5. Oświadczenie Wnioskodawcy o braku powiązań z podmiotami sankcjonowanymi:\n\nW związku z wejściem w życie dnia 16 kwietnia 2022 roku ustawy z dnia 13 kwietnia 2022 roku o szczególnych rozwiązaniach w zakresie przeciwdziałania wspieraniu agresji na Ukrainę oraz służących ochronie bezpieczeństwa narodowego (Dz.U. z 2022 r. poz. 835) (dalej „Ustawa o przeciwdziałaniu wspieraniu agresji”), która uzupełnia pakiet wiążących Polskę środków ograniczających (sankcji) przyjętych na poziomie Unii Europejskiej oraz międzynarodowym, celem egzekwowania tychże sankcji,</br>\nWnioskodawca składa oświadczenia jak poniżej.</br>\n</br>\n§ 1</br>\n1. Stypendysta oświadcza, że, bezpośrednio lub pośrednio:</br>\na) nie wspiera agresji Federacji Rosyjskiej na Ukrainę rozpoczętą w dniu 24 lutego 2022 r.,</br>\nb) nie wspiera naruszeń praw człowieka lub represji wobec społeczeństwa obywatelskiego i opozycji demokratycznej lub których działalność stanowi inne poważne zagrożenie dla demokracji lub praworządności w Federacji Rosyjskiej lub na Białorusi,</br>\nc) nie jest bezpośrednio związany z osobami lub podmiotami, które nie spełniają kryteriów o których mowa w lit. a i b powyżej, w szczególności ze względu na powiązania o charakterze osobistym, organizacyjnym, gospodarczym lub finansowym, lub wobec których istnieje prawdopodobieństwo wykorzystania w tym celu dysponowanych przez nie takich środków finansowych, funduszy lub zasobów gospodarczych,</br>\nd) nie uchyla się od jakichkolwiek środków ograniczających (sankcji), nie narusza przepisów nakładających sankcje ani nie ułatwia innym podmiotom uchylania się od sankcji.</br>\n</br>\n2. Stypendysta oświadcza, że nie znajduje się na liście osób i podmiotów, wobec których są stosowane środki ograniczające (sankcje), o których mowa w art. 2 ustawy o przeciwdziałaniu wspieraniu agresji, a w szczególności:</br>\na) nie jest wymieniony w wykazach określonych w rozporządzeniu Rady (WE) nr 765/2006 z dnia 18 maja 2006 r. dotyczącego środków ograniczających w związku z sytuacją na Białorusi i udziałem Białorusi w agresji Rosji wobec Ukrainy (dalej jako „Rozporządzenie 765/2006”),</br>\nb) nie jest wymieniony w wykazach określonych w rozporządzeniu Rady (UE) nr 269/2014 z dnia 17 marca 2014 r. w sprawie środków ograniczających w odniesieniu do działań podważających integralność terytorialną, suwerenność i niezależność Ukrainy lub im zagrażających (dalej jako „Rozporządzenie 269/2014”),</br>\nc) wobec Stypendysta nie została wydana decyzja w sprawie wpisu na listę osób i podmiotów, wobec których są stosowane środki w celu przeciwdziałania wspieraniu agresji Federacji Rosyjskiej na Ukrainę, z zastosowaniem środka w postaci wykluczenia z postępowania o udzielenie zamówienia publicznego lub konkursu prowadzonego na podstawie ustawy z dnia 11 września 2019 r. - Prawo zamówień publicznych,</br>\nd) Stypendysta nie jest umieszczony w wykazie cudzoziemców, których pobyt na terytorium Rzeczypospolitej Polskiej jest niepożądany, o którym mowa w art. 434 ustawy z dnia 12 grudnia 2013 r. o cudzoziemcach (dalej jako „Ustawa o cudzoziemcach”),</br>\ne) w stosunku do Stypendysty członkiem organów, pracownikiem szczebla kierowniczego lub Stypendystą rzeczywistym, w rozumieniu ustawy z dnia 1 marca 2018 r. o przeciwdziałaniu praniu pieniędzy oraz finansowaniu terroryzmu, ani ich krewnym (przy czym na potrzeby niniejszego oświadczenia krewny, w odniesieniu do osoby fizycznej, oznacza jej małżonka, rodzeństwo, zstępnych i wstępnych) nie jest osoba znajdująca się na liście osób i podmiotów, wobec których są stosowane środki ograniczające, o której mowa w art. 2 ustawy o przeciwdziałaniu wspierania agresji, w szczególności nie znajduje się w wykazach określonych w Rozporządzeniu 765/2006, Rozporządzeniu 269/2014 lub art. 434 Ustawy o cudzoziemcach,</br>\nf) w stosunku do Stypendysty jednostką dominującą w rozumieniu art. 3 ust. 1 pkt 37 ustawy z dnia 29 września 1994 r. o rachunkowości nie jest podmiot wymieniony w wykazach określonych w Rozporządzeniu 765/2006 i Rozporządzeniu 269/2014;</br>\ng) żaden z udziałów w kapitale zakładowym Stypendysty nie jest własnością bezpośrednio lub pośrednio, ani nie został na nim ustanowiony zastaw ani użytkowanie na rzecz podmiotów wobec których są stosowane środki ograniczające (sankcje), o których mowa w niniejszym § 2, lub jakiegokolwiek podmiotu lub osoby, która korzysta z kapitału lub finansowania zapewnionego przez taki podmiot ani władz rosyjskich; przy czym na potrzeby niniejszego oświadczenia przez władze rosyjskie należy rozumieć Federację Rosyjską (i jej kraje związkowe), federalne i lokalne władze państwowe, państwowe jednostki organizacyjne i przedsiębiorstwa państwowe, instytucje publiczne, wszelkie spółki i podmioty bezpośrednio lub pośrednio kontrolowane przez wyżej wymienione oraz wszelkie podmioty powiązane z wyżej wymienionymi.</br>\n</br>\n3. Ponadto Stypendysta oświadcza, że nie znajduje się na liście osób i podmiotów, wobec których są stosowane środki ograniczające (sankcje) nałożone przez Organizację Narodów Zjednoczonych, państwo członkowskie Organizacji Narodów Zjednoczonych lub każdą inną organizację międzyrządową wprowadzone w związku z naruszeniem integralności terytorialnej Ukrainy i inwazją na Ukrainę (w tym również aneksją Krymu i konfliktem w regionie Donbasu) przeciwko Federacji Rosyjskiej, Białorusi, wskazanym osobom fizycznym i podmiotom.</br>\n</br>\n§ 2</br>\n1. Stypendysta przyjmuje do wiadomości, że oświadczenia Stypendysty, o których mowa w § 1 powyżej, dotyczą środków ograniczających (sankcji), które obowiązują w dniu zawarcia Umowy i powinny pozostać prawdziwe przez cały okres obowiązywania Umowy.</br>\n2. Stypendysta zobowiązuje się monitorować swoje inwestycje, relacje biznesowe i działalność gospodarczą/zawodową w celu zapewnienia zgodności z wyżej wymienionymi oświadczeniami, przy jednoczesnym dochowaniu należytej staranności ogólnie wymaganej w relacjach biznesowych.</br>\n3. Stypendysta zobowiązuje się niezwłocznie poinformować Polski Instytut Sztuki Filmowej o każdej zmianie okoliczności, o których mowa w § 1 powyżej, które wystąpiły, powstały lub istniały przed dniem zawarcia Umowy, a których nie był świadomy, lub które wystąpiły, powstały lub zaistniały po zawarciu Umowy.</br>\n</br>\n§ 3</br>\n1. W przypadku nieprawdziwości któregokolwiek ze złożonych oświadczeń, o których mowa w § 1 powyżej, Polski Instytut Sztuki Filmowej jest uprawniony do wypowiedzenia Umowy w trybie natychmiastowym i żądania zwrotu przekazanych środków finansowych wraz z odsetkami ustawowymi za opóźnienie liczonymi od dnia przekazania środków, w terminie wskazanym przez Polski Instytut Sztuki Filmowej, jednak nie dłuższym niż 14 dni od dnia doręczenia wezwania zwrotu.</br>\n2. Bez uszczerbku dla postanowień ust. 1, w przypadku, w którym na skutek niepełnych, nierzetelnych lub nieprawdziwych oświadczeń Stypendysty na Polski Instytut Sztuki Filmowej nałożona zostanie jakakolwiek kara administracyjna, Stypendysta zobowiązuje się do zwrotu - regresowo na wezwanie Polskiego Instytutu Sztuki Filmowej - całości pokrytych kar oraz wszelkich związanych z tym wydatków, włączając koszty postępowania sądowego, arbitrażowego, administracyjnego lub ugodowego oraz koszty pomocy prawnej.</br>",
                "name": "applicantsStatementOfNoTies"
            }
        ]

        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Oświadczenia Wnioskodawcy",
            short_name=f"{self.helpers.int_to_roman(number)}. Oświadczenia",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label=item["label"],
                            required=True,
                            name=item["name"]
                        ) for item in components_data
                    ]
                )
            ]
        )
        self.save_part(part=part)

    def create_application_attachments(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Obowiązkowe załączniki zgodnie z rodzajem przedsięwzięcia",
            short_name=f"{self.helpers.int_to_roman(number)}. Załączniki",
            chapters=[
                self.create_chapter(
                    title="A. Oficjalne zaproszenie filmu/twórcy na festiwal",
                    components=[
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 1,
                                "maxCount": 20
                            },
                            components=[
                                self.create_chapter(
                                    title="Plik",
                                    components=[
                                        self.create_component(
                                            component_type="file",
                                            name="invitationAttachment",
                                            required=True
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="B. Lista gości zagranicznych",
                    components=[
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 1,
                                "maxCount": 20
                            },
                            components=[
                                self.create_chapter(
                                    title="Plik",
                                    components=[
                                        self.create_component(
                                            component_type="file",
                                            name="foreignersListAttachment",
                                            validators=[
                                                self.validator.related_required_if_equal_validator(
                                                    field_name="wasRelatedToParticipation",
                                                    value="Nie"
                                                )
                                            ],
                                            required=True
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="C. Zaświadczenie o zakwalifikowaniu się do udziału w przedsięwzięciu",
                    components=[
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 1,
                                "maxCount": 20
                            },
                            components=[
                                self.create_chapter(
                                    title="Plik",
                                    components=[
                                        self.create_component(
                                            component_type="file",
                                            name="qualifyConfirmAttachment",
                                            validators=[
                                                self.validator.related_required_if_equal_validator(
                                                    field_name="wasRelatedToParticipation",
                                                    value="Nie"
                                                )
                                            ],
                                            required=True
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Uwaga",
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Zapoznałem/łam się z poniższymi zasadami.<br/>- Wnioskodawca jest zobowiązany do przedstawienia rozliczenia dofinansowania zgodnie z warunkami określonymi w umowie o ustanowienie stypendium, w tym w szczególności do przedłożenia raportu końcowego, który zawiera finansowe rozliczenie przedsięwzięcia, ocenę jakościową jego realizacji.<br/>- Do raportu końcowego należy załączyć dokumenty finansowo-księgowe potwierdzające wydatkowanie kosztów poniesionych z udzielonego dofinansowania w postaci faktur (WAŻNE: faktury muszą być wystawione na Stypendystę jako osobę fizyczną) oraz biletów (jeśli z przyczyn obiektywnie niezależnych od Stypendysty niemożliwe jest otrzymanie faktury) wraz z potwierdzeniem wykonania przelewów z rachunku bankowego Stypendysty, które zostało wskazane we wniosku o stypendium.<br/>- Procentowy wkład dofinansowania PISF w finalnym budżecie przedsięwzięcia nie może przekroczyć wkładu zakładanego, określonego w umowie o ustanowienie stypendium. Jeżeli faktycznie poniesiony koszt całkowity przedsięwzięcia okazał się niższy od planowanego lub Stypendysta nie wykorzystał całego dofinansowania, należy dokonać zwrotu na rachunek PISF i dostarczyć wraz z raportem potwierdzenie przelewu.<br/>- Jedynie koszty poniesione od daty złożenia wniosku o ustanowienie stypendium w ISSW do daty zakończenia przedsięwzięcia określonej w harmonogramie, mogą zostać uznane za koszty kwalifikowalne i opłacone z dofinasowania PISF (koszty poniesione przed datą złożenia wniosku o ustanowienie stypendium nie będą uznane za koszty kwalifikowalne).<br/>- Wniosek o ustanowienie stypendium wraz z załącznikami należy podpisać przy użyciu kwalifikowanego podpisu elektronicznego lub profilu zaufanego platformy E-PUAP.<br/>- Wszelkie załączniki do wniosku o ustanowienie stypendium (w tym listy intencyjne, umowy z partnerami, itp.) wymagają poświadczenia za zgodność z oryginałem. Podpisanie wniosku o ustanowienie stypendium przez Wnioskodawcę kwalifikowanym podpisem elektronicznym lub profilem zaufanym platformy E-PUAP jest równoznaczne z poświadczeniem przez Wnioskodawcę załączników do wniosku o ustanowienie stypendium za zgodne z oryginałem.<br/>- Linki do zasobów zewnętrznych umieszczane we wniosku o ustanowienie stypendium powinny zachować ważność co najmniej do czasu wydania decyzji przez Dyrektora PISF.<br/>- Do dokumentów przedkładanych do wniosku o ustanowienie stypendium sporządzonych w językach obcych należy obligatoryjnie dołączyć tłumaczenie na język polski. Wnioskodawca, na wniosek PISF, ma obowiązek przedstawić tłumaczenie przysięgłe wskazanego dokumentu.",
                            name="acknowledgeRules",
                            required=True
                        )
                    ]
                )
            ]
        )
        self.save_part(part=part)
