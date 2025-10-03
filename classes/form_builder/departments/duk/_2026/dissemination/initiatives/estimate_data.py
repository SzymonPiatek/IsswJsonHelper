from classes.form_rules import Validator

validators = Validator()

estimate_sections_pt124 = [
    {
        "title": "Koszty osobowe i merytoryczne",
        "costs": [
            {
                "title": "Koszty zarządzania przedsięwzięciem",
                "name": "projectManagement",
                "helpText": "Nie mogą przekroczyć 15% ogólnej kwoty wnioskowanej. W przypadku uzyskania dofinansowania – nie mogą przekroczyć 15% przyznanej dotacji.",
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
                "helpText": "Nie mogą przekroczyć 35% ogólnej kwoty wnioskowanej. W przypadku uzyskania dofinansowania – nie mogą przekroczyć 35% przyznanej dotacji.",
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
                "title": "Koszty osób współpracujących (np. członków jury, twórców, moderatorów)",
                "name": "cooperatingPeople",
                "helpText": "Wyłącznie koszty udokumentowane umowami wraz z odpowiednimi dokumentami księgowymi (faktura lub rachunek)."
            },
            {
                "title": "Koszty konsultacji eksperckich",
                "name": "expertConsultation"
            },
            {
                "title": "Koszty nagród dla laureatów",
                "name": "awards"
            }
        ]
    },
    {
        "title": "Koszty materiałowe i usługowe",
        "costs": [
            {
                "title": "Koszty przygotowania kopii filmowych i napisów do filmów",
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
            },
            {
                "title": "Koszty materiałów biurowych",
                "name": "stationery"
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
                "title": "Koszty obsługi projektów online",
                "name": "onlineProjects"
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
                "helpText": "Wyłącznie koszty udokumentowane fakturami lub biletami (jeśli faktura jest niemożliwa do uzyskania). W przypadku podróży lotniczych – pokrywany jest tylko koszt biletów w klasie ekonomicznej. W przypadku zakupu paliwa – wyłącznie paliwo do samochodów wykorzystywanych do realizacji przedsięwzięcia zgodnie z przepisami (samochód jako środek trwały, leasing, najem). Nie pokrywa się kosztów podróży zagranicznych."
            },
            {
                "title": "Koszty dotyczące noclegów",
                "name": "accommodation",
                "helpText": "Wyłącznie koszty udokumentowane fakturami. Wykluczone: diety, ryczałty, inne koszty nieudokumentowane rachunkiem lub fakturą. Nie pokrywa się kosztów podróży zagranicznych."
            },
            {
                "title": "Koszty dotyczące cateringu lub poczęstunku",
                "name": "catering",
                "helpText": "Nie mogą przekroczyć 15% ogólnej kwoty wnioskowanej. W przypadku uzyskania dofinansowania – nie mogą przekroczyć 15% przyznanej dotacji.",
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
            }
        ]
    },
    {
        "title": "Koszty prawne i administracyjne",
        "costs": [
            {
                "title": "Koszty obsługi finansowej",
                "name": "financialService",
                "helpText": "Związane z otwarciem i prowadzeniem rachunku bankowego wyłącznie dla operacji finansowych przedsięwzięcia. Koszty prowadzenia księgowości związanej z realizacją przedsięwzięcia. Powinny być udokumentowane rachunkiem lub fakturą z opisem potwierdzającym, że dotyczyły realizacji przedsięwzięcia."
            },
            {
                "title": "Koszty licencyjne i najmu kopii",
                "name": "licenseRental"
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
                "title": "Dostępność cyfrowa",
                "name": "digitalAccessibility",
                "helpText": "Dostępne strony internetowe."
            },
            {
                "title": "Dostępność informacyjno–komunikacyjna",
                "name": "infoAccessibility",
                "helpText": "Wykonanie audiodeskrypcji, napisów SDH, tłumaczenia PJM."
            }
        ]
    }
]

estimate_sections_pt3 = []
