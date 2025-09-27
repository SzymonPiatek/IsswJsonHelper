from classes.form_builder.form_builder import FormBuilder


class Priority(FormBuilder):
    PRIORITY_NAME: str
    PRIORITY_NUM: str

    def __init__(self):
        super().__init__()
