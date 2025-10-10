from classes.form_builder.departments.duk._2026.dissemination.application_builder import DisseminationApplicationBuilder
from classes.form_builder.departments.duk._2026.dissemination.priority import FestivalsPriority
from classes.form_builder.departments.duk._2026.application_estimate_builder import DUKApplicationEstimateBuilder
from .estimate_data import estimate_sections
from classes.helpers import int_to_roman


class FestivalsApplicationBuilder(DisseminationApplicationBuilder, FestivalsPriority):
    FORM_ID = 20

    def __init__(self):
        super().__init__()

        self.project_type = [
            "Organizacja festiwali filmowych o charakterze ogólnopolskim lub międzynarodowym, będących wydarzeniami cyklicznymi, obejmujących szeroki program filmowy, sekcje konkursowe oceniane przez jury oraz wydarzenia towarzyszące, takie jak spotkania z twórcami, panele dyskusyjne czy warsztaty."
        ]

        estimate_builder = DUKApplicationEstimateBuilder(estimate_sections=estimate_sections)
        self.estimate_chapters = [
            estimate_builder.generate_estimate()
        ]

        self.source_of_financing_tickets = True
        self.is_basic_number_data = True

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
                        ),
                        self.create_component(
                            component_type="number",
                            label="Szacowana liczba widzów",
                            name="estimatedNumberOfViewers",
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
                            label="Liczba płatnych akredytacji",
                            name="paidAccreditations"
                        ),
                        self.create_component(
                            component_type="number",
                            label="Liczba bezpłatnych akredytacji",
                            name="freeAccreditations"
                        ),
                        self.create_component(
                            component_type="number",
                            label="Liczba płatnych biletów",
                            name="ticketsPaidNumber"
                        ),
                        self.create_component(
                            component_type="number",
                            label="Liczba bezpłatnych biletów",
                            name="ticketsFreeNumber"
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
                    title="1. Obowiązkowe załączniki",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="header",
                                    value="Harmonogram i kosztorys stanowią integralną część wniosku",
                                    name="scheduleAndCostEstimateIntegralPartOfApplication"
                                )
                            ]
                        ),
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 1,
                                "maxCount": 20
                            },
                            components=[
                                self.create_chapter(
                                    title="Załącznik",
                                    components=[
                                        self.create_component(
                                            component_type="file",
                                            name="requiredAttachment",
                                            required=True
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Inne załączniki",
                    components=[
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 1,
                                "maxCount": 20
                            },
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="file",
                                            name="additionalAttachment"
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
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
