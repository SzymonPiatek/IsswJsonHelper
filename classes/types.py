from typing import Literal, TypedDict, Optional

JSONType = Literal['application', 'report']
SessionType = Literal['I', 'II', 'III', 'IV']
DepartmentType = Literal['DPF', 'DUK', 'DWM', 'ZACHĘTY']
YearType = Literal[2025, 2026]

COMPONENT_TYPE_VALUES = (
    "date", "file", "radio", "header", "checkbox",
    "number", "select", "country", "countryMulti",
    "currency", "text", "textarea",
)
ComponentType = Literal[*COMPONENT_TYPE_VALUES]
COMPONENT_TYPES = set(COMPONENT_TYPE_VALUES)

MASK_TYPE_VALUES = (
    "fund", "phoneNumber", "bankAccount", "landline",
    "jst", "ibanAccount", "polishPostalCode", "share"
)
MaskType = Literal[*MASK_TYPE_VALUES]
MASK_TYPES = set(MASK_TYPE_VALUES)

VALUE_TYPE_VALUES = (str, int, float, bool, list[str])
ValueType = Literal[*VALUE_TYPE_VALUES]


class ClassListDictType(TypedDict):
    main: list[str]
    sub: list[str]


ClassListType = Literal[list[str], ClassListDictType]


class MultipleFormsRulesType(TypedDict):
    minCount: Optional[int]
    maxCount: Optional[int]
