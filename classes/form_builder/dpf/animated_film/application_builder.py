from classes.form_builder.dpf.application_builder import DPFApplicationBuilder


class AnimatedFilmApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'V. Produkcja filmów animowanych'
    PRIORITY_NUM = 5
    FORM_ID = 9198

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.department_data_path / 'animated_film'

    def create_application_basic_data(self, **kwargs):
        part = self.create_part(
            title="I. Dane podstawowe",
            short_name="I. Dane podstawowe",
            chapters=[
                self.section.application_basic_data.scope_of_project(
                    number="1",
                    options=[
                        "Produkcja filmowa"
                    ]
                ),
                self.section.application_basic_data.movie_kind(
                    number="2",
                    options=[
                        "animowany",
                        "seria animowana"
                    ]
                ),
                self.section.application_basic_data.movie_subject(
                    number="3",
                    options=[
                        "film autorski",
                        "film o tematyce historycznej",
                        "film dla młodego widza lub widowni familijnej"
                    ],
                    validators=[
                        self.validator.related_allowed_options_validator(
                            field_name="movieKind",
                            mapping={
                                "animowany": [
                                    "film autorski",
                                    "film o tematyce historycznej",
                                    "film dla młodego widza lub widowni familijnej"
                                ],
                                "seria animowana": [
                                    "film dla młodego widza lub widowni familijnej"
                                ]
                            }
                        )
                    ]
                ),
                self.section.application_basic_data.piece_title(
                    number="4",
                ),
                self.section.application_basic_data.short_movie_description(
                    number="5",
                ),
                self.section.application_basic_data.category_of_project(
                    number="6",
                    options=[
                        "produkcja krajowa",
                        "koprodukcja międzynarodowa większościowa"
                    ]
                ),
                self.section.application_basic_data.application_relates(
                    number="7",
                    options=[
                        "promesa",
                        "umowa"
                    ]
                ),
                self.section.application_basic_data.kind_of_support(
                    number="8",
                    options=[
                        "dotacja",
                        "pożyczka",
                        "poręczenie"
                    ]
                ),
                self.create_chapter(
                    title="9. Wybór lidera komisji eksperckiej",
                    components=[
                        self.section.application_basic_data.one_stage_commission(
                            number="9",
                        )
                    ]
                )
            ]
        )

        self.save_part(part=part)
