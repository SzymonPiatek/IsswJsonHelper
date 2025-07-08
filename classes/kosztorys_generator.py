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
        comp = json.loads(json.dumps(tpl))  # deep copy

        # Rozbijanie atrybutów własnych
        base  = node.get('baseName', "")
        after = node.get('afterName', "")
        current_prefix = prefix + base

        # Nadpisanie title
        if 'title' in node:
            comp['title'] = node['title']

        # Specjalne dla position_single: uzupełnienie textarea Rodzaj kosztów
        if part_key == 'position_single' and 'components' in comp:
            for fld in comp['components']:
                if fld.get('type') == 'textarea' and fld.get('label') == 'Rodzaj kosztów':
                    fld['value'] = node.get('title', '')
                    break

        # Prefiksowanie i suffixowanie nazwy komponentu
        if 'name' in comp:
            orig = comp['name']
            comp_name = f"{current_prefix}{orig}{after}"
            comp['name']    = comp_name
            comp['dataBDD'] = comp_name

        # Jeżeli node definiuje podkomponenty w strukturze
        if 'components' in node:
            children = [self.build_component(c, current_prefix) for c in node['components']]
            comp['components'] = children

            # 1) Lokalna suma w position_layout
            if part_key == 'position_layout':
                for idx, ch in enumerate(node['components']):
                    if ch.get('isSum'):
                        summ = children[idx]
                        peers = [children[j] for j,ch2 in enumerate(node['components']) if not ch2.get('isSum')]
                        if peers:
                            for i, fld in enumerate(summ.get('components', [])):
                                fields = [p['components'][i]['name'] for p in peers]
                                if fld.get('calculationRules'):
                                    fld['calculationRules'][0]['kwargs']['fields'] = fields
                                for v in fld.get('validators', []):
                                    if v['name']=='RelatedSumValidator':
                                        v['kwargs']['field_names']=fields

            # 2) Globalna suma w layout
            if part_key == 'layout':
                sums = [[],[],[],[]]
                for n_child, c_child in zip(node['components'], children):
                    if n_child['part']=='position_layout':
                        for j, sub in enumerate(n_child['components']):
                            if sub.get('isSum'):
                                comp_sum = c_child['components'][j]
                                for k, nf in enumerate(comp_sum.get('components', [])[1:]):
                                    sums[k].append(nf['name'])
                                break
                total_comp = None
                for n_child, c_child in zip(node['components'], children):
                    if n_child['part']=='total': total_comp=c_child; break
                if total_comp:
                    cnt=0
                    for fld in total_comp.get('components', []):
                        if fld.get('mask')=='fund':
                            if fld.get('calculationRules'):
                                fld['calculationRules'][0]['kwargs']['fields']=sums[cnt]
                            for v in fld.get('validators',[]):
                                if v['name']=='RelatedSumValidator':
                                    v['kwargs']['field_names']=sums[cnt]
                            cnt+=1
            return comp

        # Gdy template ma components, a node ich nie przedefiniowuje
        if 'components' in comp:
            def _pref(lst):
                out=[]
                for item in lst:
                    sub=json.loads(json.dumps(item))
                    if 'name' in sub:
                        nm=sub['name']; newnm=f"{current_prefix}{nm}{after}"; sub['name']=newnm; sub['dataBDD']=newnm
                    if 'components' in sub:
                        sub['components']=_pref(sub['components'])
                    out.append(sub)
                return out
            comp['components']=_pref(comp['components'])

            # Dodatkowa obsługa dla total: suffix, update field_names, field_name oraz copyFrom
            if part_key=='total' and after:
                for fld in comp['components']:
                    # Aktualizacja validators
                    for v in fld.get('validators',[]):
                        kw=v.get('kwargs',{})
                        if 'field_names' in kw:
                            kw['field_names']=[f+after for f in kw['field_names']]
                        if 'field_name' in kw:
                            kw['field_name']=kw['field_name']+after
                    # Aktualizacja calculationRules fields
                    for cr in fld.get('calculationRules',[]):
                        if 'fields' in cr.get('kwargs',{}):
                            cr['kwargs']['fields']=[f+after for f in cr['kwargs']['fields']]
                    # Aktualizacja copyFrom
                    if 'copyFrom' in fld and fld['copyFrom']:
                        fld['copyFrom'] = fld['copyFrom'] + after

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
