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
                "title": "Koszty osób współpracujących (np. nadzór merytoryczny, opieka dydaktyczna)",
                "name": "cooperatingPeople",
                "helpText": "Wyłącznie koszty udokumentowane umowami wraz z odpowiednimi dokumentami księgowymi (faktura lub rachunek)."
            },
            {
                "title": "Koszty konsultacji eksperckich",
                "name": "expertConsultation"
            }
        ]
    },
    {
        "title": "Koszty materiałowe i usługowe",
        "costs": [
            {
                "title": "Wynajem kostiumów, rekwizytów",
                "name": "costumesRental"
            },
            {
                "title": "Materiały biurowe",
                "name": "stationery"
            },
            {
                "title": "Obsługa PR, promocja i reklama",
                "name": "commercials"
            },
            {
                "title": "Usługi graficzne i poligraficzne",
                "name": "graphicService"
            },
            {
                "title": "Nagrania i usługi fotograficzne",
                "name": "recordingService"
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
                "title": "Wynajem powierzchni",
                "name": "rentalSurface"
            },
            {
                "title": "Aranżacja powierzchni",
                "name": "arrangementSurface"
            },
            {
                "title": "Wynajem lub zakup sprzętu",
                "name": "equipmentRental",
                "helpText": "Zakup sprzętu wyłącznie na potrzeby realizacji danego przedsięwzięcia."
            },
            {
                "title": "Obsługa techniczna",
                "name": "technicalService"
            },
            {
                "title": "Zabezpieczenie BHP",
                "name": "safetyBhp"
            },
            {
                "title": "Obsługa projektów edukacyjnych online",
                "name": "onlineEducationProjects"
            }
        ]
    },
    {
        "title": "Koszty logistyczne",
        "costs": [
            {
                "title": "Usługi transportowe",
                "name": "transportServices"
            },
            {
                "title": "Podróże",
                "name": "travel",
                "helpText": "Koszty udokumentowane wyłącznie fakturami lub biletami (jeśli brak faktury), W przypadku podróży lotniczych – tylko bilety w klasie ekonomicznej, W przypadku paliwa – wyłącznie koszty paliwa do samochodów wykorzystywanych do realizacji przedsięwzięcia (środek trwały, leasing, najem), Z dotacji PISF nie są pokrywane koszty podróży zagranicznych."
            },
            {
                "title": "Noclegi",
                "name": "accommodation",
                "helpText": "Koszty udokumentowane wyłącznie fakturami (z wyłączeniem diet, ryczałtów i innych kosztów niewykazanych fakturą/rachunkiem). Z dotacji PISF nie są pokrywane koszty podróży zagranicznych."
            },
            {
                "title": "Catering lub poczęstunek",
                "name": "catering",
                "helpText": "Koszty nie mogą przekroczyć 35,00% ogólnej kwoty wnioskowanej. W przypadku uzyskania dofinansowania – nie mogą przekroczyć 35,00% przyznanej dotacji.",
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
            }
        ]
    },
    {
        "title": "Koszty prawne i administracyjne",
        "costs": [
            {
                "title": "Obsługa finansowa",
                "name": "financialService",
                "helpText": "Koszty związane z otwarciem i prowadzeniem rachunku bankowego wyłącznie dla operacji finansowych związanych z realizacją przedsięwzięcia, Koszty prowadzenia księgowości związanej z realizacją przedsięwzięcia, Koszty muszą być udokumentowane rachunkiem lub fakturą z opisem potwierdzającym związek z przedsięwzięciem."
            },
            {
                "title": "Koszty licencyjne i najmu kopii",
                "name": "licenseRental"
            },
            {
                "title": "Ubezpieczenia",
                "name": "insurance"
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
                "title": "Dostępność cyfrowa (dostępne strony internetowe)",
                "name": "digitalAccessibility"
            },
            {
                "title": "Dostępność informacyjno–komunikacyjna (audiodeskrypcja, napisy SDH, tłumaczenia PJM)",
                "name": "infoAccessibility"
            }
        ]
    }
]
