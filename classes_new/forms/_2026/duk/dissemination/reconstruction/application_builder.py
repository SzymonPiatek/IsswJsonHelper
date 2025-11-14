from classes_new.forms._2026.duk.dissemination.application_builder import \
    DisseminationOperationalProgramApplicationFormBuilder
from classes_new.forms._2026.duk.pisf_structure import ReconstructionPriority
from .estimate_data import estimate_sections, estimate_section_structure
from .application_estimate_builder import ReconstructionApplicationEstimateBuilder


class ReconstructionPriorityApplicationFormBuilder(DisseminationOperationalProgramApplicationFormBuilder):
    def __init__(self):
        super().__init__(
            priority=ReconstructionPriority()
        )

        self.form_id = self.set_ids(
            local_id=16411,
            uat_id=None
        )

        # Variables
        self.project_type = [
            "Digitalizacja i rekonstrukcja cyfrowa polskich filmów oraz filmów o szczególnym znaczeniu dla polskiej kultury i ich przygotowanie do rozpowszechniania",
            "Przedsięwzięcia mające na celu zabezpieczenie materiałów filmowych, w tym wytwarzanie kopii analogowych dystrybucyjnych i zabezpieczających kanonicznych dzieł polskiej kinematografii"
        ]

        # Estimate
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
                                                    "new_table",
                                                    "grid",
                                                    "grid-cols-2"
                                                ],
                                                "sub": [
                                                    "new_table_2__col"
                                                ]
                                            },
                                            components=[
                                                self.create_chapter(
                                                    class_list={
                                                        "main": [
                                                            "new_table_2__2-2"
                                                        ]
                                                    },
                                                    components=[
                                                        self.create_component(
                                                            component_type="text",
                                                            name="projectTitle",
                                                            label="Tytuł",
                                                            required=True,
                                                        )
                                                    ]
                                                ),
                                                self.create_chapter(
                                                    components=[
                                                        self.create_component(
                                                            component_type="text",
                                                            name="projectDirector",
                                                            label="Reżyser",
                                                            required=True,
                                                        )
                                                    ]
                                                ),
                                                self.create_chapter(
                                                    class_list={
                                                        "main": [
                                                            "new_table",
                                                            "grid",
                                                            "grid-cols-2"
                                                        ],
                                                        "sub": [
                                                            "new_table_2__col"
                                                        ]
                                                    },
                                                    components=[
                                                        self.create_component(
                                                            component_type="text",
                                                            name="projectYear",
                                                            label="Rok",
                                                            required=True
                                                        ),
                                                        self.create_component(
                                                            component_type="number",
                                                            name="projectDuration",
                                                            label="Metraż",
                                                            required=True,
                                                            unit="min"
                                                        )
                                                    ]
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
                                    label="Nazwa zbioru, zakres chronologiczny i metraż",
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
                    help_text="Cel, wartość merytoryczna przedsięwzięcia, w tym uzasadnienie wyboru filmu i znaczenie dla kinematografii.",
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
                    title="3. Rodzaj i stan materiałów źródłowych",
                    help_text="Rodzaj dostępnych materiałów źródłowych, ich stan techniczny, kompletność oraz ewentualne uszkodzenia.",
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
                    help_text="Planowane technologie, narzędzia i standardy stosowane w procesie rekonstrukcji cyfrowej.",
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
                    help_text="Spodziewane efekty realizacji przedsięwzięcia w ujęciu jakościowym.",
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
                    help_text="Doświadczenie wnioskodawcy w rekonstrukcji cyfrowej oraz kompetencje zespołu zaangażowanego w realizację przedsięwzięcia.",
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

    def create_application_attachments(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Załączniki",
            chapters=[
                self.create_chapter(
                    title="Obowiązkowe załączniki",
                    components=[
                        self.section.application_attachment.document_confirming_represent_applicant(),
                        self.section.application_attachment.schedule_information(),
                        self.create_chapter(
                            title="Dokument potwierdzający posiadanie praw do digitalizacji/ rekonstrukcji filmu",
                            help_text="Należy załączyć umowę zawartą między Wnioskodawcą a właścicielem praw do digitalizowanego materiału filmowego lub inny dokument potwierdzający posiadanie praw do digitalizacji lub rekonstrukcji filmu.",
                            components=[
                                self.create_component(
                                    component_type="file",
                                    name="attachmentDigitalizationRights",
                                    required=True
                                )
                            ]
                        )
                    ]
                ),
                self.section.application_attachment.other_attachments()
            ]
        )
        self.save_part(part)
