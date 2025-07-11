from typing import Literal, ClassVar
from pathlib import Path
import json
import ast


JSONType = Literal['application', 'report']
DepartmentType = Literal['DPF', 'DUK', 'DWM']
SessionType = Literal['I', 'II', 'III', 'IV']


class FormBuilder:
    JSON_TYPE: ClassVar[JSONType]
    DEPARTMENT_NAME: ClassVar[DepartmentType]
    OPERATION_NAME: str
    PRIORITY_NAME: str
    YEAR: int
    SESSION: ClassVar[SessionType]

    def __init__(self) -> None:
        self.json_type = self.JSON_TYPE
        self.department_name = self.DEPARTMENT_NAME
        self.operation_name = self.OPERATION_NAME
        self.priority_name = self.PRIORITY_NAME
        self.year = self.YEAR
        self.session = self.SESSION

        # DIRS
        self.main_dir = Path(__file__).resolve().parents[2]
        self.data_path = self.main_dir / 'data'
        self.output_file_name = 'output.json'
        self.output_file = self.main_dir / 'output' / self.output_file_name

        self.main_dir.mkdir(parents=True, exist_ok=True)

        self.output_json = None

    def info(self):
        return f'''
        Type: {'Wniosek' if self.json_type == 'application' else 'Raport'}
        Department: {self.department_name}
        Operation: {self.operation_name}
        Priority: {self.priority_name}
        Year: {self.year}
        Session: {self.session}
        '''

    @staticmethod
    def load_json(path):
        with path.open('r', encoding='utf-8') as f:
            return json.load(f)

    def replace_placeholders(self, obj, values: dict):
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
        else:
            return obj

    def save_part(self, part):
        parts = self.output_json.setdefault('parts', [])
        parts.append(part)

    def save_output(self) -> None:
        with self.output_file.open('w', encoding='utf-8') as f:
            json.dump(self.output_json, f, ensure_ascii=False, indent=2)
        print(f'Zapisano output do {self.output_file}')

    def create_base(self, intro_text: str):
        self.output_json = self.load_json(path=self.main_dir / 'data' / 'base' / 'base.json')

        try:
            intro_list = self.output_json['introText']
            if not intro_list:
                raise KeyError("introText jest puste")
            intro_list[0]['text'] = intro_text
        except KeyError as e:
            raise RuntimeError(f"Nie znalazłem miejsca na introText w JSONie: {e!s}")

    def create_part_by_sections(self, layout_path, sections):
        part = self.load_json(path=layout_path)
        layout_chapters = []

        for section in sections:
            data = section['data']

            for key, value in data.items():
                if isinstance(value, dict) and 'options' in value:
                    options = value['options']
                    data[key]['value'] = options[0] if len(options) == 1 else ""
                    data[key]['readOnly'] = True if len(options) == 1 else False

            section_path = section['path']
            section_json = self.load_json(path=section_path)
            filled_section = self.replace_placeholders(section_json, data)

            layout_chapters.append(filled_section)

        part['chapters'] = layout_chapters
        self.save_part(part)

    def generate(self):
        raise NotImplementedError("Podklasa musi nadpisać `generate`")
