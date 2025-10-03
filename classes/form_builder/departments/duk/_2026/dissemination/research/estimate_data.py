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
                "title": "Koszty osób współpracujących",
                "name": "cooperatingPeople",
                "helpText": "(Zespół badawczy, eksperci, współpracownicy merytoryczni) Koszty osób współpracujących – wyłącznie koszty udokumentowane umowami wraz z odpowiednimi dokumentami księgowymi (faktura lub rachunek)."
            },
            {
                "title": "Ekspertyzy, konsultacje specjalistyczne",
                "name": "expertConsultation"
            }
        ]
    },
    {
        "title": "Koszty realizacji badań i opracowań analitycznych",
        "costs": [
            {
                "title": "Konstrukcja narzędzi badawczych",
                "name": "researchTools"
            },
            {
                "title": "Badania terenowe (wywiady, ankiety, grupy fokusowe)",
                "name": "fieldResearch"
            },
            {
                "title": "Analizy jakościowe (dane zastane, analiza wywiadów, case study)",
                "name": "qualitativeAnalysis"
            },
            {
                "title": "Analizy ilościowe (analiza statystyczna)",
                "name": "quantitativeAnalysis"
            },
            {
                "title": "Raport końcowy z badania",
                "name": "finalReport"
            }
        ]
    },
    {
        "title": "Koszty materiałowe i usługowe",
        "costs": [
            {
                "title": "Redakcja i korekta tekstów",
                "name": "editingProofreading"
            },
            {
                "title": "Tłumaczenia",
                "name": "translation"
            },
            {
                "title": "Usługi graficzne i poligraficzne",
                "name": "graphicServices"
            }
        ]
    },
    {
        "title": "Koszty logistyczne",
        "costs": [
            {
                "title": "Koszty dotyczące podróży",
                "name": "travel",
                "helpText": "Koszty udokumentowane wyłącznie fakturami lub biletami (jeśli brak faktury). W przypadku podróży lotniczych – tylko bilety w klasie ekonomicznej. w przypadku paliwa – wyłącznie koszty paliwa do samochodów wykorzystywanych do realizacji przedsięwzięcia (środek trwały, leasing, najem) Z dotacji PISF nie są pokrywane koszty podróży zagranicznych."
            },
            {
                "title": "Koszty dotyczące noclegów",
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
                "helpText": "Koszty związane z otwarciem i prowadzeniem rachunku bankowego wyłącznie dla operacji finansowych związanych z realizacją przedsięwzięcia. Koszty prowadzenia księgowości związanej z realizacją przedsięwzięcia, Koszty powinny być udokumentowane rachunkiem lub fakturą z opisem potwierdzającym związek z przedsięwzięciem."
            },
            {
                "title": "Koszty licencyjne",
                "name": "licenseCosts"
            },
            {
                "title": "Koszty ewaluacji przedsięwzięcia",
                "name": "evaluation"
            }
        ]
    }
]
