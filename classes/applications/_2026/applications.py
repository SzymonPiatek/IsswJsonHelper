from classes.applications.applications import Applications
from classes.form_builder.departments.test.application_builder import TestApplicationBuilder


class Applications2026(Applications):
    def __init__(self):
        super().__init__()

        self.builder_map = {
            "application": {
                "test": {
                    "po6": {
                        "pr1": TestApplicationBuilder,
                    }
                }
            },
            "report": {}
        }
