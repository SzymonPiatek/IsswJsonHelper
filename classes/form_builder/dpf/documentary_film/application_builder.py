from classes.form_builder.dpf.application_builder import DPFApplicationBuilder


class DocumentaryFilmApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'IV. Produkcja filmów dokumentalnych'
    PRIORITY_NUM = 4

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.department_data_path / 'documentary_film'

    def generate(self):
        self.create_application_base()

        # Metadane wniosku
        self.create_application_metadata(task_type='Produkcja filmowa')

        # I. Dane podstawowe
        # II. Dane wnioskodawcy
        # III. Informacje
        # IV. Termin realizacji
        # V. Dane finansowe
        # VI. Dane dodatkowe
        # VII. Załączniki
        # VIII. Oświadczenia

        self.save_output()
