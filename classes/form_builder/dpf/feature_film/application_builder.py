from classes.form_builder.dpf.application_builder import DPFApplicationBuilder


class FeatureFilmApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'III. Produkcja filmów fabularnych'
    PRIORITY_NUM = 3
    FORM_ID = 9196

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.department_data_path / 'feature_film'

    def create_application_basic_data(self, **kwargs):
        section_path = self.department_data_path / '_pages' / 'application_basic_data'
        priority_section_path = self.priority_data_path / '_pages' / 'application_basic_data'

        part = self.create_part(
            title='I. Dane podstawowe',
            short_name='I. Dane podstawowe',
        )

        sections = [
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

        self.create_part_by_sections(part=part, sections=sections)
