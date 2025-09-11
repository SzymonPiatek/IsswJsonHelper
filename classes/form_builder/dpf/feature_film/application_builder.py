from classes.form_builder.dpf.application_builder import DPFApplicationBuilder


class FeatureFilmApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'III. Produkcja filmów fabularnych'
    PRIORITY_NUM = 3
    FORM_ID = 9196

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.department_data_path / 'feature_film'

    def create_application_basic_data(self):
        part = self.create_part(
            title='I. Dane podstawowe',
            short_name='I. Dane podstawowe',
            chapters=[
                self.section.application_basic_data.scope_of_project(
                    number="1",
                    options=[
                        "Produkcja filmowa",
                    ]
                ),
                self.section.application_basic_data.scope_of_project_kind(
                    number="2",
                    options=[
                        "film fabularny"
                    ]
                ),
                self.section.application_basic_data.movie_kind(
                    number="3",
                    options=[
                        "fabularny"
                    ]
                ),
                self.section.application_basic_data.movie_subject(
                    number="4",
                    options=[
                        "film autorski",
                        "film o tematyce historycznej"
                    ]
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
                        self.section.application_basic_data.two_stages_commission(
                            number="10",
                            options=[
                                "Lider: Leszek Dawid",
                                "Lider: Sławomir Fabicki",
                                "Lider: Paweł Laskowski",
                                "Lider: Renata Czarnkowska-Listoś",
                                "Lider: Izabela Igel"
                            ]
                        )
                    ]
                )
            ]
        )

        self.save_part(part)

    def create_application_attachments(self):
        part = self.create_part(
            title="VII. Załączniki",
            short_name="VII. Załączniki",
            chapters=[
                self.section.application_attachments.common_part(),
                self.section.application_attachments.factual_report_on_goals_and_effects_of_development_of_film_project(),
                self.section.application_attachments.declaration_of_division_of_rights_coproduced_by_television_broadcaster(),
                self.section.application_attachments.film_promotion_and_distribution_plan(),
                self.section.application_attachments.feature_attachments(),
                self.section.application_attachments.opinion_of_the_historian(),
                self.section.application_attachments.other_additional_attachments()
            ]
        )

        self.save_part(part=part)
