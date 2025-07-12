from classes.form_builder.dpf.application_builder import DPFApplicationBuilder


class ScreenplayScholarshipApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'I. Stypendia scenariuszowe'
    PRIORITY_NUM = 1

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.department_data_path / 'screenplay_scholarship'

    def generate(self):
        self.create_application_base()

        # Metadane wniosku
        self.create_application_metadata(task_type='Stypendium scenariuszowe')

        # I. Dane podstawowe
        section_path = self.department_data_path / '_pages' / 'application_basic_data'

        self.create_application_basic_data(
            sections=[
                {
                    "path": section_path / "scope_of_project.json",
                    "data": {
                        "number": "1",
                        "scopeOfProject": {
                            "options": [
                                "Stypendium scenariuszowe"
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
                                "animowany"
                            ]
                        },
                        "typeOfProject": {
                            "options": [
                                "stypendium scenariuszowe"
                            ]
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
                                    "film o tematyce historycznej"
                                ]
                            }
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
                    "path": section_path / "application_relates.json",
                    "data": {
                        "number": "6",
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
                        "number": "7",
                        "typeOfSupport": {
                            "options": [
                                "stypendium scenariuszowe"
                            ]
                        }
                    }
                }
            ]
        )

        # II. Dane wnioskodawcy
        self.create_application_applicant_data(
            sections=[
                {
                    "path": self.department_data_path / '_pages' / 'application_applicant_data' / 'applicant_full_name.json',
                    "data": {
                        "number": "1"
                    }
                },
                {
                    "path": self.priority_data_path / '_pages' / 'application_applicant_data' / 'applicant_data.json',
                    "data": {
                        "number": "2"
                    }
                },
                {
                    "path": self.application_data_path / '_pages' / 'application_applicant_data' / 'responsible_person.json',
                    "data": {
                        "number": "3"
                    }
                }
            ]
        )

        # III. Informacje

        # IV. Termin realizacji
        self.create_application_completion_date_data(
            sections=[]
        )

        # V. Dane finansowe
        # VI. Dane dodatkowe
        # VII. Załączniki
        # VIII. Oświadczenia

        self.save_output()
