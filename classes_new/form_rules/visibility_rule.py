class VisibilityRule:
    def __init__(self):
        pass

    @staticmethod
    def depends_on_value(field_name: str, values: list):
        return {
            "name": "dependsOnValue",
            "kwargs": {
                "fieldName": field_name,
                "values": values
            }
        }

    @staticmethod
    def local_equals_value(field_name: str, values: list):
        return {
            "name": "localEqualsValue",
            "kwargs": {
                "fieldName": field_name,
                "values": values
            }
        }
