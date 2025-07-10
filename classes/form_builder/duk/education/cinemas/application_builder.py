from classes.form_builder.duk.education.application_builder import EducationApplicationBuilder


class CinemasApplicationBuilder(EducationApplicationBuilder):
    PRIORITY_NAME = 'IV. Edukacja w kinach'

    def __init__(self):
        super().__init__()

        self.cinemas_data_path = self.education_data_path / 'cinemas'

    def generate(self):
        self.create_application_base()

        # Metadane wniosku
        self.create_application_metadata()

        # I. Dane podstawowe
        self.create_application_basic_data(data={
            'projectType': {
                'options': [
                    "cykliczne zajęcia edukacyjne połączone z projekcją filmu o wysokich walorach artystycznych, dotyczące analizy prezentowanego utworu, jego miejsca w historii kinematografii polskiej i/lub światowej, estetyki filmowej i zastosowanych środków wyrazu oraz społecznych funkcji filmu, organizowane w kinach studyjnych, prowadzone w trakcie roku szkolnego",
                    "inne działania realizujące cele Priorytetu V"
                ]
            }
        })

        # II. Dane wnioskodawcy
        self.create_application_applicant_data()

        # III. Zakres przedsięwzięcia

        # IV. Źródła finansowania
        self.create_application_sources_of_financing()

        # V. Oświadczenia
        self.create_application_statements()

        # VI. Załączniki
        self.create_application_attachments()

        # VII. Kosztorys przedsięwzięcia

        # VIII. Harmonogram
        self.create_application_schedule()

        self.save_output()
