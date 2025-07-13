from classes.form_builder.dpf.application_builder import DPFApplicationBuilder


class AnimatedFilmApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'V. Produkcja filmów animowanych'
    PRIORITY_NUM = 5

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.department_data_path / 'animated_film'

    def create_application_basic_data(self, **kwargs):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_basic_data.json')
        self.save_part(part=part)

    def create_application_applicant_data(self, **kwargs):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_applicant_data.json')
        self.save_part(part=part)

    def create_application_information_data(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_information_data.json')
        self.save_part(part=part)

    def create_application_completion_date_data(self, **kwargs):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_completion_date_data.json')
        self.save_part(part=part)

    def create_application_financial_data(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_financial_data.json')
        self.save_part(part=part)

    def create_application_additional_data(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_additional_data.json')
        self.save_part(part=part)

    def create_application_attachments(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_attachments.json')
        self.save_part(part=part)

    def create_application_statements(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_statements.json')
        self.save_part(part=part)

    def generate(self):
        self.create_application_base()

        # Metadane wniosku
        self.create_application_metadata(task_type='Produkcja filmowa')

        # I. Dane podstawowe
        self.create_application_basic_data()

        # II. Dane wnioskodawcy
        self.create_application_applicant_data()

        # III. Informacje
        self.create_application_information_data()

        # IV. Termin realizacji
        self.create_application_completion_date_data()

        # V. Dane finansowe
        self.create_application_financial_data()

        # VI. Dane dodatkowe
        self.create_application_additional_data()

        # VII. Załączniki
        self.create_application_attachments()

        # VIII. Oświadczenia
        self.create_application_statements()

        self.save_output()
