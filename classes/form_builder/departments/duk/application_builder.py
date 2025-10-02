from classes.form_builder.application_builder import ApplicationBuilder
from classes.decorators import not_implemented_func
from classes.form_builder.departments.duk.department import DUKDepartment


class DUKApplicationBuilder(ApplicationBuilder, DUKDepartment):
    def __init__(self):
        super().__init__()

    @not_implemented_func
    def create_application_metadata(self):
        pass

    @not_implemented_func
    def create_application_basic_data(self):
        pass

    @not_implemented_func
    def create_application_applicant_data(self):
        pass

    @not_implemented_func
    def create_application_scope_of_project(self):
        pass

    @not_implemented_func
    def create_application_sources_of_financing(self):
        pass

    @not_implemented_func
    def create_application_statements(self):
        pass

    @not_implemented_func
    def create_application_attachments(self):
        pass

    @not_implemented_func
    def create_application_project_costs(self):
        pass

    @not_implemented_func
    def create_application_schedule(self):
        pass
