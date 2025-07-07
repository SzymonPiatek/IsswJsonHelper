import json

class KosztorysGenerator:
    """
    Klasa odpowiedzialna za generowanie kosztorysu na podstawie definicji parts i structure.
    """
    def __init__(self, parts: dict, structure: dict, output_path: str):
        self.parts = parts
        self.structure = structure
        self.output_path = output_path
        self.loaded_parts = {}
        self.result = None

    def load_parts(self) -> None:
        """
        Wczytuje wszystkie pliki części kosztorysu do pamięci.
        """
        for key, path in self.parts.items():
            with open(path, 'r', encoding='utf-8') as f:
                self.loaded_parts[key] = json.load(f)

    def build_component(self, node: dict) -> dict:
        """
        Rekurencyjnie buduje fragment kosztorysu zgodnie z definicją node.
        """
        part_key = node['part']
        template = self.loaded_parts.get(part_key)
        if template is None:
            raise ValueError(f"Nie znaleziono części '{part_key}'.")
        # Deep copy szablonu, aby nie modyfikować oryginału
        comp = json.loads(json.dumps(template))
        # Ustaw dodatkowe atrybuty, jeśli są zdefiniowane
        if 'title' in node:
            comp['title'] = node['title']
        if 'baseName' in node:
            comp['baseName'] = node['baseName']
        # Przetwarzaj podkomponenty, jeśli istnieją
        if 'components' in node:
            comp['components'] = []
            for child in node['components']:
                comp_child = self.build_component(child)
                comp['components'].append(comp_child)
        return comp

    def generate(self) -> None:
        """
        Generuje pełny kosztorys zgodnie z zadaną strukturą.
        """
        self.load_parts()
        self.result = self.build_component(self.structure)

    def save_output(self) -> None:
        """
        Zapisuje wygenerowany kosztorys do pliku JSON.
        """
        if self.result is None:
            raise ValueError("Brak wygenerowanego kosztorysu. Najpierw wywołaj generate().")
        with open(self.output_path, 'w', encoding='utf-8') as f:
            json.dump(self.result, f, ensure_ascii=False, indent=2)
