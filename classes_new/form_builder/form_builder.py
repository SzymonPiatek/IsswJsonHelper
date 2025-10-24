from classes_new.additional.form_helpers import FormHelpers
from classes_new.form_components.section.section import Section
from classes_new.form_factory.form_factory import FormFactory
from classes_new.pisf_structure import Priority, Session
from classes_new.types import Form, Part
from typing import Literal
from pathlib import Path
import json


class FormBuilder(FormFactory):
    def __init__(
            self,
            json_type: Literal["application", "report"],
            session: Session = Session(
                year=2026,
                num=1
            ),
            priority: Priority = None
    ):
        super().__init__()

        self.json_type: Literal["application", "report"] = json_type
        self.form_id: dict[str, int] = self.set_ids()
        self.schema_id: dict[str, int] = self.set_ids()
        self.parts: list = []
        self.intro_text: list[str] = []

        self.priority: Priority = priority
        self.session: Session = session

        self.main_dir = Path(__file__).resolve().parents[2]
        self.main_dir.mkdir(parents=True, exist_ok=True)

        self.output_json: Form = None
        self._output_file_name: str = None
        self._output_file_path: Path = None

        self.helpers = FormHelpers()
        self.section = Section()

    @property
    def output_file_name(self) -> str:
        if self._output_file_name is None:
            self._output_file_name = self.prepare_output_file_name()

        return self._output_file_name

    @property
    def output_file_path(self) -> Path:
        if self._output_file_path is None:
            self._output_file_path = self.prepare_output_file_path()

        return self._output_file_path

    def prepare_output_file_name(self, file_type: str = "json"):
        file_name = f"example"

        if self.priority and self.session:
            file_name = f"po_{self.priority.operation_program.roman_num.lower()}_pr_{self.priority.num}_{self.json_type}_{self.session.year}"

        return f"{file_name}.{file_type}"

    def prepare_output_file_path(self, dir_name: str = 'jsons'):
        file_path = (
                self.main_dir / 'output' / dir_name
        )

        if self.priority and self.session:
            file_path = (
                    file_path /
                    str(self.session.year) /
                    self.priority.operation_program.department.code.upper() /
                    f"session_{self.session.num:02}" /
                    self.json_type
            )
        else:
            file_path = (file_path / self.json_type)


        return file_path

    def set_ids(self, local_id: int = None, uat_id: int = None):
        return {
            "local": local_id,
            "uat": uat_id
        }

    def generate(self):
        self.create_base()

        for index, part in enumerate(self.parts, start=1):
            part(number=index)

        self.save_output()

    def create_base(self):
        self.output_json = self.create_form(intro_text=self.intro_text)

    def save_output(self):
        self.output_file_path.mkdir(parents=True, exist_ok=True)

        full_output_file_path = (
            self.output_file_path / self.output_file_name
        )

        with full_output_file_path.open('w', encoding='utf-8') as f:
            json.dump(self.output_json, f, ensure_ascii=False, indent=2)

        print(f'JSON zapisany do {full_output_file_path}')

    def save_part(self, part: Part):
        self.output_json["parts"].append(part)


class ApplicationFormBuilder(FormBuilder):
    def __init__(self, **kwargs):
        super().__init__(
            json_type="application",
            **kwargs
        )

        self.intro_text = [
            "Wniosek o dofinansowanie przedsięwzięcia realizowanego w ramach Programów Operacyjnych Polskiego Instytutu Sztuki Filmowej"
        ]


class ReportFormBuilder(FormBuilder):
    def __init__(self, **kwargs):
        super().__init__(
            json_type="report",
            **kwargs
        )

        self.intro_text = [
            "Raport końcowy"
        ]
