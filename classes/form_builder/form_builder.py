from typing import ClassVar
import json
from pathlib import Path
from ..form_components import Part, Component, Section
from classes.decorators import not_implemented_func
from ..form_factory.form_factory import FormFactory
from classes.types import *


class FormBuilder(FormFactory):
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

        self.main_dir = Path(__file__).resolve().parents[2]
        self.data_path = self.main_dir / 'data'
        self.main_dir.mkdir(parents=True, exist_ok=True)
        self.output_file = self._prepare_output_path()

        self.output_json: dict = {}
        self.parts = []
        self.names = set()

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

    @staticmethod
    def load_json(path: str):
        with path.open('r', encoding='utf-8') as f:
            return json.load(f)

    def replace_placeholders(self, obj: dict, values: dict):
        if isinstance(obj, dict):
            return {k: self.replace_placeholders(v, values) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self.replace_placeholders(item, values) for item in obj]
        elif isinstance(obj, str):
            try:
                result = obj.format(**values)
                try:
                    return ast.literal_eval(result)
                except (ValueError, SyntaxError):
                    return result
            except KeyError:
                return obj
        return obj

    def save_part(self, part: dict):
        self.parts = self.output_json.setdefault('parts', [])
        self.parts.append(part)
