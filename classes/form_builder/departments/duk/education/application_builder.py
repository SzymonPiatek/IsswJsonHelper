from classes.form_builder.departments.duk.application_builder import DUKApplicationBuilder


class EducationApplicationBuilder(DUKApplicationBuilder):
    OPERATION_NAME = 'II. Edukacja filmowa'
    OPERATION_NUM = "ii"

    def __init__(self):
        super().__init__()

        self.program_data_path = self.department_data_path / 'education'

    def create_application_scope_of_project(self, **kwargs):
        data = kwargs["data"]

        project_detailed_description_chapters = data["project_detailed_description_chapters"] if data.get("project_detailed_description_chapters", False) else [
            {
                "section_title": "Wartość merytoryczna przedsięwzięcia, w tym ciągłość realizacji przedsięwzięcia oraz wartość edukacyjna",
                "name": "scopeAndValueOfContent"
            },
            {
                "section_title": "Spójność, oryginalność i unikalność koncepcji przedsięwzięcia, atrakcyjność przekazu dla odbiorcy i specyfika przedsięwzięcia",
                "name": "originalityOfProject"
            },
            {
                "section_title": "Zróżnicowanie struktury odbiorców lub uczestników oraz liczba uczestników",
                "name": "diversificationOfAudience"
            },
            {
                "section_title": "Różnorodność środowisk zaangażowanych w realizację przedsięwzięcia",
                "name": "diversityOfInvolvedCommunities"
            },
            {
                "section_title": "Planowane efekty realizacji przedsięwzięcia oraz jego ewaluacja",
                "name": "plannedResultsOfProject"
            }
        ]

        part = self.create_part(
            title="III. Zakres przedsięwziecia",
            short_name="III. Zakres przedsięwzięcia",
            class_list=[
                "full-width-grid"
            ],
            chapters=[
                self.section.application_scope_of_project.project_implementation_place_education(),
                self.section.application_scope_of_project.general_project_description(),
                self.section.application_scope_of_project.project_detailed_description(chapters=project_detailed_description_chapters),
                self.section.application_scope_of_project.applicant_experience_summary(),
                self.section.application_scope_of_project.project_partners_and_experts(),
                self.section.application_scope_of_project.participants_acquired_skills(),
                *data["chapters"]
            ]
        )
        self.save_part(part)
