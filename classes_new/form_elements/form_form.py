from .form_element import FormElement
from classes_new.types import Form


class FormForm(FormElement):
    def __init__(self, intro_text: list[str]):
        super().__init__(kind="form")

        self.intro_text = intro_text

    def generate(self) -> Form:
        if not self.intro_text or not isinstance(self.intro_text, list):
            raise ValueError("Intro_text musi być niepustą listą tekstów")

        return {
            "kind": self.kind,
            "jrwa": "",
            "expert": {"name": "", "email": "", "avatar": ""},
            "status": "",
            "applicant": {},
            "title": "",
            "introText": [{"text": text} for text in self.intro_text],
            "blanks": [],
            "parts": [],
        }
