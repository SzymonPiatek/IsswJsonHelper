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

    def create_application_base_data(self, sections):
        file_path = self.dpf_data_path / 'pages' / 'application_basic_data'

        part = self.load_json(path=file_path / 'layout.json')
        layout_chapters = []

        for section in sections:
            data = section['data']

            for key, value in data.items():
                if isinstance(value, dict) and 'options' in value:
                    options = value['options']
                    data[key]['value'] = options[0] if len(options) == 1 else ""
                    data[key]['readOnly'] = True if len(options) == 1 else False

            section_path = file_path / section['path']
            section_json = self.load_json(path=section_path)
            filled_section = self.replace_placeholders(section_json, data)

            layout_chapters.append(filled_section)

        part['chapters'] = layout_chapters
        self.save_part(part)
