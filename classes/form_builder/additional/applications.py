# DPF
from classes.form_builder.dpf.family_film.application_builder import FamilyFilmApplicationBuilder
from classes.form_builder.dpf.feature_film.application_builder import FeatureFilmApplicationBuilder
from classes.form_builder.dpf.animated_film.application_builder import AnimatedFilmApplicationBuilder
from classes.form_builder.dpf.documentary_film.application_builder import DocumentaryFilmApplicationBuilder
from classes.form_builder.dpf.coproduction_film.application_builder import CoproductionFilmApplicationBuilder
from classes.form_builder.dpf.film_project_development.application_builder import FilmProjectDevelopmentApplicationBuilder
from classes.form_builder.dpf.screenplay_scholarship.application_builder import ScreenplayScholarshipApplicationBuilder
# DUK - EDUCATION
from classes.form_builder.duk.education.postgraduate_schools.application_builder import PostgraduateSchoolsApplicationBuilder
from classes.form_builder.duk.education.cinemas.application_builder import CinemasApplicationBuilder
from classes.form_builder.duk.education.secondary_schools.application_builder import SecondarySchoolsApplicationBuilder
from classes.form_builder.duk.education.professional_training.application_builder import ProfessionalTrainingApplicationBuilder
# DUK - DISSEMINATION
from classes.form_builder.duk.dissemination.festivals.application_builder import FestivalsApplicationBuilder
from classes.form_builder.duk.dissemination.documentary_distribution.application_builder import DocumentaryDistributionApplicationBuilder
from classes.form_builder.duk.dissemination.initiatives.application_builder import InitiativesApplicationBuilder
from classes.form_builder.duk.dissemination.literature.application_builder import LiteratueApplicationBuilder
from classes.form_builder.duk.dissemination.reconstruction.application_builder import ReconstructionApplicationBuilder
from classes.form_builder.duk.dissemination.research.application_builder import ResearchApplicationBuilder
# DUK - DEVELOPMENT
from classes.form_builder.duk.development.modernization.application_builder import ModernizationApplicationBuilder
from classes.form_builder.duk.development.digitalization.application_builder import DigitalizationApplicationBuilder
# DWM
from classes.form_builder.dwm.promotion.application_builder import PromotionApplicationBuilder
from classes.form_builder.dwm.foreign_scholarship.application_builder import ForeignScholarshipApplicationBuilder


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
