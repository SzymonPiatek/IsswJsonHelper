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
from classes_new.forms._2026.dpf.production.animated_film_production.application_builder import AnimatedFilmProductionPriorityApplicationFormBuilder
from classes_new.forms._2026.dpf.production.debuts_featured_film_production.application_builder import DebutsFeaturedFilmProductionPriorityApplicationFormBuilder
from classes_new.forms._2026.dpf.production.featured_film_production.application_builder import FeaturedFilmProductionPriorityApplicationFormBuilder
from classes_new.forms._2026.dpf.production.documentary_film_production.application_builder import DocumentaryFilmProductionPriorityApplicationFormBuilder
from classes_new.forms._2026.dpf.production.family_film_production.application_builder import FamilyFilmProductionPriorityApplicationFormBuilder
from classes_new.forms._2026.dpf.production.intent_letter_film_production.application_builder import IntentLetterFilmProductionPriorityApplicationFormBuilder
from classes_new.forms._2026.dpf.production.international_minority_co_production.application_builder import InternationalMinorityCoProductionPriorityApplicationFormBuilder
from classes_new.forms._2026.dpf.production.international_minority_co_postproduction.application_builder import InternationalMinorityCoPostproductionPriorityApplicationFormBuilder
from classes_new.forms._2026.dpf.production.polish_german_film_fund.application_builder import PolishGermanFilmFundPriorityApplicationFormBuilder
from classes_new.forms._2026.dpf.production.film_project_development.application_builder import FilmProjectDevelopmentPriorityApplicationFormBuilder
# TEST
from classes_new.forms._2026.test.test.application_builder import TestApplicationFormBuilder
from classes_new.forms._2026.test.visuality_test.application_builder import VisualityTestApplicationFormBuilder
from classes_new.forms._2026.test.calculation_rules.application_builder import CalculationRulesApplicationFormBuilder
from classes_new.forms._2026.test.related_validators.application_builder import RelatedValidatorsApplicationFormBuilder
from classes_new.forms._2026.test.simple_validators.application_builder import SimpleValidatorsApplicationFormBuilder
from classes_new.forms._2026.test.special_validators.application_builder import SpecialValidatorsApplicationFormBuilder
# ZACHETY
from classes_new.forms._2026.zachety.report_builder import FinancingPriorityReportFormBuilder
# Other
from classes_new.forms.forms import Forms


class Forms2026(Forms):
    def __init__(self):
        super().__init__()

        self.builder_map = {
            "application": {
                "dpf": {
                    "skip": False,
                    "po1": {
                        "pr1": FilmProjectDevelopmentPriorityApplicationFormBuilder,
                        "pr2": FeaturedFilmProductionPriorityApplicationFormBuilder,
                        "pr3": DebutsFeaturedFilmProductionPriorityApplicationFormBuilder,
                        "pr4": DocumentaryFilmProductionPriorityApplicationFormBuilder,
                        "pr5": AnimatedFilmProductionPriorityApplicationFormBuilder,
                        "pr6": FamilyFilmProductionPriorityApplicationFormBuilder,
                        "pr7": InternationalMinorityCoProductionPriorityApplicationFormBuilder,
                        "pr8": InternationalMinorityCoPostproductionPriorityApplicationFormBuilder,
                        "pr9": PolishGermanFilmFundPriorityApplicationFormBuilder,
                        "pr10": ScreenplayScholarshipPriorityApplicationFormBuilder,
                        "pr11": IntentLetterFilmProductionPriorityApplicationFormBuilder,
                    }
                },
                "duk": {
                    "skip": True,
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
                    "skip": True,
                    "po5": {
                        "pr1": PromotionPriorityApplicationFormBuilder,
                        "pr2": ForeignPriorityApplicationFormBuilder
                    }
                },
                "test": {
                    "skip": True,
                    "visuality": {
                        "test": VisualityTestApplicationFormBuilder
                    },
                    "validators": {
                        "related_validators": RelatedValidatorsApplicationFormBuilder,
                        "simple_validators": SimpleValidatorsApplicationFormBuilder,
                        "special_validators": SpecialValidatorsApplicationFormBuilder
                    },
                    "calculationRules": {
                        "test": CalculationRulesApplicationFormBuilder
                    },
                    "test": {
                        "test": TestApplicationFormBuilder
                    }
                }
            },
            "report": {
                "duk": {
                    "skip": True,
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
                    "skip": True,
                    "po5": {
                        "pr1": PromotionPriorityReportFormBuilder,
                        "pr2": ForeignScholarshipsPriorityReportFormBuilder
                    }
                },
                "zachety": {
                    "skip": True,
                    "finansowanie": {
                        "raport": FinancingPriorityReportFormBuilder
                    }
                }
            }
        }
