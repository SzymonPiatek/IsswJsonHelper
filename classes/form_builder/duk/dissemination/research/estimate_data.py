estimate_sections_pt12345 = [
    {
        'title': '1. Koszty przygotowania i zarządzania przedsięwzięciem, np. honorarium lub wynagrodzenia',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costManagement'},
            {'title': '- autorów koncepcji merytorycznej badania', 'name': 'researchAuthors'},
            {'title': '- prelegentów', 'name': 'speakers'},
            {'title': '- autorów tekstów do publikacji', 'name': 'textAuthors'},
            {'title': '- osób prowadzących wywiady', 'name': 'interviewers'},
            {'title': '- redaktorów', 'name': 'editors'},
            {
                'title': '- koordynatora zadania',
                'name': 'coordinators',
                'overrides': {
                    'RequestedAmount': {
                        'validators': [
                            {
                                "name": "RelatedFractionGTEValidator",
                                "kwargs": {
                                    "field_name": "totalRequestedAmountPt12345",
                                    "ratio": 0.1
                                },
                                "validationMsg": "Wnioskowana kwota dotacji dla kosztów honorariów wynagrodzeń koordynatorów nie może przekroczyć 10% kwoty wnioskowanej dotacji."
                            }
                        ]
                    }
                }
            }
        ]
    },
    {
        'title': '2. Koszty prowadzenia badań, ekspertyz, analiz',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'researchCosts'},
            {'title': '- konstrukcja narzędzi do badania', 'name': 'researchTools'},
            {'title': '- szkolenia badaczy', 'name': 'researchersTraining'},
            {'title': '- analiza danych zastanych, analiza wywiadów, opracowanie case study', 'name': 'dataAnalysis'},
            {'title': '- analizy statystyczne', 'name': 'statisticalAnalysis'},
            {'title': '- raport końcowy z badania', 'name': 'finalReport'}
        ]
    },
    {
        'title': '3. Koszty konsultacji eksperckich, paneli eksperckich',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'consultingCosts'}
        ]
    },
    {
        'title': '4. Koszty tłumaczenia tekstów',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'translationCost'}
        ]
    },
    {
        'title': '5. Koszty pozyskania praw autorskich',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'copyrightCosts'}
        ]
    },
    {
        'title': '6. Koszty przygotowania materiałów, redakcji i korekty',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'researchMaterialsCosts'}
        ]
    },
    {
        'title': '7. Koszty obsługi finansowej',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'financialService'}
        ]
    },
    {
        'title': '8. Koszty obsługi prawnej',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'legalService'}
        ]
    },
    {
        'title': '9. Koszty wynajęcia powierzchni/pomieszczeń na potrzeby przedsięwzięcia',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'rentalCosts'}
        ]
    },
    {
        'title': '10. Koszty promocji i reklamy',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'commercials'}
        ]
    },
    {
        'title': '11. Koszty przejazdów, noclegów realizatorów i uczestników przedsięwzięcia',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'transportationService'}
        ]
    },
    {
        'title': '12. Koszty dokumentacji/rejestracji realizacji przedsięwzięcia (filmowej, dźwiękowej, zdjęciowej)',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'documentationCosts'}
        ]
    },
    {
        'title': '13. Koszt przeprowadzenia ewaluacji przedsięwzięcia',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'evaluationCosts'}
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
                                    "field_name": "totalRequestedAmountPt6",
                                    "ratio": 0.1
                                },
                                "validationMsg": "Wnioskowana kwota dotacji dla kosztów honorariów wynagrodzeń koordynatorów nie może przekroczyć 10% kwoty wnioskowanej dotacji."
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
        'title': '6. Opracowania graficzne, usługi graficzne, fotograficzne i projektowe',
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
        'title': '11. Dokumentacja/rejestracja realizacji przedsięwzięcia',
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
    }
]
