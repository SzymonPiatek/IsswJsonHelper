from classes.form_builder.report_builder import ReportBuilder


class DUKReportBuilder(ReportBuilder):
    DEPARTMENT_NAME = 'DUK'

    def __init__(self):
        super().__init__()

        self.department_data_path = self.application_data_path / 'duk'
        self.program_data_path = None
        self.priority_data_path = None

    def create_application_basic_data(self):
        part = self.load_json(path=self.department_data_path / self.program_data_path / '_pages' / 'application_basic_data.json')
        self.save_part(part)

    def create_application_general_data(self, number: str):
        part = self.load_json(path=self.department_data_path / '_pages' / 'application_general_data.json')
        values = {
            "number": number
        }
        final_part = self.replace_placeholders(part, values)
        self.save_part(final_part)

    def create_application_estimate_report_data(self):
        part = self.load_json(path=self.department_data_path / self.program_data_path / self.priority_data_path / '_pages' / 'application_estimate_report_data.json')
        self.save_part(part)

    def create_application_achieved_results_data(self):
        part = self.load_json(path=self.department_data_path / self.program_data_path / self.priority_data_path / '_pages' / 'application_achieved_results_data.json')
        self.save_part(part)
