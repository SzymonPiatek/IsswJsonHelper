from classes.form_builder.departments.duk._2026.dissemination.application_builder import DisseminationApplicationBuilder
from .estimate_data import estimate_sections, estimate_section_structure
from ..priority import ReconstructionPriority
from .application_estimate_builder import ReconstructionApplicationEstimateBuilder


class ReconstructionApplicationBuilder(DisseminationApplicationBuilder, ReconstructionPriority):
    FORM_ID = 23

    def __init__(self):
        super().__init__()

        self.project_type = [
            "Rekonstrukcja cyfrowa i digitalizacja filmów polskich oraz ich przygotowanie do rozpowszechniania.",
            "Systemowe przedsięwzięcia, mające na celu zabezpieczenie materiałów filmowych."
        ]

        estimate_builder = ReconstructionApplicationEstimateBuilder(estimate_sections=estimate_sections, estimate_section_structure=estimate_section_structure)
        self.estimate_chapters = [
            estimate_builder.generate_estimate()
        ]


    def create_application_project_costs(self, number):
        estimate_base = ReconstructionApplicationEstimateBuilder(estimate_sections=[])

        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Kosztorys przedsięwzięcia",
            short_name=f"{self.helpers.int_to_roman(number)}. Kosztorys przedsięwzięcia",
            chapters=[
                estimate_base.generate_estimate_top(),
                self.create_chapter(
                    title="<p style='text-align: center;'>Koszty z podziałem na źródło finansowania<p>",
                    components=[
                        *self.estimate_chapters
                    ]
                )
            ]
        )

        self.save_part(part=part)

    def create_application_scope_of_project(self, number):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Zakres przedsięwzięcia i jego charakterystyka",
            short_name=f"{self.helpers.int_to_roman(number)}. Zakres przedsięwziecia",
            chapters=[
                self.create_chapter(
                    title="1. Typ przedsięwzięcia",
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="checkbox",
                                    name="isDigitizationOrReconstructionIndividualFilm",
                                    label="Digitalizacja/rekonstrukcja pojedynczych tytułów filmowych"
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="isDigitizationOrReconstructionIndividualFilm",
                                    values=[True]
                                )
                            ],
                            components=[
                                self.create_chapter(
                                    multiple_forms_rules={
                                        "minCount": 1,
                                        "maxCount": 10
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
                                                    component_type="text",
                                                    name="projectTitle",
                                                    label="Tytuł",
                                                    required=True,
                                                    class_list=[
                                                        "table-full"
                                                    ]
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    name="projectDirector",
                                                    label="Reżyser",
                                                    required=True
                                                ),
                                                self.create_component(
                                                    component_type="text",
                                                    name="projectYear",
                                                    label="Rok",
                                                    required=True
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="checkbox",
                                    name="isDigitizationOrReconstructionArchiveMaterial",
                                    label="Digitalizacja/rekonstrukcja zbiorów i materiałów archiwalnych"
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="isDigitizationOrReconstructionArchiveMaterial",
                                    values=[True]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="collectionNameAndChronologicalScope",
                                    label="Nazwa zbioru i zakres chronologiczny",
                                    required=True,
                                    validators=[
                                        self.validator.length_validator(max_value=500)
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Opis przedsięwzięcia i uzasadnienie rekonstrukcji",
                    help_text="Cel, wartość merytoryczna przedsięwzięcia, w tym uzasadnienie wyboru filmu lub pilność ze względów konserwatorskich, zastosowane technologie i standardy, sposób realizacji.",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="descriptionOfProjectAndJustificationOfReconstruction",
                            validators=[
                                self.validator.length_validator(max_value=5000)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="3. Rodzaj i stan materiałów źródłowych oraz pilność rekonstrukcji",
                    help_text="Proszę o wyszczególnienie przedsięwzięć z zakresu kinematografii realizowanych przez Wnioskodawcę w ostatnich 2 latach.",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="reconstructionMaterialsAndUrgency",
                            validators=[
                                self.validator.length_validator(max_value=3000)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="4. Zastosowane technologie i standardy",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="usedTechnologiesAndStandards",
                            validators=[
                                self.validator.length_validator(max_value=3000)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="5. Planowane efekty realizacji przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="plannedImplementationAndEvaluationEffects",
                            validators=[
                                self.validator.length_validator(max_value=3000)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="6. Doświadczenie wnioskodawcy i kompetencje zespołu",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="applicantAndTeamExperience",
                            validators=[
                                self.validator.length_validator(max_value=3000)
                            ],
                            required=True
                        )
                    ]
                )
            ]
        )
        self.save_part(part)
