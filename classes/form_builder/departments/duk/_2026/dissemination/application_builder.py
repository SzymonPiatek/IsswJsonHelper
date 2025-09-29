from classes.form_builder.departments.duk._2026.application_builder import DUKApplicationBuilder2026
from .operation import DUKDisseminationOperation


class DisseminationApplicationBuilder(DUKApplicationBuilder2026, DUKDisseminationOperation):
    def __init__(self):
        super().__init__()
