from classes.form_builder.application_builder import ApplicationBuilder


class DUKApplicationBuilder(ApplicationBuilder):
    DEPARTMENT_NAME = 'DUK'
    def __init__(self):
        super().__init__()

    def create_application_basic_data(self, data):
        part = self.load_json(path=self.main_dir / 'data' / 'base' / 'application' / 'pages' / 'application_basic_data.json')
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

        self.save_part(part)

    def create_application_applicant_data(self):
        part = self.load_json(path=self.main_dir / 'data' / 'base' / 'application' / 'pages' / 'application_applicant_data.json')
        self.save_part(part)

    def create_application_sources_of_financing(self):
        part = self.load_json(path=self.main_dir / 'data' / 'base' / 'application' / 'custom' / 'duk' / 'sources_of_financing.json')
        self.save_part(part)


class DUKApplicationBuilder2025(DUKApplicationBuilder):
    YEAR = 2025
