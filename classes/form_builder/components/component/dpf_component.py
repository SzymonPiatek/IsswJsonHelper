from classes.form_builder.components.component.component import Component
from classes.form_builder.form_builder_base import FormBuilderBase


class DPFComponent(Component):
    def __init__(self):
        super().__init__()

        self.application_statements = ApplicationStatements()
        self.application_attachments = ApplicationAttachments()


class ApplicationStatements(FormBuilderBase):
    def __init__(self):
        super().__init__()

    def statement_act_on_cinematography(self):
        return self.create_component(
            component_type="checkbox",
            label="Oświadczam, iż zapoznałem się z Ustawą o kinematografii z 30 czerwca 2005 r., Rozporządzeniem Ministra Kultury z 27 października 2005 r. w sprawie udzielania przez Polski Instytutu Sztuki Filmowej dofinansowania przedsięwzięć z zakresu kinematografii, Programem Operacyjnym PISF - Produkcja Filmowa, oraz Regulaminem pracy ekspertów.",
            name="statementActOnCinematography",
            required=True,
        )

    def statement_necessary_resources(self):
        return self.create_component(
            component_type="checkbox",
            label="Oświadczam, iż posiadam zasoby rzeczowe, finansowe i kadrowe niezbędne do realizacji zadania.",
            name="statementNecessaryResources",
            required=True,
        )

    def statement_article_twenty_two(self):
        return self.create_component(
            component_type="checkbox",
            label="Oświadczam, iż nie zachodzą przesłanki określone w art. 22 ust. 2 ustawy o kinematografii z dnia 30 czerwca 2005 r., które uniemożliwiają udzielenie dofinansowania przez PISF.",
            name="statementArticleTwentyTwo",
            required=True,
        )

    def statement_not_in_arrears(self):
        return self.create_component(
            component_type="checkbox",
            label="Oświadczam, iż nie zalegam z płatnościami podatkowymi i innymi należnościami, do których stosuje się przepisy Ustawy z dnia 29 sierpnia 1997 - Ordynacja podatkowa (Dz.U. z 2020 poz 1325,1423,2122, 2123, 2320)",
            name="statementNotInArrears",
            required=True,
        )

    def statement_pay_social_security(self):
        return self.create_component(
            component_type="checkbox",
            label="Oświadczam, iż nie zalegam w opłacaniu składek na ubezpieczenia społeczne",
            name="statementPaySocialSecurity",
            required=True,
        )

    def applicants_statement_of_no_ties(self):
        return self.create_component(
            component_type="checkbox",
            label="""
                Oświadczenie Wnioskodawcy o braku powiązań z podmiotami sankcjonowanymi: <br/><br/> 
                W związku z wejściem w życie dnia 16 kwietnia 2022 roku ustawy z dnia 13 kwietnia 2022 roku  
                o szczególnych rozwiązaniach w zakresie przeciwdziałania wspieraniu agresji na Ukrainę oraz 
                służących ochronie bezpieczeństwa narodowego (Dz.U. z 2022 r. poz. 835) 
                (dalej „Ustawa o przeciwdziałaniu wspieraniu agresji”), która uzupełnia pakiet wiążących Polskę 
                środków ograniczających (sankcji) przyjętych na poziomie Unii Europejskiej oraz międzynarodowym, 
                celem egzekwowania tychże sankcji,<br/>
                Wnioskodawca składa oświadczenia jak poniżej. <br/><br/>
                
                § 1<br/>
                1. Beneficjent oświadcza, że, bezpośrednio lub pośrednio:<br/>
                a) nie wspiera agresji Federacji Rosyjskiej na Ukrainę rozpoczętą w dniu 24 lutego 2022 r.,<br/>
                b) nie wspiera  naruszeń praw człowieka lub represji wobec społeczeństwa obywatelskiego i opozycji 
                demokratycznej lub których działalność stanowi inne poważne zagrożenie dla demokracji lub praworządności 
                w Federacji Rosyjskiej lub na Białorusi,<br/>
                c) nie jest bezpośrednio związany z osobami lub podmiotami, które nie spełniają kryteriów o  których mowa 
                w lit. a i b powyżej,  w szczególności ze względu na powiązania o charakterze osobistym, organizacyjnym, 
                gospodarczym lub finansowym, lub wobec których istnieje prawdopodobieństwo wykorzystania w tym celu 
                dysponowanych przez nie takich środków finansowych, funduszy lub zasobów gospodarczych,<br/>
                d) nie uchyla się od jakichkolwiek środków ograniczających (sankcji), nie narusza przepisów nakładających 
                sankcje ani nie ułatwia innym podmiotom uchylania się od sankcji.<br/><br/>
                
                2. Beneficjent oświadcza, że nie znajduje się na liście osób i podmiotów, wobec których są stosowane 
                środki ograniczające (sankcje), o których  mowa w art. 2 ustawy o przeciwdziałaniu wspieraniu agresji, 
                a w szczególności:<br/>
                a) nie jest wymieniony w wykazach określonych w rozporządzeniu Rady (WE) nr 765/2006 z dnia 18 maja 2006 r. 
                dotyczącego środków ograniczających w związku z sytuacją na Białorusi i udziałem Białorusi w agresji Rosji 
                wobec Ukrainy (dalej jako „Rozporządzenie 765/2006”),<br/>
                b) nie jest wymieniony w wykazach określonych w rozporządzeniu Rady (UE) nr 269/2014 z dnia 17 marca 2014 r. 
                w sprawie środków ograniczających w odniesieniu do działań podważających integralność terytorialną, 
                suwerenność i niezależność Ukrainy lub im zagrażających (dalej jako „Rozporządzenie 269/2014”),<br/>
                c) wobec Beneficjenta nie została wydana decyzja w sprawie wpisu na listę osób i podmiotów, wobec których są 
                stosowane środki w celu przeciwdziałania wspieraniu agresji Federacji Rosyjskiej na Ukrainę, z zastosowaniem 
                środka w postaci wykluczenia z postępowania o udzielenie zamówienia publicznego lub konkursu prowadzonego 
                na podstawie ustawy z dnia 11 września 2019 r. - Prawo zamówień publicznych,<br/>
                d) Beneficjent nie jest umieszczony w wykazie cudzoziemców, których pobyt na terytorium Rzeczypospolitej Polskiej 
                jest niepożądany, o którym mowa w art. 434 ustawy z dnia 12 grudnia 2013 r. o cudzoziemcach (dalej jako „Ustawa 
                o cudzoziemcach”),<br/>
                e) w stosunku do Beneficjenta członkiem organów, pracownikiem szczebla kierowniczego lub beneficjentem rzeczywistym, 
                w rozumieniu ustawy z dnia 1 marca 2018 r. o przeciwdziałaniu praniu pieniędzy oraz finansowaniu terroryzmu, 
                ani ich krewnym (przy czym na potrzeby niniejszego oświadczenia krewny, w odniesieniu do osoby fizycznej, 
                oznacza jej małżonka, rodzeństwo, zstępnych i wstępnych) nie jest osoba znajdująca się na liście osób i podmiotów, 
                wobec których są stosowane środki ograniczające, o której mowa w art. 2 ustawy o przeciwdziałaniu wspierania agresji, 
                w szczególności nie znajduje się w wykazach określonych w Rozporządzeniu 765/2006,  Rozporządzeniu 269/2014 lub 
                art. 434 Ustawy o cudzoziemcach,<br/>
                f) w stosunku do Beneficjenta jednostką dominującą w rozumieniu art. 3 ust. 1 pkt 37 ustawy z dnia 29 września 1994 r. 
                o rachunkowości nie jest podmiot wymieniony w wykazach określonych w Rozporządzeniu 765/2006 i 
                Rozporządzeniu 269/2014;<br/>
                g) żaden z udziałów w kapitale zakładowym Beneficjenta nie jest własnością bezpośrednio lub pośrednio, 
                ani nie został na nim ustanowiony zastaw ani użytkowanie na rzecz podmiotów wobec których są stosowane środki 
                ograniczające (sankcje), o których mowa w niniejszym § 2, lub jakiegokolwiek podmiotu lub osoby, która korzysta 
                z kapitału lub finansowania zapewnionego przez taki podmiot ani władz rosyjskich; przy czym na potrzeby niniejszego 
                oświadczenia przez władze rosyjskie należy rozumieć Federację Rosyjską (i jej kraje związkowe), federalne i lokalne 
                władze państwowe, państwowe jednostki organizacyjne i przedsiębiorstwa państwowe, instytucje publiczne, wszelkie 
                spółki i podmioty bezpośrednio lub pośrednio kontrolowane przez wyżej wymienione oraz wszelkie podmioty powiązane 
                z wyżej wymienionymi.<br/><br/>
                
                3. Ponadto Beneficjent oświadcza, że nie znajduje się na liście osób i podmiotów, wobec których są stosowane środki 
                ograniczające (sankcje) nałożone przez Organizację Narodów Zjednoczonych, państwo członkowskie Organizacji Narodów 
                Zjednoczonych lub każdą inną organizację międzyrządową wprowadzone w związku z naruszeniem integralności terytorialnej 
                Ukrainy i inwazją na Ukrainę (w tym również aneksją Krymu i konfliktem w regionie Donbasu) przeciwko Federacji Rosyjskiej, 
                Białorusi, wskazanym osobom fizycznym i podmiotom.<br/><br/>
                
                § 2<br/>
                1. Beneficjent przyjmuje do wiadomości, że oświadczenia Beneficjenta, o których mowa w § 1 powyżej,  dotyczą środków 
                ograniczających (sankcji), które obowiązują w dniu zawarcia Umowy i powinny pozostać prawdziwe przez cały okres 
                obowiązywania Umowy.<br/>
                2. Beneficjent zobowiązuje się monitorować swoje inwestycje, relacje biznesowe i działalność gospodarczą/zawodową  
                w celu zapewnienia zgodności z wyżej wymienionymi oświadczeniami, przy jednoczesnym dochowaniu należytej staranności 
                ogólnie wymaganej w relacjach biznesowych.<br/>
                3. Beneficjent zobowiązuje się niezwłocznie poinformować Polski Instytut Sztuki Filmowej o każdej zmianie okoliczności, 
                o których mowa w § 1 powyżej, które wystąpiły, powstały lub istniały przed dniem zawarcia Umowy, a których nie był świadomy, 
                lub które wystąpiły, powstały lub zaistniały po zawarciu Umowy. <br/><br/>
                
                § 3<br/>
                1. W przypadku nieprawdziwości któregokolwiek ze złożonych oświadczeń, o których mowa w § 1 powyżej, 
                Polski Instytut Sztuki Filmowej jest uprawniony do wypowiedzenia  Umowy w trybie natychmiastowym i żądania zwrotu 
                przekazanych środków finansowych wraz z odsetkami ustawowymi za opóźnienie liczonymi od dnia  przekazania środków, 
                w terminie wskazanym przez Polski Instytut Sztuki Filmowej, jednak nie dłuższym niż 14 dni od dnia doręczenia wezwania zwrotu.<br/>
                2. Bez uszczerbku dla postanowień ust. 1,  w przypadku, w którym na skutek niepełnych, nierzetelnych lub nieprawdziwych 
                oświadczeń Beneficjenta na Polski Instytut Sztuki Filmowej  nałożona zostanie jakakolwiek kara administracyjna, 
                Beneficjent zobowiązuje się do zwrotu - regresowo na wezwanie Polskiego Instytutu Sztuki Filmowej  - całości pokrytych kar 
                oraz wszelkich związanych z tym wydatków, włączając koszty postępowania sądowego, arbitrażowego, administracyjnego 
                lub ugodowego oraz koszty pomocy prawnej.
            """,
            name="applicantsStatementOfNoTies",
            required=True,
        )

    def producer_statement_screening_to_all_cinemas(self):
        return self.create_component(
            component_type="checkbox",
            label="film będzie oferowany do wyświetlania wszystkim podmiotom prowadzącym kina na terenie Polski, w szczególności w okresie premierowym, przy poszanowaniu zasad zapewniających uczciwą konkurencję.",
            name="producerStatementScreeningToAllCinemas",
            required=True,
        )

    def screening_requirement_no_more_than_two(self):
        return self.create_component(
            component_type="checkbox",
            label="warunkiem udostępnienia filmu podmiotom prowadzącym kina jedno i dwusalowe nie może być wymóg wyświetlania więcej niż dwóch seansów dziennie w przeliczeniu na jedną salę kinową.",
            name="screeningRequirementNoMoreThanTwo",
            required=True,
        )

    def film_had_no_public_screening(self):
        return self.create_component(
            component_type="checkbox",
            label="film nie miał publicznego pokazu",
            name="filmHadNoPublicScreeneing",
            required=True,
        )


class ApplicationAttachments(FormBuilderBase):
    def __init__(self):
        super().__init__()

    def description_of_artistic_qualities(self):
        return self.create_component(
            component_type="textarea",
            label="Opis walorów artystycznych i ekonomicznych przedsięwzięcia, tj. uzasadnienie przedsięwzięcia pod kątem kryteriów, o których mowa w art. 22. ust. 3 Ustawy o kinematografii",
            name="descriptionOfArtisticQualities",
            validators=[
                self.validator.length_validator(
                    max_value=5400
                )
            ],
            required=True,
        )

    def expected_results_indicator(self):
        return self.create_component(
            component_type="textarea",
            label="Wskaźniki oczekiwanych rezultatów przedsięwzięcia, tj. w szczególności krótka charakterystyka odbiorców filmu, spodziewana liczba widzów, estymacja rentowności filmu, potencjał festiwalowy",
            name="expectedResultsIndicator",
            validators=[
                self.validator.length_validator(
                    max_value=5400
                )
            ],
            required=True,
        )
