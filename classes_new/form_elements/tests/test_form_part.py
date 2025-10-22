import pytest
from classes.form_elements import FormPart


def test_create_with_minimal_args():
    part = FormPart(title="Test Title")

    assert part.title == "Test Title"
    assert part.short_name == "Test Title"
    assert part.class_list == ["full-width-grid"]
    assert part.chapters == []



def test_create_with_custom_values():
    chapters = [{"kind": "chapter", "title": "Chapter 1"}]

    part = FormPart(
        title="Custom Title",
        short_name="Short",
        class_list=["custom-class"],
        chapters=chapters,
    )

    assert part.title == "Custom Title"
    assert part.short_name == "Short"
    assert part.class_list == ["custom-class"]
    assert part.chapters == chapters


def test_missing_title_raises_error():
    with pytest.raises(ValueError) as exc:
        FormPart(title=None)

    assert "title musi być podane" in str(exc.value)


def test_generate_returns_correct_dict():
    chapters = [{"kind": "chapter", "title": "Chapter 1"}]
    part = FormPart(title="Form Part", short_name="FP", class_list=["grid"], chapters=chapters)

    generated = part.generate()

    assert generated == {
        "kind": "part",
        "title": "Form Part",
        "shortName": "FP",
        "classList": ["grid"],
        "chapters": chapters,
    }
