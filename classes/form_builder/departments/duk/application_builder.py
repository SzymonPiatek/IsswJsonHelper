from classes.form_builder.application_builder import ApplicationBuilder
from classes.form_builder.additional.decorators import not_implemented_func
from classes.form_builder.departments.duk.department import DUKDepartment


class DUKApplicationBuilder(ApplicationBuilder, DUKDepartment):
    def __init__(self):
        super().__init__()

        self.estimate_sections = []

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

    def generate(self):
        # Base
        self.create_base()

        # Metadane wniosku
        self.create_application_metadata()

        # I. Dane podstawowe
        self.create_application_basic_data()
        #
        # # II. Dane wnioskodawcy
        # self.create_application_applicant_data()
        #
        # # III. Zakres przedsięwzięcia
        # self.create_application_scope_of_project()
        #
        # # IV. Źródła finansowania
        # self.create_application_sources_of_financing()
        #
        # # V. Oświaczenia
        # self.create_application_statements()
        #
        # # VI. Załączniki
        # self.create_application_attachments()
        #
        # # VII. Kosztorys przedsięwzięcia
        # self.create_application_project_costs()
        #
        # # VIII. Harmonogram
        # self.create_application_schedule()
        #
        # # Zapis
        # self.save_output()
