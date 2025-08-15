from classes.generator.generator import Generator
from classes.form_builder.dpf.animated_film.application_builder import AnimatedFilmApplicationBuilder
from classes.form_builder.dpf.coproduction_film.application_builder import CoproductionFilmApplicationBuilder
from classes.form_builder.dpf.documentary_film.application_builder import DocumentaryFilmApplicationBuilder
from classes.form_builder.dpf.family_film.application_builder import FamilyFilmApplicationBuilder
from classes.form_builder.dpf.feature_film.application_builder import FeatureFilmApplicationBuilder
from classes.form_builder.dpf.film_project_development.application_builder import FilmProjectDevelopmentApplicationBuilder
from classes.form_builder.dpf.screenplay_scholarship.application_builder import ScreenplayScholarshipApplicationBuilder


class DPFGenerator(Generator):
    def __init__(self):
        super().__init__(
            applications=[
                AnimatedFilmApplicationBuilder(),
                ScreenplayScholarshipApplicationBuilder(),
                DocumentaryFilmApplicationBuilder(),
                FamilyFilmApplicationBuilder(),
                CoproductionFilmApplicationBuilder(),
                FeatureFilmApplicationBuilder(),
                FilmProjectDevelopmentApplicationBuilder(),
            ],
            reports=[]
        )
