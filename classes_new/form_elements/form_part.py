from .form_element import FormElement
from classes_new.types import *


class FormPart(FormElement):
    def __init__(self, title: str = None, short_name: str = None, class_list: ClassListType = None, chapters: list[dict] = None):
        super().__init__(kind="part")

        if not title:
            raise ValueError("title musi być podane")

        self.title = title
        self.short_name = short_name or title
        self.class_list = class_list or ["full-width-grid"]
        self.chapters = chapters or []

    def generate(self) -> Part:
        return {
            "kind": self.kind,
            "title": self.title,
            "shortName": self.short_name,
            "classList": self.class_list,
            "chapters": self.chapters,
        }
