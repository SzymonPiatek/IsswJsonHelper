from classes.form_builder.duk.education.application_builder import EducationApplicationBuilder
from classes.form_builder.duk.application_builder import DUKApplicationBuilder
from classes.form_builder.duk.education.professional_training.estimate_data import estimate_sections_pt1235, estimate_sections_pt4
from classes.form_builder.duk.application_estimate_builder import DUKApplicationEstimateBuilder


class ProfessionalTrainingApplicationBuilder(EducationApplicationBuilder):
    PRIORITY_NAME = 'III. Edukacja i kształcenie profesjonalne'
    PRIORITY_NUM = 3
    FORM_ID = 9182

    def __init__(self):
        super().__init__()

    def create_application_basic_data(self, **kwargs):
        data = {
            'projectType': {
                'options': [
                    "kształcenie zawodowe i podnoszenie kompetencji poprzez organizację szkoleń zawodowych, warsztatów, kursów i innych przedsięwzięć lub programów długoterminowych",
                    "edukacja dotycząca historii filmu polskiego i światowego, estetyki filmowej i środków wyrazu oraz społecznych funkcji filmu",
                    "projekty edukacyjne dla przedstawicieli wszystkich grup zawodowych, pracujących na potrzeby polskiej kinematografii",
                    "organizacja kursów nauki języków obcych dla przedstawicieli zawodów filmowych",
                    "inne działania realizujące cele Priorytetu V",
                    "inne działania realizujące cele Priorytetu III",
                ]
            }
        }
        DUKApplicationBuilder.create_application_basic_data(self=self, data=data)

    def create_application_scope_of_project(self):
        data = {
            "chapters": [

            ]
        }

        EducationApplicationBuilder.create_application_scope_of_project(
            self, data=data
        )

    def create_application_project_costs(self):
        estimate_pt1235 = DUKApplicationEstimateBuilder(
            estimate_sections=estimate_sections_pt1235,
            after_name="Pt1235"
        )
        estimate_pt4 = DUKApplicationEstimateBuilder(
            estimate_sections=estimate_sections_pt4,
            after_name="Pt4"
        )


        part = self.create_part(
                title="VII. Kosztorys przedsięwzięcia",
                short_name="VII. Kosztorys przedsięwzięcia",
                chapters=[
                    estimate_pt1235.generate_estimate_top(),
                    estimate_pt1235.generate_estimate_headers(),
                    self.create_chapter(
                        components=[
                            self.create_chapter(
                                visibility_rules=[
                                    self.visibility_rule.depends_on_value(
                                        field_name="projectType",
                                        values=[
                                        ]
                                    )
                                ],
                                components=[
                                    estimate_pt1235.generate_estimate(),
                                ]
                            ),
                            self.create_chapter(
                                visibility_rules=[
                                    self.visibility_rule.depends_on_value(
                                        field_name="projectType",
                                        values=[
                                        ]
                                    )
                                ],
                                components=[
                                    estimate_pt4.generate_estimate(),
                                ]
                            )
                        ]
                    ),
                    estimate_pt1235.generate_estimate_bottom()
                ]
            )

        self.save_part(part=part)
