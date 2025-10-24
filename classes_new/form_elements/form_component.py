from .form_element import FormElement
from classes_new.types import *


class FormComponent(FormElement):
    def __init__(
            self,
            component_type: ComponentType,
            mask: MaskType = '',
            label: str = '',
            name: str = '',
            value: ValueType = None,
            default_value: ValueType = None,
            unit: str = None,
            options: list = None,
            validators: list[dict] = None,
            calculation_rules: list[dict] = None,
            class_list: ClassListType = None,
            required: bool = False,
            read_only: bool = False,
            help_text: str = None,
            copy_from: str = None,
            names: list[str] = None,
            placeholder: str = None,
    ):
        super().__init__(kind="component")

        self.component_type = component_type
        self.mask = mask
        self.label = label
        self.name = name
        self.value = value
        self.default_value = default_value
        self.unit = unit
        self.options = options
        self.validators = validators
        self.calculation_rules = calculation_rules
        self.class_list = class_list
        self.required = required
        self.read_only = read_only
        self.help_text = help_text
        self.copy_from = copy_from
        self.placeholder = placeholder

        self.names = names

    def _validate_basic(self):
        # Check type
        if self.component_type not in COMPONENT_TYPES:
            raise ValueError(f"Invalid component_type: '{self.component_type}'")

        # Check mask
        if self.mask and self.mask not in MASK_TYPES:
            raise ValueError(f"Invalid mask: '{self.mask}'")

        # Check name
        if not self.name:
            raise ValueError("Component 'name' must be provided and non-empty.")

        # Header component
        if self.component_type == "header" and not self.name.startswith("headerComponent"):
            self.name = f"headerComponent-{self.name}"

        # Save and check name
        if self.name in self.names:
            raise ValueError(f"Duplicate component name detected: {self.name}")
        self.names.add(self.name)

        # Check value
        if self.value is not None and not isinstance(self.value, VALUE_TYPE_VALUES):
            raise ValueError(f"Invalid value type: '{self.value}'")

        # Check default_value
        if self.default_value is not None and not isinstance(self.default_value, VALUE_TYPE_VALUES):
            raise ValueError(f"Invalid default_value type: '{self.default_value}'")

        self.validators = self.validators or []
        self.calculation_rules = self.calculation_rules or []
        self.class_list = self.class_list or []

    def _process_value(self):
        if self.value is None:
            match self.component_type:
                case "date" | "checkbox":
                    self.value = False
                case "file" | "radio" | "header" | "select" | "country" | "countryMulti" | "currency" | "textarea":
                    self.value = ''
                case "number":
                    self.value = 0
                case "text":
                    if self.mask == "fund":
                        self.value = 0
                    else:
                        self.value = ''
                case _:
                    self.value = ''

    def _process_select_radio(self):
        if self.component_type in {"select", "radio"}:
            if not self.options:
                raise ValueError("Component 'options' must be provided for select/radio.")

            if not any(v.get("name") == "ExactValidator" for v in self.validators):
                self.validators.append(self.validator.exact_validator(values=self.options))

            if len(self.options) == 1:
                self.read_only = True
                self.value = self.options[0]

    def _process_file(self):
        if self.component_type == "file":

            message = "Maksymalny rozmiar pliku to 50 MB"
            if not self.help_text:
                self.help_text = message
            elif message not in self.help_text:
                self.help_text += f" {message}"

    def _process_number_fund(self):
        if self.mask == "fund" or self.component_type == "number":
            if not any(v.get("name") == "RangeValidator" for v in self.validators):
                self.validators.append(
                    self.validator.range_validator(
                        min_value=0
                    )
                )
        elif self.mask == "phoneNumber":
            if not any(v.get("name") == "PhoneNumberValidator" for v in self.validators):
                self.validators.append(self.validator.phone_number_validator())

    def _process_required(self):
        if self.required and not any(v.get("name") in {"RelatedRequiredIfEqualValidator", "RequiredValidator", "ExactValidator"} for v in self.validators):
            self.validators.append(self.validator.required_validator())

    def generate(self) -> Component:
        self._validate_basic()
        self._process_value()
        self._process_select_radio()
        self._process_file()
        self._process_number_fund()
        self._process_required()

        if self.value is None:
            raise ValueError("Value nie może być nullem")

        kwargs = {
            "kind": self.kind,
            "type": self.component_type,
            "label": self.label,
            "name": self.name,
            "dataBDD": self.name,
            "value": self.value
        }

        if self.default_value:
            kwargs["defaultValue"] = self.default_value
        if self.mask:
            kwargs["mask"] = self.mask
        if self.unit:
            kwargs["unit"] = self.unit
        if self.placeholder is not None:
            kwargs["placeholder"] = self.placeholder
        if self.options:
            kwargs["options"] = self.options
        if self.required:
            kwargs["required"] = self.required
        if self.read_only:
            kwargs["readOnly"] = self.read_only
        if self.help_text:
            kwargs["helpText"] = self.help_text
        if self.validators:
            kwargs["validators"] = self.validators
        if self.calculation_rules:
            kwargs["calculationRules"] = self.calculation_rules
        if self.class_list:
            kwargs["classList"] = self.class_list
        if self.copy_from:
            kwargs["copyFrom"] = self.copy_from

        return kwargs
