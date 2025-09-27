estimate_section_structure = [
    {
        'label': '',
        'name': 'Desc',
        'readOnly': True,
        'isDesc': True,
    },
    {
        'label': 'Koszt ogółem',
        'name': 'SumAmount',
        'readOnly': True,
        'sumFields': ['RequestedAmount', 'OtherFundsAmount']
    },
    {
        'label': 'Wnioskowana dotacja PISF',
        'name': 'RequestedAmount'
    },
    {
        'label': 'Pozostałe środki',
        'name': 'OtherFundsAmount'
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
        'isSum': True,
        'label': 'Koszt ogółem',
        'name': 'SumAmount',
        'unit': 'PLN'
    },
    {
        'isSum': True,
        'label': 'Wnioskowana dotacja PISF ogółem',
        'name': 'RequestedAmount',
        'unit': 'PLN'
    },
    {
        'isSum': True,
        'label': 'Pozostałe środki ogółem',
        'name': 'OtherFundsAmount',
        'unit': 'PLN'
    },
    {
        'isShare': True,
        'label': 'Udział wsparcia PISF w kosztach ogółem',
        'name': 'RequestedAmountShareInTotal',
        'unit': '%',
        'dividend': 'totalRequestedAmount',
        'divisor': 'totalSumAmount',
    }
]
