from classes.form_builder.application_builder import ApplicationBuilder


class DWMApplicationBuilder(ApplicationBuilder):
    DEPARTMENT_NAME = 'DWM'
    OPERATION_NAME = 'I. Promocja polskiej twórczości filmowej za granicą'
    OPERATION_NUM = 5

    def __init__(self):
        super().__init__()

        self.department_data_path = self.application_data_path / 'dwm'
        self.priority_data_path = None

    def create_application_description_of_the_project_data(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_description_of_the_project_data.json')
        self.save_part(part=part)

    def create_application_logo_data(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_logo_data.json')
        self.save_part(part=part)

    def create_application_implementation_effects_data(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_implementation_effects_data.json')
        self.save_part(part=part)

    def create_application_other_information_data(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_other_information_data.json')
        self.save_part(part=part)

    def create_application_financial_data(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_financial_data.json')
        self.save_part(part=part)

    def create_application_statements(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_statements.json')
        self.save_part(part=part)

    def create_application_attachments(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_attachments.json')
        self.save_part(part=part)

    def create_application_schedule_data(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_schedule_data.json')
        self.save_part(part=part)

    def generate(self):
        # Base
        self.create_application_base()

        # 1. Nazwa programu i priorytetu
        self.create_application_metadata()

        # 2. Nazwa przedsięwzięcia
        self.create_application_name_data()

        # 3. Informacja o wnioskodawcy
        self.create_application_applicant_data()

        # 4. Dorobek wnioskodawcy
        self.create_application_applicant_achievements_data()

        # 5. Opis przedsięwzięcia
        self.create_application_description_of_the_project_data()

        # 6. Logotyp PISF
        self.create_application_logo_data()

        # 7. Efekty realizacji
        self.create_application_implementation_effects_data()

        # 8. Inne informacje
        self.create_application_other_information_data()

        # 9. Koszty przedsięwzięcia
        self.create_application_financial_data()

        # 10. Oświadczenia
        self.create_application_statements()

        # 11. Załączniki
        self.create_application_attachments()

        # 12. Harmonogram
        self.create_application_schedule_data()

        self.save_output()
