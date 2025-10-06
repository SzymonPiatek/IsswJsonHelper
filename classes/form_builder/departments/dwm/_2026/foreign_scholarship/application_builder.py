from ..application_builder import DWMApplicationBuilder2026
from ..priority import ForeignScholarshipPriority


class ForeignScholarshipApplicationBuilder(DWMApplicationBuilder2026, ForeignScholarshipPriority):
    FORM_ID = 9193

    def __init__(self):
        super().__init__()

    def create_base(self):
        self.output_json = self.create_form(
            intro_text=[
                "Wniosek o ustanowaienie stypendium w ramach Programów Operacyjnych Polskiego Instytutu Sztuki Filmowej"
            ]
        )

    def create_application_metadata(self):
        part = self.create_part(
            title="I. Metadane wniosku",
            short_name="I. Metadane wniosku",
            chapters=[
                self.create_chapter(
                    title="1. Program",
                    components=[
                        self.create_component(
                            component_type="text",
                            name="programName",
                            read_only=True,
                            value=self.operation_name
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Priorytet",
                    components=[
                        self.create_component(
                            component_type="text",
                            name="priorityName",
                            read_only=True,
                            value=self.priority_name
                        )
                    ]
                ),
                self.create_chapter(
                    title="3. Czy przedsięwzięcie jest związane z udziałem w targach branżowych, pitchingach lub prezentacjach Work in Progress?",
                    components=[
                        self.create_component(
                            component_type="radio",
                            name="wasRelatedToParticipation",
                            options=[
                                "Tak",
                                "Nie"
                            ],
                            required=True
                        )
                    ]
                )
            ]
        )
        self.save_part(part)

    def create_application_name_data(self):
        part = self.create_part(
            title="II. Nazwa przedsięwzięcia, którego dotyczy wniosek",
            short_name="II. Nazwa przedsięwzięcia",
            chapters=[
                self.section.application_name_data.application_task_name(number="1"),
                self.section.application_name_data.events_names_and_dates(number="2"),
                self.section.application_name_data.country_and_city_of_events(number="3"),
                self.create_chapter(
                    title="4. Forma udziału Wnioskodawcy w wydarzeniu",
                    components=[
                        self.create_component(
                            component_type="radio",
                            options=[
                                "online",
                                "stacjonarnie/hybrydowo"
                            ],
                            name="eventParticipationType",
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="5. Czy wniosek jest składany przynajmniej 30 dni przed rozpoczęciem wydarzenia?",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    name="isApplicationSubmittedEarly",
                                    options=[
                                        "Tak",
                                        "Nie"
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="isApplicationSubmittedEarly",
                                    values=[
                                        "Nie"
                                    ]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    label="Proszę o wskazanie powodów (zgodnie z trybem naboru i wyboru wniosków dla Priorytetu II: Stypendia zagraniczne, ust. 1 pkt 4). Brak wskazania uzasadnionych przyczyn opóźnienia może skutkować formalnym odrzuceniem wniosku",
                                    validators=[
                                        self.validator.length_validator(max_value=500)
                                    ],
                                    name="lateApplicationExplanation"
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="6. Główny cel udziały Wnioskodawcy w wydarzeniu",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    name="participationGoal",
                                    options=[
                                        "Festiwal",
                                        "Market",
                                        "Co-production market/pitching",
                                        "Warsztaty/szkolenia",
                                        "Inne wydarzenie branżowe"
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="participationGoal",
                                    values=[
                                        "Inne wydarzenie branżowe"
                                    ]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    label="Jakie?",
                                    name="otherEventDesc",
                                    validators=[
                                        self.validator.length_validator(max_value=100)
                                    ],
                                    required=True
                                )
                            ]
                        )
                    ]
                ),
                self.section.application_name_data.project_for_event(number="7"),
                self.create_chapter(
                    title="8. Czy projekt/film został wsparty przez PISF?",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    name="wasMovieProjectSupportedByPisf",
                                    options=[
                                        "Tak",
                                        "Nie"
                                    ],
                                    required=True
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
                                    field_name="wasMovieProjectSupportedByPisf",
                                    values=[
                                        "Tak"
                                    ]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="Program operacyjny",
                                    name="movieProjectSupportedByPisfProgram",
                                    required=True,
                                    class_list=[
                                        "col-span-2",
                                        "table-full"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Priorytet",
                                    name="movieProjectSupportedByPisfPriority",
                                    required=True,
                                    class_list=[
                                        "col-span-2",
                                        "table-full"
                                    ]
                                ),
                                self.create_component(
                                    component_type="text",
                                    label="Rok przyznania dofinansowania",
                                    name="movieProjectSupportedPisfYear",
                                    required=True
                                ),
                                self.create_component(
                                    component_type="text",
                                    mask="fund",
                                    label="Kwota dofinansowania",
                                    name="movieProjectSupportedPisfAmount",
                                    unit="PLN",
                                    required=True
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
            title="III. Informacje o Wnioskodawcy",
            short_name="III. Informacje o Wnioskodawcy",
            chapters=[
                self.section.applicant_full_name(number="1"),
                self.create_chapter(
                    title="2. Funkcja pełniona przy projekcie",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="select",
                                    name="applicantRole",
                                    options=[
                                        "reżyser",
                                        "producent",
                                        "producent liniowy",
                                        "dystrybutor",
                                        "agent sprzedaży",
                                        "operator",
                                        "scenarzysta",
                                        "scenograf",
                                        "aktor/aktorka",
                                        "kompozytor",
                                        "montażysta",
                                        "kierownik produkcji",
                                        "inna"
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="applicantRole",
                                    values=[
                                        "inna"
                                    ]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="text",
                                    label="Nazwa pełnionej funkcji przy projekcie",
                                    name="applicantRoleOther",
                                    required=True
                                )
                            ]
                        )
                    ]
                ),
                self.section.responsible_person_data(number="3"),
                self.section.applicant_address(number="4", main_poland=True, contact_poland=True, main_foreign=True, contact_foreign=True),
                self.section.application_applicant_data.identification_numbers(number="5"),
                self.section.applicant_bank_data(number="6", poland=True, foreign=True),
                self.section.application_applicant_data.pisf_transfer_currency(number="7"),
                self.create_chapter(
                    title="W przypadku otrzymania dofinansowania od PISF proszę o przygotowanie umowy:</br>- w formie papierowej (do podpisu odręcznego)</br>- w formie elektronicznej (do podpisu kwalifikowanym podpisem elektronycznym)</br>Uwaga! W przypadku zmiany formy podpisania umowy Instytut może odstąpić od zawarcia umowy.",
                )
            ]
        )
        self.save_part(part=part)

    def create_application_applicant_achievements_data(self):
        part = self.create_part(
            title="IV. Dotychczasowy dorobek i doświadczenie Wnioskodawcy w dziedzinie, której wniosek dotyczy",
            short_name="IV. Dorobek Wnioskodawcy",
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

    def create_application_description_of_the_project_data(self):
        part = self.create_part(
            title="V. Opis zaplanowanego przedsięwzięcia",
            short_name="V. Opis przedsięwzięcia",
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

    def create_application_other_information_data(self):
        part = self.create_part(
            title="VIII. Inne informacje",
            short_name="VIII. Inne informacje",
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
                            label="4. Festiwale, warsztaty, pitchingi w któ®ych film / projekt dotychczas wziął udział",
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

    def create_application_financial_data(self):
        financing_source_chapters = [
            {
                "section_title": "Koszty akredytacji",
                "cost_title": "Koszty akredytacji",
                "name": "accreditation"
            },
            {
                "section_title": "Koszty noclegu",
                "cost_title": "Koszty noclegu",
                "name": "accommodation"
            },
            {
                "section_title": "Koszty transportu",
                "cost_title": "Koszty transportu",
                "name": "trasportation"
            },
            {
                "section_title": "Koszty uczesnictwa w warsztatach (jeśli dotyczy)",
                "cost_title": "Koszty uczestnictwa",
                "name": "participation"
            }
        ]

        part = self.create_part(
            title="IX. Koszty planowanego przedsięwzięcia",
            short_name="IX. Koszty przedsięwzięcia",
            class_list=[
                "full-width-grid"
            ],
            chapters=[
                self.create_chapter(
                    title="Nazwa przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="applicationTaskNameRepeat",
                            calculation_rules=[
                                self.calculation_rule.copy_value(from_name="applicationTaskName")
                            ],
                            read_only=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="<normal>Uwaga! W przypadku braku automatycznego przeliczenia wartości finansowych prosimy o użycie przycisku „Przelicz i waliduj”, który znajduje się w prawym, dolnym rogu ekranu. Wymusi to dokonanie niezbędnych przeliczeń oraz podświetli nieuzupełnione pola formularza.</normal>"
                ),
                self.create_chapter(
                    components=[
                        self.create_chapter(
                            title="1. Koszty wg źródeł finansowania",
                            class_list={
                                "main": [
                                    "table-6-top"
                                ],
                                "sub": [
                                    "table-6-top__col"
                                ]
                            },
                            components=[
                                self.create_chapter(
                                    title=chapter["section_title"],
                                    class_list={
                                        "main": [
                                            "table-6",
                                            "grid",
                                            "grid-cols-2"
                                        ],
                                        "sub": [
                                            "table-6__col"
                                        ]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="textarea",
                                            label="Rodzaj kosztów",
                                            value=chapter["cost_title"],
                                            name=f"{chapter["name"]}Costs",
                                            read_only=True
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Koszt całkowity",
                                            name=f"{chapter["name"]}CostTotal",
                                            read_only=True,
                                            unit="PLN",
                                            calculation_rules=[
                                                self.calculation_rule.sum_inputs(
                                                    fields=[
                                                        f"{chapter["name"]}CostRequestPisf",
                                                        f"{chapter["name"]}CostOwnFunds",
                                                        f"{chapter["name"]}CostPartnersSponsors",
                                                        f"{chapter["name"]}CostOtherSources"
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        f"{chapter["name"]}CostRequestPisf",
                                                        f"{chapter["name"]}CostOwnFunds",
                                                        f"{chapter["name"]}CostPartnersSponsors",
                                                        f"{chapter["name"]}CostOtherSources"
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Wniosek o dotację PISF",
                                            name=f"{chapter["name"]}CostRequestPisf",
                                            unit="PLN"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Środki własne",
                                            name=f"{chapter["name"]}CostOwnFunds",
                                            unit="PLN"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Środki innych partnerów/sponsorów",
                                            name=f"{chapter["name"]}CostPartnersSponsors",
                                            unit="PLN"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Pozostałe źródła publiczne",
                                            name=f"{chapter["name"]}CostOtherSources",
                                            unit="PLN"
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Udział wnioskowanej dotacji PISF we wskazanym rodzaju kosztów",
                                            name=f"{chapter["name"]}CostRequestPisfShare",
                                            unit="%",
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field=f"{chapter["name"]}CostRequestPisf",
                                                    divisor_field=f"{chapter["name"]}CostTotal"
                                                )
                                            ],
                                            read_only=True
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Udział środków własnych we wskazanym rodzaju kosztów",
                                            name=f"{chapter["name"]}CostOwnFundsShare",
                                            unit="%",
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field=f"{chapter["name"]}CostOwnFunds",
                                                    divisor_field=f"{chapter["name"]}CostTotal"
                                                )
                                            ],
                                            read_only=True
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Udział środków od partnerów/sponsorów we wskazanym rodzaju kosztów",
                                            name=f"{chapter["name"]}CostPartnersSponsorsShare",
                                            unit="%",
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field=f"{chapter["name"]}CostPartnersSponsors",
                                                    divisor_field=f"{chapter["name"]}CostTotal"
                                                )
                                            ],
                                            read_only=True
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Udział innych środków publicznych we wskazanym rodzaju kosztów",
                                            name=f"{chapter["name"]}CostOtherSourcesShare",
                                            unit="%",
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field=f"{chapter["name"]}CostOtherSources",
                                                    divisor_field=f"{chapter["name"]}CostTotal"
                                                )
                                            ],
                                            read_only=True
                                        )
                                    ]
                                ) for chapter in financing_source_chapters
                            ]
                        ),
                        self.create_chapter(
                            title="Źródła finansowania łącznie",
                            class_list={
                                "main": [
                                    "table-6-top"
                                ],
                                "sub": [
                                    "table-6-top__col"
                                ]
                            },
                            components=[
                                self.create_chapter(
                                    class_list={
                                        "main": [
                                            "table-6",
                                            "grid",
                                            "grid-cols-2"
                                        ],
                                        "sub": [
                                            "table-6__col"
                                        ]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Koszt całkowity",
                                            name="costTotalSum",
                                            read_only=True,
                                            unit="PLN",
                                            class_list=[
                                                "col-span-2"
                                            ],
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        f"{chapter["name"]}CostTotal" for chapter in financing_source_chapters
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        f"{chapter["name"]}CostTotal" for chapter in financing_source_chapters
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Wniosek o dotację PISF",
                                            name="costRequestPisfSum",
                                            read_only=True,
                                            unit="PLN",
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        f"{chapter["name"]}CostRequestPisf" for chapter in financing_source_chapters
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        f"{chapter["name"]}CostRequestPisf" for chapter in financing_source_chapters
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Środki własne",
                                            name="costOwnFundsSum",
                                            read_only=True,
                                            unit="PLN",
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        f"{chapter["name"]}CostOwnFunds" for chapter in financing_source_chapters
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        f"{chapter["name"]}CostOwnFunds" for chapter in financing_source_chapters
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Środki innych partnerów/sponsorów",
                                            name="costPartnersSponsorsSum",
                                            read_only=True,
                                            unit="PLN",
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        f"{chapter["name"]}CostPartnersSponsors" for chapter in financing_source_chapters
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        f"{chapter["name"]}CostPartnersSponsors" for chapter in financing_source_chapters
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            mask="fund",
                                            label="Pozostałe źródła publiczne",
                                            name="costOtherSourcesSum",
                                            read_only=True,
                                            unit="PLN",
                                            calculation_rules=[
                                                self.calculation_rule.dynamic_sum_inputs(
                                                    fields=[
                                                        f"{chapter["name"]}CostOtherSources" for chapter in financing_source_chapters
                                                    ]
                                                )
                                            ],
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        f"{chapter["name"]}CostOtherSources" for chapter in financing_source_chapters
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    class_list={
                                        "main": [
                                            "table-6",
                                            "grid",
                                            "grid-cols-2"
                                        ],
                                        "sub": [
                                            "table-6__col"
                                        ]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="number",
                                            label="Udział wnioskowanej dotacji PISF w kosztach razem",
                                            name="costRequestPisfSumShare",
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field="costRequestPisfSum",
                                                    divisor_field="costTotalSum"
                                                )
                                            ],
                                            read_only=True,
                                            validators=[
                                                self.validator.range_validator(
                                                    max_value=90,
                                                    message="Przekroczono maksymalny limit dofinansowania, który dla wybranego przedsięwzięcia wynosi: 90%. Wymagana będzie zgoda dyrektora PISF."
                                                )
                                            ],
                                            unit="%"
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Udział środków własnych w kosztach razem",
                                            name="costOwnFundsSumShare",
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field="costOwnFundsSum",
                                                    divisor_field="costTotalSum"
                                                )
                                            ],
                                            read_only=True,
                                            validators=[
                                                self.validator.range_validator(
                                                    min_value=10,
                                                    message="Minimalny wkład własny Wnioskodawcy powinien wynosić 10% całości budżetu przedsięwzięcia."
                                                )
                                            ],
                                            unit="%"
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Udział środków innych partnerów/sponsorów w kosztach razem",
                                            name="costPartnersSponsorsSumShare",
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field="costPartnersSponsorsSum",
                                                    divisor_field="costTotalSum"
                                                )
                                            ],
                                            read_only=True,
                                            unit="%",
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Udział innych środków publicznych w kosztach razem",
                                            name="costOtherSourcesSumShare",
                                            calculation_rules=[
                                                self.calculation_rule.share_calculator(
                                                    dividend_field="costOtherSourcesSum",
                                                    divisor_field="costTotalSum"
                                                )
                                            ],
                                            read_only=True,
                                            unit="%",
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    class_list={
                                        "main": [
                                            "table-6",
                                            "grid",
                                            "grid-cols-2"
                                        ],
                                        "sub": [
                                            "table-6__col"
                                        ]
                                    },
                                    components=[
                                        self.create_component(
                                            component_type="number",
                                            label="Udział dotacji PISF oraz innych środków publicznych w kosztach razem",
                                            name="costPisfPublicShareInTotal",
                                            calculation_rules=[
                                                self.calculation_rule.sum_inputs(
                                                    fields=[
                                                        "costRequestPisfSumShare",
                                                        "costOtherSourcesSumShare"
                                                    ]
                                                )
                                            ],
                                            read_only=True,
                                            unit="%",
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        "costRequestPisfSumShare",
                                                        "costOtherSourcesSumShare"
                                                    ]
                                                )
                                            ]
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Udział środków własnych oraz środków innych partnerów/sponsorów w kosztach razem",
                                            name="costOwnPartnersSponsorsShareInTotal",
                                            calculation_rules=[
                                                self.calculation_rule.sum_inputs(
                                                    fields=[
                                                        "costOwnFundsSumShare",
                                                        "costPartnersSponsorsSumShare"
                                                    ]
                                                )
                                            ],
                                            read_only=True,
                                            unit="%",
                                            validators=[
                                                self.validator.related_sum_validator(
                                                    field_names=[
                                                        "costOwnFundsSumShare",
                                                        "costPartnersSponsorsSumShare"
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.section.application_financial_data.other_partners_funding(number="2"),
                self.section.application_financial_data.other_public_funding(number="3"),
                self.create_chapter(
                    title="4. Dodatkowe wyjaśnienia",
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Czy któryś z kosztów został zapewniony przez organizatora wydarzenia?",
                            name="isCostsCoveredByEventOrganizer"
                        )
                    ]
                )
            ]
        )
        self.save_part(part=part)

    def create_application_statements(self):
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
                "label": "5. Oświadczenie Wnioskodawcy o braku powiązań z podmiotami sankcjonowanymi:\n\n[...]",
                "name": "applicantsStatementOfNoTies"
            }
        ]

        part = self.create_part(
            title="X. Oświadczenia Wnioskodawcy",
            short_name="X. Oświadczenia",
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

    def create_application_attachments(self):
        part = self.create_part(
            title="XI. Obowiązkowe załączniki zgodnie z rodzajem przedsięwzięcia",
            short_name="XI. Załączniki",
            chapters=[
                self.create_chapter(
                    title="A. Oficjalne zaproszenie filmu/twórcy na festiwal",
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
                ),
                self.create_chapter(
                    title="B. Lista gości zagranicznych",
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
                ),
                self.create_chapter(
                    title="C. Zaświadczenie o zakwalifikowaniu się do udziału w przedsięwzięciu",
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
                ),
                self.create_chapter(
                    title="Uwaga",
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Zapoznałem/łam się z poniższymi zasadami.<br/>- Wnioskodawca jest zobowiązany do przedstawienia rozliczenia dofinansowania zgodnie z warunkami określonymi w umowie o dofinansowanie, w tym w szczególności do przedłożenia raportu końcowego, który zawiera finansowe rozliczenie przedsięwzięcia, ocenę jakościową jego realizacji.<br/>- Do raportu końcowego należy załączyć dokumenty finansowo-księgowe potwierdzające wydatkowanie kosztów poniesionych z udzielonego dofinansowania w postaci faktur (WAŻNE: faktury muszą być wystawione na Beneficjenta jako osobę fizyczną) oraz biletów (jeśli z przyczyn obiektywnie niezależnych od Beneficjenta niemożliwe jest otrzymanie faktury) wraz z potwierdzeniem wykonania przelewów z rachunku bankowego Beneficjenta, które zostało wskazane we wniosku o dofinansowanie.<br/>- Procentowy wkład dofinansowania PISF w finalnym budżecie przedsięwzięcia nie może przekroczyć wkładu zakładanego, określonego w umowie o dofinansowanie. Jeżeli faktycznie poniesiony koszt całkowity przedsięwzięcia okazał się niższy od planowanego lub beneficjent nie wykorzystał całego dofinansowania, należy dokonać zwrotu na rachunek PISF i dostarczyć wraz z raportem potwierdzenie przelewu.<br/>- Jedynie koszty poniesione od daty złożenia wniosku o dofinansowanie w ISSW do daty zakończenia przedsięwzięcia określonej w harmonogramie, mogą zostać uznane za koszty kwalifikowalne i opłacone z dofinasowania PISF (koszty poniesione przed datą złożenia wniosku o dofinansowanie nie będą uznane za koszty kwalifikowalne).<br/>- Wniosek o dofinansowanie wraz z załącznikami należy podpisać przy użyciu kwalifikowanego podpisu elektronicznego lub profilu zaufanego platformy E-PUAP.<br/>- Wszelkie załączniki do wniosku o dofinansowanie (w tym listy intencyjne, umowy z partnerami, itp.) wymagają poświadczenia za zgodność z oryginałem. Podpisanie wniosku o dofinansowanie przez Wnioskodawcę kwalifikowanym podpisem elektronicznym lub profilem zaufanym platformy E-PUAP jest równoznaczne z poświadczeniem przez Wnioskodawcę załączników do wniosku o dofinansowanie za zgodne z oryginałem.<br/>- Linki do zasobów zewnętrznych umieszczane we wniosku o dofinansowanie powinny zachować ważność co najmniej do czasu wydania decyzji przez Dyrektora PISF.<br/>- Do dokumentów przedkładanych do wniosku o dofinansowanie sporządzonych w językach obcych należy obligatoryjnie dołączyć tłumaczenie na język polski. Wnioskodawca, na wniosek PISF, ma obowiązek przedstawić tłumaczenie przysięgłe wskazanego dokumentu.",
                            name="acknowledgeRules",
                            required=True
                        )
                    ]
                )
            ]
        )
        self.save_part(part=part)

    def create_application_schedule_data(self):
        part = self.create_part(
            title="XII. Harmonogram realizacji przedsięwzięcia",
            short_name="XII. Harmonogram",
            chapters=[
                self.create_chapter(
                    title="Nazwa przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="applicationTaskNameRepeatCopy",
                            calculation_rules=[
                                self.calculation_rule.copy_value(from_name="applicationTaskName")
                            ],
                            read_only=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="<normal>Uwaga!</br>-Harmonogram przedsięwzięcia powinien uwzględniać wszystkie działania wymienione w kosztorysie przedsięwzięcia z wyraźnie wyodrębnioną pozycją dotyczącą pobytu na wydarzeniu.</br>- Harmonogram powinien mieć charakter ciągły (brak przerw między kolejnymi pozycjami harmonogramu) w przypadku wydarzeń niezwiązanych z warsztatami.</br>- Prosimy o chronologiczne ułożenie wszystkich pozycji harmonogramu. Wymagane jest uwzględnienie przynajmniej 3 etapów realizacji przedsięwzięcia.",
                ),
                self.section.application_schedule.task_action_dates(),
                self.section.application_schedule.task_action_dates_final()
            ]
        )
        self.save_part(part=part)
