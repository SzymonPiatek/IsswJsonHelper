estimate_sections = [
    {
        'title': '1. Koszty przygotowania przedsięwzięcia',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costPreparation'},
            {'title': '- twórców, artystów', 'name': 'creatorsArtists'},
            {'title': '- prelegentów, wykładowców', 'name': 'lecturers'},
            {'title': '- osób współpracujących przy realizacji przedsięwzięcia, w tym nadzór i opieka nad studentami', 'name': 'partners'},
            {'title': '- osób prowadzących (np. imprezy towarzyszące, dyskusje panelowe, konferencje, spotkania z artystami, wystawy)', 'name': 'eventHosts'}
        ]
    },
    {
        'title': '2. Koszty zarządzania przedsięwzięciem',
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
        'title': '3. Koszty obsługi administracyjnej',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costAdmin'},
            {'title': '- wynagrodzeń i honorariów', 'name': 'adminWages'},
            {'title': '- usług księgowych, prawnych, doradczych, informatycznych, obsługi kancelaryjnej i tłumaczeń', 'name': 'adminServices'}
        ]
    },
    {
        'title': '4. Koszty podróży służbowych',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costTravel'},
            {'title': '- bilety', 'name': 'tickets'},
            {'title': '- noclegi', 'name': 'accommodation'},
            {'title': '- diety, ubezpieczenia', 'name': 'perDiemInsurance'}
        ]
    },
    {
        'title': '5. Koszty eksploatacyjne i utrzymania obiektów',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costFacilities'},
            {'title': '- czynsze, media, ochrona, sprzątanie', 'name': 'rentUtilities'}
        ]
    },
    {
        'title': '6. Koszty amortyzacji sprzętu',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costDepreciation'},
            {'title': '- sprzęt komputerowy, oprogramowanie', 'name': 'itEquipment'},
            {'title': '- inne środki trwałe', 'name': 'otherAssets'}
        ]
    },
    {
        'title': '7. Koszty materiałów biurowych i eksploatacyjnych',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costSupplies'},
            {'title': '- papier, tonery, akcesoria', 'name': 'officeSupplies'}
        ]
    },
    {
        'title': '8. Koszty promocji i informacji',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costPromotion'},
            {'title': '- działania promocyjne, reklama, publikacje', 'name': 'promoActivities'},
            {'title': '- projekt graficzny, skład, druk', 'name': 'designPrint'}
        ]
    },
    {
        'title': '9. Koszty ubezpieczeń',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costInsurance'}
        ]
    },
    {
        'title': '10. Koszty rezerwowe',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costReserve'}
        ]
    },
    {
        'title': '11. Inne koszty kwalifikowane',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'otherEligibleCosts'}
        ]
    },
    {
        'title': '12. Koszty niekwalifikowane',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'ineligibleCosts'}
        ]
    },
    {
        'title': '13. Zakup lub amortyzacja środków trwałych',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costFixedAssets'},
            {'title': '- zakup', 'name': 'purchase'},
            {'title': '- amortyzacja', 'name': 'depreciation'}
        ]
    },
    {
        'title': '14. Zakup wartości niematerialnych i prawnych',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costIntangibleAssets'},
            {'title': '- licencje, prawa autorskie', 'name': 'licenses'}
        ]
    },
    {
        'title': '15. Zakup usług obcych',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costExternalServices'},
            {'title': '- usługi techniczne, transportowe, cateringowe', 'name': 'technicalServices'},
            {'title': '- inne usługi obce', 'name': 'otherExternalServices'}
        ]
    },
    {
        'title': '16. Koszty organizacji wydarzeń edukacyjnych',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costEducationalEvents'},
            {'title': '- wynajem sal, sprzętu', 'name': 'venueRental'},
            {'title': '- obsługa techniczna', 'name': 'technicalSupport'}
        ]
    },
    {
        'title': '17. Koszty publikacji materiałów edukacyjnych',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costEducationalMaterials'},
            {'title': '- redakcja, skład, druk', 'name': 'editingPrinting'}
        ]
    },
    {
        'title': '18. Koszty organizacji szkoleń i warsztatów',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costTrainings'},
            {'title': '- prowadzący, materiały, wynajem', 'name': 'trainingComponents'}
        ]
    },
    {
        'title': '19. Koszty opłat administracyjnych i urzędowych',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costAdministrativeFees'}
        ]
    },
    {
        'title': '20. Koszty rekrutacji uczestników',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costRecruitment'}
        ]
    },
    {
        'title': '21. Koszty ewaluacji i monitoringu',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costEvaluation'},
            {'title': '- badania, raporty', 'name': 'researchReports'}
        ]
    },
    {
        'title': '22. Koszty obsługi prawnej i księgowej',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'costLegalAccounting'}
        ]
    },
    {
        'title': '23. Pozostałe koszty związane z realizacją przedsięwzięcia',
        'costs': [
            {'isSum': True, 'title': 'Razem', 'name': 'otherProjectCosts'}
        ]
    }
]
