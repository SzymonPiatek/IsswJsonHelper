from classes.form_builder.form_builder import FormBuilder


class ApplicationBuilder(FormBuilder):
    JSON_TYPE = 'application'

    def __init__(self):
        super().__init__()

        self.load_json(name='application_metadata', path=self.main_dir / 'data' / 'base' / 'application' / 'pages' / 'application_metadata.json')

    def create_application_base(self):
        self.create_base(
            intro_text="Wniosek o dofinansowanie przedsięwzięcia realizowanego w ramach Programów Operacyjnych Polskiego Instytutu Sztuki Filmowej"
        )

    def create_application_metadata(self):
        part = self.jsons['application_metadata']
        chapters = part.get('chapters', [])

        for chapter in chapters:
            for comp in chapter.get('components', []):
                name = comp.get('name')
                if name == 'sessionYear':
                    comp['value'] = f"Sesja {self.session}/{self.year}"
                elif name == 'programName':
                    comp['value'] = self.operation_name
                elif name == 'priorityName':
                    comp['value'] = self.priority_name

        base = self.jsons.get('base')
        parts = base.setdefault('parts', [])
        parts.append(part)
