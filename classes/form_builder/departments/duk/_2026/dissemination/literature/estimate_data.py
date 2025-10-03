from classes.form_rules import Validator

validators = Validator()

estimate_sections = [
    {
        "title": "Koszty osobowe i merytoryczne",
        "costs": [
            {
                "title": "Zarządzanie przedsięwzięciem",
                "name": "projectManagement"
            },
            {
                "title": "Opracowanie i redakcja publikacji (autorzy tekstów, redaktorzy, korektorzy)",
                "name": "publicationEditing"
            },
            {
                "title": "Koszty osobowe",
                "name": "personal",
                "helpText": "Koszty osobowe przedsięwzięcia nie mogą przekroczyć 35,00% ogólnej kwoty wnioskowanej. W przypadku uzyskania dofinansowania koszty osobowe nie mogą przekroczyć 35,00% przyznanej dotacji.",
                "overrides": {
                    "RequestedAmount": {
                        "validators": [
                            validators.related_fraction_gte_validator(
                                field_name="pisfSupportAmount",
                                ratio=0.35,
                                message="Kwota dofinansowania dla tego kosztu nie może przekroczyć 35% kwoty wnioskowanej."
                            )
                        ]
                    }
                }
            },
            {
                "title": "Konsultacje eksperckie",
                "name": "expertConsultation"
            }
        ]
    },
    {
        "title": "Koszty przygotowania i publikacji",
        "costs": [
            {
                "title": "Usługi graficzne, fotograficzne i typograficzne",
                "name": "graphicPhotoTypography"
            },
            {
                "title": "Usługi wydawnicze i poligraficzne",
                "name": "publishingPrinting"
            },
            {
                "title": "Przygotowanie wersji cyfrowych (e-book, audiobook)",
                "name": "digitalVersions"
            },
            {
                "title": "Obsługa i utrzymanie serwisu internetowego",
                "name": "websiteMaintenance"
            },
            {
                "title": "Tłumaczenia",
                "name": "translation"
            },
            {
                "title": "Dystrybucja",
                "name": "distribution"
            }
        ]
    },
    {
        "title": "Koszty prawne i organizacyjne",
        "costs": [
            {
                "title": "Obsługa prawna i finansowa",
                "name": "legalFinancialService",
                "helpText": "W tym koszty związane z otwarciem i prowadzeniem rachunku bankowego wyłącznie dla operacji finansowych związanych z realizacją przedsięwzięcia. Koszty prowadzenia księgowości związanej z realizacją przedsięwzięcia. Wszystkie koszty muszą być udokumentowane rachunkiem lub fakturą z opisem potwierdzającym związek z przedsięwzięciem."
            },
            {
                "title": "Koszty nabycia praw",
                "name": "rightsAcquisition"
            },
            {
                "title": "Koszty przejazdów i noclegów osób współpracujących przy przedsięwzięciu",
                "name": "travelAccommodation",
                "helpText": "Koszty udokumentowane wyłącznie fakturami lub biletami (jeśli brak faktury). W przypadku podróży lotniczych – tylko bilety w klasie ekonomicznej, W przypadku paliwa – wyłącznie koszty paliwa do samochodów wykorzystywanych do realizacji przedsięwzięcia (środek trwały, leasing, najem), Z dotacji PISF nie są pokrywane koszty podróży zagranicznych."
            },
            {
                "title": "Ewaluacja przedsięwzięcia",
                "name": "evaluation"
            }
        ]
    },
    {
        "title": "Koszty związane z dostępnością",
        "costs": [
            {
                "title": "Dostępność cyfrowa",
                "name": "digitalAccessibility",
                "helpText": "Dostępne strony internetowe."
            }
        ]
    }
]
