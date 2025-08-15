from classes.generator.generator import Generator

# APPLICATIONS
# EDUCATION
from classes.form_builder.duk.education.postgraduate_schools.application_builder import PostgraduateSchoolsApplicationBuilder
from classes.form_builder.duk.education.secondary_schools.application_builder import SecondarySchoolsApplicationBuilder
from classes.form_builder.duk.education.cinemas.application_builder import CinemasApplicationBuilder
from classes.form_builder.duk.education.professional_training.application_builder import ProfessionalTrainingApplicationBuilder
# DISSEMINATION
from classes.form_builder.duk.dissemination.research.application_builder import ResearchApplicationBuilder
from classes.form_builder.duk.dissemination.festivals.application_builder import FestivalsApplicationBuilder
from classes.form_builder.duk.dissemination.literature.application_builder import LiteratueApplicationBuilder
from classes.form_builder.duk.dissemination.initiatives.application_builder import InitiativesApplicationBuilder
from classes.form_builder.duk.dissemination.documentary_distribution.application_builder import DocumentaryDistributionApplicationBuilder
from classes.form_builder.duk.dissemination.reconstruction.application_builder import ReconstructionApplicationBuilder
# DEVELOPMENT
from classes.form_builder.duk.development.modernization.application_builder import ModernizationApplicationBuilder
from classes.form_builder.duk.development.digitalization.application_builder import DigitalizationApplicationBuilder

# REPORTS
# EDUCATION
from classes.form_builder.duk.education.postgraduate_schools.report_builder import PostgraduateSchoolsReportBuilder
from classes.form_builder.duk.education.secondary_schools.report_builder import SecondarySchoolsReportBuilder
from classes.form_builder.duk.education.cinemas.report_builder import CinemasReportBuilder
from classes.form_builder.duk.education.professional_training.report_builder import ProfessionalTrainingReportBuilder


class DUKGenerator(Generator):
    def __init__(self):
        super().__init__(
            applications=[
                # EDUCATION
                PostgraduateSchoolsApplicationBuilder(),
                SecondarySchoolsApplicationBuilder(),
                CinemasApplicationBuilder(),
                ProfessionalTrainingApplicationBuilder(),

                # DISSEMINATION
                ResearchApplicationBuilder(),
                FestivalsApplicationBuilder(),
                LiteratueApplicationBuilder(),
                InitiativesApplicationBuilder(),
                DocumentaryDistributionApplicationBuilder(),
                ReconstructionApplicationBuilder(),

                # DEVELOPMENT
                ModernizationApplicationBuilder(),
                DigitalizationApplicationBuilder(),
            ],
            reports=[
                # EDUCATION
                PostgraduateSchoolsReportBuilder(),
                SecondarySchoolsReportBuilder(),
                CinemasReportBuilder(),
                ProfessionalTrainingReportBuilder()
            ]
        )
