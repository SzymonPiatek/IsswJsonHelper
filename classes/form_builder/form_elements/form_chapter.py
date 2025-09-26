from .form_element import FormElement


class FormChapter(FormElement):
    def __init__(
            self,
            title: str = '',
            class_list: list | dict = None,
            visibility_rules: list = None,
            components: list = None,
            multiple_forms_rules: dict = None,
            is_paginated: bool = False,
    ):
        super().__init__(kind="chapter")

        self.title = title
        self.class_list = class_list
        self.visibility_rules = visibility_rules
        self.components = components or []
        self.multiple_forms_rules = multiple_forms_rules
        self.is_paginated = is_paginated

    def generate(self):
        if self.multiple_forms_rules:
            if self.multiple_forms_rules.get("maxCount", 1) > 5:
                self.is_paginated = True

            mf_min_count = self.multiple_forms_rules.get("minCount", 1)

            if len(self.components) == 0:
                raise ValueError("Chapter z multipleForms powinien posiadać przynajmniej jeden chapter")
            if len(self.components) != mf_min_count:
                start_chapter = self.components[0]
                start_title = start_chapter.get("title", "")
                self.components = self.duplicate_chapter_with_indexing(start_chapter, mf_min_count, start_title)

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

            set_default_value(self.components)

        kwargs = {
            "kind": self.kind,
            "title": self.title,
            "components": self.components,
        }

        if self.class_list:
            kwargs["classList"] = self.class_list
        if self.visibility_rules:
            kwargs["visibilityRules"] = self.visibility_rules
        if self.multiple_forms_rules:
            kwargs["isMultipleForms"] = True
            kwargs["multipleFormsRules"] = self.multiple_forms_rules
            kwargs["isPaginated"] = self.is_paginated

        return kwargs

    @staticmethod
    def duplicate_chapter_with_indexing(start_chapter: dict, mf_min_count: int, start_title: str = None) -> list:
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
