from classes.form_builder.dpf.application_builder import DPFApplicationBuilder


class FamilyFilmApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'VII. Produkcja filmów kina familijnego'
    PRIORITY_NUM = 7
    FORM_ID = 9199

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.department_data_path / 'family_film'

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
                self.section.application_basic_data.scope_of_project_kind(
                    number="2",
                    options=[
                        "film kina familijnego"
                    ]
                ),
                self.section.application_basic_data.movie_kind(
                    number="3",
                    options=[
                        "fabularny",
                        "dokumentalny",
                        "animowany"
                    ]
                ),
                self.section.application_basic_data.movie_subject(
                    number="4",
                    options=[
                        "film dla młodego widza lub widowni familijnej"
                    ],
                    is_film_about_history=True
                ),
                self.section.application_basic_data.piece_title(
                    number="5",
                ),
                self.section.application_basic_data.short_movie_description(
                    number="6",
                ),
                self.section.application_basic_data.category_of_project(
                    number="7",
                    options=[
                        "produkcja krajowa",
                        "koprodukcja międzynarodowa większościowa"
                    ]
                ),
                self.section.application_basic_data.application_relates(
                    number="8",
                    options=[
                        "promesa",
                        "umowa"
                    ]
                ),
                self.section.application_basic_data.kind_of_support(
                    number="9",
                    options=[
                        "dotacja",
                        "pożyczka",
                        "poręczenie"
                    ]
                ),
                self.create_chapter(
                    title="10. Wybór lidera komisji eksperckiej",
                    components=[
                        self.section.application_basic_data.one_stage_commission(
                            number="10",
                        )
                    ]
                )
            ]
        )

        self.save_part(part=part)
