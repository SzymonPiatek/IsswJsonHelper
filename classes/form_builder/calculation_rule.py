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
