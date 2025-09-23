from classes.form_builder.departments.duk.report_builder import DUKReportBuilder


class EducationReportBuilder(DUKReportBuilder):
    OPERATION_NAME = 'II. Edukacja filmowa'
    OPERATION_NUM = 2

    def __init__(self):
        super().__init__()

        self.program_data_path = self.department_data_path / 'education'

    def generate(self):
        # Base
        self.create_report_base()

        # Dane podstawowe
        self.create_application_basic_data()

        # I. Informacje ogólne
        self.create_application_general_data(number="I")

        # II. Sprawozdanie z wykonania wydatków
        self.create_application_estimate_report_data()

        # III. Osiągnięte rezultaty
        self.create_application_achieved_results_data()

        # Zapis
        self.save_output()
