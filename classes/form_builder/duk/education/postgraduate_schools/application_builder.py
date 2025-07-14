from classes.form_builder.duk.education.application_builder import EducationApplicationBuilder
from classes.form_builder.duk.application_builder import DUKApplicationBuilder
from classes.form_builder.estimate_builder.duk.application_estimate_builder import DUKApplicationEstimateBuilder


class PostgraduateSchoolsApplicationBuilder(EducationApplicationBuilder):
    PRIORITY_NAME = 'I. Szkoły wyższe i podyplomowe'
    PRIORITY_NUM = 1

    def __init__(self):
        super().__init__()

        self.priority_data_path = self.program_data_path / 'postgraduate_schools'

    def create_application_basic_data(self, **kwargs):
        data = {
            'projectType': {
                'options': [
                    "programy edukacyjne wchodzące w skład edukacji ciągłej",
                    "realizacja szkolnych i pozaszkolnych filmów krótko- i średniometrażowych",
                    "kształcenie zawodowe i podnoszenie kompetencji poprzez organizację studiów podyplomowych",
                    "inne działania realizujące cele Priorytetu I"
                ]
            }
        }
        DUKApplicationBuilder.create_application_basic_data(self=self, data=data)

    def create_application_project_costs(self):
        estimate = DUKApplicationEstimateBuilder(
            data={
                'chapters': {
                    'estimate': {
                        'sections': [
                            {
                                'title': '1. Koszty zarządzania przedsięwzięciem, np. honorarium lub wynagrodzenie',
                                'costs': [
                                    {
                                        'isSum': True,
                                        'title': 'Razem',
                                        'name': 'costManagement'
                                    },
                                    {
                                        'title': '- koordynatorów',
                                        'name': 'coordinators'
                                    },
                                    {
                                        'title': '- dyrektorów',
                                        'name': 'directors'
                                    }
                                ]
                            },
                            {
                                'title': '2. Koszty przygotowania przedsięwzięcia',
                                'costs': [
                                    {
                                        'isSum': True,
                                        'title': 'Razem',
                                        'name': 'costPreparation'
                                    },
                                    {
                                        'title': '- twórców, artystów',
                                        'name': 'creatorsArtists'
                                    },
                                    {
                                        'title': '- prelegentów, wykładowców',
                                        'name': 'lecturers'
                                    },
                                    {
                                        'title': '- osób współpracujących przy realizacji przedsięwzięcia, w tym nadzór i opieka nad studentami ',
                                        'name': 'partners'
                                    },
                                    {
                                        'title': '- osób prowadzących (np. imprezy towarzyszące, dyskusje panelowe, konferencje, spotkania z artystami, wystawy) ',
                                        'name': 'eventHosts'
                                    }
                                ]
                            },
                            {
                                'title': '3. Koszty konsultacji eksperckich, paneli eksperckich',
                                'costs': [
                                    {
                                        'isSum': True,
                                        'title': '',
                                        'name': 'expertConsultation'
                                    }
                                ]
                            },
                        ],
                        'section_structure': [
                            {
                                'label': 'Koszt ogółem',
                                'name': 'SumAmount',
                                'readOnly': True,
                            },
                            {
                                'label': 'Wnioskowana dotacja PISF',
                                'name': 'RequestedAmount'
                            },
                            {
                                'label': 'Pozostałe środki',
                                'name': 'OtherFundsAmount'
                            }
                        ],
                        'section_construct': {
                            'chapter_title': {
                                'classList': {
                                    "sub": [
                                        "table-1-2-top"
                                    ]
                                }
                            },
                            'section_title': {
                                'classList': {
                                    "main": [
                                        "table-1-3-narrow",
                                        "grid",
                                        "grid-cols-3"
                                    ],
                                    "sub": [
                                        "table-1-3__col"
                                    ]
                                }
                            }
                        }
                    },
                    'sum_estimate': {
                        'sections': [
                            {
                                'title': 'Podsumowanie',
                                'costs': [
                                    {
                                        'name': 'total'
                                    }
                                ]
                            }
                        ],
                        'section_structure': [
                            {
                                'isSum': True,
                                'label': 'Koszt ogółem',
                                'name': 'SumAmount',
                                'unit': 'PLN'
                            },
                            {
                                'isSum': True,
                                'label': 'Wnioskowana dotacja PISF ogółem',
                                'name': 'RequestedAmount',
                                'unit': 'PLN'
                            },
                            {
                                'isSum': True,
                                'label': 'Pozostałe środki ogółem',
                                'name': 'OtherFundsAmount',
                                'unit': 'PLN'
                            },
                            {
                                'isShare': True,
                                'label': 'Udział wsparcia PISF w kosztach ogółem',
                                'name': 'RequestedAmountShareInTotal',
                                'unit': '%',
                                'dividend': 'totalRequestedAmount',
                                'divisor': 'totalSumAmount',
                            }
                        ],
                        'section_construct': {
                            'section_title': {
                                'classList': {
                                    "main": [
                                        "table-1-3-narrow",
                                        "grid",
                                        "grid-cols-3"
                                    ],
                                    "sub": [
                                        "table-1-3__col"
                                    ]
                                }
                            }
                        }
                    }
                }
            }
        )

        part = self.create_part(
            title='VII. Kosztorys przedsięwzięcia',
            short_name='VII. Kosztorys przedsięwzięcia',

            chapters=[
                estimate.generate()
            ]
        )

        self.save_part(part=part)
