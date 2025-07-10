from classes.form_builder.duk.education.application_builder import EducationApplicationBuilder


class CinemasApplicationBuilder(EducationApplicationBuilder):
    PRIORITY_NAME = 'IV. Edukacja w kinach'

    def __init__(self):
        super().__init__()

        self.postgraduate_data_path = self.education_data_path / 'cinemas'

    def generate(self):
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
        # V. Oświadczenia
        # VI. Załączniki
        # VII. Kosztorys przedsięwzięcia
        # VIII. Harmonogram

        self.save_output()
