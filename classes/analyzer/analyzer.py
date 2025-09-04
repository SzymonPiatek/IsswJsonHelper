import json
from pathlib import Path
from collections import defaultdict
import os


class Analyzer:
    @staticmethod
    def find_json_files(base_dir: str) -> list[Path]:
        base_path = Path(base_dir)
        return list(base_path.rglob("*.json"))

    @staticmethod
    def analyze_duplicates(json_files: list[Path]) -> dict:
        name_occurrences = defaultdict(list)

        def walk_components(components, file_path, part_idx=None, chapter_idx=None, path=None):
            if path is None:
                path = []
            for idx, component in enumerate(components):
                current_path = path + [f"component[{idx}]"]
                if component.get("kind") == "component":
                    name = component.get("name")
                    if name:
                        name_occurrences[name].append({
                            "file": str(file_path),
                            "path": current_path
                        })
                if "components" in component:
                    walk_components(component["components"], file_path, part_idx, chapter_idx, current_path)
                if "chapters" in component:
                    for chap_idx, chapter in enumerate(component["chapters"]):
                        chapter_path = current_path + [f"chapter[{chap_idx}]"]
                        inner_components = chapter.get("components", [])
                        walk_components(inner_components, file_path, part_idx, chap_idx, chapter_path)

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
                    path = [f"part[{part_idx}]", f"chapter[{chap_idx}]"]
                    components = chapter.get("components", [])
                    walk_components(components, file_path, part_idx, chap_idx, path)

        return {
            name: locations
            for name, locations in name_occurrences.items()
            if len(locations) > 1
        }

    @staticmethod
    def report_duplicates(base_dir: str, output_path: str):
        files = Analyzer.find_json_files(base_dir)
        duplicates = Analyzer.analyze_duplicates(files)

        os.makedirs(output_path, exist_ok=True)

        output_data = {}

        file_name = f"{output_path}/duplicates_report.json"
        if os.path.exists(file_name):
            with open(file_name, "r", encoding="utf-8") as f:
                existing_data = json.load(f)
        else:
            existing_data = {}

        ignored_names = set(existing_data.get("__ignored_names__", []))

        for name, occurrences in duplicates.items():
            if name in ignored_names:
                continue
            existing_entry = existing_data.get(name, {})
            was_checked = False
            if isinstance(existing_entry, dict):
                was_checked = existing_entry.get("isChecked", False)
            if was_checked:
                ignored_names.add(name)
                continue
            files = sorted({occ["file"] for occ in occurrences})
            output_data[name] = {
                "isChecked": was_checked,
                "filesCount": len(files),
                "files": files
            }

        total_duplicates = len(output_data)
        total_checked = sum(1 for entry in output_data.values()
                            if isinstance(entry, dict) and entry.get("isChecked"))
        total_unchecked = sum(1 for entry in output_data.values()
                              if isinstance(entry, dict) and not entry.get("isChecked"))

        summary = {"total_duplicates": total_duplicates, "total_checked": total_checked,
                   "total_unchecked": total_unchecked}
        output_data = {
            "__summary__": summary,
            "__ignored_names__": sorted(ignored_names),
            **output_data
        }

        file_name = f"{output_path}/duplicates_report.json"
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)

        print(f"📄 Raport JSON zapisany do: {file_name}")
