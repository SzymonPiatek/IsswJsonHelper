from classes.form_builder.departments.duk._2026.application_builder import DUKApplicationBuilder2026
from classes.helpers import int_to_roman


class EducationApplicationBuilder(DUKApplicationBuilder2026):
    def __init__(self):
        super().__init__()

        self.basic_number_data = None

    def create_application_scope_of_project(self, number):
        part = self.create_part(
            title=f"{int_to_roman(number)}. Zakres przedsięwzięcia i jego charakterystyka",
            short_name=f"{int_to_roman(number)}. Zakres przedsięwzięcia",
            chapters=[
                self.create_chapter(
                    title="1. Miejsce realizacji przedsięwzięcia",
                    components=[
                        self.create_component(
                            name="projectLocation",
                            component_type="textarea",
                            validators=[
                                self.validator.length_validator(
                                    max_value=3000
                                )
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Zakres przedsięwzięcia i jego charakterystyka",
                    components=[
                        self.create_chapter(
                            title="Opis przedsięwzięcia",
                            help_text="Cel i zakres merytoryczny, zastosowane technologie, sposób realizacji przedsięwzięcia, promocja.",
                            components=[
                                self.create_component(
                                    name="generalProjectDescription",
                                    component_type="textarea",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=3000
                                        )
                                    ],
                                    required=True,
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Wartość merytoryczna oferty dydaktycznej",
                            help_text="W tym ciągłość realizacji oraz wartość edukacyjna przedsięwzięcia.",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="offerEducationalValue",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=3000
                                        )
                                    ],
                                    required=True,
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Innowacyjność w zakresie metod nauczania, z uwzględnieniem produkcji filmowej",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="teachingMethodsInnovation",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=3000
                                        )
                                    ],
                                    required=True,
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Umiejętności lub kompetencje zawodowe nabywane przez studentów",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="skillsAcquiredByStudents",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=3000
                                        )
                                    ],
                                    required=True,
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Liczba i zróżnicowanie struktury studentów",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="numberAndDiversityOfStudents",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=3000
                                        )
                                    ],
                                    required=True,
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Doświadczenie wnioskodawcy i kompetencje zespołu",
                            help_text="Proszę o wyszczególnienie przedsięwzięć z zakresu kinematografii realizowanych przez wnioskodawcę w ostatnich 2 latach.",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="applicantAndTeamExperience",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=3000
                                        )
                                    ],
                                    required=True
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Dostępność przedsięwzięcia",
                            help_text="Działania podejmowane na rzecz osób ze szczególnymi potrzebami oraz wspierania inkluzywności.",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="projectAccessibility",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=3000
                                        )
                                    ],
                                    required=True
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Planowane efekty realizacji przedsięwzięcia oraz jego ewaluacja",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="plannedImplementationAndEvaluationEffects",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=3000
                                        )
                                    ],
                                    required=True,
                                )
                            ]
                        )
                    ]
                )
            ]
        )

        if self.basic_number_data:
            part["chapters"].append(self.basic_number_data)

        self.save_part(part)
