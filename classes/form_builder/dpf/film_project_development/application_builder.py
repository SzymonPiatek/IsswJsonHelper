from classes.form_builder.dpf.application_builder import DPFApplicationBuilder


class FilmProjectDevelopmentApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'II. Rozwój projektów filmowych'
    PRIORITY_NUM = 2

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.department_data_path / 'film_project_development'

    def generate(self):
        self.create_application_base()

        # Metadane wniosku
        self.create_application_metadata(task_type='Przygotowanie projektów filmowych')

        # I. Dane podstawowe

        # II. Dane wnioskodawcy
        # III. Informacje
        # IV. Termin realizacji
        # V. Dane finansowe
        # VI. Dane dodatkowe
        # VII. Załączniki
        # VIII. Oświadczenia

        self.save_output()
