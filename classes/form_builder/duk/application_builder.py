from classes.form_builder.application_builder import ApplicationBuilder


class DUKApplicationBuilder(ApplicationBuilder):
    DEPARTMENT_NAME = 'DUK'

class DUKApplicationBuilder2025(DUKApplicationBuilder):
    YEAR = 2025
