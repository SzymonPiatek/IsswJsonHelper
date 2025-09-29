from classes.form_builder.additional.decorators import not_implemented_func
from classes.form_builder.application_builder import ApplicationBuilder
from classes.form_builder.departments.duk.department import DUKDepartment


class DUKApplicationBuilder2026(ApplicationBuilder, DUKDepartment):
    YEAR = 2026

    def __init__(self):
        super().__init__()


    def create_application_metadata(self):
        part = self.create_part(
            title="Wniosek o dofinansowanie przedsięwzięcia realizowanego w ramach Programów Operacyjnych Polskiego Instytutu Sztuki Filmowej",
            short_name="I. Metadane wniosku",
            chapters=[
                self.create_chapter(
                    title="1. Tryb naboru",
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Nr sesji i rok",
                            name="sessionYear",
                            value=f"Sesja {self.session}/{self.year}",
                            read_only=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="2. Program operacyjny",
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Program",
                            name="programName",
                            value=self.operation_name,
                            read_only=True
                        )
                    ]
                ),
                self.create_chapter(
                    title="3. Priorytet",
                    components=[
                        self.create_component(
                            component_type="text",
                            label="Priorytet",
                            name="priorytetName",
                            value=self.priority_name,
                            read_only=True
                        )
                    ]
                )
            ]
        )
        self.save_part(part=part)

    @not_implemented_func
    def create_application_basic_data(self):
        pass

    def create_application_applicant_data(self):
        pass

    def generate(self):
        # Base
        self.create_base()

        # Metadane wniosku
        self.create_application_metadata()

        # # I. Dane podstawowe
        self.create_application_basic_data()

        # II. Dane wnioskodawcy
        self.create_application_applicant_data()
        #
        # # III. Zakres przedsięwzięcia
        # self.create_application_scope_of_project()
        #
        # # IV. Źródła finansowania
        # self.create_application_sources_of_financing()
        #
        # # V. Oświaczenia
        # self.create_application_statements()
        #
        # # VI. Załączniki
        # self.create_application_attachments()
        #
        # # VII. Kosztorys przedsięwzięcia
        # self.create_application_project_costs()
        #
        # # VIII. Harmonogram
        # self.create_application_schedule()
        #
        # # Zapis
        # self.save_output()
