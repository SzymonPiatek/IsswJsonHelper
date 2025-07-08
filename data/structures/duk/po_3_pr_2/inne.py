structure = {
    'part': 'layout',
    'components': [
        {
            'part': 'position_layout',
            'title': "1. Koszty przygotowania i zarządzania przedsięwzięciem (konieczne jest wyszczególnienie funkcji oraz podanie honorarium lub wynagrodzenia). <br /><normal><small>Wyłącznie koszty finansowane w oparciu o umowy wraz z fakturami lub rachunkami i umowy zlecenia lub o dzieło wraz z rachunkami</small></normal>",
            'components': [
                {
                    'isSum': True,
                    'part': 'position_total',
                    'baseName': 'costManagement',
                    'title': "1. Koszty przygotowania i zarządzania przedsięwzięciem - RAZEM",
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'costManagementSumAmountPr4',
                        'requestedPlanned': 'costManagementRequestedAmountPr4'
                    }
                },
                {
                    'part': 'position_single',
                    'baseName': 'artists',
                    'title': 'Koszty twórców i artystów',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'artistsSumAmountPr4',
                        'requestedPlanned': 'artistsRequestedAmountPr4'
                    }
                },
                {
                    'part': 'position_single',
                    'baseName': 'speakers',
                    'title': 'Koszty prelegentów, wykładowców',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'speakersSumAmountPr4',
                        'requestedPlanned': 'speakersRequestedAmountPr4'
                    }
                },
                {
                    'part': 'position_single',
                    'baseName': 'curator',
                    'title': 'Koszty komisarza wystawy',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'curatorSumAmountPr4',
                        'requestedPlanned': 'curatorRequestedAmountPr4'
                    }
                },
                {
                    'part': 'position_single',
                    'baseName': 'organizers',
                    'title': 'Koszty koordynatorów',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'organizersSumAmountPr4',
                        'requestedPlanned': 'organizersRequestedAmountPr4'
                    }
                },
                {
                    'part': 'position_single',
                    'baseName': 'eventHosts',
                    'title': 'Koszty osób prowadzących',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'eventHostsSumAmountPr4',
                        'requestedPlanned': 'eventHostsRequestedAmountPr4'
                    }
                }
            ]
        },
        {
            'part': 'position_layout',
            'title': '2. Koszty tłumaczeń',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_single',
                    'baseName': 'translation',
                    'title': 'Koszty tłumaczeń',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'translationCostSumAmountPr4',
                        'requestedPlanned': 'translationRequestedAmountPr4'
                    }
                }
            ]
        },
        {
            'part': 'position_layout',
            'title': '3. Koszty promocji i reklamy',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_total',
                    'baseName': 'commercials',
                    'title': "3. Koszty promocji i reklamy - RAZEM",
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'commercialsSumAmountPr4',
                        'requestedPlanned': 'commercialsRequestedAmountPr4'
                    }
                },
                {
                    'part': 'position_single',
                    'baseName': 'pr',
                    'title': 'Koszty usług PR',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'prSumAmountPr4',
                        'requestedPlanned': 'prRequestedAmountPr4'
                    }
                },
                {
                    'part': 'position_single',
                    'baseName': 'outdoorCommercials',
                    'title': 'Reklama outdoor, prasowa, radiowa, telewizyjna, internetowa, standy, rollupy, banery',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'outdoorCommercialsSumAmountPr4',
                        'requestedPlanned': 'outdoorCommercialsRequestedAmountPr4'
                    }
                },
            ]
        },
        {
            'part': 'position_layout',
            'title': '4. Koszty przygotowania materiałów, redakcji i korekty',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_single',
                    'baseName': 'proofreading',
                    'title': '4. Koszty przygotowania materiałów, redakcji i korekty',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'proofreadingCostSumAmountPr4',
                        'requestedPlanned': 'proofreadingCostRequestedAmountPr4'
                    }
                },
            ]
        },
        {
            'part': 'position_layout',
            'title': '5. Koszty usług graficznych, fotograficznych i projektowych',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_single',
                    'baseName': 'graphicService',
                    'title': '5. Koszty usług graficznych, fotograficznych i projektowych',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'graphicServiceSumAmountPr4',
                        'requestedPlanned': 'graphicServiceRequestedAmountPr4'
                    }
                },
            ]
        },
        {
            'part': 'position_layout',
            'title': '6. Koszty usług poligraficznych/DTP (w tym m.in. publikacje towarzyszące przedsięwzięciu np. program, wydruki wielkoformatowe)',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_total',
                    'baseName': 'printing',
                    'title': "6. Koszty usług poligraficznych/DTP - RAZEM",
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'printingCostsSumAmountPr4',
                        'requestedPlanned': 'printingRequestedAmountPr4'
                    }
                },
                {
                    'part': 'position_single',
                    'baseName': 'printingProject',
                    'title': 'Koszty projektu',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'printingCostsProjectSumAmountPr4',
                        'requestedPlanned': 'printingCostsProjectSumAmountPr4'
                    }
                },
                {
                    'part': 'position_single',
                    'baseName': 'printingTypesetting',
                    'title': 'Koszty składu',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'printingCostsTypesettingSumAmountPr4',
                        'requestedPlanned': 'printingCostsTypesettingRequestedAmountPr4'
                    }
                },
                {
                    'part': 'position_single',
                    'baseName': 'printingPrint',
                    'title': 'Koszty druku',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'printingCostsPrintSumAmountPr4',
                        'requestedPlanned': 'printingCostsPrintRequestedAmountPr4'
                    }
                },
            ]
        },
        {
            'part': 'position_layout',
            'title': '7. Koszty przygotowania materiałów multimedialnych',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_single',
                    'baseName': 'multimediaMaterials',
                    'title': '7. Koszty przygotowania materiałów multimedialnych',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'multimediaMaterialsCostSumAmountPr4',
                        'requestedPlanned': 'multimediaMaterialsRequestedAmountPr4'
                    }
                },
            ]
        },
        {
            'part': 'position_layout',
            'title': '8. Koszty konsultacji eksperckich, paneli eksperckich',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_single',
                    'baseName': 'consultingExperts',
                    'title': '8. Koszty konsultacji eksperckich, paneli eksperckich',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'consultingExpertsCostSumAmountPr4',
                        'requestedPlanned': 'consultingExpertsCostRequestedAmountPr4'
                    }
                },
            ]
        },
        {
            'part': 'position_layout',
            'title': '9. Koszty pozyskania praw autorskich (licencje, kopie) - wyłącznie na potrzeby realizowanego przedsięwzięcia',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_single',
                    'baseName': 'financialService',
                    'title': '9. Koszty pozyskania praw autorskich lub licencji',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'financialServiceSumAmountPr4',
                        'requestedPlanned': 'financialServiceRequestedAmountPr4'
                    }
                },
            ]
        },
        {
            'part': 'position_layout',
            'title': '10. Koszty obsługi finansowej <br><normal><small>1) Opłaty związane z otwarciem i prowadzeniem rachunku bankowego, jeżeli umowa dotacji nakłada na beneficjenta obowiązek posiadania wyodrębnionego rachunku bankowego wyłącznie dla operacji finansowych związanych z realizacją przedsięwzięcia; <br />2) koszty prowadzenia księgowości związanej z realizacją danego przedsięwzięcia. Koszt ten powinien zostać udokumentowany rachunkiem lub fakturą z opisem, potwierdzającym, że koszty prowadzenia księgowości dotyczyły realizacji danego przedsięwzięcia.</small></normal>',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_single',
                    'baseName': 'copyright',
                    'title': '10. Koszty obsługi finansowej',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'financialServiceSumAmountPr4',
                        'requestedPlanned': 'financialServiceRequestedAmountPr4'
                    }
                },
            ]
        },
        {
            'part': 'position_layout',
            'title': '11. Koszty obsługi prawnej',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_single',
                    'baseName': 'lawAdvice',
                    'title': '11. Koszty obsługi prawnej',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'lawAdviceSumAmountPr4',
                        'requestedPlanned': 'lawAdviceRequestedAmountPr4'
                    }
                },
            ]
        },
        {
            'part': 'position_layout',
            'title': '12. Koszty związane z miejscem realizacji przedsięwzięcia <br /><normal><small>z wyłączeniem zakupu środków trwałych </small></normal>',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_total',
                    'baseName': 'location',
                    'title': '12. Koszty związane z miejscem realizacji przedsięwzięcia - RAZEM',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'locationCostsSumAmountPr4',
                        'requestedPlanned': 'locationCostsRequestedAmountPr4'
                    }
                },
                {
                    'part': 'position_single',
                    'baseName': 'rental',
                    'title': 'Koszty wynajmu miejsca oraz wypożyczenia i obsługi sprzętu',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'rentalCostsSumAmountPr4',
                        'requestedPlanned': 'rentalCostsRequestedAmountPr4'
                    }
                },
                {
                    'part': 'position_single',
                    'baseName': 'spaceArrangement',
                    'title': 'Koszty aranżacji przestrzeni',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'spaceArrangementCostsSumAmountPr4',
                        'requestedPlanned': 'spaceArrangementCostsRequestedAmountPr4'
                    }
                },
            ]
        },
        {
            'part': 'position_layout',
            'title': '13. Koszty obsługi przedsięwzięcia',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_total',
                    'baseName': 'eventHosting',
                    'title': '13. Koszty obsługi przedsięwzięcia - RAZEM',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'eventHostingCostsSumAmountPr4',
                        'requestedPlanned': 'eventHostingCostsRequestedAmountPr4'
                    }
                },
                {
                    'part': 'position_single',
                    'baseName': 'personal',
                    'title': 'Koszty osobowe',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'personalCostsSumAmountPr4',
                        'requestedPlanned': 'personalCostsRequestedAmountPr4'
                    }
                },
                {
                    'part': 'position_single',
                    'baseName': 'equipmentRental',
                    'title': 'Koszty najmu sprzętu',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'equipmentRentalCostsSumAmountPr4',
                        'requestedPlanned': 'equipmentRentalCostsRequestedAmountPr4'
                    }
                },
            ]
        },
        {
            'part': 'position_layout',
            'title': '14. Koszty usług transportowych',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_single',
                    'baseName': 'transportationService',
                    'title': '14. Koszty usług transportowych',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'transportationServiceSumAmountPr4',
                        'requestedPlanned': 'transportationServiceRequestedAmountPr4'
                    }
                },
            ]
        },
        {
            'part': 'position_layout',
            'title': '15. Koszty dotyczące podróży <br /><normal><small>Koszty przejazdu udokumentowane wyłącznie fakturami lub biletami; w przypadku podróży lotniczych pokrywa się z dotacji tylko koszt biletów w klasie ekonomicznej (z wyłączeniem diet, ryczałtów i innych kosztów udokumentowanych w inny sposób, niż rachunkiem lub fakturą). </small></normal>',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_total',
                    'baseName': 'trip',
                    'title': '15. Koszty dotyczące podróży - RAZEM',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'tripCostsSumAmountPr4',
                        'requestedPlanned': 'tripCostsRequestedAmountPr4'
                    }
                },
                {
                    'part': 'position_single',
                    'baseName': 'hostsTrip',
                    'title': 'Organizatorów przedsięwzięcia',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'hostsTripCostsSumAmountPr4',
                        'requestedPlanned': 'hostsTripCostsRequestedAmountPr4'
                    }
                },
                {
                    'part': 'position_single',
                    'baseName': 'participantsTrip',
                    'title': 'Twórców, artystów, prelegentów',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'participantsTripCostsSumAmountPr4',
                        'requestedPlanned': 'participantsTripCostsRequestedAmountPr4'
                    }
                },
                {
                    'part': 'position_single',
                    'baseName': 'questsTrip',
                    'title': 'Zaproszonych gości',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'guestsTripCostsSumAmountPr4',
                        'requestedPlanned': 'guestsTripCostsRequestedAmountPr4'
                    }
                },
            ]
        },
        {
            'part': 'position_layout',
            'title': '16. Koszty dotyczące noclegów <br /><normal><small>Koszty zakwaterowania udokumentowane wyłącznie fakturami (z wyłączeniem diet, ryczałtów i innych kosztów udokumentowanych w inny sposób, niż rachunkiem lub fakturą). </normal></small>',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_total',
                    'baseName': 'accommodation',
                    'title': '16. Koszty dotyczące noclegów - RAZEM',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'accommodationCostsSumAmountPr4',
                        'requestedPlanned': 'accommodationCostsRequestedAmountPr4'
                    }
                },
                {
                    'part': 'position_single',
                    'baseName': 'hostsAccommodation',
                    'title': 'Organizatorów przedsięwzięcia',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'hostsAccommodationCostsSumAmountPr4',
                        'requestedPlanned': 'hostsAccommodationCostsRequestedAmountPr4'
                    }
                },
                {
                    'part': 'position_single',
                    'baseName': 'participantsAccommodation',
                    'title': 'Twórców, artystów, prelegentów',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'participantsAccommodationCostsSumAmountPr4',
                        'requestedPlanned': 'participantsAccommodationCostsRequestedAmountPr4'
                    }
                },
                {
                    'part': 'position_single',
                    'baseName': 'questsAccommodation',
                    'title': 'Zaproszonych gości',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'guestsAccommodationCostsSumAmountPr4',
                        'requestedPlanned': 'guestsAccommodationCostsRequestedAmountPr4'
                    }
                },
            ]
        },
        {
            'part': 'position_layout',
            'title': '17. Koszty niezbędnych ubezpieczeń',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_total',
                    'baseName': 'insuranceAndSecurity',
                    'title': '17. Koszty niezbędnych ubezpieczeń - RAZEM',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'insuranceAndSecurityCostsSumAmountPr4',
                        'requestedPlanned': 'insuranceAndSecurityCostsRequestedAmountPr4'
                    }
                },
                {
                    'part': 'position_single',
                    'baseName': 'insurance',
                    'title': 'Koszty ubezpieczenia',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'insuranceCostsSumAmountPr4',
                        'requestedPlanned': 'insuranceCostsRequestedAmountPr4'
                    }
                },
                {
                    'part': 'position_single',
                    'baseName': 'security',
                    'title': 'Koszty ochrony',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'securityCostsSumAmountPr4',
                        'requestedPlanned': 'securityCostsRequestedAmountPr4'
                    }
                },
            ]
        },
        {
            'part': 'position_layout',
            'title': '18. Koszty dokumentacji/rejestracji realizacji przedsięwzięcia (filmowej, dźwiękowej, zdjęciowej)',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_single',
                    'baseName': 'documentation',
                    'title': '18. Koszty dokumentacji/rejestracji realizacji przedsięwzięcia',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'documentationCostsSumAmountPr4',
                        'requestedPlanned': 'documentationCostsRequestedAmountPr4'
                    }
                },
            ]
        },
        {
            'part': 'position_layout',
            'title': '19. Koszty nagród dla uczestników',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_single',
                    'baseName': 'awards',
                    'title': '19. Koszty nagród dla uczestników',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'awardsCostsSumAmountPr4',
                        'requestedPlanned': 'awardsCostsRequestedAmountPr4'
                    }
                },
            ]
        },
        {
            'part': 'position_layout',
            'title': '20. Koszty cateringu',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_single',
                    'baseName': 'catering',
                    'title': '20. Koszty cateringu',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'cateringCostsSumAmountPr4',
                        'requestedPlanned': 'cateringCostsRequestedAmountPr4'
                    }
                },
            ]
        },
        {
            'part': 'position_layout',
            'title': '21. Koszt przeprowadzenia ewaluacji przedsięwzięcia',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_single',
                    'baseName': 'evaluation',
                    'title': '21. Koszt przeprowadzenia ewaluacji przedsięwzięcia',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'evaluationCostsSumAmountPr4',
                        'requestedPlanned': 'evaluationCostsRequestedAmountPr4'
                    }
                },
            ]
        },
        {
            'part': 'position_layout',
            'title': '22. Koszty obsługi projektów online',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_single',
                    'baseName': 'onlineManagement',
                    'title': '22. Koszty obsługi projektów online',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'onlineManagementCostsSumAmountPr4',
                        'requestedPlanned': 'onlineManagementCostsRequestedAmountPr4'
                    }
                },
            ]
        },
        {
            'part': 'position_layout',
            'title': '23. Koszty związane z dostosowaniem działań i formy przekazu do osób ze szczególnymi potrzebami, w tym osób z niepełnosprawnościami',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_single',
                    'baseName': 'accessibility',
                    'title': '23. Koszty związane z dostosowaniem działań i formy przekazu do osób ze szczególnymi potrzebami, w tym osób z niepełnosprawnościami',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'accessibilityCostsSumAmountPr4',
                        'requestedPlanned': 'accessibilityCostsRequestedAmountPr4'
                    }
                },
            ]
        },
        {
            'part': 'total',
            'afterName': 'Pr4',
        }
    ]
}
