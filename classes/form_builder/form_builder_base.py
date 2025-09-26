from typing import Literal, Sequence
import json
import copy
import ast
from pathlib import Path
from classes.form_builder.additional.rules.validator import Validator
from classes.form_builder.additional.rules.visibility_rule import VisibilityRule
from classes.form_builder.additional.rules.calculation_rule import CalculationRule


COMPONENT_TYPE_VALUES = (
    "date", "file", "radio", "header", "checkbox",
    "number", "select", "country", "countryMulti",
    "currency", "text", "textarea",
)
ComponentType = Literal[*COMPONENT_TYPE_VALUES]
COMPONENT_TYPES = set(COMPONENT_TYPE_VALUES)

MASK_TYPE_VALUES = (
    "fund", "phoneNumber", "bankAccount", "landline",
    "jst", "ibanAccount", "polishPostalCode", "share"
)
MaskType = Literal[*MASK_TYPE_VALUES]
MASK_TYPES = set(MASK_TYPE_VALUES)

VALUE_TYPES = (str, int, float, bool, list)


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
            "helpText": "",
            "unit": "",
            "defaultValue": "",
            "mask": "",
        }
        drop_if_empty = ["validators", "calculationRules", "classList", "options"]

        for key, val in drop_if_equal.items():
            if component.get(key) == val:
                component.pop(key, None)

        for key in drop_if_empty:
            if key in component and not component[key]:
                component.pop(key, None)

        return component

    @staticmethod
    def delete_unused_chapter_args(chapter: dict):
        drop_if_equal = {"isMultipleForms": False, "isPaginated": False}
        drop_if_empty = ["visibilityRules", "multipleFormsRules", "classList"]

        for key, val in drop_if_equal.items():
            if chapter.get(key) == val:
                chapter.pop(key, None)

        for key in drop_if_empty:
            if not chapter.get(key):
                chapter.pop(key, None)

        return chapter

    @staticmethod
    def delete_unused_part_args(part: dict):
        if not part.get("classList"):
            part.pop("classList", None)
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
        return obj

    def save_part(self, part: dict):
        self.parts = self.output_json.setdefault('parts', [])
        self.parts.append(part)

    def create_base(self, intro_text: Sequence[str]):
        if not intro_text or not isinstance(intro_text, list):
            raise ValueError("intro_text musi być niepustą listą tekstów")

        self.output_json = {
            "kind": "form",
            "jrwa": "",
            "expert": {"name": "", "email": "", "avatar": ""},
            "status": "",
            "applicant": {},
            "title": "",
            "introText": [{"text": text} for text in intro_text],
            "blanks": [],
            "parts": [],
        }

    def create_part(self, title: str = None, short_name: str = None, class_list: list | dict = None, chapters: list = None):
        if not title:
            raise ValueError("title musi być podane")

        part = {
            "kind": "part",
            "title": title,
            "shortName": short_name or title,
            "classList": class_list or ["full-width-grid"],
            "chapters": chapters or [],
        }
        return self.delete_unused_part_args(part)

    @staticmethod
    def duplicate_chapter_with_indexing(start_chapter: dict, mf_min_count: int, start_title: str = "") -> list:
        start_title = start_title or "Pozycja"

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
        components = components or []

        if multiple_forms_rules:
            if multiple_forms_rules.get("maxCount", 1) > 5:
                is_paginated = True

            mf_min_count = multiple_forms_rules.get("minCount", 1)

            if len(components) == 0:
                raise ValueError("Chapter z multipleForms powinien posiadać przynajmniej jeden chapter")
            if len(components) != mf_min_count:
                start_chapter = components[0]
                start_title = start_chapter.get("title", "")
                components = self.duplicate_chapter_with_indexing(start_chapter, mf_min_count, start_title)

            def set_default_value(obj):
                if isinstance(obj, dict):
                    if obj.get("kind") == "component":
                        if "value" in obj and "defaultValue" not in obj:
                            obj["defaultValue"] = obj["value"]
                    for v in obj.values():
                        set_default_value(v)
                elif isinstance(obj, list):
                    for item in obj:
                        set_default_value(item)

            set_default_value(components)

        kwargs = {
            "kind": "chapter",
            "title": title,
            "components": components,
        }

        if class_list:
            kwargs["classList"] = class_list
        if visibility_rules:
            kwargs["visibilityRules"] = visibility_rules
        if multiple_forms_rules:
            kwargs["isMultipleForms"] = True
            kwargs["multipleFormsRules"] = multiple_forms_rules
        if is_paginated:
            kwargs["isPaginated"] = is_paginated

        return self.delete_unused_chapter_args(kwargs)

    def create_component(
            self,
            component_type: ComponentType,
            mask: MaskType = '',
            label: str = '',
            name: str = '',
            value: VALUE_TYPES = '',
            default_value: VALUE_TYPES = '',
            unit: str = '',
            options: list = None,
            validators: list = None,
            calculation_rules: list = None,
            class_list: list | dict = None,
            required: bool = False,
            read_only: bool = False,
            help_text: str = '',
            copy_from: str = '',
    ):
        # Check type
        if component_type not in COMPONENT_TYPES:
            raise ValueError(f"Invalid component_type: '{component_type}'")

        # Check mask
        if mask and mask not in MASK_TYPES:
            raise ValueError(f"Invalid mask: '{mask}'")

        # Check name
        if not name:
            raise ValueError("Component 'name' must be provided and non-empty.")

        # Header component
        if component_type == "header" and not name.startswith("headerComponent"):
            name = f"headerComponent-{name}"

        # Save and check name
        if name in self.names:
            raise ValueError(f"Duplicate component name detected: {name}")
        self.names.add(name)

        # Check value
        if value and not isinstance(value, VALUE_TYPES):
            raise ValueError(f"Invalid value type: '{value}'")

        # Check default_value
        if default_value and not isinstance(default_value, VALUE_TYPES):
            raise ValueError(f"Invalid default_value type: '{default_value}'")

        validators = validators or []
        calculation_rules = calculation_rules or []
        class_list = class_list or []

        # Select & Radio
        if component_type in {"select", "radio"}:
            if not options:
                raise ValueError("Component 'options' must be provided for select/radio.")
            if not any(v.get("name") == "ExactValidator" for v in validators):
                validators.append(Validator.exact_validator(values=options))
            if len(options) == 1:
                read_only = True
                value = options[0]

        # File
        if component_type == "file":
            message = "Maksymalny rozmiar pliku to 50 MB"
            if not help_text:
                help_text = message
            elif message not in help_text:
                help_text += f" {message}"

        # Date
        if component_type in {"date", "checkbox"}:
            value = False

        # Fund & Number
        if mask == "fund" or component_type == "number":
            if not (isinstance(value, int) or not isinstance(value, float)) or (isinstance(value, str) and value.isdigit()):
                value = 0
            if mask == "fund":
                validators.append(
                    self.validator.range_validator(
                        min_value=0
                    )
                )
        elif mask == "phoneNumber":
            validators.append(Validator.phone_number_validator())

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

        if default_value is not None:
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
            kwargs["readOnly"] = read_only
        if help_text:
            kwargs["helpText"] = help_text
        if validators:
            kwargs["validators"] = validators
        if calculation_rules:
            kwargs["calculationRules"] = calculation_rules
        if class_list:
            kwargs["classList"] = class_list
        if copy_from:
            kwargs["copyFrom"] = copy_from

        return self.delete_unused_component_args(component=kwargs)
