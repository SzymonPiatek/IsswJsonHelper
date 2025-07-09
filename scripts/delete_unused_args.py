from pathlib import Path
import json

def delete_unused_args_in_file(path: Path):
    with path.open('r', encoding='utf-8') as f:
        data = json.load(f)
    changed = False

    def traverse(obj):
        nonlocal changed
        if isinstance(obj, dict):
            kind = obj.get("kind")
            if kind == "chapter" and obj.get("visibilityRules") == []:
                obj.pop("visibilityRules", None)
                changed = True
            if kind == "component":
                for key, bad_val in (("required", False), ("readOnly", False), ("helpText", "")):
                    if obj.get(key) == bad_val:
                        obj.pop(key, None)
                        changed = True
            for v in list(obj.values()):
                traverse(v)
        elif isinstance(obj, list):
            for item in obj:
                traverse(item)

    traverse(data)

    if changed:
        with path.open('w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Cleaned {path}")
    else:
        print(f"No changes in {path}")

def main():
    data_dir = Path('data')
    for json_file in data_dir.rglob('*.json'):
        delete_unused_args_in_file(json_file)

if __name__ == "__main__":
    main()
