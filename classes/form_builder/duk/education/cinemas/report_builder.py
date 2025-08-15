from classes.form_builder.duk.education.report_builder import EducationReportBuilder


class CinemasReportBuilder(EducationReportBuilder):
    PRIORITY_NAME = 'IV. Edukacja w kinach'
    PRIORITY_NUM = 4

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'cinemas'

