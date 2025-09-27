from .form_element import FormElement


class FormPart(FormElement):
    def __init__(self, title: str = None, short_name: str = None, class_list: list | dict = None, chapters: list = None):
        super().__init__(kind="part")

        if not title:
            raise ValueError("title musi być podane")

        self.title = title
        self.short_name = short_name or title
        self.class_list = class_list or ["full-width-grid"]
        self.chapters = chapters or []

    def generate(self):
        return {
            "kind": self.kind,
            "title": self.title,
            "short_name": self.short_name,
            "class_list": self.class_list,
            "chapters": self.chapters,
        }
