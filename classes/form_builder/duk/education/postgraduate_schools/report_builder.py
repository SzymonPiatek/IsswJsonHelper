from classes.form_builder.duk.education.report_builder import EducationReportBuilder


class PostgraduateSchoolsReportBuilder(EducationReportBuilder):
    PRIORITY_NAME = 'I. Szkoły wyższe i podyplomowe'
    PRIORITY_NUM = 1

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'postgraduate_schools'

