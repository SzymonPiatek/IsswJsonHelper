from classes.form_builder.duk.application_builder import DUKApplicationBuilder
from classes.form_builder.additional.decorators import not_implemented_func


class DisseminationApplicationBuilder(DUKApplicationBuilder):
    OPERATION_NAME = 'III. Upowszechnianie kultury filmowej'
    OPERATION_NUM = "iii"

    def __init__(self):
        super().__init__()

        self.program_data_path = self.department_data_path / 'dissemination'
        self.priority_data_path = None

    def create_application_scope_of_project(self):
        part = self.load_json(path=self.program_data_path / '_pages' / 'scope_of_the_project.json')
        chapter = self.section.application_scope_of_project.cinema_project_relation_to_other_fundings()
        chapter["title"] = "Czy przedsięwzięcie, na które składany jest wniosek jest powiązane z innymi przedsięwzięciami, o dofinansowanie których ubiega się Wnioskodawca w bieżącym roku z innych programów operacyjnych PISF? Jeżeli tak, proszę podać nazwę przedsięwzięcia, program oraz wnioskowaną kwotę dofinansowania"
        part["chapters"].append(chapter)
        self.save_part(part)
