from classes.form_builder.dpf.application_builder import DPFApplicationBuilder


class AnimatedFilmApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'V. Produkcja filmów animowanych'
    PRIORITY_NUM = 5
    FORM_ID = 9198

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.department_data_path / 'animated_film'
