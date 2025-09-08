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
    def report_duplicates(base_dir: str, output_path: str, file_name: str):
        files = Analyzer.find_json_files(base_dir)

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

        for file_path in files:
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

        duplicates = {
            name: locations
            for name, locations in name_occurrences.items()
            if len(locations) > 1
        }

        os.makedirs(output_path, exist_ok=True)

        output_data = {}

        file_name = f"{output_path}/{file_name}.json"
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
        total_unchecked = sum(1 for entry in output_data.values()
                              if isinstance(entry, dict) and not entry.get("isChecked"))

        summary = {"total_duplicates": total_duplicates,
                   "total_unchecked": total_unchecked}
        output_data = {
            "__summary__": summary,
            "__ignored_names__": sorted(ignored_names),
            **output_data
        }

        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)

        print(f"📄 Raport JSON zapisany do: {file_name}")

    @staticmethod
    def report_missing_validators(base_dir: str, output_path: str, file_name: str):
        files = Analyzer.find_json_files(base_dir)
        results = []

        required_validators = ["RequiredValidator", "RelatedRequiredIfEqualValidator", "ExactValidator"]
        length_validators = ["LengthValidator"]

        def walk_components(components, file_path, path=None):
            if path is None:
                path = []
            for idx, component in enumerate(components):
                current_path = path + [f"component[{idx}]"]
                validators = component.get("validators", [])

                base = {
                    "file": str(file_path),
                    "name": component.get("name"),
                    "type": component.get("type"),
                    "missing": []
                }

                if component.get("required") is True:
                    has_valid_required = any(
                        v.get("name") in required_validators for v in validators
                    )
                    if not has_valid_required:
                        base["missing"].append("Any required validator")
                if component.get("type") == "textarea":
                    has_valid_required = any(
                        v.get("name") in length_validators for v in validators
                    )
                    if not has_valid_required:
                        base["missing"].append("Length validator")

                if "components" in component:
                    walk_components(component["components"], file_path, current_path)
                if "chapters" in component:
                    for chap_idx, chapter in enumerate(component["chapters"]):
                        chapter_path = current_path + [f"chapter[{chap_idx}]"]
                        inner_components = chapter.get("components", [])
                        walk_components(inner_components, file_path, chapter_path)

                if base.get("missing", []):
                    results.append(base)

        for file_path in files:
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
                    walk_components(components, file_path, path)

        os.makedirs(output_path, exist_ok=True)
        full_path = os.path.join(output_path, f"{file_name}.json")

        if os.path.exists(full_path):
            with open(full_path, "r", encoding="utf-8") as f:
                existing_data = json.load(f)
        else:
            existing_data = {}

        ignored_names = set(existing_data.get("__ignored_names__", []))
        output_data = {}

        for item in results:
            name = item.get("name")
            if not name or name in ignored_names:
                continue

            existing_entry = existing_data.get(name, {})
            is_checked = existing_entry.get("isChecked", False) if isinstance(existing_entry, dict) else False

            output_data[name] = {
                "isChecked": is_checked,
                **item
            }

        total = len(output_data)
        total_unchecked = sum(1 for entry in output_data.values() if not entry.get("isChecked"))

        summary = {
            "total_missing_required_validators": total,
            "total_unchecked": total_unchecked
        }

        output_data = {
            "__summary__": summary,
            "__ignored_names__": sorted(ignored_names),
            **output_data
        }

        with open(full_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)

        print(f"📄 Raport brakujących RequiredValidator zapisany do: {full_path}")
