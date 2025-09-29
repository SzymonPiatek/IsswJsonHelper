from classes.form_builder.departments.duk._2026.application_builder import DUKApplicationBuilder2026
from .operation import DUKEducationOperation


class EducationApplicationBuilder(DUKApplicationBuilder2026, DUKEducationOperation):
    def __init__(self):
        super().__init__()
