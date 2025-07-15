from typing import Literal, Optional
import json
import ast
from pathlib import Path


class FormBuilderBase:
    def __init__(self):
        # DIRS
        self.main_dir = Path(__file__).resolve().parents[2]
        self.data_path = self.main_dir / 'data'

        self.main_dir.mkdir(parents=True, exist_ok=True)

        self.output_json = None

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

    def create_chapter(self, title='', layout_path=None, class_list=None, visibility_rules=None, components=None):
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
            component_type: Literal['date', 'number', 'select', 'text', 'textarea', 'file', 'radio', 'header'],
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
