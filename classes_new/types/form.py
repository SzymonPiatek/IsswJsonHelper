from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Literal, TypedDict


COMPONENT_TYPE_VALUES = (
    "date", "file", "radio", "header", "checkbox",
    "number", "select", "country", "countryMulti",
    "currency", "text", "textarea",
)
ComponentType = Literal[*COMPONENT_TYPE_VALUES]
COMPONENT_TYPES = set(COMPONENT_TYPE_VALUES)


MASK_TYPE_VALUES = (
    "fund", "phoneNumber", "bankAccount", "landline",
    "jst", "ibanAccount", "polishPostalCode"
)
MaskType = Literal[*MASK_TYPE_VALUES]
MASK_TYPES = set(MASK_TYPE_VALUES)


VALUE_TYPE_VALUES = (str, int, float, bool, list[str])
ValueType = Literal[*VALUE_TYPE_VALUES]


FormKind = Literal['form']
PartKind = Literal['part']
ChapterKind = Literal['chapter']
ComponentKind = Literal['component']


class ClassListDictType(TypedDict):
    main: list[str]
    sub: list[str]


ClassListType = Literal[list[str], ClassListDictType]


class MultipleFormsRulesType(TypedDict):
    minCount: Optional[int]
    maxCount: Optional[int]


@dataclass
class Component:
    type: ComponentType
    mask: Optional[MaskType]
    label: str
    name: str
    dataBDD: str
    value: ValueType
    defaultValue: Optional[ValueType]
    unit: Optional[str]
    options: Optional[list[str]]
    validators: Optional[list[dict]]
    calculationRules: Optional[list[dict]]
    classList: Optional[ClassListType]
    required: Optional[bool]
    readOnly: Optional[bool]
    helpText: Optional[str]
    copyFrom: Optional[str]
    placeholder: Optional[str]
    kind: ComponentKind = 'component'


@dataclass
class Chapter:
    title: str
    helpText: Optional[str]
    classList: Optional[ClassListType]
    visibilityRules: Optional[list[dict]]
    multipleFormsRules: Optional[MultipleFormsRulesType]
    isMultipleForms: Optional[bool]
    isPaginated: Optional[bool]
    components: list[Chapter | Component] = field(default_factory=list)
    kind: ChapterKind = 'chapter'


@dataclass
class Part:
    title: str
    shortName: str
    classList: Optional[ClassListType]
    chapters: list[Chapter] = field(default_factory=list)
    kind: PartKind = 'part'


@dataclass
class Form:
    kind: FormKind = 'form',
    jrwa: str = '',
    expert: dict = {
        "name": "",
        "email": "",
        "avatar": ""
    },
    status: str = ''
    applicant: dict = field(default_factory=dict)
    title: str = ""
    introText: list[dict] = field(default_factory=list)
    blanks: list = field(default_factory=list)
    parts: list[Part] = field(default_factory=list)
