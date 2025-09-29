from classes.form_builder.departments.duk._2026.application_builder import DUKApplicationBuilder2026
from .operation import DUKDevelopmentOperation


class DevelopmentApplicationBuilder(DUKApplicationBuilder2026, DUKDevelopmentOperation):
    def __init__(self):
        super().__init__()
