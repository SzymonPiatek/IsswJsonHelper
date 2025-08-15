from pathlib import Path
import json


def delete_unused_args_in_file(path: Path):
    try:
        content = path.read_text(encoding='utf-8').strip()
        if not content:
            print(f"Skipped empty or whitespace-only file: {path}")
            return

        data = json.loads(content)
    except json.JSONDecodeError as e:
        print(f"⚠️ Błąd parsowania JSON w pliku {path}: {e}")
        return

    changed = False

    def traverse(obj):
        nonlocal changed
        if isinstance(obj, dict):
            for key, bad_val in (("required", False), ("readOnly", False), ("helpText", ""), ("isMultipleForms", False), ("isPaginated", False), ("unit", "")):
                if obj.get(key) == bad_val:
                    obj.pop(key, None)
                    changed = True

            for drop_key in ['visibilityRules', 'classList', 'validators', 'calculationRules', 'errorMsgs', 'options', 'mask']:
                if not obj.get(drop_key, False):
                    obj.pop(drop_key, None)
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


def main():
    data_dir = Path('data')
    for json_file in data_dir.rglob('*.json'):
        delete_unused_args_in_file(json_file)

    data_dir = Path('output')
    for json_file in data_dir.rglob('*.json'):
        delete_unused_args_in_file(json_file)


if __name__ == "__main__":
    main()
