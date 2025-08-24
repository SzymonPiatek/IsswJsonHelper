from classes.form_builder.dpf.application_builder import DPFApplicationBuilder


class ScreenplayScholarshipApplicationBuilder(DPFApplicationBuilder):
    PRIORITY_NAME = 'I. Stypendia scenariuszowe'
    PRIORITY_NUM = 1
    FORM_ID = 9194

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.department_data_path / 'screenplay_scholarship'

    def create_application_metadata(self, task_type: str = 'Stypendium scenariuszowe'):
        DPFApplicationBuilder.create_application_metadata(self, task_type)

    def create_application_basic_data(self, **kwargs):
        section_path = self.department_data_path / '_pages' / 'application_basic_data'

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
                                            "film o tematyce historycznej"
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

        self.create_part_by_sections(part=part, sections=sections)

    def create_application_applicant_data(self, **kwargs):
        part = self.create_part(
            title="II. Dane wnioskodawcy",
            short_name="II. Dane wnioskodawcy"
        )

        sections = [
            # {
            #     "path": self.department_data_path / '_pages' / 'application_applicant_data' / 'applicant_full_name.json',
            #     "data": {
            #         "number": "1"
            #     }
            # },
            # {
            #     "path": self.priority_data_path / '_pages' / 'application_applicant_data' / 'applicant_data.json',
            #     "data": {
            #         "number": "2"
            #     }
            # },
            # {
            #     "path": self.application_data_path / '_pages' / 'application_applicant_data' / 'responsible_person.json',
            #     "data": {
            #         "number": "3"
            #     }
            # }
        ]

        self.create_part_by_sections(
            part=part,
            sections=sections
        )

    def create_application_completion_date_data(self, **kwargs):
        priority_data_path = self.priority_data_path / '_pages' / 'application_completion_date_data'

        part = self.create_part(
            title="IV. Termin realizacji",
            short_name="IV. Termin realizacji",
            chapters=[
                self.create_chapter(
                    title='Stypendium scenariuszowe',
                ),
                self.create_chapter(
                    title='Termin realizacji stypendium scenariuszowego 12 miesięcy od daty podpisania umowy',
                    components=[
                        self.load_json(path=priority_data_path / 'activity_schedule.json')
                    ]
                ),
                self.create_chapter(
                    title='OBLIGATORYJNE CZYNNOŚCI W PRZYPADKU ZAWARCIA UMOWY O DOFINANSOWANIE'
                ),
                self.create_chapter(
                    title='Akceptacja scenariusza'
                ),
                self.create_chapter(
                    title='Raport końcowy'
                ),
                self.create_chapter(
                    title='Wykonanie i udokumentowanie działań obligatoryjnych wymaganych Programem operacyjnym PISF'
                )
            ]
        )

        self.save_part(part)

    def create_application_financial_data(self):
        part = self.load_json(path=self.priority_data_path / '_pages' / 'application_financial_data' / 'requested_pisf_support_amount.json')
        self.save_part(part)
