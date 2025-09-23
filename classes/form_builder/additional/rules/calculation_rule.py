from typing import TypedDict, Optional, List


class CalculationRule:
    def __init__(self):
        self.names = [
            "copyValue",
            "relateToLastDate",
            "localSum",
            "sumInputs",
            "dynamicSumInputs",
            "localShareCalculator",
            "shareCalculator",
            "singlePositionShareCalculator",
            "firstDate",
            "lastDate",
            "conditionalCopyValue",
            "copyCompanyData",
            "multiplyInputs"
        ]

    @staticmethod
    def copy_value(from_name: str):
        return {
            "name": "copyValue",
            "from": from_name
        }

    @staticmethod
    def relate_to_last_date(field: str, parameter: int):
        return {
            "name": "relateToLastDate",
            "kwargs": {
                "field": field,
                "parameter": parameter
            }
        }

    @staticmethod
    def local_sum(fields: List[str]):
        return {
            "name": "localSum",
            "kwargs": {
                "fields": fields
            }
        }

    @staticmethod
    def sum_inputs(fields: List[str]):
        return {
            "name": "sumInputs",
            "kwargs": {
                "fields": fields
            }
        }

    @staticmethod
    def dynamic_sum_inputs(fields: List[str]):
        return {
            "name": "dynamicSumInputs",
            "kwargs": {
                "fields": fields
            }
        }

    @staticmethod
    def local_share_calculator(dividend_field: str, divisor_field: str):
        return {
            "name": "localShareCalculator",
            "kwargs": {
                "dividendField": dividend_field,
                "divisorField": divisor_field
            }
        }

    @staticmethod
    def share_calculator(dividend_field: str, divisor_field: str):
        return {
            "name": "shareCalculator",
            "kwargs": {
                "dividendField": dividend_field,
                "divisorField": divisor_field
            }
        }

    @staticmethod
    def single_position_share_calculator(dividend_field: str, divisor_field: str):
        return {
            "name": "singlePositionShareCalculator",
            "kwargs": {
                "dividendField": dividend_field,
                "divisorField": divisor_field
            }
        }

    @staticmethod
    def first_date(field: str):
        return {
            "name": "firstDate",
            "kwargs": {
                "field": field
            }
        }

    @staticmethod
    def last_date(field: str):
        return {
            "name": "lastDate",
            "kwargs": {
                "field": field
            }
        }

    class ConditionalCopyValueCondition(TypedDict, total=False):
        fieldName: Optional[str]
        fieldNameLocal: Optional[str]
        maxRatio: Optional[float]
        minRatio: Optional[float]
        equalNumber: Optional[bool]
        equalString: Optional[bool]
        containValues: Optional[List[str]]

    @staticmethod
    def conditional_copy_value(
        field_name: Optional[str] = None,
        field_name_local: Optional[str] = None,
        condition: Optional[ConditionalCopyValueCondition] = None,
        correct_field_name: Optional[str] = None,
        correct_field_name_local: Optional[str] = None,
        incorrect_field_name: Optional[str] = None,
        incorrect_field_name_local: Optional[str] = None,
    ):
        kwargs = {}

        if field_name:
            kwargs["fieldName"] = field_name
        elif field_name_local:
            kwargs["fieldNameLocal"] = field_name_local

        if condition:
            kwargs["condition"] = condition

        if correct_field_name:
            kwargs["correctFieldName"] = correct_field_name
        elif correct_field_name_local:
            kwargs["correctFieldNameLocal"] = correct_field_name_local

        if incorrect_field_name:
            kwargs["incorrectFieldName"] = incorrect_field_name
        elif incorrect_field_name_local:
            kwargs["incorrectFieldNameLocal"] = incorrect_field_name_local

        return {
            "name": "conditionalCopyValue",
            "kwargs": kwargs
        }

    @staticmethod
    def copy_company_data(
        field: str,
        force: Optional[bool] = False,
    ):
        kwargs = {
            "field": field,
        }
        if force:
            kwargs["force"] = True

        return {
            "name": "copyCompanyData",
            "kwargs": kwargs
        }

    @staticmethod
    def assign_value(options: dict):
        return {
            "name": "assignValue",
            "kwargs": {
                "options": options
            }
        }

    @staticmethod
    def multiply_inputs(
        fields: List[str],
    ):
        return {
            "name": "multiplyInputs",
            "kwargs": {
                "fields": fields
            }
        }
