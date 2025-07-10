from classes.form_builder.application_builder import ApplicationBuilder


class DPFApplicationBuilder(ApplicationBuilder):
    DEPARTMENT_NAME = 'DPF'
    OPERATION_NAME = 'I. Produkcja filmowa'

    def __init__(self):
        super().__init__()

        self.dpf_data_path = self.application_data_path / 'dpf'

    def create_application_metadata(self, task_type: str):
        part = self.load_json(path=self.dpf_data_path / 'pages' / 'application_metadata.json')

        values = {
            "sessionYear": f"Sesja {self.session}/{self.year}",
            "programName": self.operation_name,
            "priorityName": self.priority_name,
            "taskType": task_type
        }

        final_part = self.replace_placeholders(part, values)
        self.save_part(final_part)

