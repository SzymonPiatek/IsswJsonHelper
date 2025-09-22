from classes.form_builder.applications.applications import Applications
from classes.form_builder.dpf import *
from classes.form_builder.duk.education import *
from classes.form_builder.duk.dissemination import *
from classes.form_builder.duk.development import *
from classes.form_builder.dwm._2025 import *


class Applications2025(Applications):
    def __init__(self):
        super().__init__()

        self.builder_map = {
            "application": {
                "dpf": {
                    "po1": {
                        "pr1": ScreenplayScholarshipApplicationBuilder,
                        "pr2": FilmProjectDevelopmentApplicationBuilder,
                        "pr3": FeatureFilmApplicationBuilder,
                        "pr4": DocumentaryFilmApplicationBuilder,
                        "pr5": AnimatedFilmApplicationBuilder,
                        "pr6": CoproductionFilmApplicationBuilder,
                        "pr7": FamilyFilmApplicationBuilder,
                    },
                },
                "duk": {
                    "po2": {
                        "pr1": PostgraduateSchoolsApplicationBuilder,
                        "pr2": SecondarySchoolsApplicationBuilder,
                        "pr3": ProfessionalTrainingApplicationBuilder,
                        "pr4": CinemasApplicationBuilder,
                    },
                    "po3": {
                        "pr1": FestivalsApplicationBuilder,
                        "pr2": InitiativesApplicationBuilder,
                        "pr3": LiteratueApplicationBuilder,
                        "pr4": ReconstructionApplicationBuilder,
                        "pr5": ResearchApplicationBuilder,
                        "pr6": DocumentaryDistributionApplicationBuilder,
                    },
                    "po4": {
                        "pr1": ModernizationApplicationBuilder,
                        "pr2": DigitalizationApplicationBuilder,
                    }
                },
                "dwm": {
                    "po5": {
                        "pr1": PromotionApplicationBuilder,
                        "pr2": ForeignScholarshipApplicationBuilder,
                    }
                }
            },
            "report": {}
        }
