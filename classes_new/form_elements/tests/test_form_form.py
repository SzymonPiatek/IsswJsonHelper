import pytest
from classes.form_elements import FormForm


def test_create_with_valid_intro_text():
    form = FormForm(intro_text=["Witaj", "To jest formularz"])
    assert form.kind == "form"
    assert form.intro_text == ["Witaj", "To jest formularz"]


def test_generate_with_valid_intro_text():
    form = FormForm(intro_text=["Witaj", "Druga linia"])
    generated = form.generate()

    assert generated == {
        "kind": "form",
        "jrwa": "",
        "expert": {
            "name": "",
            "email": "",
            "avatar": ""
        },
        "status": "",
        "applicant": {},
        "title": "",
        "blanks": [],
        "parts": [],
        "introText": [
            {
                "text": "Witaj",
            },
            {
                "text": "Druga linia",
            }
        ]
    }


def test_generate_raises_error_when_intro_text_is_empty():
    form = FormForm(intro_text=[])
    with pytest.raises(ValueError) as exc:
        form.generate()
    assert "Intro_text musi być niepustą listą tekstów" in str(exc.value)


def test_generate_raises_error_when_intro_text_is_not_a_list():
    form = FormForm(intro_text="Nie lista")
    with pytest.raises(ValueError) as exc:
        form.generate()
    assert "Intro_text musi być niepustą listą tekstów" in str(exc.value)
