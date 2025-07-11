from classes.form_builder.dpf.application_builder import DPFApplicationBuilder


class ScreenplayScholarshipApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'I. Stypendia scenariuszowe'

    def __init__(self):
        super().__init__()

        self.screenplay_data_path = self.dpf_data_path / 'screenplay_scholarship'

    def generate(self):
        self.create_application_base()

        # Metadane wniosku
        self.create_application_metadata(task_type='Stypendium scenariuszowe')

        # I. Dane podstawowe
        self.create_application_base_data(
            sections=[
                {
                    "path": "scope_of_project.json",
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
                    "path": "movie_kind.json",
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
                    "path": "movie_subject.json",
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
                    "path": "piece_title.json",
                    "data": {
                        "number": "4"
                    }
                },
                {
                    "path": "short_movie_description.json",
                    "data": {
                        "number": "5"
                    }
                },
                {
                    "path": "application_relates.json",
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
                    "path": "type_of_support.json",
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
        # III. Informacje
        # IV. Termin realizacji
        # V. Dane finansowe
        # VI. Dane dodatkowe
        # VII. Załączniki
        # VIII. Oświadczenia

        self.save_output()
