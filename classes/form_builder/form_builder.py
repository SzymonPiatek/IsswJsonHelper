from typing import Literal, ClassVar, Optional
import json

from classes.form_builder.form_builder_base import FormBuilderBase

JSONType = Literal['application', 'report']
DepartmentType = Literal['DPF', 'DUK', 'DWM']
SessionType = Literal['I', 'II', 'III', 'IV']


class FormBuilder(FormBuilderBase):
    JSON_TYPE: ClassVar[JSONType]
    DEPARTMENT_NAME: ClassVar[DepartmentType]
    OPERATION_NAME: str
    OPERATION_NUM: int
    PRIORITY_NAME: str
    PRIORITY_NUM: int
    YEAR: int
    SESSION: ClassVar[SessionType]

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

        self.output_file_name = f'po{self.operation_num}_pr{self.priority_num}_{self.json_type}_{self.year}.json'
        self.output_file = self.main_dir / 'output' / self.department_name / self.json_type / self.output_file_name

    def info(self):
        return f'''
            Typ formularza: {'Wniosek' if self.json_type == 'application' else 'Raport'}
            Dział: {self.department_name}
            Program oparacyjny: {self.operation_name}
            Priorytet: {self.priority_name}
            Rok: {self.year}
            Sesja: {self.session}
            '''

    def save_output(self) -> None:
        self.output_file.parent.mkdir(parents=True, exist_ok=True)

        with self.output_file.open('w', encoding='utf-8') as f:
            json.dump(self.output_json, f, ensure_ascii=False, indent=2)

        print(f'Zapisano output do {self.output_file}')

    def generate(self):
        raise NotImplementedError("Podklasa musi nadpisać `generate`")
