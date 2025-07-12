import subprocess

# DPF
from classes.form_builder.dpf.animated_film.application_builder import AnimatedFilmApplicationBuilder
from classes.form_builder.dpf.screenplay_scholarship.application_builder import ScreenplayScholarshipApplicationBuilder
from classes.form_builder.dpf.documentary_film.application_builder import DocumentaryFilmApplicationBuilder
from classes.form_builder.dpf.family_film.application_builder import FamilyFilmApplicationBuilder
from classes.form_builder.dpf.coproduction_film.application_builder import CoproductionFilmApplicationBuilder
from classes.form_builder.dpf.feature_film.priority_data_path import FeatureFilmApplicationBuilder
from classes.form_builder.dpf.film_project_development.application_builder import FilmProjectDevelopmentApplicationBuilder
# DUK - education
from classes.form_builder.duk.education.postgraduate_schools.application_builder import PostgraduateSchoolsApplicationBuilder
from classes.form_builder.duk.education.secondary_schools.application_builder import SecondarySchoolsApplicationBuilder
from classes.form_builder.duk.education.cinemas.application_builder import CinemasApplicationBuilder
from classes.form_builder.duk.education.professional_training.application_builder import ProfessionalTrainingApplicationBuilder
# DUK - dissemination
from classes.form_builder.duk.dissemination.research.application_builder import ResearchApplicationBuilder
from classes.form_builder.duk.dissemination.festivals.application_builder import FestivalsApplicationBuilder
from classes.form_builder.duk.dissemination.literature.application_builder import LiteratueApplicationBuilder
from classes.form_builder.duk.dissemination.initiatives.application_builder import InitiativesApplicationBuilder
from classes.form_builder.duk.dissemination.documentary_distribution.application_builder import DocumentaryDistributionApplicationBuilder
from classes.form_builder.duk.dissemination.reconstruction.application_builder import ReconstructionApplicationBuilder
# DUK - development
from classes.form_builder.duk.development.modernization.application_builder import ModernizationApplicationBuilder
from classes.form_builder.duk.development.digitalization.application_builder import DigitalizationApplicationBuilder


def main():
    applications = [
        # DPF
        AnimatedFilmApplicationBuilder(),
        ScreenplayScholarshipApplicationBuilder(),
        DocumentaryFilmApplicationBuilder(),
        FamilyFilmApplicationBuilder(),
        CoproductionFilmApplicationBuilder(),
        FeatureFilmApplicationBuilder(),
        FilmProjectDevelopmentApplicationBuilder(),

        # DUK - education
        PostgraduateSchoolsApplicationBuilder(),
        SecondarySchoolsApplicationBuilder(),
        CinemasApplicationBuilder(),
        ProfessionalTrainingApplicationBuilder(),

        # DUK - dissemination
        ResearchApplicationBuilder(),
        FestivalsApplicationBuilder(),
        LiteratueApplicationBuilder(),
        InitiativesApplicationBuilder(),
        DocumentaryDistributionApplicationBuilder(),
        ReconstructionApplicationBuilder(),

        # DUK - development
        ModernizationApplicationBuilder(),
        DigitalizationApplicationBuilder(),
    ]

    for application in applications:
        application.generate()

    subprocess.run(["python", "scripts/delete_unused_args.py"], check=True)


if __name__ == '__main__':
    main()
