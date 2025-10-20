from classes.decorators import not_implemented_func
from classes.form_builder.departments.dwm.department import DWMDepartment
from classes.form_builder.departments.dwm.operation import DWMOperation
from classes.form_builder.report_builder import ReportBuilder


class DWMReportBuilder(ReportBuilder, DWMDepartment, DWMOperation):
    def __init__(self):
        super().__init__()

        self.parts = [
            self.create_report_basic_data,
            self.create_report_general_data,
            self.create_report_expenditure_exacution,
            self.create_report_additional_information
        ]

    def create_base(self):
        self.output_json = self.create_form(
            intro_text=[
                "Raport końcowy",
                "<small>z wykonania przedsięwzięcia realizowanego w ramach Programu Operacyjnego \"Promocja polskiej twórczości filmowej za granicą\"</small> <br> Priorytet I \"Promocja polskiej twórczości filmowej za granicą\""
            ]
        )

    @not_implemented_func
    def create_report_basic_data(self, number: int):
        pass

    @not_implemented_func
    def create_report_general_data(self, number: int):
        pass

    @not_implemented_func
    def create_report_expenditure_exacution(self, number: int):
        pass

    @not_implemented_func
    def create_report_additional_information(self, number: int):
        pass
