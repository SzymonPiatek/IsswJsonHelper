estimate_sections_pt1234 = [
    {
        'title': '1. Koszty przygotowania i zarządzania przedsięwzięciem',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costManagement'},
            {'title': '- autorów tekstów do publikacji', 'name': 'textAuthors'},
            {'title': '- redaktorów', 'name': 'bookEditors'},
            {'title': '- korektorów', 'name': 'proofreaders'}
        ]
    },
    {
        'title': '2. Koszty publikacji',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'publicationCosts'},
            {'title': '- opracowania typograficznego', 'name': 'typographicCosts'},
            {'title': '- opracowanie graficzne usługi graficzne, fotograficzne i projektowe',
             'name': 'graphicCosts'},
            {'title': '- usługi wydawnicze i poligraficzne', 'name': 'printingCosts'},
            {'title': '- nagrania i zwielokrotnienia utworu wydanego w formie audiobooka',
             'name': 'audiobookCosts'},
            {'title': '- przygotowania publikacji w wersji elektronicznej', 'name': 'ebookCosts'},
            {'title': '- tworzenia wersji internetowej czasopisma i jej obsługa',
             'name': 'onlineMagazineCosts'}
        ]
    },
    {
        'title': '3. Koszty tłumaczenia tekstów',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'translationCost'}
        ]
    },
    {
        'title': '4. Koszty pozyskania praw autorskich',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'copyrightCosts'}
        ]
    },
    {
        'title': '5. Koszty obsługi finansowej',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'financialService'}
        ]
    },
    {
        'title': '6. Koszty obsługi prawnej',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'legalCosts'}
        ]
    },
    {
        'title': '7. Koszty przejazdów, noclegów realizatorów przedsięwzięcia',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'transportationService'}
        ]
    },
    {
        'title': '8. Koszty dokumentacji/rejestracji realizacji przedsięwzięcia',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'documentationCosts'}
        ]
    },
    {
        'title': '9. Koszty dystrybucji',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'distributionCosts'}
        ]
    },
    {
        'title': '10. Koszt przeprowadzenia ewaluacji przedsięwzięcia',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'evaluationCosts'}
        ]
    }
]

estimate_sections_pt5 = [
    {
        'title': '1. Koszty przygotowania i zarządzania przedsięwzięciem',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costManagement'},
            {'title': '- twórców', 'name': 'creators'},
            {'title': '- autorów', 'name': 'textAuthors'},
            {'title': '- redaktorów', 'name': 'bookEditors'},
            {'title': '- informatyków', 'name': 'itSpecialists'}
        ]
    },
    {
        'title': '2. Koszty utrzymania portali, serwisów, baz z zakresu wiedzy o filmie',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'publicationCosts'},
            {'title': '- koszty projektu, w tym koszty programowania i testowania - wyłącznie na potrzeby zadania',
             'name': 'programmingCosts'},
            {'title': '- koszty opracowań graficznych, usług graficznych, fotograficznych i projektowych',
             'name': 'graphicCosts'}
        ]
    },
    {
        'title': '3. Koszty tłumaczenia tekstów',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'translationCost'}
        ]
    },
    {
        'title': '4. Koszty pozyskania praw autorskich',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'copyrightCosts'}
        ]
    },
    {
        'title': '5. Koszty obsługi finansowej',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'financialService'}
        ]
    },
    {
        'title': '6. Koszty obsługi prawnej',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'legalCosts'}
        ]
    },
    {
        'title': '7. Koszty przejazdów, noclegów realizatorów przedsięwzięcia',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'transportationService'}
        ]
    },
    {
        'title': '8. Koszty dokumentacji/rejestracji realizacji przedsięwzięcia',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'documentationCosts'}
        ]
    },
    {
        'title': '9. Koszt przeprowadzenia ewaluacji przedsięwzięcia',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'evaluationCosts'}
        ]
    },
    {
        'title': '10. Koszty związane z dostosowaniem działań i formy przekazu do osób ze szczególnymi potrzebami',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'accessibility'}
        ]
    }
]

estimate_sections_pt6 = [
    {
        'title': '1. Koszty przygotowania i zarządzania przedsięwzięciem',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costManagement'},
            {
                'title': '- koordynatora projektu',
                'name': 'coordinators',
                'overrides': {
                    'RequestedAmount': {
                        'validators': [
                            {
                                "name": "RelatedFractionGTEValidator",
                                "kwargs": {
                                    "field_name": "pisfSupportAmount",
                                    "ratio": 0.1
                                },
                                "validationMsg": "Kwota dofinansowania dla kosztów honorariów koordynatora nie może przekroczyć 10% kwoty wnioskowanej."
                            }
                        ]
                    }
                }
            },
            {'title': '- inne (podać jakie)', 'name': 'otherManagement'}
        ]
    },
    {
        'title': '2. Koszty konsultacji eksperckich',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'consultingCosts'}
        ]
    },
    {
        'title': '3. Koszty tłumaczeń',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'translationCost'}
        ]
    },
    {
        'title': '4. Koszty obsługi PR',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'prService'}
        ]
    },
    {
        'title': '5. Koszty promocji i reklamy',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'commercials'},
            {'title': '- outdoor', 'name': 'outdoorCommercials'},
            {'title': '- reklama prasowa, radiowa, telewizyjna, internetowa', 'name': 'mediaCommercials'}
        ]
    },
    {
        'title': '6. Koszty opracowań graficznych, usług graficznych, fotograficznych i projektowych',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'graphicService'}
        ]
    },
    {
        'title': '7. Koszty usług poligraficznych/DTP',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'printingCosts'},
            {'title': '- projekt', 'name': 'printingCostsProject'},
            {'title': '- skład', 'name': 'printingCostsTypesetting'},
            {'title': '- druk', 'name': 'printingCostsPrint'}
        ]
    },
    {
        'title': '8. Koszty przygotowania materiałów multimedialnych',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'multimediaMaterialsCosts'}
        ]
    },
    {
        'title': '9. Koszty obsługi finansowej',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'financialService'}
        ]
    },
    {
        'title': '10. Koszty przejazdów, noclegów realizatorów przedsięwzięcia',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'transportationService'}
        ]
    },
    {
        'title': '11. Koszty dokumentacji/rejestracji realizacji przedsięwzięcia',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'documentationCosts'}
        ]
    },
    {
        'title': '12. Koszty praw autorskich',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'copyrightCosts'}
        ]
    },
    {
        'title': '13. Koszt przeprowadzenia ewaluacji przedsięwzięcia',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'evaluationCosts'}
        ]
    },
    {
        'title': '14. Koszty związane z dostosowaniem działań i formy przekazu do osób ze szczególnymi potrzebami',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'accessibility'}
        ]
    }
]
