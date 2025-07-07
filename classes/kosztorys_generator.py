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
        Rekurencyjnie buduje fragment kosztorysu według node.
        prefix: skumulowany baseName od rodziców.
        """
        part_key = node['part']
        template = self.loaded_parts.get(part_key)
        if template is None:
            raise ValueError(f"Nie znaleziono części '{part_key}'.")
        # 1) Deep copy szablonu
        comp = json.loads(json.dumps(template))

        # 2) Rozszerz prefix o własny baseName (jeśli jest)
        current_prefix = prefix + node.get('baseName', "")

        # 3) Nadpisz title
        if 'title' in node:
            comp['title'] = node['title']

        # 4) Jeśli szablon ma własne pole name, prefixuj je
        if 'name' in comp:
            orig = comp['name']
            new_name = current_prefix + orig
            comp['name']    = new_name
            comp['dataBDD'] = new_name

        # 5) Obsługa dzieci zdefiniowanych w strukturze
        if 'components' in node:
            # Budujemy rekurencyjnie każdy child
            built_children = [
                self.build_component(child, current_prefix)
                for child in node['components']
            ]
            comp['components'] = built_children

            # Jeżeli to rozdział position_layout, wstrzyknij sumowanie
            if part_key == 'position_layout':
                # przejrzyj każdy node+jego built_child
                for idx, child_node in enumerate(node['components']):
                    if child_node.get('isSum', False):
                        summary = built_children[idx]
                        # zbierz wszystkie rodzeństwa bez isSum
                        siblings = [
                            built_children[j]
                            for j, sib_node in enumerate(node['components'])
                            if not sib_node.get('isSum', False)
                        ]
                        # jeśli jest co najmniej dwóch, to sumujemy
                        if len(siblings) > 1:
                            # dla każdego pola w podsumowaniu
                            for f_idx, field_comp in enumerate(summary.get('components', [])):
                                # pola do sumowania
                                fields_list = [
                                    sib['components'][f_idx]['name']
                                    for sib in siblings
                                ]
                                # 5.1) uzupełnij calculationRules
                                if 'calculationRules' in field_comp and field_comp['calculationRules']:
                                    field_comp['calculationRules'][0]['kwargs']['fields'] = fields_list
                                # 5.2) uzupełnij validators(RelatedSumValidator)
                                for v in field_comp.get('validators', []):
                                    if v['name'] == 'RelatedSumValidator':
                                        v['kwargs']['field_names'] = fields_list
            return comp

        # 6) Gdy node nie definiuje sub-komponentów, ale template je ma,
        #    prefixujemy te template’owe dzieci
        elif 'components' in comp:
            def _prefix_list(lst):
                out = []
                for c in lst:
                    sub = json.loads(json.dumps(c))
                    if 'name' in sub:
                        nn = current_prefix + sub['name']
                        sub['name']    = nn
                        sub['dataBDD'] = nn
                    if 'components' in sub:
                        sub['components'] = _prefix_list(sub['components'])
                    out.append(sub)
                return out
            comp['components'] = _prefix_list(comp['components'])
            return comp

        # 7) Liść – zwróć po modyfikacji nazwy
        return comp

    def generate(self) -> None:
        self.load_parts()
        self.result = self.build_component(self.structure, "")

    def save_output(self) -> None:
        if self.result is None:
            raise ValueError("Brak wygenerowanego kosztorysu. Najpierw wywołaj generate().")
        with open(self.output_path, 'w', encoding='utf-8') as f:
            json.dump(self.result, f, ensure_ascii=False, indent=2)
