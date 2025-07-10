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
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'costManagementSumAmountPr4',
                        'requestedPlanned': 'costManagementRequestedAmountPr4'
                    }
                },
                {
                    'part': 'position_single',
                    'baseName': 'artists',
                    'title': 'Koszty twórców i artystów',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'artistsSumAmountPr4',
                        'requestedPlanned': 'artistsRequestedAmountPr4'
                    }
                },
                {
                    'part': 'position_single',
                    'baseName': 'speakers',
                    'title': 'Koszty prelegentów, wykładowców',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'speakersSumAmountPr4',
                        'requestedPlanned': 'speakersRequestedAmountPr4'
                    }
                },
                {
                    'part': 'position_single',
                    'baseName': 'curator',
                    'title': 'Koszty komisarza wystawy',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'curatorSumAmountPr4',
                        'requestedPlanned': 'curatorRequestedAmountPr4'
                    }
                },
                {
                    'part': 'position_single',
                    'baseName': 'organizers',
                    'title': 'Koszty koordynatorów',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'organizersSumAmountPr4',
                        'requestedPlanned': 'organizersRequestedAmountPr4'
                    }
                },
                {
                    'part': 'position_single',
                    'baseName': 'eventHosts',
                    'title': 'Koszty osób prowadzących',
                    'afterName': 'Pr4',
                    'copyFrom': {
                        'totalPlanned': 'eventHostsSumAmountPr4',
                        'requestedPlanned': 'eventHostsRequestedAmountPr4'
                    }
                }
            ]
        },
        {
            'part': 'total',
            'afterName': 'Pr1',
        }
    ]
}
