from email.policy import default
from typing import Literal, Optional
import json
import ast
from pathlib import Path
from classes.form_builder.validator import Validator
from classes.form_builder.visibility_rule import VisibilityRule
from classes.form_builder.calculation_rule import CalculationRule


class FormBuilderBase:
    def __init__(self):
        self.main_dir = Path(__file__).resolve().parents[2]
        self.data_path = self.main_dir / 'data'
        self.main_dir.mkdir(parents=True, exist_ok=True)
        self.output_json = None

        self.parts = []
        self.names = set()

        self.validator = Validator()
        self.visibility_rule = VisibilityRule()
        self.calculation_rule = CalculationRule()

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
        self.parts = self.output_json.setdefault('parts', [])
        self.parts.append(part)

    def create_base(self, intro_text: [str]):
        self.output_json = {
            "kind": "form",
            "jrwa": "",
            "expert": {
                "name": "",
                "email": "",
                "avatar": ""
            },
            "status": "",
            "applicant": {},
            "title": "",
            "introText": [],
            "blanks": [],
            "parts": []
        }

        if not intro_text or not isinstance(intro_text, list):
            raise ValueError("intro_text musi być niepustą listą tekstów")

        self.output_json["introText"] = [{"text": text} for text in intro_text]

    def create_part(self, title: str = None, short_name: str = None, class_list: list | dict = None, chapters: list = None):
        if title is None:
            raise ValueError("title musi być podane")
        if short_name is None:
            short_name = title
        if class_list is None:
            class_list = []
        if chapters is None:
            chapters = []

        return {
            "kind": "part",
            "title": title,
            "shortName": short_name,
            "classList": class_list,
            "chapters": chapters
        }

    def create_chapter(self, title='', class_list=None, visibility_rules=None, components=None, is_multiple_forms=False, multiple_forms_rules=None):
        if class_list is None:
            class_list = []
        if visibility_rules is None:
            visibility_rules = []
        if components is None:
            components = []
        if multiple_forms_rules is None:
            multiple_forms_rules = {}

        return {
            "kind": "chapter",
            "title": title,
            "classList": class_list,
            "visibilityRules": visibility_rules,
            "components": components,
            "isMultipleForms": is_multiple_forms,
            "multipleFormsRules": multiple_forms_rules
        }

    def create_component(
            self,
            component_type: Literal['date', 'number', 'select', 'text', 'textarea', 'file', 'radio', 'header', 'checkbox'],
            mask: Literal['fund', 'phoneNumber', 'bankAccount'] = '',
            label: str = '',
            name: str = '',
            value: str | int | bool = '',
            default_value: str | int | bool = None,
            unit: str = '',
            options: Optional[list] = None,
            validators: Optional[list] = None,
            calculation_rules: Optional[list] = None,
            class_list: Optional[list] = None,
            required: bool = False,
            read_only: bool = False,
            help_text: str = '',
    ):
        allowed_types = {'date', 'number', 'select', 'text', 'textarea', 'file', 'radio', 'header', 'checkbox'}
        if component_type not in allowed_types:
            raise ValueError(f"Invalid component_type '{component_type}'. Must be one of: {', '.join(allowed_types)}.")

        if not name:
            raise ValueError("Component 'name' must be provided and non-empty.")

        if validators is None:
            validators = []
        if mask == "fund":
            if not (isinstance(value, int) or (isinstance(value, str) and value.isdigit())):
                value = 0
        elif mask == "phoneNumber":
            validators.append(Validator.phone_number_validator())
        if component_type == 'date' or component_type == 'checkbox':
            value = False
        if options is None:
            options = []
        if calculation_rules is None:
            calculation_rules = []
        if class_list is None:
            class_list = []
        if value == 0:
            validators.append(
                {
                    "name": "RangeValidator",
                    "kwargs": {
                        "min": 0
                    },
                    "validationMsg": "Wartość musi być większa od zera."
                },
            )
        if default_value is None:
            default_value = value

        if required and not any(v.get("name") == "RelatedRequiredIfEqualValidator" for v in validators):
            validators.append(Validator.required_validator())

        if name in self.names:
            raise ValueError(f"Duplicate component name detected: {name}")
        self.names.add(name)

        return {
            "kind": "component",
            "type": component_type,
            "mask": mask,
            "label": label,
            "name": name,
            "value": value,
            "defaultValue": default_value,
            "unit": unit,
            "options": options,
            "validators": validators,
            "calculationRules": calculation_rules,
            "classList": class_list,
            "required": required,
            "readOnly": read_only,
            "dataBDD": name,
            "helpText": help_text
        }

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
