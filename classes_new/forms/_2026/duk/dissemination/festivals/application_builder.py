from classes_new.forms._2026.duk.dissemination.application_builder import \
    DisseminationOperationalProgramApplicationFormBuilder
from .estimate_data import estimate_sections
from classes_new.forms._2026.duk.estimate.application_estimate_builder import DUKApplicationEstimateBuilder
from classes_new.forms._2026.duk.pisf_structure import FestivalsPriority


class FestivalsPriorityApplicationFormBuilder(DisseminationOperationalProgramApplicationFormBuilder):
    def __init__(self):
        super().__init__(
            priority=FestivalsPriority()
        )

        self.form_id = self.set_ids(
            local_id=16408,
            uat_id=None
        )

        # Variables
        self.project_type = [
            "Organizacja festiwali filmowych o charakterze ogólnopolskim lub międzynarodowym, będących wydarzeniami cyklicznymi, obejmujących szeroki program filmowy, sekcje konkursowe oceniane przez jury oraz wydarzenia towarzyszące, takie jak spotkania z twórcami, panele dyskusyjne czy warsztaty"
        ]

        # Estimate
        estimate_builder = DUKApplicationEstimateBuilder(estimate_sections=estimate_sections)
        self.estimate_chapters = [
            estimate_builder.generate_estimate()
        ]

    def create_application_scope_of_project(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Zakres i charakterystyka przedsięwzięcia",
            short_name=f"{self.helpers.int_to_roman(number)}. Zakres przedsięwzięcia",
            chapters=[
                self.create_chapter(
                    title="Nazwa przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="applicationTaskNameRepeatPage4",
                            read_only=True,
                            calculation_rules=[
                                self.calculation_rule.copy_value(
                                    from_name="applicationTaskName"
                                )
                            ],
                            required=True
                        )
                    ]
                ),
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
                            help_text="Misja i wartości festiwalu oraz charakter przezentowanego kina.",
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
                            help_text="Repertuar, konkursy, sekcje, jury.",
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
                            help_text="Liczba, rodzaj i wysokość przyznawanych nagród.",
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
                            help_text="Np. spotkania z twórcami, warsztaty, retrospektywy, prelekcje.",
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
                            help_text="Doświadczenie wnioskodawcy w organizacji wydarzeń filmowych i kulturalnych oraz kompetencje zespołu odpowiedzialnego za realizację festiwalu.",
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
                            help_text="Plan promocji, działania marketingowe, współprace, partnerzy i patroni medialni.",
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
                            help_text="Działania podejmowane na rzecz osób ze szczególnymi potrzebami oraz wspieranie inkluzywności.",
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
                            title="Profil publiczności i odbiorcy festiwalu",
                            help_text="Do kogo kierowane jest wydarzenie oraz jakie grupy uczestników stanowią jego główną widownię (np. studenci szkół filmowych, seniorzy, widzowie zainteresowani kinem niezależnym).",
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
                            help_text="Spodziewane rezultaty realizacji festiwalu w ujęciu jakościowym.",
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
            title=f"{self.helpers.int_to_roman(number)}. Załączniki",
            short_name=f"{self.helpers.int_to_roman(number)}. Załączniki",
            chapters=[
                self.create_chapter(
                    title="1. Obowiązkowe załączniki",
                    components=[
                        self.section.application_attachment.document_confirming_represent_applicant(),
                        self.section.application_attachment.schedule_information(),
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
