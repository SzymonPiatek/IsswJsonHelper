from classes.form_builder.departments.duk._2026.application_builder import DUKApplicationBuilder2026
from classes.helpers import int_to_roman


class EducationApplicationBuilder(DUKApplicationBuilder2026):
    def __init__(self):
        super().__init__()

        self.basic_number_data = None
