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
        part_key = node['part']
        tpl = self.loaded_parts.get(part_key)
        if tpl is None:
            raise ValueError(f"Nie znaleziono części '{part_key}'.")
        comp = json.loads(json.dumps(tpl))

        # 1) rozbuduj prefix o własne baseName
        current_prefix = prefix + node.get('baseName', "")

        # 2) tytuł
        if 'title' in node:
            comp['title'] = node['title']

        # 3) prefiksuj własną nazwę
        if 'name' in comp:
            orig = comp['name']
            new_name = current_prefix + orig
            comp['name']    = new_name
            comp['dataBDD'] = new_name

        # 4) buduj dzieci z struktury
        if 'components' in node:
            built = [ self.build_component(ch, current_prefix)
                      for ch in node['components'] ]
            comp['components'] = built

            # 4a) lokalne sumy dla position_layout
            if part_key == 'position_layout':
                for idx, child_node in enumerate(node['components']):
                    if child_node.get('isSum', False):
                        summary = built[idx]
                        siblings = [ built[j]
                                     for j,ch in enumerate(node['components'])
                                     if not ch.get('isSum', False) ]
                        if len(siblings) > 1:
                            for f_i, fld in enumerate(summary.get('components', [])):
                                # pola do sumowania z każdego sibling
                                fields = [
                                    sib['components'][f_i]['name']
                                    for sib in siblings
                                ]
                                # uzupełnij calculationRules i validators
                                if 'calculationRules' in fld and fld['calculationRules']:
                                    fld['calculationRules'][0]['kwargs']['fields'] = fields
                                for v in fld.get('validators', []):
                                    if v['name'] == 'RelatedSumValidator':
                                        v['kwargs']['field_names'] = fields

            # 4b) globalne sumy dla part 'layout'
            if part_key == 'layout':
                # 1) zbierz listy czterech pól z każdego position_layout->isSum
                lists = [ [], [], [], [] ]  # idx: 0->Planned,1->Requested,2->Actual,3->Support
                for node_child, comp_child in zip(node['components'], built):
                    if node_child['part'] == 'position_layout':
                        # znajdź summary index
                        for j, sub in enumerate(node_child['components']):
                            if sub.get('isSum', False):
                                summ = comp_child['components'][j]
                                num_fields = summ.get('components', [])[1:]
                                for k, nf in enumerate(num_fields):
                                    lists[k].append(nf['name'])
                                break

                # 2) znajdź globalny total
                total_comp = None
                for node_child, comp_child in zip(node['components'], built):
                    if node_child['part'] == 'total':
                        total_comp = comp_child
                        break

                # 3) wstrzyknięcie
                if total_comp:
                    cnt = 0
                    for fld in total_comp.get('components', []):
                        if fld.get('mask') == 'fund':
                            # sumInputs
                            if 'calculationRules' in fld and fld['calculationRules']:
                                fld['calculationRules'][0]['kwargs']['fields'] = lists[cnt]
                            # RelatedSumValidator
                            for v in fld.get('validators', []):
                                if v['name'] == 'RelatedSumValidator':
                                    v['kwargs']['field_names'] = lists[cnt]
                            cnt += 1

            return comp

        # 5) gdy template ma własne komponenty bez defs w strukturze
        if 'components' in comp:
            def _pref(lst):
                out = []
                for c in lst:
                    sub = json.loads(json.dumps(c))
                    if 'name' in sub:
                        nm = current_prefix + sub['name']
                        sub['name']    = nm
                        sub['dataBDD'] = nm
                    if 'components' in sub:
                        sub['components'] = _pref(sub['components'])
                    out.append(sub)
                return out
            comp['components'] = _pref(comp['components'])

        return comp

    def generate(self) -> None:
        self.load_parts()
        self.result = self.build_component(self.structure, "")

    def save_output(self) -> None:
        if self.result is None:
            raise ValueError("Brak wygenerowanego kosztorysu. Najpierw wywołaj generate().")
        with open(self.output_path, 'w', encoding='utf-8') as f:
            json.dump(self.result, f, ensure_ascii=False, indent=2)