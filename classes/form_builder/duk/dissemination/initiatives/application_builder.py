from classes.form_builder.duk.dissemination.application_builder import DisseminationApplicationBuilder
from classes.form_builder.duk.application_builder import DUKApplicationBuilder
from classes.form_builder.duk.application_estimate_builder import DUKApplicationEstimateBuilder
from classes.form_builder.duk.dissemination.initiatives.estimate_data import estimate_sections_pt1, estimate_sections_pt2, estimate_sections_pt3, estimate_sections_pt4


class InitiativesApplicationBuilder(DisseminationApplicationBuilder):
    PRIORITY_NAME = 'II. Inicjatywy filmowe'
    PRIORITY_NUM = 2
    FORM_ID = 9185

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'initiatives'

    def create_application_basic_data(self, **kwargs):
        data = {
            'projectType': {
                'options': [
                    "Organizacja przeglądów i innych wydarzeń filmowych o charakterze lokalnym",
                    "Działalność kin studyjnych i lokalnych",
                    "Działalność klubów filmowych",
                    "Organizacja kongresów, konferencji i sympozjów, mających na celu pogłębianie i upowszechnianie wiedzy o filmie",
                    "Organizacja konkursów filmowych, wystaw oraz innych wydarzeń promujących sztukę filmową",
                    "Inne działania realizujące cele Priorytetu II"
                ]
            }
        }
        DUKApplicationBuilder.create_application_basic_data(self=self, data=data)

    def create_application_project_costs(self):
        estimate_pt1 = DUKApplicationEstimateBuilder(
            estimate_sections=estimate_sections_pt1,
            after_name="Pt1"
        )
        estimate_pt2 = DUKApplicationEstimateBuilder(
            estimate_sections=estimate_sections_pt2,
            after_name="Pt2"
        )
        estimate_pt3 = DUKApplicationEstimateBuilder(
            estimate_sections=estimate_sections_pt3,
            after_name="Pt3"
        )
        estimate_pt4 = DUKApplicationEstimateBuilder(
            estimate_sections=estimate_sections_pt4,
            after_name="Pt4"
        )

        part = self.create_part(
            title="VII. Kosztorys przedsięwzięcia",
            short_name="VII. Kosztorys przedsięwzięcia",
            chapters=[
                estimate_pt1.generate_estimate_top(),
                estimate_pt1.generate_estimate_headers(),
                self.create_chapter(
                    components=[
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Organizacja przeglądów i innych wydarzeń filmowych o charakterze lokalnym"
                                    ]
                                )
                            ],
                            components=[
                                estimate_pt1.generate_estimate(),
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Działalność kin studyjnych i lokalnych"
                                    ]
                                )
                            ],
                            components=[
                                estimate_pt2.generate_estimate(),
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Działalność klubów filmowych"
                                    ]
                                )
                            ],
                            components=[
                                estimate_pt3.generate_estimate(),
                            ]
                        ),
                        self.create_chapter(
                            visibility_rules=[
                                self.visibility_rule.depends_on_value(
                                    field_name="projectType",
                                    values=[
                                        "Organizacja kongresów, konferencji i sympozjów, mających na celu pogłębianie i upowszechnianie wiedzy o filmie",
                                        "Organizacja konkursów filmowych, wystaw oraz innych wydarzeń promujących sztukę filmową",
                                        "Inne działania realizujące cele Priorytetu II"
                                    ]
                                )
                            ],
                            components=[
                                estimate_pt4.generate_estimate(),
                            ]
                        )
                    ]
                ),
                estimate_pt1.generate_estimate_bottom()
            ]
        )

        self.save_part(part=part)

    def create_application_scope_of_project(self):
        pass
