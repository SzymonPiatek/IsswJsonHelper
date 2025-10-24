import pytest
from classes.form_elements import FormComponent


@pytest.fixture
def names_registry():
    return set()


def test_basic_component_generation(names_registry):
    comp = FormComponent(
        component_type="text",
        label="Label",
        name="field1",
        value="hello",
        names=names_registry
    )
    result = comp.generate()

    assert result == {
        "kind": "component",
        "type": "text",
        "label": "Label",
        "name": "field1",
        "dataBDD": "field1",
        "value": "hello"
    }


def test_invalid_component_type_raises(names_registry):
    comp = FormComponent(
        component_type="invalid",
        name="bad",
        names=names_registry
    )
    with pytest.raises(ValueError) as exc:
        comp.generate()
    assert "Invalid component_type" in str(exc.value)


def test_invalid_mask_raises(names_registry):
    comp = FormComponent(
        component_type="text",
        mask="wrongMask",
        name="x",
        names=names_registry
    )
    with pytest.raises(ValueError) as exc:
        comp.generate()
    assert "Invalid mask" in str(exc.value)


def test_missing_name_raises(names_registry):
    comp = FormComponent(
        component_type="text",
        name="",
        names=names_registry
    )
    with pytest.raises(ValueError):
        comp.generate()


def test_duplicate_name_raises(names_registry):
    names_registry.add("dup")
    comp = FormComponent(
        component_type="text",
        name="dup",
        names=names_registry
    )
    with pytest.raises(ValueError):
        comp.generate()


def test_header_component_name_auto_prefixed(names_registry):
    comp = FormComponent(
        component_type="header",
        name="myHeader",
        names=names_registry
    )
    result = comp.generate()
    assert result["name"].startswith("headerComponent-")


def test_select_component_requires_options(names_registry):
    comp = FormComponent(
        component_type="select",
        name="sel1",
        options=None,
        names=names_registry
    )
    with pytest.raises(ValueError):
        comp.generate()


def test_select_component_with_single_option_sets_readonly_and_value(names_registry):
    comp = FormComponent(
        component_type="select",
        name="sel2",
        options=["only-one"],
        names=names_registry
    )
    result = comp.generate()
    assert result["readOnly"] is True
    assert result["value"] == "only-one"


def test_file_component_sets_help_text(names_registry):
    comp = FormComponent(
        component_type="file",
        name="file1",
        names=names_registry
    )
    result = comp.generate()
    assert "Maksymalny rozmiar pliku to 50 MB" in result["helpText"]


def test_date_component_sets_value_false(names_registry):
    comp = FormComponent(
        component_type="date",
        name="d1",
        names=names_registry
    )
    result = comp.generate()
    assert result["value"] is False


def test_fund_mask_adds_range_validator(names_registry):
    comp = FormComponent(
        component_type="text",
        mask="fund",
        name="fund1",
        value="not-valid",
        names=names_registry
    )
    result = comp.generate()
    validators = result.get("validators", [])
    assert any(v["name"] == "RangeValidator" for v in validators)


def test_required_component_adds_validator(names_registry):
    comp = FormComponent(
        component_type="text",
        name="req1",
        required=True,
        names=names_registry
    )
    result = comp.generate()
    validators = result.get("validators", [])
    assert any(v["name"] == "RequiredValidator" for v in validators)
