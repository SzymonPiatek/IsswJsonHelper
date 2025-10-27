# DUK - Development
from classes_new.forms._2026.duk.development.modernization.application_builder import \
    ModernizationPriorityApplicationFormBuilder
from classes_new.forms._2026.duk.development.digitalization.application_builder import \
    DigitalizationPriorityApplicationFormBuilder
# DUK - Dissemination
from classes_new.forms._2026.duk.dissemination.dkf.application_builder import DkfPriorityApplicationFormBuilder
from classes_new.forms._2026.duk.dissemination.festivals.application_builder import \
    FestivalsPriorityApplicationFormBuilder
from classes_new.forms._2026.duk.dissemination.initiatives.application_builder import \
    InitiativesPriorityApplicationFormBuilder
from classes_new.forms._2026.duk.dissemination.literature.application_builder import \
    LiteraturePriorityApplicationFormBuilder
from classes_new.forms._2026.duk.dissemination.reconstruction.application_builder import \
    ReconstructionPriorityApplicationFormBuilder
from classes_new.forms._2026.duk.dissemination.research.application_builder import \
    ResearchPriorityApplicationFormBuilder
# DUK - Education
from classes_new.forms._2026.duk.education.audience.application_builder import AudiencePriorityApplicationFormBuilder
from classes_new.forms._2026.duk.education.higher_schools.application_builder import HigherSchoolsPriorityApplicationFormBuilder
from classes_new.forms._2026.duk.education.professional_training.application_builder import \
    ProfessionalTrainingPriorityApplicationFormBuilder
from classes_new.forms._2026.duk.education.secondary_schools.application_builder import \
    SecondarySchoolsPriorityApplicationFormBuilder
# DWM - Promotion
from classes_new.forms._2026.dwm.promotion.promotion.application_builder import PromotionPriorityApplicationFormBuilder
from classes_new.forms._2026.dwm.promotion.promotion.report_builder import PromotionPriorityReportFormBuilder
from classes_new.forms._2026.dwm.promotion.foreign_scholarships.application_builder import ForeignPriorityApplicationFormBuilder
from classes_new.forms._2026.dwm.promotion.foreign_scholarships.report_builder import ForeignScholarshipsPriorityReportFormBuilder
# DPF - Production
from classes_new.forms._2026.dpf.production.screenplay_scholarship.application_builder import ScreenplayScholarshipPriorityApplicationFormBuilder
# Other
from classes_new.forms.forms import Forms


class Forms2026(Forms):
    def __init__(self):
        super().__init__()

        self.builder_map = {
            "application": {
                "dpf": {
                    "po1": {
                        "pr1": ScreenplayScholarshipPriorityApplicationFormBuilder,
                        "pr2": None,
                        "pr3": None,
                        "pr4": None,
                        "pr5": None,
                        "pr6": None,
                        "pr7": None
                    }
                },
                "duk": {
                    "po2": {
                        "pr1": HigherSchoolsPriorityApplicationFormBuilder,
                        "pr2": SecondarySchoolsPriorityApplicationFormBuilder,
                        "pr3": ProfessionalTrainingPriorityApplicationFormBuilder,
                        "pr4": AudiencePriorityApplicationFormBuilder
                    },
                    "po3": {
                        "pr1": FestivalsPriorityApplicationFormBuilder,
                        "pr2": InitiativesPriorityApplicationFormBuilder,
                        "pr3": LiteraturePriorityApplicationFormBuilder,
                        "pr4": ReconstructionPriorityApplicationFormBuilder,
                        "pr5": ResearchPriorityApplicationFormBuilder,
                        "pr6": DkfPriorityApplicationFormBuilder
                    },
                    "po4": {
                        "pr1": ModernizationPriorityApplicationFormBuilder,
                        "pr2": DigitalizationPriorityApplicationFormBuilder,
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
