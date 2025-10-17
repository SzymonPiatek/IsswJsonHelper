from classes.form_builder.form_builder import FormBuilder


class ApplicationBuilder(FormBuilder):
    JSON_TYPE = 'application'

    def __init__(self):
        super().__init__()

        self.intro_text = [
            "Wniosek o dofinansowanie przedsięwzięcia realizowanego w ramach Programów Operacyjnych Polskiego Instytutu Sztuki Filmowej"
        ]
