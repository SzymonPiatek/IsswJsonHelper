class VisibilityRule:
    def __init__(self):
        self.names = [
            "dependsOnValue"
        ]

    @staticmethod
    def depends_on_value(field_name: str, values: list):
        return {
            "name": "dependsOnValue",
            "kwargs": {
                "fieldName": field_name,
                "values": values
            }
        }
