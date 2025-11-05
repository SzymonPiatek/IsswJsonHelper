from classes_new.forms._2026.duk.dissemination.application_builder import DisseminationOperationalProgramApplicationFormBuilder
from classes_new.forms._2026.duk.pisf_structure import DkfPriority
from classes_new.forms._2026.duk.estimate.application_estimate_builder import DUKApplicationEstimateBuilder
from .estimate_data import estimate_sections


class DkfPriorityApplicationFormBuilder(DisseminationOperationalProgramApplicationFormBuilder):
    def __init__(self):
        super().__init__(
            priority=DkfPriority()
        )

        self.form_id = self.set_ids(
            local_id=16413,
            uat_id=None
        )

        # Variables
        self.project_type = [
            "Działalność klubów filmowych o charakterze cyklicznym, obejmująca organizację co najmniej 10 wydarzeń rocznie realizowanych w formule: prelekcja, projekcja, dyskusja"
        ]
        self.source_of_financing_tickets = True
        self.is_dkf = True

        # Estimate
        estimate_builder = DUKApplicationEstimateBuilder(estimate_sections=estimate_sections)
        self.estimate_chapters = [
            estimate_builder.generate_estimate()
        ]

    def create_application_scope_of_project(self, number):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Zakres przedsięwzięcia i jego charakterystyka",
            short_name=f"{self.helpers.int_to_roman(number)}. Zakres przedsięwziecia",
            chapters=[
                self.create_chapter(
                    title="Nazwa przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="applicationTaskNamePage4",
                            required=True,
                            read_only=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="1. Informacje ogólne",
                    components=[
                        self.create_component(
                            component_type="radio",
                            label="Czy klub jest zrzeszony w Polskiej Federacji Dyskusyjnych Klubów Filmowych?",
                            options=[
                                "Tak", "Nie"
                            ],
                            required=True,
                            name="isClubAffiliatedWithPFDKF"
                        ),
                        self.create_component(
                            label="Miejsce realizacji przedsięwzięcia",
                            name="projectLocation",
                            component_type="textarea",
                            validators=[
                                self.validator.length_validator(
                                    max_value=500
                                )
                            ],
                            required=True
                        ),
                    ]
                ),
                self.create_chapter(
                    title="2. Zakres przedsięwzięcia i jego charakterystyka",
                    components=[
                        self.create_chapter(
                            title="Idea i opis przedsięwzięcia",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="characterAndDescriptionOfProject",
                                    validators=[
                                        self.validator.length_validator(max_value=5000)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Planowany repertuar",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="plannedReperoire",
                                    validators=[
                                        self.validator.length_validator(max_value=5000)
                                    ],
                                    required=True,
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Planowani prelegenci",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="plannedSpeakers",
                                    validators=[
                                        self.validator.length_validator(max_value=5000)
                                    ],
                                    required=True,
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Promocja przedsięwzięcia",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="projectPromotion",
                                    validators=[
                                        self.validator.length_validator(max_value=1500)
                                    ],
                                    required=True,
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Dostępność przedsięwzięcia",
                            help_text="Planowany zakres udogodnień zwiększających dostępność wydarzenia.",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="projectAccessibility",
                                    validators=[
                                        self.validator.length_validator(max_value=1000)
                                    ],
                                    required=True,
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Planowane efekty realizacji przedsięwzięcia",
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
                        self.create_chapter(
                            title="Doświadczenie wnioskodawcy i kompetencje zespołu",
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
                            label="Liczba stałych członków klubu filmowego",
                            component_type="number",
                            name="numberOfRegularFilmClubMembers",
                            unit="szt."
                        ),
                        self.create_component(
                            label="Planowana liczba spotkań",
                            component_type="number",
                            name="plannedNumberOfMeetings",
                            unit="szt."
                        ),
                        self.create_component(
                            label="Planowany procentowy udział polskich filmów (w tym koprodukcji) w repertuarze",
                            component_type="text",
                            mask="fund",
                            name="plannedPercentageOfPolishFilmReperoire",
                            unit="%"
                        ),
                        self.create_component(
                            label="Planowany procentowy udział klasyki filmowej w repertuarze",
                            component_type="text",
                            mask="fund",
                            name="plannedPercentageOfClassicalFilmReperoire",
                            unit="%"
                        )
                    ]
                )
            ]
        )
        self.save_part(part)
