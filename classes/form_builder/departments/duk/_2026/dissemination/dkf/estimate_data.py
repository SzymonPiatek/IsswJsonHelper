from classes.form_rules import Validator

validators = Validator()

estimate_sections = [
    {
        "title": "Koszty osobowe i merytoryczne",
        "costs": [
            {
                "title": "Koszty zarządzania przedsięwzięciem",
                "name": "projectManagement",
                "helpText": "Koszty zarządzania przedsięwzięciem nie mogą przekroczyć 15,00% ogólnej kwoty wnioskowanej. W przypadku uzyskania dofinansowania koszty zarządzania nie mogą przekroczyć 15,00% przyznanej dotacji.",
                "overrides": {
                    "RequestedAmount": {
                        "validators": [
                            validators.related_fraction_gte_validator(
                                field_name="pisfSupportAmount",
                                ratio=0.15,
                                message="Kwota dofinansowania dla tego kosztu nie może przekroczyć 15% kwoty wnioskowanej."
                            )
                        ]
                    }
                }
            },
            {
                "title": "Koszty osobowe",
                "name": "personal",
                "helpText": "Koszty osobowe nie mogą przekroczyć 35,00% ogólnej kwoty wnioskowanej. W przypadku uzyskania dofinansowania koszty osobowe nie mogą przekroczyć 35,00% przyznanej dotacji.",
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
                "title": "Koszty osób współpracujących (np. twórców, prelegentów, moderatorów)",
                "name": "cooperatingPeople",
                "helpText": "Wyłącznie koszty udokumentowane umowami wraz z odpowiednimi dokumentami księgowymi (faktura lub rachunek)."
            }
        ]
    },
    {
        "title": "Koszty materiałowe i usługowe",
        "costs": [
            {
                "title": "Promocja i reklama",
                "name": "promotion"
            },
            {
                "title": "Usługi graficzne i poligraficzne",
                "name": "graphicServices"
            },
            {
                "title": "Dokumentacja fotograficzna i filmowa",
                "name": "photoFilmDoc"
            },
            {
                "title": "Tłumaczenia",
                "name": "translation"
            }
        ]
    },
    {
        "title": "Koszty lokalowe i techniczne",
        "costs": [
            {
                "title": "Przygotowanie kopii filmowych i napisów do filmów",
                "name": "copyingAndSubtitling"
            },
            {
                "title": "Wynajem powierzchni",
                "name": "rentalSurface"
            },
            {
                "title": "Wynajem sprzętu",
                "name": "equipmentRental"
            },
            {
                "title": "Obsługa techniczna",
                "name": "technicalService"
            },
            {
                "title": "Obsługa projektów online",
                "name": "onlineProjects"
            }
        ]
    },
    {
        "title": "Koszty logistyczne",
        "costs": [
            {
                "title": "Koszty podróży",
                "name": "travel",
                "helpText": "Koszty udokumentowane wyłącznie fakturami lub biletami (jeśli brak faktury). W przypadku podróży lotniczych – tylko bilety w klasie ekonomicznej. W przypadku paliwa – wyłącznie koszty paliwa do samochodów wykorzystywanych do realizacji przedsięwzięcia (środek trwały, leasing, najem) Z dotacji PISF nie są pokrywane koszty podróży zagranicznych."
            },
            {
                "title": "Koszty noclegów",
                "name": "accommodation",
                "helpText": "Koszty udokumentowane wyłącznie fakturami (z wyłączeniem diet, ryczałtów i innych kosztów niewykazanych fakturą/rachunkiem). Z dotacji PISF nie są pokrywane koszty podróży zagranicznych."
            }
        ]
    },
    {
        "title": "Koszty prawne i administracyjne",
        "costs": [
            {
                "title": "Obsługa finansowa",
                "name": "financialService",
                "helpText": "Koszty związane z otwarciem i prowadzeniem rachunku bankowego wyłącznie dla operacji finansowych związanych z realizacją przedsięwzięcia. Koszty prowadzenia księgowości związanej z realizacją przedsięwzięcia. Koszty muszą być udokumentowane rachunkiem lub fakturą z opisem potwierdzającym związek z przedsięwzięciem."
            },
            {
                "title": "Koszty licencji lub nabycia praw do publicznego pokazu",
                "name": "publicPerformanceRights",
                "helpText": "Niezależnie od formuły fakturowania."
            },
            {
                "title": "Koszty składki Polskiej Federacji Dyskusyjnych Klubów Filmowych",
                "name": "pfdkfFee",
                "helpText": "Pokrywana wyłącznie ze środków własnych Wnioskodawcy lub z innych źródeł finansowania."
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
            },
            {
                "title": "Dostępność informacyjno–komunikacyjna",
                "name": "infoAccessibility",
                "helpText": "Wykonanie napisów SDH, tłumaczenia PJM."
            }
        ]
    }
]
