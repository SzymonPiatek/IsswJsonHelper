from classes_new.forms.forms import Forms
from classes_new.forms._2026.dwm.promotion.promotion.application_builder import PromotionPriorityApplicationFormBuilder
from classes_new.forms._2026.dwm.promotion.promotion.report_builder import PromotionPriorityReportFormBuilder
from classes_new.forms._2026.dwm.promotion.foreign_scholarships.application_builder import ForeignPriorityApplicationFormBuilder
from classes_new.forms._2026.dwm.promotion.foreign_scholarships.report_builder import ForeignScholarshipsPriorityReportFormBuilder


class Forms2026(Forms):
    def __init__(self):
        super().__init__()

        self.builder_map = {
            "application": {
                "dpf": {
                    "po1": {
                        "pr1": None
                    }
                },
                "duk": {
                    "po2": {
                        "pr1": None,
                        "pr2": None,
                        "pr3": None,
                        "pr4": None
                    },
                    "po3": {
                        "pr1": None,
                        "pr2": None,
                        "pr3": None,
                        "pr4": None,
                        "pr5": None,
                        "pr6": None
                    },
                    "po4": {
                        "pr1": None,
                        "pr2": None,
                    }
                },
                "dwm": {
                    "po5": {
                        "pr1": PromotionPriorityApplicationFormBuilder,
                        "pr2": ForeignPriorityApplicationFormBuilder
                    }
                }
            },
            "report": {
                "duk": {
                    "po2": {
                        "pr1": None,
                        "pr2": None,
                        "pr3": None,
                        "pr4": None
                    },
                    "po3": {
                        "pr1": None,
                        "pr2": None,
                        "pr3": None,
                        "pr4": None,
                        "pr5": None,
                        "pr6": None
                    },
                    "po4": {
                        "pr1": None,
                        "pr2": None,
                    }
                },
                "dwm": {
                    "po5": {
                        "pr1": PromotionPriorityReportFormBuilder,
                        "pr2": ForeignScholarshipsPriorityReportFormBuilder
                    }
                }
            }
        }
