from classes_new.form_builder.form_builder import ApplicationFormBuilder


class DUKDepartmentApplicationFormBuilder(ApplicationFormBuilder):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.parts = []

