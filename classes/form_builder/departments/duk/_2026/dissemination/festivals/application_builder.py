from classes.form_builder.departments.duk._2026.dissemination.application_builder import DisseminationApplicationBuilder
from classes.form_builder.departments.duk._2026.dissemination.priority import FestivalsPriority
from classes.form_builder.departments.duk._2026.estimate.application_estimate_builder import DUKApplicationEstimateBuilder
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


    def create_application_scope_of_project(self, number: int):
        part = self.create_part(
            title=f"{int_to_roman(number)}. Zakres i charakterystyka przedsięwzięcia",
            short_name=f"{int_to_roman(number)}. Zakres przedsięwzięcia",
            chapters=[
                self.create_chapter(
                    title="1. Termin i miejsce realizacji przedsięwzięcia",
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
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Zakres przedsięwzięcia i jego charakterystyka",
                    components=[
                        self.create_chapter(
                            title="Idea i profil artystyczny festiwalu",
                            help_text="Misja i wartości festiwalu oraz charakter przezentowanego kina",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="strategicFestivalGoals",
                                    validators=[
                                        self.validator.length_validator(max_value=2000)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Program festiwalu",
                            help_text="Repertuar, konkursy, sekcje, jury",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="festivalProgram",
                                    validators=[
                                        self.validator.length_validator(max_value=5000)
                                    ],
                                    required=True,
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Przyznane nagrody",
                            help_text="Liczba, rodzaj i wysokość przyznawanych nagród",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="prizesAwarded",
                                    validators=[
                                        self.validator.length_validator(max_value=1000)
                                    ],
                                    required=True,
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Wydarzenia towarzyszące",
                            help_text="Np. spotkania z twórcami, warsztaty, retrospektywy, prelekcje",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="accompanyingEvents",
                                    validators=[
                                        self.validator.length_validator(max_value=5000)
                                    ],
                                    required=True,
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Doświadczenie wnioskodawcy i kompetencje zespołu",
                            help_text="Doświadczenie wnioskodawcy w organizacji wydarzeń filmowych i kulturalnych oraz kompetencje zespołu odpowiedzialnego za realizację festiwalu",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="applicantExperienceAndTeamCompetences",
                                    validators=[
                                        self.validator.length_validator(max_value=1500)
                                    ],
                                    required=True,
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Promocja festiwalu",
                            help_text="Plan promocji, działania marketingowe, współprace, partnerzy i patroni medialni",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="festivalPromotion",
                                    validators=[
                                        self.validator.length_validator(max_value=1500)
                                    ],
                                    required=True,
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Dostępność wydarzenia",
                            help_text="Działania podejmowane na rzecz osób ze szczególnymi potrzebami oraz wspieranie inkluzywności",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="eventAccessibility",
                                    validators=[
                                        self.validator.length_validator(max_value=1000)
                                    ],
                                    required=True,
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Profil publiczności i odbiory festiwalu",
                            help_text="Do kogo kierowane jest wydarzenie oraz jakie grupy uczestników stanowią jego główną widownię (np. studenci szkół filmowych, seniorzy, widzowie zainteresowani kinem niezależnym)",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="audienceProfile",
                                    validators=[
                                        self.validator.length_validator(max_value=1000)
                                    ],
                                    required=True,
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Planowane efekty realizacji przedsięwzięcia",
                            help_text="Spodziewane rezultaty realizacji festiwalu w ujęciu jakościowym",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="plannedEffects",
                                    validators=[
                                        self.validator.length_validator(max_value=1000)
                                    ],
                                    required=True,
                                )
                            ]
                        ),
                    ]
                ),
                self.create_chapter(
                    title="<normal>Udział w przedsięwzięciach jest</normal>",
                    components=[
                        self.create_component(
                            component_type="radio",
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
                        )
                    ]
                ),
                self.create_chapter(
                    title="3. Podstawowe dane liczbowe i wskaźniki",
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
                            title="Załącznik",
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
                    title="<small>Uwaga!<br/><normal>Harmonogram zadania powinien uwzględniać wszystkie działania wymienione w kosztorysie.</br>Proszimy o chronologiczne ułożenie wszystkich pozycji harmonogramu.</br></br>Harmonogram zadania powinien uwzględniać etapy:</br>- przygotowawczy (np. poszukiwania partnerów, zaproszenie uczestników, przygotowanie promocji wydarzenia itp.);</br>- realizacji zadania (np. wykonanie i/lub wysyłka materiałów promocyjnych, pokaz filmu na festiwalu);</br>- podsumowanie (ewaluacja i rozliczenie zadania - ostateczna data zakończenia realizacji zadania: dzień, miesiąc i rok).</br></br>Wszystkie wydatki (w tym faktury, rachunki oraz inne dokumenty księgowe) muszą być poniesione i opłacone <b>w terminie realizacji zadania określonym w harmonogramie</b> - to znaczy <b>nie wcześniej niż od dnia rozpoczęcia naboru wniosków oraz nie później niż do dnia zakończenia realizacji zadania.</b></normal></small>",
                    components=[]
                ),
                self.create_chapter(
                    title="Etap przygotowawczy",
                    components=[
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 1,
                                "maxCount": 20
                            },
                            components=[
                                self.create_chapter(
                                    title="Pozycja",
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
                                            name="preparatoryStageStartDate",
                                            validators=[
                                                self.validator.related_local_date_lte_validator(
                                                    field_name="preparatoryStageEndDate",
                                                    message="Termin rozpoczęcia działania musi być wcześniejszy niż termin jego zakończenia."
                                                )
                                            ],
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="date",
                                            label="Termin do",
                                            name="preparatoryStageEndDate",
                                            validators=[
                                                self.validator.related_local_date_gte_validator(
                                                    field_name="preparatoryStageStartDate",
                                                    message="Termin zakończenia działania musi być późniejszy niż termin jego rozpoczęcia."
                                                )
                                            ],
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="textarea",
                                            label="Działanie",
                                            name="preparatoryStageDescription",
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
                    ]
                ),
                self.create_chapter(
                    title="Etap realizacji zadania",
                    components=[
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 1,
                                "maxCount": 20
                            },
                            components=[
                                self.create_chapter(
                                    title="Pozycja",
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
                                            name="implementationStageStartDate",
                                            validators=[
                                                self.validator.related_local_date_lte_validator(
                                                    field_name="implementationStageEndDate",
                                                    message="Termin rozpoczęcia działania musi być wcześniejszy niż termin jego zakończenia."
                                                )
                                            ],
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="date",
                                            label="Termin do",
                                            name="implementationStageEndDate",
                                            validators=[
                                                self.validator.related_local_date_gte_validator(
                                                    field_name="implementationStageStartDate",
                                                    message="Termin zakończenia działania musi być późniejszy niż termin jego rozpoczęcia."
                                                )
                                            ],
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="textarea",
                                            label="Działanie",
                                            name="implementationStageDescription",
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
                    ]
                ),
                self.create_chapter(
                    title="Etap podsumowania zadania",
                    components=[
                        self.create_chapter(
                            multiple_forms_rules={
                                "minCount": 1,
                                "maxCount": 20
                            },
                            components=[
                                self.create_chapter(
                                    title="Pozycja",
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
                                            name="summaryStageStartDate",
                                            validators=[
                                                self.validator.related_local_date_lte_validator(
                                                    field_name="summaryStageEndDate",
                                                    message="Termin rozpoczęcia działania musi być wcześniejszy niż termin jego zakończenia."
                                                )
                                            ],
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="date",
                                            label="Termin do",
                                            name="summaryStageEndDate",
                                            validators=[
                                                self.validator.related_local_date_gte_validator(
                                                    field_name="summaryStageStartDate",
                                                    message="Termin zakończenia działania musi być późniejszy niż termin jego rozpoczęcia."
                                                )
                                            ],
                                            required=True
                                        ),
                                        self.create_component(
                                            component_type="textarea",
                                            label="Działanie",
                                            name="summaryStageDescription",
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
                    ]
                ),
                self.create_chapter(
                    title="Podsumowanie harmonogramu",
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
                                    field="preparatoryStageStartDate",
                                )
                            ]
                        ),
                        self.create_component(
                            component_type="date",
                            label="Zakończenie realizacji przedsięwzięcia",
                            name="projectCompletion",
                            required=True
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
