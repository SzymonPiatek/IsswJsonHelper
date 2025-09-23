from classes.form_builder.departments.duk.education.report_builder import EducationReportBuilder


class SecondarySchoolsReportBuilder(EducationReportBuilder):
    PRIORITY_NAME = 'II. Edukacja w szkołach średnich i zawodowych'
    PRIORITY_NUM = 2

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'professional_training'
