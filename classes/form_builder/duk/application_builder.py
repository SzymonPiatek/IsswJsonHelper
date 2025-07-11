from classes.form_builder.application_builder import ApplicationBuilder


class DUKApplicationBuilder(ApplicationBuilder):
    DEPARTMENT_NAME = 'DUK'

    def __init__(self):
        super().__init__()

        self.duk_data_path = self.application_data_path / 'duk'

    def create_application_metadata(self):
        part = self.load_json(path=self.duk_data_path / '_pages' / 'application_metadata.json')

        values = {
            "sessionYear": f"Sesja {self.session}/{self.year}",
            "programName": self.operation_name,
            "priorityName": self.priority_name
        }

        final_part = self.replace_placeholders(part, values)
        self.save_part(final_part)

    def create_application_basic_data(self, data):
        part = self.load_json(path=self.duk_data_path / '_pages' / 'application_basic_data.json')
        values = {
            "programNamePartTwo": self.operation_name,
            "priorityNamePartTwo": self.priority_name,
            "projectType": {
                "options": data["projectType"]["options"],
                "value": data['projectType']['options'][0] if len(data['projectType']['options']) == 1 else "",
                "readOnly": True if len(data['projectType']['options']) == 1 else False
            }
        }
        final_part = self.replace_placeholders(part, values)
        self.save_part(final_part)

    def create_application_applicant_data(self):
        part = self.create_part(
            title="II. Dane wnioskodawcy",
            short_name="II. Dane wnioskodawcy"
        )

        self.create_part_by_sections(
            part=part,
            sections=[
                {
                    "path": self.duk_data_path / '_pages' / 'application_applicant_data' / 'applicant_full_name.json',
                    "data": {
                        "number": "1"
                    }
                },
                {
                    "path": self.application_data_path / '_pages' / 'application_applicant_data' / 'eligible_person.json',
                    "data": {
                        "number": "2"
                    }
                },
                {
                    "path": self.application_data_path / '_pages' / 'application_applicant_data' / 'responsible_person.json',
                    "data": {
                        "number": "3"
                    }
                },
                {
                    "path": self.application_data_path / '_pages' / 'application_applicant_data' / 'applicant_main_address.json',
                    "data": {
                        "number": "4",
                        "applicantResidence": {
                            "options": [
                                "w Polsce",
                                "za granicą"
                            ]
                        }
                    }
                },
                {
                    "path": self.application_data_path / '_pages' / 'application_applicant_data' / 'applicant_contact_address.json',
                    "data": {
                        "number": "5",
                        "applicantContactResidence": {
                            "options": [
                                "w Polsce",
                                "za granicą"
                            ]
                        }
                    }
                },
                {
                    "path": self.application_data_path / '_pages' / 'application_applicant_data' / 'bank_data.json',
                    "data": {
                        "number": "6"
                    }
                },
                {
                    "path": self.application_data_path / '_pages' / 'application_applicant_data' / 'legal_information.json',
                    "data": {
                        "number": "7"
                    }
                },
                {
                    "path": self.application_data_path / '_pages' / 'application_applicant_data' / 'statistical_data.json',
                    "data": {
                        "number": "8"
                    }
                },
            ]
        )

    def create_application_sources_of_financing(self):
        part = self.load_json(path=self.duk_data_path / '_pages' / 'application_sources_of_financing.json')
        self.save_part(part)

    def create_application_statements(self):
        part = self.load_json(path=self.duk_data_path / '_pages' / 'application_statements.json')
        self.save_part(part)

    def create_application_attachments(self):
        part = self.load_json(path=self.duk_data_path / '_pages' / 'application_attachments.json')
        self.save_part(part)

    def create_application_schedule(self):
        part = self.load_json(path=self.duk_data_path / '_pages' / 'application_schedule.json')
        self.save_part(part)
