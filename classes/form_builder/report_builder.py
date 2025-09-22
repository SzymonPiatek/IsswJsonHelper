from classes.form_builder.form_builder import FormBuilder


class ReportBuilder(FormBuilder):
    JSON_TYPE = 'report'

    def __init__(self):
        super().__init__()

        self.application_data_path = self.data_path / 'report'

    def create_report_base(self):
        self.create_base(
            intro_text=[
                "Raport końcowy"
            ]
        )
