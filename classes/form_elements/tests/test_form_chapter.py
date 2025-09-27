import pytest
from classes.form_elements import FormChapter


def test_generate_basic_chapter_without_multiple_forms():
    chapter = FormChapter(
        title="Basic Chapter",
        components=[{"kind": "component", "name": "field1"}],
    )
    generated = chapter.generate()

    assert generated["kind"] == "chapter"
    assert generated["title"] == "Basic Chapter"
    assert generated["components"] == [{"kind": "component", "name": "field1"}]
    assert "isMultipleForms" not in generated


def test_generate_with_multiple_forms_min_count_creates_duplicates():
    start_chapter = {"kind": "chapter", "title": "Start", "components": [
        {"kind": "component", "name": "field1", "value": "X"}
    ]}

    chapter = FormChapter(
        title="Has Multiple",
        components=[start_chapter],
        multiple_forms_rules={"minCount": 3, "maxCount": 10}
    )
    generated = chapter.generate()

    assert generated["isMultipleForms"] is True
    assert generated["isPaginated"] is True
    assert len(generated["components"]) == 3
    assert generated["components"][0]["components"][0]["name"] == "field1_1"
    assert generated["components"][1]["components"][0]["name"] == "field1_2"
    assert generated["components"][2]["components"][0]["name"] == "field1_3"
    assert generated["components"][0]["components"][0]["defaultValue"] == "X"


def test_generate_with_multiple_forms_but_no_components_raises_error():
    chapter = FormChapter(
        title="Broken",
        components=[],
        multiple_forms_rules={"minCount": 2}
    )

    with pytest.raises(ValueError) as exc:
        chapter.generate()

    assert "Chapter z multipleForms powinien posiadać przynajmniej jeden chapter" in str(exc.value)


def test_duplicate_chapter_with_indexing_standalone():
    start_chapter = {
        "kind": "chapter",
        "title": "Pozycja",
        "components": [
            {"kind": "component", "name": "f1"},
            {"kind": "chapter", "components": [
                {"kind": "component", "name": "nested"}
            ]}
        ]
    }

    result = FormChapter.duplicate_chapter_with_indexing(start_chapter, 2)

    assert len(result) == 2
    assert result[0]["title"] == "Pozycja 1"
    assert result[1]["title"] == "Pozycja 2"
    assert result[0]["components"][0]["name"] == "f1_1"
    assert result[1]["components"][0]["name"] == "f1_2"
    assert result[0]["components"][1]["components"][0]["name"] == "nested_1"
