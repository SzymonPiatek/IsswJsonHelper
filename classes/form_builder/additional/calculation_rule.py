class CalculationRule:
    def __init__(self):
        pass

    @staticmethod
    def copy_value(from_name: str):
        return {
            "name": "copyValue",
            "from": from_name
        }

    @staticmethod
    def last_date(field: str):
        return {
            "name": "lastDate",
            "kwargs": {
                "field": field
            }
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
    def local_sum(fields: [str]):
        return {
            "name": "localSum",
            "kwargs": {
                "fields": fields
            }
        }

    @staticmethod
    def sum_inputs(fields: [str]):
        return {
            "name": "sumInputs",
            "kwargs": {
                "fields": fields
            }
        }

    @staticmethod
    def dynamic_sum_inputs(fields: [str]):
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
