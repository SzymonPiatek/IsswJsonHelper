from classes.form_elements import FormForm, FormPart, FormChapter, FormComponent


class FormFactory:
    def __init__(self):
        self.output_json: dict = None
        self.parts: list = []
        self.names = set[str] = set()

    @staticmethod
    def create_form(intro_text: list[str]):
        form = FormForm(intro_text)
        return form.generate()

    @staticmethod
    def create_part(
            title: str = None,
            short_name: str = None,
            class_list: list | dict = None,
            chapters: list = None,
    ):
        part = FormPart(
            title=title,
            short_name=short_name,
            class_list=class_list,
            chapters=chapters,
        )
        return part.generate()

    @staticmethod
    def create_chapter(
            title: str = '',
            class_list: list | dict = None,
            visibility_rules: list = None,
            components: list = None,
            multiple_forms_rules: dict = None,
            is_paginated: bool = False,
    ):
        chapter = FormChapter(
            title=title,
            class_list=class_list,
            visibility_rules=visibility_rules,
            components=components,
            multiple_forms_rules=multiple_forms_rules,
            is_paginated=is_paginated,
        )
        return chapter.generate()

    @staticmethod
    def create_component(
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
