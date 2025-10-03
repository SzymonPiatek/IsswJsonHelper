from classes.form_builder.departments.duk._2025.dissemination.application_builder import DisseminationApplicationBuilder
from classes.form_builder.departments.duk.application_builder import DUKApplicationBuilder
from classes.form_builder.departments.duk.application_estimate_builder import DUKApplicationEstimateBuilder
from classes.form_builder.departments.duk._2025.dissemination.research.estimate_data import estimate_sections_pt12345, estimate_sections_pt6


class ResearchApplicationBuilder(DisseminationApplicationBuilder):
    PRIORITY_NAME = 'V. Badania rynku audiowizualnego'
    PRIORITY_NUM = 5
    FORM_ID = 9188

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'research'

    def create_application_basic_data(self, **kwargs):
        data = {
            'projectType': {
                'options': [
                    "Badania ilościowe i jakościowe o charakterze cyklicznym, dotyczące widza kinowego oraz bilansu kompetencji",
                    "Badania rynkowe w sferze kinematografii",
                    "Przygotowanie analiz w zakresie organizacji i finansowania rynku kinematograficznego w Polsce, a także przedsięwzięć wspierających jego systemowy rozwój",
                    "Przygotowanie innowacyjnych przedsięwzięć o szczególnym znaczeniu dla rozwoju rynku audiowizualnego",
                    "Badania i analizy zjawiska piractwa w sferze kinematografii oraz wdrażanie przedsięwzięć, których celem jest zwalczanie piractwa i zapobieganie łamaniu praw autorskich",
                    "Inne działania realizujące cele Priorytetu V"
                ]
            }
        }
        DUKApplicationBuilder.create_application_basic_data(self=self, data=data)

    def create_application_project_costs(self):
        estimate_pt12345 = DUKApplicationEstimateBuilder(
            estimate_sections=estimate_sections_pt12345,
            after_name="Pt12345"
        )
        estimate_pt6 = DUKApplicationEstimateBuilder(
            estimate_sections=estimate_sections_pt6,
            after_name="Pt6"
        )

        part = self.create_part(
            title="VII. Kosztorys przedsięwzięcia",
            short_name="VII. Kosztorys przedsięwzięcia",
            chapters=[
                estimate_pt12345.generate_estimate_top(),
                estimate_pt12345.generate_estimate_headers(),
                self.create_chapter(
                    components=[
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Badania ilościowe i jakościowe o charakterze cyklicznym, dotyczące widza kinowego oraz bilansu kompetencji",
                                        "Badania rynkowe w sferze kinematografii",
                                        "Przygotowanie analiz w zakresie organizacji i finansowania rynku kinematograficznego w Polsce, a także przedsięwzięć wspierających jego systemowy rozwój",
                                        "Przygotowanie innowacyjnych przedsięwzięć o szczególnym znaczeniu dla rozwoju rynku audiowizualnego",
                                        "Badania i analizy zjawiska piractwa w sferze kinematografii oraz wdrażanie przedsięwzięć, których celem jest zwalczanie piractwa i zapobieganie łamaniu praw autorskich"
                                    ]
                                )
                            ],
                            components=[
                                estimate_pt12345.generate_estimate(),
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Inne działania realizujące cele Priorytetu V"
                                    ]
                                )
                            ],
                            components=[
                                estimate_pt6.generate_estimate()
                            ]
                        )
                    ]
                ),
                estimate_pt12345.generate_estimate_bottom()
            ]
        )

        self.save_part(part=part)

    def create_application_scope_of_project(self):
        part = self.create_part(
            title="III. Zakres przedsięwzięcia i jego charakterystyka",
            short_name="III. Zakres przedsięwięcia",
            chapters=[
                self.create_chapter(
                    title="Miejsce realizacji i rodzaj organizowanego przedsięwzięcia",
                    components=[
                        self.create_chapter(
                            components=[
                                self.component.project_location()
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Opis przedsięwzięcia",
                    components=[
                        self.create_chapter(
                            title="<normal>Cel przedsięwzięcia</normal>",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="projectGoal",
                                    validators=[
                                        self.validator.length_validator(max_value=1000)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="<normal>Charakter przedsięwzięcia</normal>",
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Badania i analizy zjawiska piractwa w sferze kinematografii oraz wdrażanie przedsięwzięć, których celem jest zwalczanie piractwa i zapobieganie łamaniu praw autorskich"
                                    ]
                                )
                            ],
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
                                    component_type="checkbox",
                                    label="Edukacyjny",
                                    name="isEducationalProject"
                                ),
                                self.create_component(
                                    component_type="checkbox",
                                    label="Informacyjny",
                                    name="isInformativeProject"
                                ),
                                self.create_component(
                                    component_type="checkbox",
                                    label="Legislacyjny",
                                    name="isLegislativeProject"
                                ),
                                self.create_component(
                                    component_type="checkbox",
                                    label="Badawczy",
                                    name="isResearchProject"
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="<normal>Zakres merytoryczny przedsięwzięcia</normal>",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="projectScope",
                                    validators=[
                                        self.validator.length_validator(max_value=1000)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="<normal>Zastosowane techonologie</normal>",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="utilizedTechnologies",
                                    validators=[
                                        self.validator.length_validator(max_value=1000)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="<normal>Sposób realizacji przedsięwzięcia</normal>",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="implementationMethod",
                                    validators=[
                                        self.validator.length_validator(max_value=1000)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="<normal>Promocja przedsięwzięcia</normal>",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="projectPromotion",
                                    validators=[
                                        self.validator.length_validator(max_value=1000)
                                    ],
                                    required=True
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Badania ilościowe i jakościowe o charakterze cyklicznym, dotyczące widza kinowego oraz bilansu kompetencji",
                                        "Badania rynkowe w sferze kinematografii",
                                        "Przygotowanie analiz w zakresie organizacji i finansowania rynku kinematograficznego w Polsce, a także przedsięwzięć wspierających jego systemowy rozwój",
                                        "Przygotowanie innowacyjnych przedsięwzięć o szczególnym znaczeniu dla rozwoju rynku audiowizualnego",
                                        "Inne działania realizujące cele Priorytetu V"
                                    ]
                                )
                            ],
                            components=[
                                self.create_chapter(
                                    title="<normal>Celowość, innowacyjność i wieloaspektowość podjętej tematyki na tle dostępnych wyników badań polskich i światowych</normal>",
                                    components=[
                                        self.create_component(
                                            component_type="textarea",
                                            name="projectInnovativeness",
                                            validators=[
                                                self.validator.length_validator(max_value=1000)
                                            ],
                                            required=True
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>Jakie aktualne trendy w projektach badawczych i ewaluacyjnych w Polsce i na świecie uwzględnia przedsięwzięcie</normal>",
                                    components=[
                                        self.create_component(
                                            component_type="textarea",
                                            name="currentResearchTrends",
                                            validators=[
                                                self.validator.length_validator(max_value=1000)
                                            ],
                                            required=True
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>Udział autorytetów międzynarodowych i specjalistów w danej dziedzinie</normal>",
                                    components=[
                                        self.create_component(
                                            component_type="textarea",
                                            name="expertsParticipation",
                                            validators=[
                                                self.validator.length_validator(max_value=1000)
                                            ],
                                            required=True
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>Jaki obszar wiedzy o filmie diagnozuje przedsięwzięcie</normal>",
                                    components=[
                                        self.create_component(
                                            component_type="textarea",
                                            name="movieResearchField",
                                            validators=[
                                                self.validator.length_validator(max_value=1000)
                                            ],
                                            required=True
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="Charakterystyka respondentów podlegających badaniu",
                                    components=[
                                        self.create_chapter(
                                            title="<normal>Wiek</normal>",
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
                                                    label="Wiek od",
                                                    name="ageFrom",
                                                    validators=[
                                                        self.validator.range_validator(
                                                            min_value=0,
                                                            max_value=100
                                                        )
                                                    ],
                                                    required=True
                                                ),
                                                self.create_component(
                                                    component_type="number",
                                                    label="Wiek do",
                                                    name="ageTo",
                                                    validators=[
                                                        self.validator.range_validator(
                                                            min_value=0,
                                                            max_value=100
                                                        )
                                                    ],
                                                    required=True
                                                )
                                            ]
                                        ),
                                        self.create_chapter(
                                            title="<normal>Płeć</normal>",
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
                                                    component_type="checkbox",
                                                    label="Kobiety",
                                                    name="sexFemale"
                                                ),
                                                self.create_component(
                                                    component_type="checkbox",
                                                    label="Mężczyźni",
                                                    name="sexMale"
                                                )
                                            ]
                                        ),
                                        self.create_chapter(
                                            title="<normal>Wykształcenie</normal>",
                                            components=[
                                                self.create_component(
                                                    component_type="textarea",
                                                    name="respondentEducationLevel",
                                                    validators=[
                                                        self.validator.length_validator(max_value=1000)
                                                    ],
                                                    required=True
                                                )
                                            ]
                                        ),
                                        self.create_chapter(
                                            title="<normal>Miejsce zamieszkania</normal>",
                                            components=[
                                                self.create_component(
                                                    component_type="textarea",
                                                    name="respondentAddress",
                                                    validators=[
                                                        self.validator.length_validator(max_value=1000)
                                                    ],
                                                    required=True
                                                )
                                            ]
                                        ),
                                        self.create_chapter(
                                            title="<normal>Inne</normal>",
                                            components=[
                                                self.create_component(
                                                    component_type="textarea",
                                                    name="respondentOtherInfo",
                                                    validators=[
                                                        self.validator.length_validator(max_value=1000)
                                                    ],
                                                    required=True
                                                )
                                            ]
                                        ),
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Badania i analizy zjawiska piractwa w sferze kinematografii oraz wdrażanie przedsięwzięć, których celem jest zwalczanie piractwa i zapobieganie łamaniu praw autorskich"
                                    ]
                                )
                            ],
                            components=[
                                self.create_chapter(
                                    title="<normal>Innowacyjność podejmowanych działań na tle dostępnej wiedzy na temat piractwa w sferze kinematografii</normal>",
                                    components=[
                                        self.create_component(
                                            component_type="textarea",
                                            name="projectPiracyInnovativeness",
                                            validators=[
                                                self.validator.length_validator(max_value=1000)
                                            ],
                                            required=True
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>Jaki obszar wiedzy o filmie diagnozuje projekt</normal>",
                                    components=[
                                        self.create_component(
                                            component_type="textarea",
                                            name="projectPiracyDiagnosis",
                                            validators=[
                                                self.validator.length_validator(max_value=1000)
                                            ],
                                            required=True
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="<normal>Dla jakiej grupy odbiorców przeznaczone jest przedsięwzięcie</normal>",
                            components=[
                                self.create_component(
                                    component_type="textarea",
                                    name="recipientsGroupKind",
                                    validators=[
                                        self.validator.length_validator(max_value=1000)
                                    ],
                                    required=True
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Planowane efekty realizacji przedsięwzięcia",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="projectOutcomes",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Dotychczasowe doświadczenia Wnioskodawcy w działaniach będących przedmiotem przedsięwzięcia. </br><normal>Proszę o wyszczególnienie przedsięwzięć z zakresu kinematografii realizowanych przez Wnioskodawcę w ostatnich 2 latach, o budżecie przekraczającym 50 000 zł</normal>",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="granteeExperience",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Partnerzy, eksperci i specjaliści zaangażowani w przedsięwzięcie i ich dotychczasowy dorobek w tym zakresie (z wyszczególnieniem stopni i tytułów naukowych oraz afiliacji instytucjonalnych)",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="projectCooperators",
                            validators=[
                                self.validator.length_validator(max_value=1000)
                            ],
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="Podstawowe dane liczbowe na temat przedsięwzięcia",
                    components=[
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Badania ilościowe i jakościowe o charakterze cyklicznym, dotyczące widza kinowego oraz bilansu kompetencji",
                                        "Badania rynkowe w sferze kinematografii",
                                        "Przygotowanie analiz w zakresie organizacji i finansowania rynku kinematograficznego w Polsce, a także przedsięwzięć wspierających jego systemowy rozwój",
                                        "Przygotowanie innowacyjnych przedsięwzięć o szczególnym znaczeniu dla rozwoju rynku audiowizualnego",
                                        "Inne działania realizujące cele Priorytetu V"
                                    ]
                                )
                            ],
                            components=[
                                self.create_chapter(
                                    title="<normal>Próba</normal>",
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
                                            label="Poprzednia edycja (jeśli dotyczy)",
                                            name="previousResearchSample",
                                            validators=[
                                                self.validator.range_validator(min_value=0)
                                            ],
                                            unit="os."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Planowana",
                                            name="currentResearchSample",
                                            validators=[
                                                self.validator.range_validator(min_value=0)
                                            ],
                                            unit="os."
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>Liczba osób prowadzących wywiady</normal>",
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
                                            label="Poprzednia edycja (jeśli dotyczy)",
                                            name="previousNumInterviewers",
                                            validators=[
                                                self.validator.range_validator(min_value=0)
                                            ],
                                            unit="os."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Planowana",
                                            name="currentNumInterviewers",
                                            validators=[
                                                self.validator.range_validator(min_value=0)
                                            ],
                                            unit="os."
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    title="<normal>Liczba ekspertów zaangażowanych w przedsięwzięcie</normal>",
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
                                            label="Poprzednia edycja (jeśli dotyczy)",
                                            name="previousNumExperts",
                                            validators=[
                                                self.validator.range_validator(min_value=0)
                                            ],
                                            unit="os."
                                        ),
                                        self.create_component(
                                            component_type="number",
                                            label="Planowana",
                                            name="currentNumExperts",
                                            validators=[
                                                self.validator.range_validator(min_value=0)
                                            ],
                                            unit="os."
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Badania i analizy zjawiska piractwa w sferze kinematografii oraz wdrażanie przedsięwzięć, których celem jest zwalczanie piractwa i zapobieganie łamaniu praw autorskich"
                                    ]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="number",
                                    label="Liczba warsztatów/kursów/szkoleń",
                                    name="numWorkshops",
                                    validators=[
                                        self.validator.length_validator(min_value=0)
                                    ],
                                    unit="szt."
                                ),
                                self.create_component(
                                    component_type="number",
                                    label="Liczba uczestników",
                                    name="numParticipants",
                                    validators=[
                                        self.validator.length_validator(min_value=0)
                                    ],
                                    unit="os."
                                ),
                                self.create_component(
                                    component_type="number",
                                    label="Liczba inicjatyw legislacyjnych",
                                    name="numLegalInitiatives",
                                    validators=[
                                        self.validator.length_validator(min_value=0)
                                    ],
                                    unit="szt."
                                ),
                                self.create_component(
                                    component_type="number",
                                    label="Liczba odbiorców",
                                    name="numRecipients",
                                    validators=[
                                        self.validator.length_validator(min_value=0)
                                    ],
                                    unit="os."
                                ),
                                self.create_component(
                                    component_type="number",
                                    label="Liczba działań medialno-marketingowych",
                                    name="numMediaActions",
                                    validators=[
                                        self.validator.length_validator(min_value=0)
                                    ],
                                    unit="szt."
                                ),
                                self.create_component(
                                    component_type="number",
                                    label="Liczba publikacji",
                                    name="numPublications",
                                    validators=[
                                        self.validator.length_validator(min_value=0)
                                    ],
                                    unit="szt."
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        self.save_part(part=part)
