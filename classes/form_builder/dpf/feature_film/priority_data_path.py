from classes.form_builder.dpf.application_builder import DPFApplicationBuilder


class FeatureFilmApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'III. Produkcja filmów fabularnych'
    PRIORITY_NUM = 3

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.department_data_path / 'feature_film'

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

        # III. Informacje

        # IV. Termin realizacji

        # V. Dane finansowe

        # VI. Dane dodatkowe

        # VII. Załączniki

        # VIII. Oświadczenia

        self.save_output()
