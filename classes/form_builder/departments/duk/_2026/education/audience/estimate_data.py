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
                "title": "Koszty osób współpracujących (np. ekspertów, prelegentów, artystów)",
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
                "title": "Koszty opracowania materiałów dydaktycznych",
                "name": "educationalMaterials"
            },
            {
                "title": "Koszty najmu i przygotowania kopii filmowych oraz napisów do filmów",
                "name": "copyingAndSubtitling"
            },
            {
                "title": "Koszty obsługi PR, promocji i reklamy",
                "name": "commercials"
            },
            {
                "title": "Koszty usług graficznych i poligraficznych",
                "name": "graphicService"
            },
            {
                "title": "Koszty nagrań i usług fotograficznych",
                "name": "recordingService"
            },
            {
                "title": "Koszty tłumaczeń",
                "name": "translation"
            }
        ]
    },
    {
        "title": "Koszty lokalowe i techniczne",
        "costs": [
            {
                "title": "Koszty wynajmu powierzchni",
                "name": "rentalSurface"
            },
            {
                "title": "Koszty aranżacji powierzchni",
                "name": "arrangementSurface"
            },
            {
                "title": "Koszty wynajmu sprzętu",
                "name": "equipmentRental"
            },
            {
                "title": "Koszty obsługi technicznej",
                "name": "technicalService"
            },
            {
                "title": "Koszty zabezpieczenia BHP",
                "name": "safetyBhp"
            },
            {
                "title": "Koszty obsługi projektów edukacyjnych online",
                "name": "onlineEducationProjects"
            }
        ]
    },
    {
        "title": "Koszty logistyczne",
        "costs": [
            {
                "title": "Koszty usług transportowych",
                "name": "transportServices"
            },
            {
                "title": "Koszty dotyczące podróży",
                "name": "travel",
                "helpText": "Koszty udokumentowane wyłącznie fakturami lub biletami (jeśli brak faktury), W przypadku podróży lotniczych – tylko bilety w klasie ekonomicznej, W przypadku paliwa – wyłącznie koszty paliwa do samochodów wykorzystywanych do realizacji przedsięwzięcia (środek trwały, leasing, najem), Z dotacji PISF nie są pokrywane koszty podróży zagranicznych."
            },
            {
                "title": "Koszty dotyczące noclegów",
                "name": "accommodation",
                "helpText": "Koszty udokumentowane wyłącznie fakturami (z wyłączeniem diet, ryczałtów i innych kosztów niewykazanych fakturą/rachunkiem), Z dotacji PISF nie są pokrywane koszty podróży zagranicznych."
            }
        ]
    },
    {
        "title": "Koszty prawne i administracyjne",
        "costs": [
            {
                "title": "Koszty obsługi finansowej",
                "name": "financialService",
                "helpText": "Koszty związane z otwarciem i prowadzeniem rachunku bankowego wyłącznie dla operacji finansowych związanych z realizacją przedsięwzięcia, Koszty prowadzenia księgowości związanej z realizacją przedsięwzięcia, Koszty te powinny być udokumentowane rachunkiem lub fakturą z opisem potwierdzającym związek z przedsięwzięciem."
            },
            {
                "title": "Koszty licencyjne",
                "name": "license"
            },
            {
                "title": "Koszty ubezpieczeń",
                "name": "insurance"
            },
            {
                "title": "Koszty ewaluacji przedsięwzięcia",
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
