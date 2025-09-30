from classes.form_rules import Validator

validators = Validator()

estimate_sections = [
    {
        'title': 'Koszty osobowe i merytoryczne',
        'costs': [
            {
                'title': 'Koszty zarządzania przedsięwzięciem',
                'name': 'projectManagement',
                'helpText': 'Koszty zarządzania przedsięwzięciem nie mogą przekroczyć 15,00% ogólnej kwoty wnioskowanej. W przypadku uzyskania dofinansowania koszty, o których mowa powyżej nie mogą przekroczyć 15,00% przyznanej dotacji.',
                'overrides': {
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
                'title': 'Koszty osobowe',
                'name': 'personal',
                'helpText': 'Koszty osobowe przedsięwzięcia nie mogą przekroczyć 35,00% ogólnej kwoty wnioskowanej. W przypadku uzyskania dofinansowania koszty, o których mowa powyżej nie mogą przekroczyć 35,00% przyznanej dotacji.',
                'overrides': {
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
                'title': 'Koszty osób współpracujących (np. członków jury, twórców, moderatorów)',
                'helpText': 'Wyłącznie koszty udokumentowane umowami wraz z odpowiednimi dokumentami księgowymi (tj. faktura lub rachunek).',
                'name': 'cooperatingPeople',
            },
            {
                'title': 'Koszty konsultacji eksperckich',
                'name': 'expertConsultation',
            },
            {
                'title': 'Koszty nagród dla laureatów',
                'name': 'awards',
            }
        ]
    },
    {
        'title': 'Koszty materiałowe i usługowe',
        'costs': [
            {
                'title': 'Koszty przygotowania kopii filmowych i napisów do filmów',
                'name': 'copyingAndSubtitling',
            },
            {
                'title': 'Koszty usług PR, promocji i reklam',
                'name': 'commercials',
            },
            {
                'title': 'Koszty usług graficznych i poligraficznych',
                'name': 'graphicService',
            },
            {
                'title': 'Koszty nagrań i usług fotograficznych',
                'name': 'recordingService',
            },
            {
                'title': 'Koszty tłumaczeń',
                'name': 'translation',
            },
            {
                'title': 'Koszty materiałów biurowych',
                'name': 'stationery',
            }
        ]
    },
    {
        'title': 'Koszty lokalowe i techniczne',
        'costs': [
            {
                "title": "Koszty wynajmu powierzchni",
                "name": "rentalSurface",
            },
            {
                "title": "Koszty aranżacji powierzchni",
                "name": "arrangementSurface",
            },
            {
                "title": "Koszty wynajmu sprzętu",
                "name": "equipmentRental",
            },
            {
                "title": "Koszty obsługi technicznej",
                "name": "technicalService",
            },
            {
                "title": "Koszty zabezpieczenia BHP",
                "name": "safetyBhp",
            },
            {
                "title": "Koszty obsługi festiwalu online",
                "name": "onlineFestival",
            },
        ]
    },
    {
        "title": "Koszty logistyczne",
        "costs": [
            {
                "title": "Koszty usług transportowych",
                "name": "transportServices",
            },
            {
                "title": "Koszty dotyczące podróży",
                "helpText": "Koszty udokumentowane wyłącznie fakturami lub biletami (jeśli niemożliwe jest otrzymanie faktury). W przypadku podróży lotniczych pokrywa się z dotacji tylko koszt biletów w klasie ekonomicznej. W przypadku zakupu paliwa wyłącznie koszty paliwa do samochodów wykorzystywanych do realizacji przedsięwzięcia zgodnie z obowiązującymi przepisami (tj. jeżeli samochód stanowi środek trwały Wnioskodawcy lub jest przedmiotem leasingu bądź najmu na rzecz Wnioskodawcy). Z dotacji PISF nie są pokrywane koszty podróży zagranicznych.",
                "name": "travel",
            },
            {
                "title": "Koszty dotyczące noclegów",
                "helpText": "Koszty udokumentowane wyłącznie fakturami (z wyłączeniem diet, ryczałtów i innych kosztów udokumentowanych w inny sposób, niż rachunkiem lub fakturą). Z dotacji PISF nie są pokrywane koszty podróży zagranicznych.",
                "name": "accommodation",
            },
            {
                "title": "Koszty dotyczące cateringu lub poczęstunku",
                "helpText": "Koszty cateringu lub poczęstunku nie mogą przekroczyć 15,00% ogólnej kwoty wnioskowanej. W przypadku uzyskania dofinansowania koszty, o których mowa powyżej nie mogą przekroczyć 15,00% przyznanej dotacji.",
                "name": "catering",
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
        ]
    },
    {
        "title": "Koszty prawne i administracyjne",
        "costs": [
            {
                "title": "Koszty obsługi finansowej",
                "helpText": "Koszty związane z otwarciem i prowadzeniem rachunku bankowego wyłącznie dla operacji finansowych związanych z realizacją przedsięwzięcia oraz koszty prowadzenia księgowości związanej z realizacją danego przedsięwzięcia. Koszty te powinny zostać udokumentowane rachunkiem lub fakturą z opisem potwierdzającym, że dotyczyły realizacji danego przedsięwzięcia.",
                "name": "financialService",
            },
            {
                "title": "Koszty licencyjne i najmu kopii",
                "name": "licenseRental",
            },
            {
                "title": "Koszty ubezpieczeń",
                "name": "insurance",
            },
            {
                "title": "Koszty ewaluacji przedsięwzięcia",
                "name": "evaluation",
            },
        ]
    },
    {
        "title": "Koszty związane z dostępnością",
        "costs": [
            {
                "title": "Koszty związane z dostępnością cyfrową (dostępne strony internetowe)",
                "name": "digitalAccessibility",
            },
            {
                "title": "Koszty związane z dostępnością informacyjno–komunikacyjną (audiodeskrypcja, napisy SDH, tłumaczenie PJM)",
                "name": "infoAccessibility",
            },
        ]
    }
]
