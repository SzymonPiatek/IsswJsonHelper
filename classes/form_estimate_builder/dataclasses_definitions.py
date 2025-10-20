from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any


@dataclass
class CostOverride:
    validators: List[Any] = field(default_factory=list)
    calculationRules: List[Any] = field(default_factory=list)
    readOnly: bool = False


@dataclass
class CostItem:
    title: str
    name: str
    helpText: Optional[str] = None
    overrides: Dict[str, CostOverride] = field(default_factory=dict)
    isSum: bool = False


@dataclass
class EstimateSection:
    title: str
    costs: List[CostItem]
    helpText: Optional[str] = None
