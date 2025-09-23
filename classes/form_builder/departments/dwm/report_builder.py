from classes.form_builder.additional.rules.decorators import not_implemented_func
from classes.form_builder.departments.dwm.department import DWMDepartment
from classes.form_builder.departments.dwm.operation import DWMOperation
from classes.form_builder.report_builder import ReportBuilder


class DWMReportBuilder(ReportBuilder, DWMDepartment, DWMOperation):
    def __init__(self):
        super().__init__()

    def create_report_base(self):
        self.create_base(
            intro_text=[
                "Raport końcowy",
                "<small>z wykonania przedsięwzięcia realizowanego w ramach Programu Operacyjnego \"Promocja polskiej twórczości filmowej za granicą\"</small> <br> Priorytet I \"Promocja polskiej twórczości filmowej za granicą\""
            ]
        )

    @not_implemented_func
    def create_report_basic_data(self):
        pass

    @not_implemented_func
    def create_report_general_data(self):
        pass

    @not_implemented_func
    def create_report_expenditure_exacution(self):
        pass

    @not_implemented_func
    def create_report_additional_information(self):
        pass

    def generate(self):
        # Base
        self.create_report_base()

        # 1. Dane podstawowe
        self.create_report_basic_data()

        # 2. Informacje ogólne
        self.create_report_general_data()

        # 3. Sprawozdanie z wykonania wydatków
        self.create_report_expenditure_exacution()

        # 4. Dodatkowe informacje
        self.create_report_additional_information()

        # Zapis
        self.save_output()

