from classes.form_builder.departments.duk._2025.education.report_builder import EducationReportBuilder


class ProfessionalTrainingReportBuilder(EducationReportBuilder):
    PRIORITY_NAME = 'III. Edukacja i kształcenie profesjonalne'
    PRIORITY_NUM = 3

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'professional_training'

