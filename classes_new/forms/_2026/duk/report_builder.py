from classes_new.form_builder.form_builder import ReportFormBuilder


class DUKDepartmentReportFormBuilder(ReportFormBuilder):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.parts = []
