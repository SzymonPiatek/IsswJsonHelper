import json
from pathlib import Path
from collections import defaultdict


class Analyzer:
    @staticmethod
    def find_json_files(base_dir: str) -> list[Path]:
        base_path = Path(base_dir)
        return list(base_path.rglob("*.json"))

    @staticmethod
    def analyze_duplicates(json_files: list[Path]) -> dict:
        name_occurrences = defaultdict(list)

        for file_path in json_files:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception as e:
                print(f"[Błąd] Nie udało się wczytać {file_path}: {e}")
                continue

            parts = data.get("parts", [])
            for part_idx, part in enumerate(parts):
                chapters = part.get("chapters", [])
                for chap_idx, chapter in enumerate(chapters):
                    components = chapter.get("components", [])
                    for comp_idx, component in enumerate(components):
                        if component.get("kind") == "component":
                            name = component.get("name")
                            if name:
                                name_occurrences[name].append({
                                    "file": str(file_path),
                                    "part_index": part_idx,
                                    "chapter_index": chap_idx,
                                    "component_index": comp_idx
                                })

        return {
            name: locations
            for name, locations in name_occurrences.items()
            if len(locations) > 1
        }

    @staticmethod
    def report_duplicates(base_dir: str):
        files = Analyzer.find_json_files(base_dir)
        duplicates = Analyzer.analyze_duplicates(files)

        if not duplicates:
            print("✅ Brak duplikatów komponentów.")
            return

        print("╔══════════════════════════════════════════════════════╗")
        print("║      ⚠️  Znaleziono duplikaty komponentów (name)     ║")
        print("╚══════════════════════════════════════════════════════╝\n")

        for name, occurrences in duplicates.items():
            print(f"📛 Name: {name}")
            for occ in occurrences:
                print(f"   ├─ Plik: {occ['file']}")
                location = f"part[{occ['part_index']}], chapter[{occ['chapter_index']}], component[{occ['component_index']}]"
                print(f"   └─ Lokalizacja: {location}")
            print("─" * 60)

        print(f"\n🔍 Łącznie zduplikowanych nazw: {len(duplicates)}")


if __name__ == "__main__":
    Analyzer.report_duplicates("./output/json")
