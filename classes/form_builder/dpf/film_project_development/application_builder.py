from classes.form_builder.dpf.application_builder import DPFApplicationBuilder


class FilmProjectDevelopmentApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'II. Rozwój projektów filmowych'
    PRIORITY_NUM = 2

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.department_data_path / 'film_project_development'

    def create_application_metadata(self, task_type: str = 'Przygotowania projektów filmowych'):
        DPFApplicationBuilder.create_application_metadata(self, task_type)

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
                            "Rozwój projektu"
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
                            "fabularny",
                            "dokumentalny",
                            "animowany",
                            "seria animowana"
                        ]
                    },
                    "typeOfProject": {
                        "options": [
                            "rozwój projektu",
                            "seria animowana"
                        ],
                        "validators": [
                            {
                                "name": "RequiredValidator"
                            },
                        ],
                        "calculationRules": [
                            {
                                "name": "assignValue",
                                "kwargs": {
                                    "options": [
                                        {
                                            "fieldName": "movieKind",
                                            "value": "fabularny",
                                            "inputValue": "rozwój projektu"
                                        },
                                        {
                                            "fieldName": "movieKind",
                                            "value": "animowany",
                                            "inputValue": "rozwój projektu"
                                        },
                                        {
                                            "fieldName": "movieKind",
                                            "value": "dokumentalny",
                                            "inputValue": "rozwój projektu"
                                        },
                                        {
                                            "fieldName": "movieKind",
                                            "value": "seria animowana",
                                            "inputValue": "seria animowana"
                                        },
                                    ]
                                }
                            }
                        ],
                        "readOnly": True,
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
                            "film o tematyce historycznej",
                            "film dla młodego widza i widowni familijnej"
                        ],
                        "validators": [
                            {
                                "name": "RelatedAllowedOptionsValidator",
                                "kwargs": {
                                    "field_name": "movieKind",
                                    "mapping": {
                                        "fabularny": [
                                            "film autorski",
                                            "film o tematyce historycznej",
                                            "film dla młodego widza i widowni familijnej"
                                        ],
                                        "animowany": [
                                            "film autorski",
                                            "film o tematyce historycznej",
                                            "film dla młodego widza i widowni familijnej"
                                        ],
                                        "dokumentalny": [
                                            "film autorski",
                                            "film o tematyce historycznej",
                                            "film dla młodego widza i widowni familijnej"
                                        ],
                                        "seria animowana": [
                                            "film dla młodego widza i widowni familijnej"
                                        ]
                                    }
                                }
                            },
                            {
                                "name": "RequiredValidator"
                            }
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
