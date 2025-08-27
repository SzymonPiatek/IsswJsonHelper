estimate_sections_pt1 = [
    {
        'title': '1. Koszty zarządzania przedsięwzięciem',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costManagement'},
            {
                'title': '- dyrektora festiwalu lub przeglądu',
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
                                "validationMsg": "Kwota dofinansowania dla kosztów honorariów dyrektora festiwalu lub przeglądu nie może przekroczyć 10% kwoty wnioskowanej."
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
            {'isSum': True, 'title': 'Razem', 'name': 'copyrightCosts'},
            {'title': '- koszty nabycia praw autorskich lub licencji', 'name': 'copyrightsPurchaseCosts'},
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
        'title': '18. Koszty wydarzeń bezpośrednio związanych z realizacją przedsięwzięcia',
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
        'title': '21. Koszty obsługi projektów online',
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

estimate_sections_pt2 = [
    {
        'title': '1. Działalność ekspercka',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'expertsCosts'},
            {'title': '- wynagrodzenia ekspertów', 'name': 'expertsFees'},
            {'title': '- koszty podróży ekspertów', 'name': 'expertsTripCosts'},
            {'title': '- koszty noclegów ekspertów', 'name': 'expertsAccommodationCosts'}
        ]
    },
    {
        'title': '2. Rozpowszechnianie repertuaru studyjnego',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'disseminationSubsidies'}
        ]
    },
    {
        'title': '3. Koszty wsparcia wydarzeń filmowych realizowanych przez kina studyjne',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'localCinemasSupport'},
            {'title': '- wynagrodzenia twórców, artystów, prelegentów', 'name': 'artistsRemunerationCostsA'},
            {'title': '- wynagrodzenia osób prowadzących', 'name': 'hostsRemunerationCostsA'},
            {'title': '- koszty tłumaczeń', 'name': 'translationCostA'},
            {'title': '- koszty promocji i reklamy', 'name': 'commercialsA'},
            {'title': '- koszty usług graficznych, fotograficznych i projektowych', 'name': 'graphicServiceA'},
            {'title': '- koszty usług poligraficznych/DTP', 'name': 'printingCostsA'},
            {'title': '- koszty najmu sprzętu', 'name': 'equipmentRentalCostsA'},
            {'title': '- koszty usług transportowych', 'name': 'transportationServiceA'},
            {'title': '- koszty podróży', 'name': 'tripCostsA'},
            {'title': '- koszty noclegów', 'name': 'accommodationCostsA'},
            {'title': '- koszty dokumentacji/rejestracji', 'name': 'documentationCostsA'},
            {'title': '- koszty ubezpieczeń', 'name': 'insuranceCostsA'},
            {'title': '- koszty pozyskania praw autorskich lub licencji', 'name': 'copyrightsPurchaseCostsA'},
            {'title': '- koszty najmu kopii', 'name': 'copyRentalCostsA'},
            {'title': '- koszty nagród', 'name': 'awardsCostsA'},
            {'title': '- koszty szkoleń', 'name': 'trainingCostsA'},
            {
                'title': '- koszty cateringu',
                'name': 'cateringCostsA',
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
        'title': '4. Koszty wsparcia wydarzeń filmowych realizowanych przez Stowarzyszenie Kin Studyjnych',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'localCinemasAssociationSupport'},
            {'title': '- wynagrodzenia twórców, artystów, prelegentów', 'name': 'artistsRemunerationCostsB'},
            {'title': '- wynagrodzenia osób prowadzących', 'name': 'hostsRemunerationCostsB'},
            {'title': '- koszty tłumaczeń', 'name': 'translationCostB'},
            {'title': '- koszty promocji i reklamy', 'name': 'commercialsB'},
            {'title': '- koszty usług graficznych, fotograficznych i projektowych', 'name': 'graphicServiceB'},
            {'title': '- koszty usług poligraficznych/DTP', 'name': 'printingCostsB'},
            {'title': '- koszty najmu sprzętu', 'name': 'equipmentRentalCostsB'},
            {'title': '- koszty usług transportowych', 'name': 'transportationServiceB'},
            {'title': '- koszty podróży', 'name': 'tripCostsB'},
            {'title': '- koszty noclegów', 'name': 'accommodationCostsB'},
            {'title': '- koszty dokumentacji/rejestracji', 'name': 'documentationCostsB'},
            {'title': '- koszty ubezpieczeń', 'name': 'insuranceCostsB'},
            {'title': '- koszty pozyskania praw autorskich lub licencji', 'name': 'copyrightsPurchaseCostsB'},
            {'title': '- koszty najmu kopii', 'name': 'copyRentalCostsB'},
            {'title': '- koszty nagród', 'name': 'awardsCostsB'},
            {'title': '- koszty szkoleń', 'name': 'trainingCostsB'},
            {
                'title': '- koszty cateringu',
                'name': 'cateringCostsB',
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
        'title': '5. Koszty działań na rzecz integracji i reprezentacji SKS',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'networkIntegrationCosts'},
            {'title': '- konferencje kin studyjnych', 'name': 'networkConferences'},
            {'title': '- szkolenia', 'name': 'trainingCostsNetwork'},
            {'title': '- obsługa i reprezentacja prawna', 'name': 'networkLegalCosts'}
        ]
    },
    {
        'title': '6. Działalność Rady Kin Studyjnych',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'networkCommitteeCosts'}
        ]
    },
    {
        'title': '7. Koszty organizacji i obsługi SKS',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'networkOrganisationCosts'},
            {
                'title': '- koszty osobowe',
                'name': 'networkPersonalCosts',
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
            {'title': '- koszty obsługi finansowej', 'name': 'networkFinancialCosts'},
            {'title': '- koszty najmu biura', 'name': 'networkOfficeRentalCosts'},
            {'title': '- koszty podróży służbowych', 'name': 'networkTripCosts'},
            {'title': '- koszty noclegów', 'name': 'networkAccommodationCosts'},
            {'title': '- koszty promocji SKS', 'name': 'networkPromotionCosts'}
        ]
    },
    {
        'title': '8. Koszty obsługi projektów online',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'onlineManagementCosts'}
        ]
    }
]

estimate_sections_pt3 = [
    {
        'title': '1. Koszty przygotowania i zarządzania przedsięwzięciem',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costManagement'},
            {'title': '- twórców, artystów', 'name': 'creatorsArtists'},
            {'title': '- prelegentów', 'name': 'speakers'},
            {'title': '- osób prowadzących (np. spotkania z artystami)', 'name': 'eventHosts'},
            {'title': '- koordynatorów (pokrywane wyłącznie ze środków Wnioskodawcy)', 'name': 'coordinators'}
        ]
    },
    {
        'title': '2. Koszty promocji i reklamy',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'commercials'}
        ]
    },
    {
        'title': '3. Koszty związane z miejscem realizacji przedsięwzięcia',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'locationCosts'}
        ]
    },
    {
        'title': '4. Koszty obsługi przedsięwzięcia',
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
                                    "field_name": "pisfSupportAmountPr3",
                                    "ratio": 0.3
                                },
                                "validationMsg": "Kwota dofinansowania dla kosztów osobowych nie może przekroczyć 30% kwoty wnioskowanej."
                            }
                        ]
                    }
                }
            },
            {'title': '- najem sprzętu', 'name': 'equipmentRentalCosts'}
        ]
    },
    {
        'title': '5. Koszty dotyczące podróży',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'tripCosts'},
            {'title': '- organizatorów przedsięwzięcia', 'name': 'hostsTripCosts'},
            {'title': '- twórców, artystów, prelegentów', 'name': 'participantsTripCosts'},
            {'title': '- zaproszonych gości', 'name': 'guestsTripCosts'}
        ]
    },
    {
        'title': '6. Koszty dotyczące noclegów',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'accommodationCosts'},
            {'title': '- organizatorów przedsięwzięcia', 'name': 'hostsAccommodationCosts'},
            {'title': '- twórców, artystów, prelegentów', 'name': 'participantsAccommodationCosts'},
            {'title': '- zaproszonych gości', 'name': 'guestsAccommodationCosts'}
        ]
    },
    {
        'title': '7. Koszty składki Polskiej Federacji Dyskusyjnych Klubów Filmowych',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'polishDkfFederationFee'}
        ]
    },
    {
        'title': '8. Koszty nabycia praw autorskich lub licencji',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'copyrightCost'}
        ]
    },
    {
        'title': '9. Koszty najmu kopii filmowych',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'copyRentalCost'}
        ]
    },
    {
        'title': '10. Koszty obsługi projektów online',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'onlineManagementCost'}
        ]
    },
    {
        'title': '11. Koszty związane z dostosowaniem działań i formy przekazu do osób ze szczególnymi potrzebami, w tym osób z niepełnosprawnościami',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'accessibilityCost'}
        ]
    }
]

estimate_sections_pt4 = [
    {
        'title': '1. Koszty przygotowania i zarządzania przedsięwzięciem',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costManagement'},
            {'title': '- twórców, artystów', 'name': 'creatorsArtists'},
            {'title': '- prelegentów, wykładowców', 'name': 'lecturers'},
            {'title': '- komisarza wystawy', 'name': 'curator'},
            {
                'title': '- koordynatorów przedsięwzięcia',
                'name': 'organizers',
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
            {'title': '- osób prowadzących (np. imprezy towarzyszące, dyskusje panelowe, konferencje, spotkania z artystami, wystawy)', 'name': 'eventHosts'}
        ]
    },
    {
        'title': '2. Koszty tłumaczeń',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'translationCost'}
        ]
    },
    {
        'title': '3. Koszty promocji i reklamy',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'commercials'},
            {'title': '- usługi PR', 'name': 'prServiceCosts'},
            {'title': '- outdoor, reklamy prasowa, radiowa, telewizyjna, internetowa, standy, rollupy, banery', 'name': 'mediaCommercials'}
        ]
    },
    {
        'title': '4. Koszty przygotowania materiałów, redakcji i korekty',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'proofreadingCost'}
        ]
    },
    {
        'title': '5. Koszty usług graficznych, fotograficznych i projektowych',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'graphicService'}
        ]
    },
    {
        'title': '6. Koszty usług poligraficznych/DTP',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'printingCosts'},
            {'title': '- projekt', 'name': 'printingCostsProject'},
            {'title': '- skład', 'name': 'printingCostsTypesetting'},
            {'title': '- druk', 'name': 'printingCostsPrint'}
        ]
    },
    {
        'title': '7. Koszty przygotowania materiałów multimedialnych',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'multimediaMaterialsCost'}
        ]
    },
    {
        'title': '8. Koszty konsultacji eksperckich, paneli eksperckich',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'expertConsultation'}
        ]
    },
    {
        'title': '9. Koszt pozyskania praw autorskich',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'copyrightsCosts'}
        ]
    },
    {
        'title': '10. Koszt obsługi finansowej',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'financialService'}
        ]
    },
    {
        'title': '11. Koszty obsługi prawnej',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'lawAdvice'}
        ]
    },
    {
        'title': '12. Koszty związane z miejscem realizacji przedsięwzięcia',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'locationCosts'},
            {'title': '- koszty wynajmu miejsca oraz wyposażenia i obsługi sprzętu', 'name': 'rentalCosts'},
            {'title': '- koszty aranżacji przestrzeni, w tym zabezpieczenia BHP', 'name': 'spaceArrangementCosts'}
        ]
    },
    {
        'title': '13. Koszty obsługi przedsięwzięcia',
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
        'title': '14. Koszty usług transportowych',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'transportationService'}
        ]
    },
    {
        'title': '15. Koszty dotyczące podróży',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'tripCosts'},
            {'title': '- organizatorów przedsięwzięcia', 'name': 'hostsTripCosts'},
            {'title': '- twórców, artystów, prelegentów', 'name': 'participantsTripCosts'},
            {'title': '- zaproszonych gości', 'name': 'guestsTripCosts'}
        ]
    },
    {
        'title': '16. Koszty dotyczące noclegów',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'accommodationCosts'},
            {'title': '- organizatorów przedsięwzięcia', 'name': 'hostsAccommodationCosts'},
            {'title': '- twórców, artystów, prelegentów', 'name': 'participantsAccommodationCosts'},
            {'title': '- zaproszonych gości', 'name': 'guestsAccommodationCosts'}
        ]
    },
    {
        'title': '17. Koszty niezbędnych ubezpieczeń',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'insuranceAndSecurityCosts'},
            {'title': '- ubezpieczenie', 'name': 'insuranceCosts'},
            {'title': '- ochrona', 'name': 'securityCosts'}
        ]
    },
    {
        'title': '18. Koszty dokumentacji/rejestracji realizacji przedsięwzięcia',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'documentationCosts'}
        ]
    },
    {
        'title': '19. Koszty nagród dla uczestników',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'awardsCosts'}
        ]
    },
    {
        'title': '20. Koszty cateringu',
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
        'title': '21. Koszty przeprowadzenia ewaluacji przedsięwzięcia',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'evaluationCosts'}
        ]
    },
    {
        'title': '22. Koszty obsługi projektów online',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'onlineManagementCosts'}
        ]
    },
    {
        'title': '23. Koszty związane z dostosowaniem działań i formy przekazu do osób ze szczególnymi potrzebami',
        'costs': [
            {'isSum': True, 'title': '', 'name': 'accessibilityCosts'}
        ]
    }
]
