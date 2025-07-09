from classes.form_builder.application_builder import ApplicationBuilder


class DUKApplicationBuilder(ApplicationBuilder):
    DEPARTMENT_NAME = 'DUK'
    def __init__(self):
        super().__init__()

        self.load_json(name='application_basic_data',
                       path=self.main_dir / 'data' / 'base' / 'application' / 'pages' / 'application_basic_data.json')

    def create_application_basic_data(self, data):
        part = self.jsons['application_basic_data']
        chapters = part.get('chapters', [])

        for chapter in chapters:
            for comp in chapter.get('components', []):
                name = comp.get('name')
                if name == 'programNamePartTwo':
                    comp['value'] = self.operation_name
                elif name == 'priorityNamePartTwo':
                    comp['value'] = self.priority_name
                elif name == 'projectType':
                    comp['options'] = data['projectType']['options']

                    validators = comp.get('validators', [])
                    for validator in validators:
                        if validator.get('name') == 'ExactValidator':
                            validator['kwargs']['values'] = data['projectType']['options']

        base = self.jsons.get('base')
        parts = base.setdefault('parts', [])
        parts.append(part)

class DUKApplicationBuilder2025(DUKApplicationBuilder):
    YEAR = 2025
