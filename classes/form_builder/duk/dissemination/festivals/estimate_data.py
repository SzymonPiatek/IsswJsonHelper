estimate_sections = [
    {
        'title': '1. Koszty przygotowania i zarządzania przedsięwzięciem',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costManagement'},
            {
                'title': '- dyrektora festiwalu',
                'name': 'festivalDirector',
                'overrides': {
                    'RequestedAmount': {
                        'validators': [
                            {
                                "name": "RelatedFractionGTEValidator",
                                "kwargs": {
                                    "field_name": "pisfSupportAmount",
                                    "ratio": 0.1
                                },
                                "validationMsg": "Kwota dofinansowania dla kosztów honorariów dyrektora festiwalu nie może przekroczyć 10% kwoty wnioskowanej."
                            }
                        ]
                    }
                }
            },
            {
                'title': '- dyrektora artystycznego/dyrektora programowego',
                'name': 'artisticDirector',
                'overrides': {
                    'RequestedAmount': {
                        'validators': [
                            {
                                "name": "RelatedFractionGTEValidator",
                                "kwargs": {
                                    "field_name": "pisfSupportAmount",
                                    "ratio": 0.1
                                },
                                "validationMsg": "Kwota dofinansowania dla kosztów honorariów dyrektora artystycznego lub programowego nie może przekroczyć 10% kwoty wnioskowanej."
                            }
                        ]
                    }
                }
            },
            {'title': '- twórców, artystów', 'name': 'creatorsArtists'},
            {'title': '- członków jury', 'name': 'juryMembers'},
            {'title': '- osób prowadzących (np. imprezy towarzyszące, dyskusje panelowe, konferencje, spotkania z artystami, wystawy)', 'name': 'eventHosts'}
        ]
    },
    {
        'title': '2. Koszty konsultacji eksperckich, paneli eksperckich',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'expertConsultation'}
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
            {'isSum': True, 'title': '', 'name': 'prServiceCosts'}
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
        'title': '6. Koszty usług graficznych, fotograficznych i projektowych',
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
        'title': '8. Koszty obsługi finansowej',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'financialService'}
        ]
    },
    {
        'title': '9. Koszty związane z miejscem realizacji przedsięwzięcia',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'locationCosts'},
            {'title': '- koszty wynajmu sali lub powierzchni na potrzeby przedsięwzięcia', 'name': 'rentalCosts'},
            {'title': '- koszty aranżacji przestrzeni, w tym zabezpieczenia BHP', 'name': 'spaceArrangementCosts'}
        ]
    },
    {
        'title': '10. Koszty obsługi przedsięwzięcia',
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
            },
            {'title': '- koszty najmu sprzętu', 'name': 'equipmentRentalCosts'}
        ]
    },
    {
        'title': '11. Koszty usług transportowych',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'transportationService'}
        ]
    },
    {
        'title': '12. Koszty dotyczące podróży',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'tripCosts'},
            {'title': '- organizatorów przedsięwzięcia', 'name': 'hostsTripCosts'},
            {'title': '- twórców, artystów, prelegentów', 'name': 'participantsTripCosts'},
            {'title': '- zaproszonych gości', 'name': 'guestsTripCosts'}
        ]
    },
    {
        'title': '13. Koszty dotyczące noclegów',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'accommodationCosts'},
            {'title': '- organizatorów przedsięwzięcia', 'name': 'hostsAccommodationCosts'},
            {'title': '- twórców, artystów, prelegentów', 'name': 'participantsAccommodationCosts'},
            {'title': '- zaproszonych gości', 'name': 'guestsAccommodationCosts'}
        ]
    },
    {
        'title': '14. Koszty dokumentacji/rejestracji realizacji przedsięwzięcia',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'documentationCosts'}
        ]
    },
    {
        'title': '15. Koszty ubezpieczeń',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'insuranceCosts'}
        ]
    },
    {
        'title': '16. Koszty praw autorskich',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'copyrightsCosts'},
            {'title': '- koszty nabycia praw autorskich lub licencji', 'name': 'copyrightsAcquisitionCosts'},
            {'title': '- koszty najmu kopii', 'name': 'copyRentalCosts'}
        ]
    },
    {
        'title': '17. Koszty nagród dla twórców, uczestniczących w konkursach',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'awardsCosts'}
        ]
    },
    {
        'title': '18. Koszty działań i wydarzeń bezpośrednio związanych z realizacją przedsięwzięcia',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'relatedEventsCosts'}
        ]
    },
    {
        'title': '19. Koszty cateringu',
        'costs': [
            {
                'isSum': True,
                'title': '',
                'name': 'cateringCosts',
                'overrides': {
                    'RequestedAmount': {
                        'validators': [
                            {
                                "name": "RelatedFractionGTEValidator",
                                "kwargs": {
                                    "field_name": "pisfSupportAmount",
                                    "ratio": 0.1
                                },
                                "validationMsg": "Kwota dofinansowania dla kosztów cateringu nie może przekroczyć 10% kwoty wnioskowanej."
                            }
                        ]
                    }
                }
            }
        ]
    },
    {
        'title': '20. Koszt przeprowadzenia ewaluacji przedsięwzięcia',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'evaluationCosts'}
        ]
    },
    {
        'title': '21. Koszty obsługi festiwalu online',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'onlineManagementCosts'}
        ]
    },
    {
        'title': '22. Koszty związane z przygotowaniem kopii filmowych oraz napisów do filmów',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'copyingAndSubtitlingCosts'}
        ]
    },
    {
        'title': '23. Koszty związane z dostosowaniem działań i formy przekazu do osób ze szczególnymi potrzebami, w tym osób z niepełnosprawnościami',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'accessibilityCosts'}
        ]
    }
]
