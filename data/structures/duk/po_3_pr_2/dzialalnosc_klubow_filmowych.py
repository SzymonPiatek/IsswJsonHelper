structure = {
    'part': 'layout',
    'components': [
        {
            'part': 'position_layout',
            'title': "1. Koszty przygotowania i zarządzania przedsięwzięciem (konieczne jest wyszczególnienie funkcji oraz podanie honorarium lub wynagrodzenia). <br /><normal><small>Wyłącznie koszty finansowane w oparciu o umowy wraz z fakturami lub rachunkami i umowy zlecenia lub o dzieło wraz z rachunkami</small></normal>",
            'components': [
                {
                    'isSum': True,
                    'part': 'position_total',
                    'baseName': 'costManagement',
                    'title': "1. Koszty przygotowania i zarządzania przedsięwzięciem - RAZEM",
                    'afterName': 'Pr3',
                },
                {
                    'part': 'position_single',
                    'baseName': 'creatorsArtists',
                    'title': 'Koszty twórców i artystów',
                    'afterName': 'Pr3',
                },
                {
                    'part': 'position_single',
                    'baseName': 'speakers',
                    'title': 'Koszty prelegentów',
                    'afterName': 'Pr3',
                },
                {
                    'part': 'position_single',
                    'baseName': 'eventHosts',
                    'title': 'Koszty osób prowadzących',
                    'afterName': 'Pr3',
                },
                {
                    'part': 'position_single',
                    'baseName': 'coordinators',
                    'title': 'Koszty koordynatorów',
                    'afterName': 'Pr3',
                }
            ]
        },
        {
            'part': 'position_layout',
            'title': '2. Koszty promocji i reklamy',
            "components": [
                {
                    'isSum': True,
                    'part': 'position_single',
                    'baseName': 'commercials',
                    'title': '2. Koszty promocji i reklamy',
                    'afterName': 'Pr3'
                }
            ]
        },
        {
            'part': 'position_layout',
            'title': '3. Koszty związane z miejscem realizacji przedsięwzięcia <br /><normal><small>np. koszty najmu sali lub powierzchni na potrzeby przedsięwzięcia (z wyłączeniem zakupu środków trwałych) </small></normal>',
            "components": [
                {
                    'isSum': True,
                    'part': 'position_single',
                    'baseName': 'location',
                    'title': '3. Koszty związane z miejscem realizacji przedsięwzięcia',
                    'afterName': 'Pr3'
                }
            ]
        },
        {
            'part': 'position_layout',
            'title': "4. Koszty obsługi przedsięwzięcia",
            'components': [
                {
                    'isSum': True,
                    'part': 'position_total',
                    'baseName': 'eventHosting',
                    'title': "4. Koszty obsługi przedsięwzięcia - RAZEM",
                    'afterName': 'Pr3',
                },
                {
                    'part': 'position_single',
                    'baseName': 'personal',
                    'title': 'Koszty osobowe',
                    'afterName': 'Pr3',
                },
                {
                    'part': 'position_single',
                    'baseName': 'equipmentRental',
                    'title': 'Koszty najmu sprzętu',
                    'afterName': 'Pr3',
                },
            ]
        },
        {
            'part': 'position_layout',
            'title': "5. Koszty dotyczące podróży <br /><normal><small>Koszty przejazdu udokumentowane wyłącznie fakturami lub biletami; w przypadku podróży lotniczych pokrywa się z dotacji tylko koszt biletów w klasie ekonomicznej (z wyłączeniem diet, ryczałtów i innych kosztów udokumentowanych w inny sposób, niż rachunkiem lub fakturą). </small></normal>",
            'components': [
                {
                    'isSum': True,
                    'part': 'position_total',
                    'baseName': 'trip',
                    'title': "5. Koszty dotyczące podróży - RAZEM",
                    'afterName': 'Pr3',
                },
                {
                    'part': 'position_single',
                    'baseName': 'hostsTrip',
                    'title': 'Organizatorów przedsięwzięcia',
                    'afterName': 'Pr3',
                },
                {
                    'part': 'position_single',
                    'baseName': 'participantsTrip',
                    'title': 'Twórców, artystów, prelegentów',
                    'afterName': 'Pr3',
                },
                {
                    'part': 'position_single',
                    'baseName': 'questsTrip',
                    'title': 'Zaproszonych gości',
                    'afterName': 'Pr3',
                },
            ]
        },
        {
            'part': 'position_layout',
            'title': '6. Koszty dotyczące noclegów <br /><normal><small>Koszty zakwaterowania udokumentowane wyłącznie fakturami (z wyłączeniem diet, ryczałtów i innych kosztów udokumentowanych w inny sposób, niż rachunkiem lub fakturą). </normal></small> ',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_total',
                    'baseName': 'accommodation',
                    'title': '6. Koszty dotyczące noclegów - RAZEM',
                    'afterName': 'Pr3',
                },
                {
                    'part': 'position_single',
                    'baseName': 'hostsAccommodation',
                    'title': 'Organizatorów przedsięwzięcia',
                    'afterName': 'Pr3',
                },
                {
                    'part': 'position_single',
                    'baseName': 'participantsAccommodation',
                    'title': 'Twórców, artystów, prelegentów',
                    'afterName': 'Pr3',
                },
                {
                    'part': 'position_single',
                    'baseName': 'questsAccommodation',
                    'title': 'Zaproszonych gości',
                    'afterName': 'Pr3',
                },
            ]
        },
        {
            'part': 'position_layout',
            'title': '7. Koszty składki Polskiej Federacji Dyskusyjnych Klubów Filmowych <br /><normal><small>(pokrywane tylko ze środków wnioskodawcy) </small></normal>',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_single',
                    'baseName': 'polishDkfFederationFee',
                    'title': '7. Koszty składki PFDKF',
                    'afterName': 'Pr3',
                },
            ]
        },
        {
            'part': 'position_layout',
            'title': '8. Koszty praw autorskich',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_single',
                    'baseName': 'copyright',
                    'title': '8. Koszty praw autorskich',
                    'afterName': 'Pr3',
                },
            ]
        },
        {
            'part': 'position_layout',
            'title': '9. Koszty najmu kopii filmowych',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_single',
                    'baseName': 'copyRental',
                    'title': '9. Koszty najmu kopii filmowych',
                    'afterName': 'Pr3',
                },
            ]
        },
        {
            'part': 'position_layout',
            'title': '10. Koszty obsługi projektów online',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_single',
                    'baseName': 'onlineManagement',
                    'title': '10. Koszty obsługi projektów online',
                    'afterName': 'Pr3',
                },
            ]
        },
        {
            'part': 'position_layout',
            'title': '11. Koszty związane z dostosowaniem działań i formy przekazu do osób ze szczególnymi potrzebami, w tym osób z niepełnosprawnościami',
            'components': [
                {
                    'isSum': True,
                    'part': 'position_single',
                    'baseName': 'accessibility',
                    'title': '11. Koszty związane z dostosowaniem działań i formy przekazu do osób ze szczególnymi potrzebami, w tym osób z niepełnosprawnościami',
                    'afterName': 'Pr3',
                },
            ]
        },
        {
            'part': 'total',
            'afterName': 'Pr3',
        }
    ]
}
