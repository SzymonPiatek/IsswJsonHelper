import json
import ast
from pathlib import Path
from .additional.rules import CalculationRule, Validator, VisibilityRule
from .form_elements import FormForm, FormPart, FormChapter, FormComponent
from .form_elements.form_component import ComponentType, MaskType, ValueType


class FormBuilderBase:
    def __init__(self):
        self.main_dir = Path(__file__).resolve().parents[2]
        self.data_path = self.main_dir / 'data'
        self.main_dir.mkdir(parents=True, exist_ok=True)

        self.output_json: dict = None
        self.parts = []
        self.names = set()

        self.validator = Validator()
        self.visibility_rule = VisibilityRule()
        self.calculation_rule = CalculationRule()

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

    def create_form(self, intro_text: list[str]):
        form = FormForm(intro_text)

        self.output_json = form.generate()

    def create_part(self, title: str = None, short_name: str = None, class_list: list | dict = None, chapters: list = None):
        part = FormPart(
            title=title,
            short_name=short_name,
            class_list=class_list,
            chapters=chapters,
        )

        return part.generate()

    def create_chapter(self, title: str = '', class_list: list | dict = None, visibility_rules: list = None, components: list = None, multiple_forms_rules: dict = None, is_paginated: bool = False):
        chapter = FormChapter(
            title=title,
            class_list=class_list,
            visibility_rules=visibility_rules,
            components=components,
            multiple_forms_rules=multiple_forms_rules,
            is_paginated=is_paginated,
        )
        return chapter.generate()

    def create_component(
            self,
            component_type: ComponentType,
            mask: MaskType = '',
            label: str = '',
            name: str = '',
            value: ValueType = '',
            default_value: ValueType = '',
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
        component = FormComponent(
            component_type=component_type,
            mask=mask,
            label=label,
            name=name,
            value=value,
            default_value=default_value,
            unit=unit,
            options=options,
            validators=validators,
            calculation_rules=calculation_rules,
            class_list=class_list,
            required=required,
            read_only=read_only,
            help_text=help_text,
            copy_from=copy_from,
            names=self.names,
        )

        return component.generate()
