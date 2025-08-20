from classes.form_builder.dwm.application_builder import DWMApplicationBuilder


class ForeignScholarshipApplicationBuilder(DWMApplicationBuilder):
    PRIORITY_NAME = 'II. Stypendia zagraniczne'
    PRIORITY_NUM = 2
    FORM_ID = 9193

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.department_data_path / 'foreign_scholarship'
