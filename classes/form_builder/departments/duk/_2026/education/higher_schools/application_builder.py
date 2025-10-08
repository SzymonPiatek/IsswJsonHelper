from classes.helpers import int_to_roman
from .estimate_data import estimate_sections
from classes.form_builder.departments.duk._2026.application_estimate_builder import DUKApplicationEstimateBuilder
from ..priority import HigherSchoolsPriority
from ..application_builder import EducationApplicationBuilder


class HigherSchoolsApplicationBuilder(EducationApplicationBuilder, HigherSchoolsPriority):
    FORM_ID = 9180

    def __init__(self):
        super().__init__()

        self.project_type = [
            ""
        ]

        estimate_builder = DUKApplicationEstimateBuilder(estimate_sections=estimate_sections)
        self.estimate_chapters = [
            estimate_builder.generate_estimate()
        ]

    def create_application_scope_of_project(self, number):
        part = self.create_part(
            title=f"{int_to_roman(number)}. Zakres przedsięwzięcia",
            chapters=[
                self.create_chapter(
                    title="Zakres przedsięwzięcia i jego charakterystyka",
                    components=[
                        self.create_component(
                            label="Miejsce realizacji przedsięwzięcia",
                            name="projectLocation",
                            component_type="textarea",
                            validators=[
                                self.validator.length_validator(
                                    max_value=3000
                                )
                            ],
                            required=True
                        ),
                        self.create_component(
                            label="Opis ogólny przedsięwzięcia",
                            name="generalProjectDescription",
                            component_type="textarea",
                            validators=[
                                self.validator.length_validator(
                                    max_value=3000
                                )
                            ],
                            required=True,
                            help_text="Cel i zakres merytoryczny, zastosowane technologie, sposób realizacji przedsięwzięcia, promocja."
                        )
                    ]
                ),
                self.create_chapter(
                    title="Opis szczegółowy przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="offerEducationalValue",
                            label="Wartość merytoryczna oferty dydaktycznej",
                            validators=[
                                self.validator.length_validator(
                                    max_value=3000
                                )
                            ],
                            required=True,
                            help_text="W tym ciągłość realizacji oraz wartość edukacyjna przedsięwzięcia."
                        ),
                        self.create_component(
                            component_type="textarea",
                            name="teachingMethodsInnovation",
                            label="Innowacyjność w zakresie metod nauczania, z uwzględnieniem produkcji filmowej",
                            validators=[
                                self.validator.length_validator(
                                    max_value=3000
                                )
                            ],
                            required=True,
                        ),
                        self.create_component(
                            component_type="textarea",
                            name="skillsAcquiredByStudents",
                            label="Umiejętności lub kompetencje zawodowe nabywane przez studentów",
                            validators=[
                                self.validator.length_validator(
                                    max_value=3000
                                )
                            ],
                            required=True,
                        ),
                        self.create_component(
                            component_type="textarea",
                            name="numberAndDiversityOfStudents",
                            label="Liczba i zróżnicowanie struktury studentów",
                            validators=[
                                self.validator.length_validator(
                                    max_value=3000
                                )
                            ],
                            required=True,
                        ),
                        self.create_component(
                            component_type="textarea",
                            name="plannedImplementationAndEvaluationEffects",
                            label="Planowane efekty realizacji przedsięwzięcia oraz jego ewaluacja",
                            validators=[
                                self.validator.length_validator(
                                    max_value=3000
                                )
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
                            name="applicantAndTeamExperience",
                            help_text="Proszę o wyszczególnienie przedsięwzięć z zakresu kinematografii realizowanych przez wnioskodawcę w ostatnich 2 latach.",
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
                    title="Dostępność przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="projectAccessibility",
                            help_text="Działania podejmowane na rzecz osób ze szczególnymi potrzebami oraz wspierania inkluzywności.",
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
                    title="Czy przedsięwzięcie, na które składany jest wniosek jest powiązane z innymi przedsięwzięciami, o dofinansowanie których ubiega się Wnioskodawca w bieżącym roku z innych programów operacyjnych PISF? Jeżeli tak, proszę podać nazwę przedsięwzięcia, program oraz wnioskowaną kwotę dofinansowania",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="radio",
                                    name="wasSubmittedBefore",
                                    options=["Tak", "Nie"],
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="wasSubmittedBefore",
                                    values=["Tak"])
                            ],
                            multiple_forms_rules={"minCount": 1, "maxCount": 20},
                            components=[
                                self.create_chapter(
                                    class_list=["grid", "grid-cols-3"],
                                    components=[
                                        self.create_component(
                                            component_type="text",
                                            label="Nazwa przedsięwzięcia",
                                            name="otherProjectName"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Program operacyjny",
                                            name="programmeName"
                                        ),
                                        self.create_component(
                                            component_type="text",
                                            label="Wnioskowana kwota",
                                            name="otherProjectFundingAmount",
                                            unit="PLN",
                                            mask="fund"
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

    def create_application_attachments(self, number):
        pass

    def create_application_statements(self, number):
        pass

    def create_application_schedule(self, number):
        pass
