from classes.form_rules import Validator

validators = Validator()

estimate_sections = [
    {
        "title": "ETAP",
        "helpText": "Wyłącznie koszty finansowane w oparciu o umowy wraz z fakturami/rachunkami oraz umowy zlecenia lub o dzieło wraz z rachunkami.",
        "costs": [
            {
                "title": "Wypożyczenie materiałów wyjściowych",
                "name": "sourceMaterialsRental"
            },
            {
                "title": "Czyszczenie materiałów wyjściowych – obraz i dźwięk",
                "name": "sourceMaterialsCleaning"
            },
            {
                "title": "Skanowanie materiałów wyjściowych – obraz i dźwięk",
                "name": "sourceMaterialsScanning"
            },
            {
                "title": "Digitalizacja materiałów wyjściowych dźwięku",
                "name": "sourceSoundDigitization"
            },
            {
                "title": "Wykonanie cyfrowych kopii archiwizacyjnych materiałów wyjściowych – obraz",
                "name": "archivalCopiesImage"
            },
            {
                "title": "Wykonanie cyfrowych kopii archiwizacyjnych materiałów wyjściowych – dźwięk",
                "name": "archivalCopiesSound"
            },
            {
                "title": "Nośniki kopii archiwizacyjnych materiałów wyjściowych",
                "name": "archivalCopiesMedia"
            },
            {
                "title": "Opis stanu technicznego materiałów wyjściowych – przegląd i ocena stanu zniszczeń",
                "name": "technicalConditionReport"
            }
        ]
    },
    {
        "title": "ETAP",
        "costs": [
            {
                "title": "Konforming – porównanie zeskanowanego materiału filmowego z dostępnymi kopiami filmu i przygotowanie wersji referencyjnej do rekonstrukcji",
                "name": "conforming"
            },
            {
                "title": "Rekonstrukcja obrazu",
                "name": "imageRestoration"
            },
            {
                "title": "Rekonstrukcja dźwięku",
                "name": "soundRestoration"
            },
            {
                "title": "Synchronizacja dźwięku z obrazem",
                "name": "soundSynchronization"
            },
            {
                "title": "Wykonanie cyfrowych kopii master – archiwizacyjnych i operacyjnych TIFF/LTO",
                "name": "masterCopies"
            },
            {
                "title": "Nośniki kopii master",
                "name": "masterCopiesMedia"
            },
            {
                "title": "Wykonanie dystrybucyjnych cyfrowych kopii wzorcowych filmu – archiwizacyjnych i operacyjnych",
                "name": "distributionCopies"
            },
            {
                "title": "Nośniki kopii dystrybucyjnych",
                "name": "distributionCopiesMedia"
            },
            {
                "title": "Wykonanie kopii wieczystej filmu na taśmie światłoczułej",
                "name": "permanentFilmCopy"
            },
            {
                "title": "Nadzór lub opieka artystyczna",
                "name": "artisticSupervision"
            },
            {
                "title": "Kontrola techniczna jakości wykonania rekonstrukcji obrazu i dźwięku",
                "name": "technicalQualityControl"
            },
            {
                "title": "Koordynacja procesu digitalizacji i rekonstrukcji cyfrowej",
                "name": "processCoordination"
            },
            {
                "title": "Przygotowanie wersji językowej (maks. 3 wersje)",
                "name": "languageVersion"
            },
            {
                "title": "Opracowanie i wykonanie filmowych materiałów promocyjnych",
                "name": "promotionalMaterials",
                "helpText": "Pokrywane wyłącznie ze środków własnych lub innych źródeł finansowania."
            },
            {
                "title": "Organizacja kolaudacji",
                "name": "screeningOrganization",
                "helpText": "Pokrywane wyłącznie ze środków własnych lub innych źródeł finansowania.",
                "overrides": {
                    "RequestedAmount": {
                        "readOnly": True
                    }
                }
            },
            {
                "title": "Transport materiałów filmowych",
                "name": "materialsTransport",
                "helpText": "Pokrywane wyłącznie ze środków własnych lub innych źródeł finansowania.",
                "overrides": {
                    "RequestedAmount": {
                        "readOnly": True
                    }
                }
            }
        ]
    }
]
