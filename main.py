from classes.kosztorys_generator import KosztorysGenerator
from structure import structure


def main():
    generator = KosztorysGenerator(
        parts={
            'layout': "data/report/kosztorys/kosztorys_layout.json",
            'total': "data/report/kosztorys/kosztorys_total.json",
            'position_layout': "data/report/kosztorys/kosztorys_position_layout.json",
            'position_single': "data/report/kosztorys/kosztorys_position_single.json",
            'position_total': "data/report/kosztorys/kosztorys_position_total.json"
        },
        structure=structure,
        output_path='output.json'
    )
    generator.generate()
    generator.save_output()
    print('Plik output.json został utworzony na podstawie kosztorys_layout.json.')


if __name__ == '__main__':
    main()
