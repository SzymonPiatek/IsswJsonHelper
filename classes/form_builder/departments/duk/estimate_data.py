estimate_section_structure = [
    {
        'type': 'text',
        'label': '',
        'name': 'Desc',
        'readOnly': True,
        'isDesc': True,
    },
    {
        'type': 'text',
        'mask': 'fund',
        'label': 'Koszt ogółem',
        'name': 'SumAmount',
        'readOnly': True,
        'sumFields': ['RequestedAmount', 'OtherFundsAmount'],
        'unit': 'PLN'
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
