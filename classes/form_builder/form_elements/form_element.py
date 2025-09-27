from typing import Literal
from abc import ABC, abstractmethod

from ..additional.rules import CalculationRule, Validator, VisibilityRule


class FormElement(ABC):
    def __init__(self, kind: Literal["form", "part", "chapter", "component"]):
        self.kind = kind

        self.validator = Validator()
        self.visibility_rule = VisibilityRule()
        self.calculation_rule = CalculationRule()

    @abstractmethod
    def generate(self):
        pass
