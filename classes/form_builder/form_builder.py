from typing import Literal, ClassVar, Optional
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
    OPERATION_NUM: int
    PRIORITY_NAME: str
    PRIORITY_NUM: int
    YEAR: int
    SESSION: ClassVar[SessionType]

    def __init__(self) -> None:
        self.json_type = self.JSON_TYPE
        self.department_name = self.DEPARTMENT_NAME
        self.operation_name = self.OPERATION_NAME
        self.operation_num = self.OPERATION_NUM
        self.priority_name = self.PRIORITY_NAME
        self.priority_num = self.PRIORITY_NUM
        self.year = self.YEAR
        self.session = self.SESSION

        # DIRS
        self.main_dir = Path(__file__).resolve().parents[2]
        self.data_path = self.main_dir / 'data'
        self.output_file_name = f'po{self.operation_num}_pr{self.priority_num}_{self.json_type}_{self.year}.json'
        self.output_file = self.main_dir / 'output' / self.department_name / self.json_type / self.output_file_name

        self.main_dir.mkdir(parents=True, exist_ok=True)

        self.output_json = None

    def info(self):
        return f'''
        Typ formularza: {'Wniosek' if self.json_type == 'application' else 'Raport'}
        Dział: {self.department_name}
        Program oparacyjny: {self.operation_name}
        Priorytet: {self.priority_name}
        Rok: {self.year}
        Sesja: {self.session}
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
        self.output_file.parent.mkdir(parents=True, exist_ok=True)

        with self.output_file.open('w', encoding='utf-8') as f:
            json.dump(self.output_json, f, ensure_ascii=False, indent=2)

        print(f'Zapisano output do {self.output_file}')

    def create_base(self, intro_text: str, layout_path=None):
        if layout_path is None:
            layout_path = self.main_dir / 'data' / 'base' / 'base.json'

        self.output_json = self.load_json(path=layout_path)

        try:
            intro_list = self.output_json['introText']
            if not intro_list:
                raise KeyError("introText jest puste")
            intro_list[0]['text'] = intro_text
        except KeyError as e:
            raise RuntimeError(f"Nie znalazłem miejsca na introText w JSONie: {e!s}")

    def create_part(self, title, short_name, layout_path=None, class_list=None, chapters=None):
        if class_list is None:
            class_list = []
        if layout_path is None:
            layout_path = self.main_dir / 'data' / 'base' / 'part.json'
        if chapters is None:
            chapters = []

        part = self.load_json(path=layout_path)
        values = {
            "title": title,
            "shortName": short_name,
            "classList": class_list,
            "chapters": chapters
        }

        return self.replace_placeholders(part, values)

    def create_chapter(self, title, layout_path=None, class_list=None, visibility_rules=None, components=None):
        if class_list is None:
            class_list = []
        if visibility_rules is None:
            visibility_rules = []
        if layout_path is None:
            layout_path = self.main_dir / 'data' / 'base' / 'chapter.json'
        if components is None:
            components = []

        chapter = self.load_json(path=layout_path)
        values = {
            "title": title,
            "classList": class_list,
            "visibilityRules": visibility_rules,
            "components": components
        }

        return self.replace_placeholders(chapter, values)

    def create_component(
            self,
            component_type: Literal['date', 'fund', 'number', 'select', 'text', 'textarea', 'file'],
            mask: str = '',
            label: str = '',
            name: str = '',
            value: str = '',
            unit: str = '',
            options: Optional[list] = None,
            validators: Optional[list] = None,
            calculation_rules: Optional[list] = None,
            class_list: Optional[list] = None,
            required: bool = False,
            read_only: bool = False
    ):
        if validators is None:
            validators = []
        if options is None:
            options = []
        if calculation_rules is None:
            calculation_rules = []
        if class_list is None:
            class_list = []

        component = self.load_json(path=self.main_dir / 'data' / 'base' / 'component.json')
        values = {
            "type": component_type,
            "mask": mask,
            "label": label,
            "name": name,
            "value": value,
            "unit": unit,
            "options": options,
            "validators": validators,
            "calculationRules": calculation_rules,
            "classList": class_list,
            "required": required,
            "readOnly": read_only
        }

        return self.replace_placeholders(component, values)

    def create_part_by_sections(self, part, sections):
        layout_chapters = []

        for section in sections:
            data = section['data']

            for key, value in data.items():
                if isinstance(value, dict) and 'options' in value:
                    options = value['options']
                    data[key]['value'] = options[0] if len(options) == 1 else ""
                    read_only = value.get('readOnly', False)
                    data[key]['readOnly'] = read_only if read_only else True if len(options) == 1 else False

            section_json = self.load_json(path=section['path'])
            filled_section = self.replace_placeholders(section_json, data)

            layout_chapters.append(filled_section)

        part['chapters'] = layout_chapters
        self.save_part(part)

    def generate(self):
        raise NotImplementedError("Podklasa musi nadpisać `generate`")
