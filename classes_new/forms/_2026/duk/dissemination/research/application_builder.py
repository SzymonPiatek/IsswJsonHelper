from classes_new.forms._2026.duk.pisf_structure import ResearchPriority
from classes_new.forms._2026.duk.dissemination.application_builder import DisseminationOperationalProgramApplicationFormBuilder
from .estimate_data import estimate_sections
from classes_new.forms._2026.duk.estimate.application_estimate_builder import DUKApplicationEstimateBuilder


class ResearchPriorityApplicationFormBuilder(DisseminationOperationalProgramApplicationFormBuilder):
    def __init__(self):
        super().__init__(
            priority=ResearchPriority()
        )

        # Variables
        self.project_type = [
            "Badania widowni kinowej oraz bilansu kompetencji (ilościowe, jakościowe, cykliczne).",
            "Badania i analizy rynku kinematograficznego.",
            "Przygotowanie innowacyjnych przedsięwzięć o szczególnym znaczeniu dla rozwoju rynku audiowizualnego.",
            "Badania i analizy zjawiska tzw. piractwa w sferze kinematografii oraz działania na rzecz jego zwalczania."
        ]
        self.source_of_financing_tickets = True

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
                    title="1. Zakres przedsięwzięcia i jego charakterystyka",
                    components=[
                        self.create_chapter(
                            title="Zakres przedmiotowo-tematyczny badania",
                            help_text="Merytoryczny zakres badania, główne tematy i obszary analizy.",
                            components=[
                                self.create_component(
                                    name="subjectAndTopicScopeOfStudy",
                                    component_type="textarea",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=5000
                                        )
                                    ],
                                    required=True,
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Analiza zapotrzebowania rynku na realizację przedsięwzięcia",
                            help_text="Identyfikacja potrzeb i oczekiwań oraz zastosowanie praktyczne rezultatów badania.",
                            components=[
                                self.create_component(
                                    name="marketAnalysisForProjectImplementation",
                                    component_type="textarea",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=2000
                                        )
                                    ],
                                    required=True,
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Metody realizacji i narzędzie technologiczne zastosowane w projekcie",
                            help_text="Organizacja, przebieg i zaplecze technologiczne przedsięwzięcia, zastosowanie innowacyjnych metod badawczych.",
                            components=[
                                self.create_component(
                                    name="implementationMethodsAndTechnologicalToolsUsedInProject",
                                    component_type="textarea",
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
                            title="Grupa docelowa realizowanego przedsięwzięcia",
                            help_text="Adresaci i praktyczni użytkownicy efektów badawczych.",
                            components=[
                                self.create_component(
                                    name="targetGroup",
                                    component_type="textarea",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=1000
                                        )
                                    ],
                                    required=True,
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Doświadczenie wnioskodawcy i kompetencje zespołu",
                            help_text="W tym udział specjalistów w realizację przedsięwzięcia.",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="applicantAndTeamExperience",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=1500
                                        )
                                    ],
                                    required=True
                                ),
                            ]
                        ),
                        self.create_chapter(
                            title="Planowane efekty realizacji przedsięwzięcia i sposób ich prezentacji ",
                            help_text="Oczekiwane rezultaty badania, forma publikacji wyników oraz sposób ich rozpowszechnienia.",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="plannedEffects",
                                    validators=[
                                        self.validator.length_validator(
                                            max_value=1000
                                        )
                                    ],
                                    required=True
                                ),
                            ]
                        ),
                    ]
                )
            ]
        )
        self.save_part(part)
