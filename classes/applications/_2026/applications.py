from classes.applications.applications import Applications
from classes.form_builder.departments.dwm._2026 import *
from classes.form_builder.departments.duk._2026.education import *
from classes.form_builder.departments.duk._2026.dissemination import *
from classes.form_builder.departments.duk._2026.development import *
from classes.form_builder.departments.test.application_builder import TestApplicationBuilder


class Applications2026(Applications):
    def __init__(self):
        super().__init__()

        self.builder_map = {
            "application": {
                "duk": {
                    "po2": {
                        "pr1": HigherSchoolsApplicationBuilder,
                        "pr2": SecondarySchoolsApplicationBuilder,
                        "pr3": ProfessionalTrainingApplicationBuilder,
                        "pr4": AudienceApplicationBuilder,
                    },
                    "po3": {
                        "pr1": FestivalsApplicationBuilder,
                        "pr2": InitiativesApplicationBuilder,
                        "pr3": LiteratureApplicationBuilder,
                        "pr4": ReconstructionApplicationBuilder,
                        "pr5": ResearchApplicationBuilder,
                        "pr6": DkfApplicationBuilder,
                    },
                    "po4": {
                        "pr1": ModernizationApplicationBuilder,
                        # "pr2": DigitalizationApplicationBuilder,
                    }
                },
                "dwm": {
                    "po5": {
                        "pr1": PromotionApplicationBuilder,
                        "pr2": ForeignScholarshipApplicationBuilder,
                    }
                },
                "test": {
                    "po6": {
                        "pr1": TestApplicationBuilder,
                    }
                }
            },
            "report": {
                "dwm": {
                    "po5": {
                        "pr1": PromotionReportBuilder,
                        "pr2": ForeignScholarshipReportBuilder,
                    }
                }
            }
        }
