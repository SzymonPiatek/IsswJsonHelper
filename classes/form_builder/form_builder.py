from typing import ClassVar
import json
from ..form_components import Part, Component, Section
from .additional.decorators import not_implemented_func
from .form_builder_base import FormBuilderBase
from classes.types import *


class FormBuilder(FormBuilderBase):
    JSON_TYPE: ClassVar[JSONType]
    DEPARTMENT_NAME: ClassVar[DepartmentType]
    OPERATION_NAME: str
    OPERATION_NUM: str
    PRIORITY_NAME: str
    PRIORITY_NUM: str
    YEAR: YearType = 2026
    SESSION: ClassVar[SessionType] = 'I'
    FORM_ID: int

    def __init__(self) -> None:
        super().__init__()

        self.json_type = self.JSON_TYPE
        self.department_name = self.DEPARTMENT_NAME
        self.operation_name = self.OPERATION_NAME
        self.operation_num = self.OPERATION_NUM
        self.priority_name = self.PRIORITY_NAME
        self.priority_num = self.PRIORITY_NUM
        self.year = self.YEAR
        self.session = self.SESSION
        self.form_id = self.FORM_ID

        self.output_file = self._prepare_output_path()

        self.part = Part()
        self.section = Section()
        self.component = Component()

        self.application_data_path = self.data_path / 'application'
        self.report_data_path = self.data_path / 'report'

    def _prepare_output_path(self):
        output_file_name = (
            f'po_{self.operation_num}_pr_{self.priority_num}_{self.json_type}_{self.year}.json'
        )
        return (
                self.main_dir
                / 'output'
                / 'json'
                / str(self.year)
                / self.department_name
                / self.json_type
                / output_file_name
        )


    def save_output(self) -> None:
        self.output_file.parent.mkdir(parents=True, exist_ok=True)

        with self.output_file.open('w', encoding='utf-8') as f:
            json.dump(self.output_json, f, ensure_ascii=False, indent=2)

        print(f'JSON zapisany do {self.output_file}')

    @not_implemented_func
    def generate(self):
        pass

    @not_implemented_func
    def create_base(self):
        pass
