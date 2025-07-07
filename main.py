from classes.kosztorys_generator import KosztorysGenerator


def main():
    generator = KosztorysGenerator(
        parts={
            'layout': "data/report/kosztorys/kosztorys_layout.json",
            'total': "data/report/kosztorys/kosztorys_total.json",
            'position_layout': "data/report/kosztorys/kosztorys_position_layout.json",
            'position_single': "data/report/kosztorys/kosztorys_position_single.json",
            'position_total': "data/report/kosztorys/kosztorys_position_total.json"
        },
        structure={
            'part': 'layout',
            'components': [
                {
                    'part': 'position_layout',
                    'title': "1. Koszty przygotowania",
                    'components': [
                        {
                            'part': 'position_total',
                            'baseName': 'preparation',
                            'title': "1. Koszty przygotowania i zarządzania - RAZEM",
                        },
                        {
                            'part': 'position_single',
                            'baseName': 'festivalDirector',
                            'title': 'Koszty dyrektora festiwalu'
                        },
                        {
                            'part': 'position_single',
                            'baseName': 'artisticDirector',
                            'title': 'Koszty dyrektora artystycznego'
                        }
                    ]
                },
                {
                    'part': 'position_layout',
                    'title': "2. Koszty zarządzania",
                    'components': [
                        {
                            'part': 'position_total',
                            'baseName': 'management',
                            'title': "2. Koszty zarządzania - RAZEM",
                        },
                        {
                            'part': 'position_single',
                            'baseName': 'prefestivalDirector',
                            'title': 'Koszty dyrektora festiwalu'
                        },
                        {
                            'part': 'position_single',
                            'baseName': 'preartisticDirector',
                            'title': 'Koszty dyrektora artystycznego'
                        }
                    ]
                },
                {
                    'part': 'total',
                }
            ]
        },
        output_path='output.json'
    )
    generator.generate()
    generator.save_output()
    print('Plik output.json został utworzony na podstawie kosztorys_layout.json.')


if __name__ == '__main__':
    main()
