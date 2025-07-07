import json

class KosztorysGenerator:
    """
    Klasa odpowiedzialna za generowanie kosztorysu na podstawie definicji parts i structure.
    Obsługuje baseName, afterName, lokalne sumy (isSum) oraz globalne sumy.
    """
    def __init__(self, parts: dict, structure: dict, output_path: str):
        self.parts = parts
        self.structure = structure
        self.output_path = output_path
        self.loaded_parts = {}
        self.result = None

    def load_parts(self) -> None:
        """Wczytuje wszystkie pliki części kosztorysu do pamięci."""
        for key, path in self.parts.items():
            with open(path, 'r', encoding='utf-8') as f:
                self.loaded_parts[key] = json.load(f)

    def build_component(self, node: dict, prefix: str = "") -> dict:
        """
        Rekurencyjnie buduje fragment kosztorysu według node.
        prefix: skumulowany ciąg baseName od rodziców (bez afterName).
        """
        part_key = node['part']
        tpl = self.loaded_parts.get(part_key)
        if tpl is None:
            raise ValueError(f"Nie znaleziono części '{part_key}'.")
        comp = json.loads(json.dumps(tpl))

        # Rozbijamy own attributes
        base  = node.get('baseName', "")
        after = node.get('afterName', "")

        # Nowy prefix do dzieci (bez afterName)
        current_prefix = prefix + base

        # Nadpisanie title
        if 'title' in node:
            comp['title'] = node['title']

        # Prefiksowanie i suffixowanie własnej nazwy
        if 'name' in comp:
            orig = comp['name']
            new_name = f"{current_prefix}{orig}{after}"
            comp['name']    = new_name
            comp['dataBDD'] = new_name

        # Jeżeli node definiuje własne children w strukturze
        if 'components' in node:
            built_children = [
                self.build_component(child, current_prefix)
                for child in node['components']
            ]
            comp['components'] = built_children

            # 1) Lokalna suma wewnątrz position_layout
            if part_key == 'position_layout':
                for idx, child_node in enumerate(node['components']):
                    if child_node.get('isSum', False):
                        summary = built_children[idx]
                        siblings = [
                            built_children[j]
                            for j, sib in enumerate(node['components'])
                            if not sib.get('isSum', False)
                        ]
                        if len(siblings) > 1:
                            for f_i, fld in enumerate(summary.get('components', [])):
                                fields = [
                                    sib['components'][f_i]['name']
                                    for sib in siblings
                                ]
                                # wypełnienie calculationRules
                                if 'calculationRules' in fld and fld['calculationRules']:
                                    fld['calculationRules'][0]['kwargs']['fields'] = fields
                                # wypełnienie validatorów
                                for v in fld.get('validators', []):
                                    if v['name'] == 'RelatedSumValidator':
                                        v['kwargs']['field_names'] = fields

            # 2) Globalna suma w głównym układzie (layout)
            if part_key == 'layout':
                # Zbierz cztery listy z każdego position_layout->isSum
                lists = [[], [], [], []]  # 0:Planned,1:Requested,2:Actual,3:Support
                for node_child, comp_child in zip(node['components'], built_children):
                    if node_child['part'] == 'position_layout':
                        for j, sub in enumerate(node_child['components']):
                            if sub.get('isSum', False):
                                summ = comp_child['components'][j]
                                # pomiń pierwszy textarea
                                num_fields = summ.get('components', [])[1:]
                                for k, nf in enumerate(num_fields):
                                    lists[k].append(nf['name'])
                                break
                # Znajdź globalny total
                total_comp = None
                for node_child, comp_child in zip(node['components'], built_children):
                    if node_child['part'] == 'total':
                        total_comp = comp_child
                        break
                # Wstrzyknięcie globalnych list do total
                if total_comp:
                    cnt = 0
                    for fld in total_comp.get('components', []):
                        if fld.get('mask') == 'fund':
                            if 'calculationRules' in fld and fld['calculationRules']:
                                fld['calculationRules'][0]['kwargs']['fields'] = lists[cnt]
                            for v in fld.get('validators', []):
                                if v['name'] == 'RelatedSumValidator':
                                    v['kwargs']['field_names'] = lists[cnt]
                            cnt += 1

            return comp

        # Gdy template ma własne components, ale node ich nie nadpisuje
        if 'components' in comp:
            def _prefix_list(lst):
                out = []
                for c in lst:
                    sub = json.loads(json.dumps(c))
                    if 'name' in sub:
                        orig2 = sub['name']
                        newn = f"{current_prefix}{orig2}{after}"
                        sub['name']    = newn
                        sub['dataBDD'] = newn
                    if 'components' in sub:
                        sub['components'] = _prefix_list(sub['components'])
                    out.append(sub)
                return out
            comp['components'] = _prefix_list(comp['components'])

        return comp

    def generate(self) -> None:
        """Generuje pełny kosztorys według zadanej struktury."""
        self.load_parts()
        self.result = self.build_component(self.structure, "")

    def save_output(self) -> None:
        """Zapisuje wygenerowany kosztorys do pliku JSON."""
        if self.result is None:
            raise ValueError("Brak wygenerowanego kosztorysu. Najpierw wywołaj generate().")
        with open(self.output_path, 'w', encoding='utf-8') as f:
            json.dump(self.result, f, ensure_ascii=False, indent=2)
