from classes.form_builder.dpf.application_builder import DPFApplicationBuilder


class FilmProjectDevelopmentApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'II. Rozwój projektów filmowych'

    def __init__(self):
        super().__init__()

        self.screenplay_data_path = self.dpf_data_path / 'film_project_development'

    def generate(self):
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
