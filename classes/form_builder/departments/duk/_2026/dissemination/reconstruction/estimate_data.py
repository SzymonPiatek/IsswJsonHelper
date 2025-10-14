from dataclasses import asdict
from classes.form_estimate_builder.dataclasses_definitions import EstimateSection, CostItem, CostOverride


estimate_sections = [
    EstimateSection(
        title="ETAP",
        helpText="Wyłącznie koszty finansowane w oparciu o umowy wraz z fakturami/rachunkami oraz umowy zlecenie lub o dzieło wraz z rachunkami.",
        costs=[
            CostItem(
                title="Wypożyczenie materiałów wyjściowych",
                name="sourceMaterialsRental",
            ),
            CostItem(
                title="Czyszczenie materiałów wyjściowych – obraz i dźwięk",
                name="sourceMaterialsCleaning",
            ),
            CostItem(
                title="Skanowanie materiałów wyjściowych – obraz i dźwięk",
                name="sourceMaterialsScanning",
            ),
            CostItem(
                title="Digitalizacja materiałów wyjściowych dźwięku",
                name="sourceSoundDigitization",
            ),
            CostItem(
                title="Wykonanie cyfrowych kopii archiwizacyjnych materiałów wyjściowych – obraz",
                name="archivalCopiesImage",
            ),
            CostItem(
                title="Wykonanie cyfrowych kopii archiwizacyjnych materiałów wyjściowych – dźwięk",
                name="archivalCopiesSound",
            ),
            CostItem(
                title="Nośniki kopii archiwizacyjnych materiałów wyjściowych",
                name="archivalCopiesMedia",
            ),
            CostItem(
                title="Opis stanu technicznego materiałów wyjściowych – przegląd i ocena stanu zniszczeń",
                name="technicalConditionReport",
            ),
        ],
    ),
    EstimateSection(
        title="ETAP",
        costs=[
            CostItem(
                title="Konforming – porównanie zeskanowanego materiału filmowego z dostępnymi kopiami filmu i przygotowanie wersji referencyjnej do rekonstrukcji",
                name="conforming",
            ),
            CostItem(
                title="Rekonstrukcja obrazu",
                name="imageRestoration",
            ),
            CostItem(
                title="Rekonstrukcja dźwięku",
                name="soundRestoration",
            ),
            CostItem(
                title="Synchronizacja dźwięku z obrazem",
                name="soundSynchronization",
            ),
            CostItem(
                title="Wykonanie cyfrowych kopii master – archiwizacyjnych i operacyjnych TIFF/LTO",
                name="masterCopies",
            ),
            CostItem(
                title="Nośniki kopii master",
                name="masterCopiesMedia",
            ),
            CostItem(
                title="Wykonanie dystrybucyjnych cyfrowych kopii wzorcowych filmu – archiwizacyjnych i operacyjnych",
                name="distributionCopies",
            ),
            CostItem(
                title="Nośniki kopii dystrybucyjnych",
                name="distributionCopiesMedia",
            ),
            CostItem(
                title="Wykonanie kopii wieczystej filmu na taśmie światłoczułej",
                name="permanentFilmCopy",
            ),
            CostItem(
                title="Nadzór lub opieka artystyczna",
                name="artisticSupervision",
            ),
            CostItem(
                title="Kontrola techniczna jakości wykonania rekonstrukcji obrazu i dźwięku",
                name="technicalQualityControl",
            ),
            CostItem(
                title="Koordynacja procesu digitalizacji i rekonstrukcji cyfrowej",
                name="processCoordination",
            ),
            CostItem(
                title="Przygotowanie wersji językowej (maks. 3 wersje)",
                name="languageVersion",
            ),
            CostItem(
                title="Opracowanie i wykonanie filmowych materiałów promocyjnych",
                name="promotionalMaterials",
                helpText="Pokrywane wyłącznie ze środków własnych lub innych źródeł finansowania.",
            ),
            CostItem(
                title="Organizacja kolaudacji",
                name="screeningOrganization",
                helpText="Pokrywane wyłącznie ze środków własnych lub innych źródeł finansowania.",
                overrides={
                    "RequestedAmount": CostOverride(
                        readOnly=True,
                    ),
                },
            ),
            CostItem(
                title="Transport materiałów filmowych",
                name="materialsTransport",
                helpText="Pokrywane wyłącznie ze środków własnych lub innych źródeł finansowania.",
                overrides={
                    "RequestedAmount": CostOverride(
                        readOnly=True,
                    ),
                },
            ),
        ],
    ),
]

estimate_sections = [asdict(section) for section in estimate_sections]
