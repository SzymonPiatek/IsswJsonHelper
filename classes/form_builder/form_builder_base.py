from typing import Literal, Optional, Sequence
import json
import copy
import ast
from pathlib import Path
from classes.form_builder.additional.validator import Validator
from classes.form_builder.additional.visibility_rule import VisibilityRule
from classes.form_builder.additional.calculation_rule import CalculationRule


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
    def load_json(path: str):
        with path.open('r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def delete_unused_component_args(component: dict):
        drop_if_equal = {
            "required": False,
            "readOnly": False,
            "helpText": '',
            "unit": '',
            "defaultValue": '',
            "mask": ''
        }

        drop_if_empty = [
            "validators",
            "calculationRules",
            "classList",
            "options"
        ]


        for key, val in drop_if_equal.items():
            if component.get(key) == val:
                component.pop(key, None)

        for key in drop_if_empty:
            if key in component and not component[key]:
                component.pop(key, None)

        return component

    @staticmethod
    def delete_unused_chapter_args(chapter: dict):
        drop_if_equal = {
            "isMultipleForms": False,
            "isPaginated": False
        }

        drop_if_empty = [
            "visibilityRules",
            "multipleFormsRules",
            "classList"
        ]

        for key, val in drop_if_equal.items():
            if chapter.get(key) == val:
                chapter.pop(key, None)

        for key in drop_if_empty:
            if key in chapter and not chapter[key]:
                chapter.pop(key, None)

        return chapter

    @staticmethod
    def delete_unused_part_args(part: dict):
        drop_if_empty = [
            "classList"
        ]

        for key in drop_if_empty:
            if key in part and not part[key]:
                part.pop(key, None)

        return part

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
        else:
            return obj

    def save_part(self, part: dict):
        self.parts = self.output_json.setdefault('parts', [])
        self.parts.append(part)

    def create_base(self, intro_text: Sequence[str]):
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

        part = {
            "kind": "part",
            "title": title,
            "shortName": short_name,
            "classList": class_list,
            "chapters": chapters
        }

        return self.delete_unused_part_args(part=part)


    @staticmethod
    def duplicate_chapter_with_indexing(start_chapter: dict, mf_min_count: int, start_title: str = "") -> list:
        if start_title == "":
            start_title = "Pozycja"
        def update_names_recursively(obj, index):
            if isinstance(obj, dict):
                if obj.get("kind") == "component" and "name" in obj:
                    obj["name"] = f"{obj['name']}_{index}"
                    obj["dataBDD"] = obj["name"]
                elif obj.get("kind") == "chapter":
                    for comp in obj.get("components", []):
                        update_names_recursively(comp, index)
            elif isinstance(obj, list):
                for item in obj:
                    update_names_recursively(item, index)

        new_chapters = []
        for i in range(1, mf_min_count + 1):
            new_chapter = copy.deepcopy(start_chapter)
            new_chapter["title"] = f"{start_title} {i}"
            update_names_recursively(new_chapter, i)
            new_chapters.append(new_chapter)

        return new_chapters

    def create_chapter(self, title: str = '', class_list: list | dict = None, visibility_rules: list = None, components: list = None, multiple_forms_rules: dict = None, is_paginated: bool = False):
        if class_list is None:
            class_list = []
        if visibility_rules is None:
            visibility_rules = []
        if components is None:
            components = []
        if multiple_forms_rules is None:
            multiple_forms_rules = {}
            is_multiple_forms = False
        else:
            is_multiple_forms = True

            mf_min_count = multiple_forms_rules.get("minCount", 1)

            if len(components) == 0:
                raise ValueError("Chapter z multipleForms powinien posiadać przynajmniej jeden chapter")
            if len(components) != mf_min_count:
                start_chapter = components[0]
                start_title = start_chapter.get("title", "")
                components = self.duplicate_chapter_with_indexing(start_chapter, mf_min_count, start_title)

        chapter = {
            "kind": "chapter",
            "title": title,
            "classList": class_list,
            "visibilityRules": visibility_rules,
            "isMultipleForms": is_multiple_forms,
            "multipleFormsRules": multiple_forms_rules,
            "isPaginated": is_paginated,
            "components": components
        }

        return self.delete_unused_chapter_args(chapter=chapter)

    def create_component(
            self,
            component_type: Literal['date', 'number', 'select', 'text', 'textarea', 'file', 'radio', 'header', 'checkbox', 'country', 'countryMulti'],
            mask: Literal['fund', 'phoneNumber', 'bankAccount', 'landline', 'jst', 'ibanAccount', 'polishPostalCode'] = '',
            label: str = '',
            name: str = '',
            value: str | int | bool = '',
            default_value: str | int | bool = '',
            unit: str = '',
            options: list = None,
            validators: list = None,
            calculation_rules: list = None,
            class_list: list | dict = None,
            required: bool = False,
            read_only: bool = False,
            help_text: str = '',
    ):
        # Check type
        allowed_types = {'date', 'number', 'select', 'text', 'textarea', 'file', 'radio', 'header', 'checkbox', 'country', 'countryMulti'}
        if component_type not in allowed_types:
            raise ValueError(f"Invalid component_type '{component_type}'. Must be one of: {', '.join(allowed_types)}.")
        # Check mask
        allowed_masks = {'fund', 'phoneNumber', 'bankAccount', 'landline', 'jst', 'ibanAccount', 'polishPostalCode'}
        if mask and mask not in allowed_masks:
            raise ValueError(f"Invalid mask '{mask}'. Must be one of: {', '.join(allowed_masks)}")
        # Check name
        if not name:
            raise ValueError("Component 'name' must be provided and non-empty.")
        if name in self.names:
            raise ValueError(f"Duplicate component name detected: {name}")
        self.names.add(name)

        if validators is None:
            validators = []
        if calculation_rules is None:
            calculation_rules = []
        if class_list is None:
            class_list = []

        if component_type == 'select' or component_type == 'radio':
            if options is None:
                raise ValueError("Component 'options' must be provided and non-empty.")
            else:
                if not any(v.get("name") in {"ExactValidator"} for v in validators):
                    validators.append(Validator.exact_validator(values=options))
                if len(options) == 1:
                    read_only = True
                    value = options[0]
        else:
            options = []

        if component_type == "file" and not help_text:
            help_text = "Maksymalny rozmiar pliku to 50 MB"
        if component_type == "file" and not label:
            label = "Plik"

        if mask == "fund" and not unit:
            unit = "PLN"
        if mask == "fund" or component_type == "number":
            if not (isinstance(value, int) or (isinstance(value, str) and value.isdigit())):
                value = 0
            if mask == "fund":
                validators.append(
                    self.validator.range_validator(
                        min_value=0
                    )
                )
        elif mask == "phoneNumber":
            validators.append(Validator.phone_number_validator())
        if component_type == 'date' or component_type == 'checkbox':
            value = False

        if not default_value and value == 0:
            default_value = value

        if required and not any(v.get("name") in {"RelatedRequiredIfEqualValidator", "RequiredValidator", "ExactValidator"} for v in validators):
            validators.append(Validator.required_validator())

        kwargs = {
            "kind": "component",
            "type": component_type,
            "label": label,
            "name": name,
            "dataBDD": name,
            "value": value
        }

        if default_value:
            kwargs["defaultValue"] = default_value
        if mask:
            kwargs["mask"] = mask
        if unit:
            kwargs["unit"] = unit
        if options:
            kwargs["options"] = options
        if required:
            kwargs["required"] = required
        if read_only:
            kwargs["read_only"] = read_only
        if help_text:
            kwargs["help_text"] = help_text
        if validators:
            kwargs["validators"] = validators
        if calculation_rules:
            kwargs["calculation_rules"] = calculation_rules
        if class_list:
            kwargs["class_list"] = class_list

        return self.delete_unused_component_args(component=kwargs)

    def create_part_by_sections(self, part: dict, sections: list):
        layout_chapters = part["chapters"]

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
