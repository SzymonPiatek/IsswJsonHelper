estimate_sections = [
    {
        'title': '1. Koszty zarządzania przedsięwzięciem',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costManagement'},
            {
                'title': '- koordynatorów',
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
                                "validationMsg": "Kwota dofinansowania dla kosztów honorariów koordynatorów nie może przekroczyć 10% kwoty wnioskowanej."
                            }
                        ]
                    }
                }
            },
            {
                'title': '- dyrektorów',
                'name': 'directors',
                'overrides': {
                    'RequestedAmount': {
                        'validators': [
                            {
                                "name": "RelatedFractionGTEValidator",
                                "kwargs": {
                                    "field_name": "pisfSupportAmount",
                                    "ratio": 0.1
                                },
                                "validationMsg": "Kwota dofinansowania dla kosztów honorariów dyrektorów nie może przekroczyć 10% kwoty wnioskowanej."
                            }
                        ]
                    }
                }
            }
        ]
    },
    {
        'title': '2. Koszty przygotowania przedsięwzięcia',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costPreparation'},
            {'title': '- twórców, artystów', 'name': 'creatorsArtists'},
            {'title': '- prelegentów, wykładowców', 'name': 'lecturers'}
        ]
    },
    {
        'title': '3. Koszty promocji i reklamy',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'prServiceCosts'}
        ]
    },
    {
        'title': '4. Koszty usług graficznych, fotograficznych lub projektowych',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'graphicService'}
        ]
    },
    {
        'title': '5. Koszty usług poligraficznych/DTP',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'printingCosts'},
            {'title': '- projekt', 'name': 'printingCostsProject'},
            {'title': '- skład', 'name': 'printingCostsTypesetting'},
            {'title': '- druk', 'name': 'printingCostsPrint'}
        ]
    },
    {
        'title': '6. Koszty obsługi finansowej',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'financialService'}
        ]
    },
    {
        'title': '7. Koszty związane z miejscem realizacji przedsięwzięcia',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'locationCosts'},
            {'title': '- koszty wynajmu sali lub powierzchni na potrzeby przedsięwzięcia', 'name': 'rentalCosts'}
        ]
    },
    {
        'title': '8. Koszty obsługi przedsięwzięcia',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'eventHostingCosts'},
            {
                'title': '- koszty osobowe',
                'name': 'personalCosts',
                'overrides': {
                    'RequestedAmount': {
                        'validators': [
                            {
                                "name": "RelatedFractionGTEValidator",
                                "kwargs": {
                                    "field_name": "pisfSupportAmount",
                                    "ratio": 0.3
                                },
                                "validationMsg": "Kwota dofinansowania dla kosztów osobowych nie może przekroczyć 30% kwoty wnioskowanej."
                            }
                        ]
                    }
                }
            }
        ]
    },
    {
        'title': '9. Koszty dotyczące podróży',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'tripCosts'},
            {'title': '- organizatorów przedsięwzięcia', 'name': 'hostsTripCosts'},
            {'title': '- twórców, artystów, prelegentów', 'name': 'participantsTripCosts'},
            {'title': '- zaproszonych gości', 'name': 'guestsTripCosts'}
        ]
    },
    {
        'title': '10. Koszty dotyczące noclegów',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'accommodationCosts'},
            {'title': '- organizatorów przedsięwzięcia', 'name': 'hostsAccommodationCosts'},
            {'title': '- twórców, artystów, prelegentów', 'name': 'participantsAccommodationCosts'},
            {'title': '- zaproszonych gości', 'name': 'guestsAccommodationCosts'}
        ]
    },
    {
        'title': '11. Koszty ubezpieczeń',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'insuranceCosts'}
        ]
    },
    {
        'title': '12. Koszty praw autorskich',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'copyrightsCosts'},
            {'title': '- koszty pozyskania praw autorskich lub licencji', 'name': 'copyrightsAcquisitionCosts'},
            {'title': '- koszty najmu kopii', 'name': 'copyRentalCosts'}
        ]
    },
    {
        'title': '13. Koszty związane z dostosowaniem działań i formy przekazu do osób ze szczególnymi potrzebami, w tym osób z niepełnosprawnościami',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'disabledAdaptationCosts'}
        ]
    },
    {
        'title': '14. Koszty bezpośrednio związane z realizacją przedsięwzięcia',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'otherDirectCosts'}
        ]
    },
    {
        'title': '15. Koszt przeprowadzenia ewaluacji przedsięwzięcia',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'evaluationCosts'}
        ]
    },
    {
        'title': '16. Koszty obsługi projektów edukacyjnych online',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'onlineManagementCosts'}
        ]
    }
]
