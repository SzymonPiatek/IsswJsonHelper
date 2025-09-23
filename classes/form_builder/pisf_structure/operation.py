from classes.form_builder.form_builder import FormBuilder


class Operation(FormBuilder):
    OPERATION_NAME: str
    OPERATION_NUM: str

    def __init__(self):
        super().__init__()
