# DPF
from classes.form_builder.dpf import (
    AnimatedFilmApplicationBuilder,
    CoproductionFilmApplicationBuilder,
    DocumentaryFilmApplicationBuilder,
    FamilyFilmApplicationBuilder,
    FeatureFilmApplicationBuilder,
    FilmProjectDevelopmentApplicationBuilder,
    ScreenplayScholarshipApplicationBuilder
)

# DUK - EDUCATION
from classes.form_builder.duk.education import (
    CinemasApplicationBuilder,
    PostgraduateSchoolsApplicationBuilder,
    ProfessionalTrainingApplicationBuilder,
    SecondarySchoolsApplicationBuilder
)
# DUK - DISSEMINATION
from classes.form_builder.duk.dissemination import (
    DocumentaryDistributionApplicationBuilder,
    FestivalsApplicationBuilder,
    InitiativesApplicationBuilder,
    LiteratueApplicationBuilder,
    ReconstructionApplicationBuilder,
    ResearchApplicationBuilder
)
# DUK - DEVELOPMENT
from classes.form_builder.duk.development import ModernizationApplicationBuilder, DigitalizationApplicationBuilder
# DWM
from classes.form_builder.dwm import ForeignScholarshipApplicationBuilder, PromotionApplicationBuilder


_builder_map = {
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
}


def get_application_builder(department: str, program: str, priority: str):
    try:
        return _builder_map[department][program][priority]
    except KeyError:
        raise ValueError(f"Nieobsługiwany wariant: {department}.{program}.{priority}")
