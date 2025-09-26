from typing import Literal

from ..additional.rules.decorators import not_implemented_func
from ..additional.rules.validator import Validator
from ..additional.rules.visibility_rule import VisibilityRule
from ..additional.rules.calculation_rule import CalculationRule


class FormElement:
    def __init__(self, kind: Literal["form", "part", "chapter", "component"]):
        self.kind = kind

        self.names = set()

        self.validator = Validator()
        self.visibility_rule = VisibilityRule()
        self.calculation_rule = CalculationRule()

    @not_implemented_func
    def generate(self):
        pass
