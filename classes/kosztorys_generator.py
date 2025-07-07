import json

class KosztorysGenerator:
    def __init__(self, parts: dict, structure: dict, output_path: str):
        self.parts = parts
        self.structure = structure
        self.output_path = output_path
        self.loaded_parts = {}
        self.result = None

    def load_parts(self) -> None:
        for key, path in self.parts.items():
            with open(path, 'r', encoding='utf-8') as f:
                self.loaded_parts[key] = json.load(f)

    def build_component(self, node: dict, prefix: str = "") -> dict:
        """
        Rekurencyjnie buduje fragment kosztorysu zgodnie z definicją `node`.
        prefix: dotychczasowy skumulowany baseName od rodziców.
        """
        part_key = node['part']
        template = self.loaded_parts.get(part_key)
        if template is None:
            raise ValueError(f"Nie znaleziono części '{part_key}'.")
        # deep copy szablonu
        comp = json.loads(json.dumps(template))

        # 1) nowy prefix = przekazany + własny baseName (jeśli jest)
        current_prefix = prefix + node.get('baseName', "")

        # 2) nadpisz title, jeśli jest
        if 'title' in node:
            comp['title'] = node['title']

        # 3) jeśli szablon ma pole 'name', prefixuj je i dataBDD
        if 'name' in comp:
            orig = comp['name']
            new_name = current_prefix + orig
            comp['name']    = new_name
            comp['dataBDD'] = new_name

        # 4A) jeśli struktura node ma children, buduj po node['components']
        if 'components' in node:
            comp['components'] = [
                self.build_component(child, current_prefix)
                for child in node['components']
            ]

        # 4B) w przeciwnym razie – prefixuj template’owe komponenty
        elif 'components' in comp:
            def prefix_children(children_list):
                new_list = []
                for child in children_list:
                    # deep copy each child fragment
                    c = json.loads(json.dumps(child))
                    if 'name' in c:
                        orig2 = c['name']
                        nn = current_prefix + orig2
                        c['name']    = nn
                        c['dataBDD'] = nn
                    # jeśli są głębsze podkomponenty, idziemy rekurencyjnie
                    if 'components' in c:
                        c['components'] = prefix_children(c['components'])
                    new_list.append(c)
                return new_list

            comp['components'] = prefix_children(comp['components'])

        return comp

    def generate(self) -> None:
        self.load_parts()
        # start bez prefixu
        self.result = self.build_component(self.structure, "")

    def save_output(self) -> None:
        if self.result is None:
            raise ValueError("Brak wygenerowanego kosztorysu. Najpierw wywołaj generate().")
        with open(self.output_path, 'w', encoding='utf-8') as f:
            json.dump(self.result, f, ensure_ascii=False, indent=2)
