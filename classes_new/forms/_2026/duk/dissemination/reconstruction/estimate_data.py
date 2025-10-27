from classes_new.forms._2026.duk.estimate.dataclasses_definitions import EstimateSection, CostItem, CostOverride
from dataclasses import asdict


estimate_section_structure = [
    {
        'type': 'text',
        'mask': 'fund',
        'label': 'Koszt jednostkowy',
        'name': 'CostSingle',
        'unit': 'PLN'
    },
    {
        'type': 'number',
        'label': 'Liczba',
        'name': 'Amount',
        'options': []
    },
    {
        'type': 'select',
        'label': 'Jednostka',
        'name': 'Unit'
    },
    {
        'type': 'text',
        'mask': 'fund',
        'label': 'Koszt łączny',
        'name': 'CostTotal',
        'unit': 'PLN',
        'readOnly': True,
    },
    {
        'type': 'text',
        'mask': 'fund',
        'label': 'Wnioskowana dotacja PISF',
        'name': 'RequestedAmount',
        'unit': 'PLN'
    },
    {
        'type': 'text',
        'mask': 'fund',
        'label': 'Pozostałe środki',
        'name': 'OtherFundsAmount',
        'unit': 'PLN'
    }
]

sum_estimate_sections = [
    {
        'title': 'Podsumowanie',
        'costs': [
            {
                'name': 'total'
            }
        ]
    }
]

sum_estimate_section_structure = [
    {
        'type': 'text',
        'mask': 'fund',
        'isSum': True,
        'label': 'Koszt ogółem',
        'name': 'SumAmount',
        'unit': 'PLN'
    },
    {
        'type': 'text',
        'mask': 'fund',
        'isSum': True,
        'label': 'Wnioskowana dotacja PISF ogółem',
        'name': 'RequestedAmount',
        'unit': 'PLN'
    },
    {
        'type': 'text',
        'mask': 'fund',
        'isSum': True,
        'label': 'Pozostałe środki ogółem',
        'name': 'OtherFundsAmount',
        'unit': 'PLN'
    }
]

estimate_sections = [
    EstimateSection(
        title="ETAP",
        helpText="Wyłącznie koszty finansowane w oparciu o umowy wraz z fakturami/rachunkami oraz umowy zlecenie lub o dzieło wraz z rachunkami.",
        costs=[
            CostItem(
                title="Wypożyczenie materiałów wyjściowych",
                name="sourceMaterialsRental",
                overrides={
                    "Unit": {
                        "options": [
                            "akt"
                        ]
                    }
                }
            ),
            CostItem(
                title="Czyszczenie materiałów wyjściowych – obraz i dźwięk",
                name="sourceMaterialsCleaning",
                overrides={
                    "Unit": {
                        "options": [
                            "---",
                            "min",
                            "godz",
                            "akt"
                        ]
                    }
                }
            ),
            CostItem(
                title="Skanowanie materiałów wyjściowych – obraz i dźwięk",
                name="sourceMaterialsScanning",
                overrides={
                    "Unit": {
                        "options": [
                            "---",
                            "min",
                            "godz",
                            "akt"
                        ]
                    }
                }
            ),
            CostItem(
                title="Digitalizacja materiałów wyjściowych dźwięku",
                name="sourceSoundDigitization",
                overrides={
                    "Unit": {
                        "options": [
                            "---",
                            "min",
                            "godz",
                            "akt"
                        ]
                    }
                }
            ),
            CostItem(
                title="Wykonanie cyfrowych kopii archiwizacyjnych materiałów wyjściowych – obraz",
                name="archivalCopiesImage",
                overrides={
                    "Unit": {
                        "options": [
                            "---",
                            "min",
                            "godz",
                            "akt"
                        ]
                    }
                }
            ),
            CostItem(
                title="Wykonanie cyfrowych kopii archiwizacyjnych materiałów wyjściowych – dźwięk",
                name="archivalCopiesSound",
                overrides={
                    "Unit": {
                        "options": [
                            "---",
                            "min",
                            "ryczałt"
                        ]
                    }
                }
            ),
            CostItem(
                title="Nośniki kopii archiwizacyjnych materiałów wyjściowych",
                name="archivalCopiesMedia",
                overrides={
                    "Unit": {
                        "options": [
                            "szt"
                        ]
                    }
                }
            ),
            CostItem(
                title="Opis stanu technicznego materiałów wyjściowych – przegląd i ocena stanu zniszczeń",
                name="technicalConditionReport",
                overrides={
                    "Unit": {
                        "options": [
                            "---",
                            "godz",
                            "ryczałt",
                            "akt"
                        ]
                    }
                }
            ),
        ],
    ),
    EstimateSection(
        title="ETAP",
        costs=[
            CostItem(
                title="Konforming – porównanie zeskanowanego materiału filmowego z dostępnymi kopiami filmu i przygotowanie wersji referencyjnej do rekonstrukcji",
                name="conforming",
                overrides={
                    "Unit": {
                        "options": [
                            "akt"
                        ]
                    }
                }
            ),
            CostItem(
                title="Rekonstrukcja obrazu",
                name="imageRestoration",
                overrides={
                    "Unit": {
                        "options": [
                            "---",
                            "min",
                            "godz",
                            "akt"
                        ]
                    }
                }
            ),
            CostItem(
                title="Rekonstrukcja dźwięku",
                name="soundRestoration",
                overrides={
                    "Unit": {
                        "options": [
                            "---",
                            "min",
                            "godz",
                            "akt"
                        ]
                    }
                }
            ),
            CostItem(
                title="Synchronizacja dźwięku z obrazem",
                name="soundSynchronization",
                overrides={
                    "Unit": {
                        "options": [
                            "min"
                        ]
                    }
                }
            ),
            CostItem(
                title="Wykonanie cyfrowych kopii master – archiwizacyjnych i operacyjnych TIFF/LTO",
                name="masterCopies",
                overrides={
                    "Unit": {
                        "options": [
                            "---",
                            "min",
                            "ryczałt",
                            "akt"
                        ]
                    }
                }
            ),
            CostItem(
                title="Nośniki kopii master",
                name="masterCopiesMedia",
                overrides={
                    "Unit": {
                        "options": [
                            "szt"
                        ]
                    }
                }
            ),
            CostItem(
                title="Wykonanie dystrybucyjnych cyfrowych kopii wzorcowych filmu – archiwizacyjnych i operacyjnych",
                name="distributionCopies",
                overrides={
                    "Unit": {
                        "options": [
                            "---",
                            "min",
                            "ryczałt",
                            "szt"
                        ]
                    }
                }
            ),
            CostItem(
                title="Nośniki kopii dystrybucyjnych",
                name="distributionCopiesMedia",
                overrides={
                    "Unit": {
                        "options": [
                            "szt"
                        ]
                    }
                }
            ),
            CostItem(
                title="Wykonanie kopii wieczystej filmu na taśmie światłoczułej",
                name="permanentFilmCopy",
                overrides={
                    "Unit": {
                        "options": [
                            "min"
                        ]
                    }
                }
            ),
            CostItem(
                title="Nadzór lub opieka artystyczna",
                name="artisticSupervision",
                overrides={
                    "Unit": {
                        "options": [
                            "---",
                            "godz",
                            "ryczałt"
                        ]
                    }
                }
            ),
            CostItem(
                title="Kontrola techniczna jakości wykonania rekonstrukcji obrazu i dźwięku",
                name="technicalQualityControl",
                overrides={
                    "Unit": {
                        "options": [
                            "---",
                            "godz",
                            "ryczałt"
                        ]
                    }
                }
            ),
            CostItem(
                title="Koordynacja procesu digitalizacji i rekonstrukcji cyfrowej",
                name="processCoordination",
                overrides={
                    "Unit": {
                        "options": [
                            "---",
                            "godz",
                            "ryczałt"
                        ]
                    }
                }
            ),
            CostItem(
                title="Przygotowanie wersji językowej (maks. 3 wersje)",
                name="languageVersion",
                overrides={
                    "Unit": {
                        "options": [
                            "---",
                            "godz",
                            "ryczałt"
                        ]
                    }
                }
            ),
            CostItem(
                title="Opracowanie i wykonanie filmowych materiałów promocyjnych",
                name="promotionalMaterials",
                helpText="Pokrywane wyłącznie ze środków własnych lub innych źródeł finansowania.",
                overrides={
                    "RequestedAmount": CostOverride(
                        readOnly=True,
                    ),
                    "Unit": {
                        "options": [
                            "---",
                            "szt",
                            "ryczałt"
                        ]
                    }
                }
            ),
            CostItem(
                title="Organizacja kolaudacji",
                name="screeningOrganization",
                helpText="Pokrywane wyłącznie ze środków własnych lub innych źródeł finansowania.",
                overrides={
                    "RequestedAmount": CostOverride(
                        readOnly=True,
                    ),
                    "Unit": {
                        "options": [
                            "ryczałt"
                        ]
                    }
                }
            ),
            CostItem(
                title="Transport materiałów filmowych",
                name="materialsTransport",
                helpText="Pokrywane wyłącznie ze środków własnych lub innych źródeł finansowania.",
                overrides={
                    "RequestedAmount": CostOverride(
                        readOnly=True,
                    ),
                    "Unit": {
                        "options": [
                            "ryczałt"
                        ]
                    }
                },
            ),
        ],
    ),
]

estimate_sections = [asdict(section) for section in estimate_sections]
