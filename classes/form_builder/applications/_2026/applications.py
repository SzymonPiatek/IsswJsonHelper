from classes.form_builder.applications.applications import Applications
from classes.form_builder.dwm._2026 import *


class Applications2026(Applications):
    def __init__(self):
        super().__init__()

        self.builder_map = {
            "dwm": {
                "po5": {
                    "pr1": PromotionApplicationBuilder,
                    "pr2": ForeignScholarshipApplicationBuilder,
                }
            }
        }
