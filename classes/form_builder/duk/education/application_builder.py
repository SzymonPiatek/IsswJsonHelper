from classes.form_builder.duk.application_builder import DUKApplicationBuilder2025


class EducationApplicationBuilder2025(DUKApplicationBuilder2025):
    OPERATION_NAME = 'II. Edukacja filmowa'

class PostgraduateSchoolsApplicationBuilder2025(EducationApplicationBuilder2025):
    PRIORITY_NAME = 'I. Szkoły wyższe i podyplomowe'

class PostgraduateSchoolsApplicationBuilder2025Session01(PostgraduateSchoolsApplicationBuilder2025):
    SESSION = 'I'

    def generate(self):
        self.create_application_base()
        self.create_application_metadata()
        self.save_output()
