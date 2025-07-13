from classes.form_builder.dpf.application_builder import DPFApplicationBuilder


class FeatureFilmApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'III. Produkcja filmów fabularnych'
    PRIORITY_NUM = 3

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.department_data_path / 'feature_film'

    def create_application_applicant_data(self, **kwargs):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_applicant_data.json')
        self.save_part(part=part)

    def create_application_information_data(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_information_data.json')
        self.save_part(part=part)

    def create_application_completion_date_data(self, **kwargs):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_completion_date_data.json')
        self.save_part(part=part)

    def create_application_financial_data(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_financial_data.json')
        self.save_part(part=part)

    def create_application_additional_data(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_additional_data.json')
        self.save_part(part=part)

    def create_application_attachments(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_attachments.json')
        self.save_part(part=part)

    def create_application_statements(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_statements.json')
        self.save_part(part=part)

    def generate(self):
        self.create_application_base()

        # Metadane wniosku
        self.create_application_metadata(task_type='Produkcja filmowa')

        # I. Dane podstawowe
        section_path = self.department_data_path / '_pages' / 'application_basic_data'
        priority_section_path = self.priority_data_path / '_pages' / 'application_basic_data'

        self.create_application_basic_data(
            sections=[
                {
                    "path": section_path / "scope_of_project.json",
                    "data": {
                        "number": "1",
                        "scopeOfProject": {
                            "options": [
                                "Produkcja filmowa",
                            ]
                        }
                    }
                },
                {
                    "path": section_path / "movie_kind.json",
                    "data": {
                        "number": "2",
                        "movieKind": {
                            "options": [
                                "fabularny"
                            ]
                        },
                        "typeOfProject": {
                            "options": [
                                "film fabularny"
                            ],
                            "validators": [
                                {
                                    "name": "RequiredValidator"
                                },
                            ],
                            "calculationRules": []
                        }
                    }
                },
                {
                    "path": section_path / "movie_subject.json",
                    "data": {
                        "number": "3",
                        "movieSubject": {
                            "options": [
                                "film autorski",
                                "film o tematyce historycznej"
                            ],
                            "validators": [
                                {
                                    "name": "RequiredValidator"
                                },
                                {
                                    "name": "ExactValidator",
                                    "kwargs": {
                                        "values": [
                                            "film autorski",
                                            "film o tematyce historycznej"
                                        ]
                                    }
                                },
                            ]
                        }
                    }
                },
                {
                    "path": section_path / "piece_title.json",
                    "data": {
                        "number": "4"
                    }
                },
                {
                    "path": section_path / "short_movie_description.json",
                    "data": {
                        "number": "5"
                    }
                },
                {
                    "path": section_path / "category_of_project.json",
                    "data": {
                        "number": "6"
                    }
                },
                {
                    "path": section_path / "application_relates.json",
                    "data": {
                        "number": "7",
                        "applicationRelates": {
                            "options": [
                                "promesa",
                                "umowa"
                            ]
                        }
                    }
                },
                {
                    "path": section_path / "type_of_support.json",
                    "data": {
                        "number": "8",
                        "typeOfSupport": {
                            "options": [
                                "dotacja",
                                "pożyczka",
                                "poręczenie"
                            ]
                        }
                    }
                },
                {
                    "path": priority_section_path / "committee.json",
                    "data": {
                        "number": "9"
                    }
                },
            ]
        )

        # II. Dane wnioskodawcy
        self.create_application_applicant_data()

        # III. Informacje
        self.create_application_information_data()

        # IV. Termin realizacji
        self.create_application_completion_date_data()

        # V. Dane finansowe
        self.create_application_financial_data()

        # VI. Dane dodatkowe
        self.create_application_additional_data()

        # VII. Załączniki
        self.create_application_attachments()

        # VIII. Oświadczenia
        self.create_application_statements()

        self.save_output()
