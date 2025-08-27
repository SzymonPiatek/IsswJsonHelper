from classes.form_builder.duk.dissemination.application_builder import DisseminationApplicationBuilder
from classes.form_builder.duk.application_builder import DUKApplicationBuilder
from classes.form_builder.estimate_builder.duk.application_estimate_builder import DUKApplicationEstimateBuilder
from classes.form_builder.duk.dissemination.research.estimate_data import estimate_sections_pt12345, estimate_sections_pt6


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
