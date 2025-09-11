from classes.form_builder.dpf.application_builder import DPFApplicationBuilder


class FilmProjectDevelopmentApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'II. Rozwój projektów filmowych'
    PRIORITY_NUM = 2
    FORM_ID = 9195

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.department_data_path / 'film_project_development'

    def create_application_metadata(self, task_type: str = 'Przygotowania projektów filmowych'):
        DPFApplicationBuilder.create_application_metadata(self, task_type)

    def create_application_basic_data(self):
        part = self.create_part(
            title='I. Dane podstawowe',
            short_name='I. Dane podstawowe',
            chapters=[
                self.section.application_basic_data.scope_of_project(
                    number='1',
                    options=[
                        "Rozwój projektu"
                    ]
                ),
                self.section.application_basic_data.movie_kind(
                    number='2',
                    options=[
                        "fabularny",
                        "dokumentalny",
                        "animowany",
                        "seria animowana"
                    ]
                ),
                self.section.application_basic_data.scope_of_project_kind(
                    number='3',
                    options=[
                        "rozwój projektu",
                        "seria animowana"
                    ],
                    calculation_rules=[
                        self.calculation_rule.assign_value(
                            options=[
                                {
                                    "fieldName": "movieKind",
                                    "value": "fabularny",
                                    "inputValue": "rozwój projektu"
                                },
                                {
                                    "fieldName": "movieKind",
                                    "value": "animowany",
                                    "inputValue": "rozwój projektu"
                                },
                                {
                                    "fieldName": "movieKind",
                                    "value": "dokumentalny",
                                    "inputValue": "rozwój projektu"
                                },
                                {
                                    "fieldName": "movieKind",
                                    "value": "seria animowana",
                                    "inputValue": "seria animowana"
                                }
                            ]
                        )
                    ]
                ),
                self.section.application_basic_data.movie_subject(
                    number='4',
                    options=[
                        "film autorski",
                        "film o tematyce historycznej",
                        "film dla młodego widza i widowni familijnej"
                    ],
                    validators=[
                        self.validator.related_allowed_options_validator(
                            field_name='movieKind',
                            mapping={
                                "fabularny": [
                                    "film autorski",
                                    "film o tematyce historycznej",
                                    "film dla młodego widza i widowni familijnej"
                                ],
                                "animowany": [
                                    "film autorski",
                                    "film o tematyce historycznej",
                                    "film dla młodego widza i widowni familijnej"
                                ],
                                "dokumentalny": [
                                    "film autorski",
                                    "film o tematyce historycznej",
                                    "film dla młodego widza i widowni familijnej"
                                ],
                                "seria animowana": [
                                    "film dla młodego widza i widowni familijnej"
                                ]
                            }
                        )
                    ]
                ),
                self.section.application_basic_data.piece_title(
                    number='5',
                ),
                self.section.application_basic_data.short_movie_description(
                    number='6',
                ),
                self.section.application_basic_data.category_of_project(
                    number='7',
                    options=[
                        "produkcja krajowa",
                        "koprodukcja międzynarodowa większościowa"
                    ]
                ),
                self.section.application_basic_data.application_relates(
                    number='8',
                    options=[
                        "umowa"
                    ]
                ),
                self.section.application_basic_data.kind_of_support(
                    number='9',
                    options=[
                        "dotacja",
                        "pożyczka",
                        "poręczenie"
                    ]
                ),
                self.create_chapter(
                    title="10. Wybór lidera komisji eksperckiej",
                    components=[
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="movieKind",
                                    values=[
                                      "animowany",
                                      "seria animowana"
                                    ]
                                )
                            ],
                            components=[
                                self.section.application_basic_data.one_stage_commission(
                                    number="10"
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="movieKind",
                                    values=[
                                        "fabularny",
                                        "dokumentalny"
                                    ]
                                )
                            ],
                            components=[
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="movieKind",
                                            values=[
                                                "fabularny"
                                            ]
                                        )
                                    ],
                                    components=[
                                        self.section.application_basic_data.two_stages_commission(
                                            number="10",
                                            options=[
                                                "Lider: Beata Pisula",
                                                "Lider: Joanna Kos Krauze",
                                                "Lider: Anna Kazejak"
                                            ],
                                            after_name="fab"
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="movieKind",
                                            values=[
                                                "dokumentalny"
                                            ]
                                        )
                                    ],
                                    components=[
                                        self.section.application_basic_data.two_stages_commission(
                                            number="10",
                                            options=[
                                                "Lider: Małgorzata Prociak",
                                                "Lider: Jakub Mikurda",
                                                "Lider: Bartosz Paduch"
                                            ],
                                            after_name="doc"
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
