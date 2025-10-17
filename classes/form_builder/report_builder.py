from classes.form_builder.form_builder import FormBuilder


class ReportBuilder(FormBuilder):
    JSON_TYPE = 'report'

    def __init__(self):
        super().__init__()

        self.intro_text = ["Raport końcowy"]
