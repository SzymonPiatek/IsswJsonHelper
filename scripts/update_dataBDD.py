from pathlib import Path
import json

def update_databdd_in_file(path: Path):
    with path.open('r', encoding='utf-8') as f:
        data = json.load(f)
    changed = False

    def traverse(obj):
        nonlocal changed
        if isinstance(obj, dict):
            if obj.get("kind") == "component":
                name = obj.get("name")
                if name and obj.get("dataBDD") != name:
                    obj["dataBDD"] = name
                    changed = True
            for value in obj.values():
                traverse(value)
        elif isinstance(obj, list):
            for item in obj:
                traverse(item)

    traverse(data)

    if changed:
        with path.open('w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Updated {path}")
    else:
        print(f"No changes in {path}")

def main():
    data_dir = Path('data')
    for json_file in data_dir.rglob('*.json'):
        update_databdd_in_file(json_file)

if __name__ == "__main__":
    main()
