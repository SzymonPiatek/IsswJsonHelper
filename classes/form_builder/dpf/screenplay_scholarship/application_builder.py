from classes.form_builder.dpf.application_builder import DPFApplicationBuilder


class ScreenplayScholarshipApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'I. Stypendia scenariuszowe'
    PRIORITY_NUM = 1
    FORM_ID = 9194

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.department_data_path / 'screenplay_scholarship'

    def create_application_metadata(self, task_type: str = 'Stypendium scenariuszowe'):
        DPFApplicationBuilder.create_application_metadata(self, task_type)

    def create_application_basic_data(self):
        part = self.create_part(
            title='I. Dane podstawowe',
            short_name='I. Dane podstawowe',
            chapters=[
                self.section.application_basic_data.scope_of_project(
                    number="1",
                    options=[
                        "Stypendium scenariuszowe"
                    ]
                ),
                self.section.application_basic_data.movie_kind(
                    number="2",
                    options=[
                        "fabularny",
                        "dokumentalny",
                        "animowany"
                    ]
                ),
                self.section.application_basic_data.scope_of_project_kind(
                    number="3",
                    options=[
                        "stypendium scenariuszowe"
                    ]
                ),
                self.section.application_basic_data.movie_subject(
                    number="4",
                    options=[
                        "film autorski",
                        "film o tematyce historycznej",
                        "film dla młodego widza i widowni familijnej"
                    ],
                    validators=[
                        self.validator.related_allowed_options_validator(
                            field_name="movieKind",
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
                                    "film o tematyce historycznej"
                                ]
                            }
                        )
                    ]
                ),
                self.section.application_basic_data.piece_title(
                    number="5",
                ),
                self.section.application_basic_data.short_movie_description(
                    number="6",
                ),
                self.section.application_basic_data.application_relates(
                    number="7",
                    options=[
                        "umowa"
                    ]
                ),
                self.section.application_basic_data.kind_of_support(
                    number="8",
                    options=[
                        "stypendium scenariuszowe"
                    ]
                )
            ]
        )

        self.save_part(part)

    def create_application_applicant_data(self, **kwargs):
        part = self.create_part(
            title="II. Dane wnioskodawcy",
            short_name="II. Dane wnioskodawcy"
        )

        sections = [
            # {
            #     "path": self.department_data_path / '_pages' / 'application_applicant_data' / 'applicant_full_name.json',
            #     "data": {
            #         "number": "1"
            #     }
            # },
            # {
            #     "path": self.priority_data_path / '_pages' / 'application_applicant_data' / 'applicant_data.json',
            #     "data": {
            #         "number": "2"
            #     }
            # },
            # {
            #     "path": self.application_data_path / '_pages' / 'application_applicant_data' / 'responsible_person.json',
            #     "data": {
            #         "number": "3"
            #     }
            # }
        ]

        self.create_part_by_sections(
            part=part,
            sections=sections
        )

    def create_application_completion_date_data(self, **kwargs):
        priority_data_path = self.priority_data_path / '_pages' / 'application_completion_date_data'

        part = self.create_part(
            title="IV. Termin realizacji",
            short_name="IV. Termin realizacji",
            chapters=[
                self.create_chapter(
                    title='Stypendium scenariuszowe',
                ),
                self.create_chapter(
                    title='Termin realizacji stypendium scenariuszowego 12 miesięcy od daty podpisania umowy',
                    components=[
                        self.load_json(path=priority_data_path / 'activity_schedule.json')
                    ]
                ),
                self.create_chapter(
                    title='OBLIGATORYJNE CZYNNOŚCI W PRZYPADKU ZAWARCIA UMOWY O DOFINANSOWANIE'
                ),
                self.create_chapter(
                    title='Akceptacja scenariusza'
                ),
                self.create_chapter(
                    title='Raport końcowy'
                ),
                self.create_chapter(
                    title='Wykonanie i udokumentowanie działań obligatoryjnych wymaganych Programem operacyjnym PISF'
                )
            ]
        )

        self.save_part(part)

    def create_application_financial_data(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_financial_data' / 'requested_pisf_support_amount.json')
        self.save_part(part)

    def create_application_statements(self):
        part = self.create_part(
            title="VIII. Oświadczenia",
            short_name="VIII. Oświadczenia",
            chapters=[
                self.section.application_statements.applicant_statements(),
                self.section.application_statements.script_statements(),
                self.section.application_statements.storage_of_blank_public_documents()
            ]
        )

        self.save_part(part)

    def create_application_attachments(self):
        part = self.create_part(
            title="VII. Załączniki",
            short_name="VII. Załączniki",
            chapters=[
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="movieKind",
                            values=[
                                "fabularny",
                                "animowany"
                            ]
                        )
                    ],
                    components=[
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="movieKind",
                                    values=["animowany"]
                                )
                            ],
                            components=[
                                self.create_chapter(
                                    components=[
                                        self.create_component(
                                            component_type="checkbox",
                                            label="Nie dotyczy zgodnie z Programem Operacyjnym PISF - Produkcja Filmowa",
                                            name="notDialogScene"
                                        )
                                    ]
                                ),
                                self.create_chapter(
                                    visibility_rules=[
                                        self.visibility_rule.depends_on_value(
                                            field_name="notDialogScene",
                                            values=[False]
                                        )
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="file",
                                            label="Scena dialogowa",
                                            name="dialogSceneAni",
                                            required=True
                                        )
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="movieKind",
                                    values=["fabularny"]
                                )
                            ],
                            components=[
                                self.create_component(
                                    component_type="file",
                                    label="Scena dialogowa",
                                    name="dialogSceneFab",
                                    required=True
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="directorVacat",
                            values=[False]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="checkbox",
                            label="Nie dotyczy zgodnie z Programem Operacyjnym PISF - Produkcja Filmowa",
                            name="notDirectorLetterOfIntention"
                        )
                    ]
                ),
                self.create_chapter(
                    visibility_rules=[
                        self.visibility_rule.depends_on_value(
                            field_name="notDirectorLetterOfIntention",
                            values=[False]
                        ),
                        self.visibility_rule.depends_on_value(
                            field_name="directorVacat",
                            values=[False]
                        )
                    ],
                    components=[
                        self.create_component(
                            component_type="file",
                            label="List intencyjny od reżysera",
                            name="directorLetterOfIntention",
                            required=True
                        )
                    ]
                ),
                self.create_chapter(
                    components=[
                        self.component.application_attachments.description_of_artistic_qualities()
                    ]
                ),
                self.section.application_attachments.other_additional_attachments()
            ]
        )

        self.save_part(part=part)
