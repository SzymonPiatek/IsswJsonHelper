from .estimate_data import estimate_sections
from classes.form_builder.departments.duk._2026.application_estimate_builder import DUKApplicationEstimateBuilder
from ..priority import SecondarySchoolsPriority
from ..application_builder import EducationApplicationBuilder
from classes.helpers import int_to_roman


class SecondarySchoolsApplicationBuilder(EducationApplicationBuilder, SecondarySchoolsPriority):
    FORM_ID = 17

    def __init__(self):
        super().__init__()

        self.project_type = [
            "Programy edukacyjne wchodzące w skład edukacji ciągłej.",
            "Kształcenie w kierunku zdobycia zawodów związanych z potrzebami współczesnego rynku audiowizualnego.",
            "Praktyki zawodowe."
        ]

        estimate_builder = DUKApplicationEstimateBuilder(estimate_sections=estimate_sections)
        self.estimate_chapters = [
            estimate_builder.generate_estimate()
        ]

        self.is_basic_number_data = True

    def create_application_basic_number_data(self, number):
        part = self.create_part(
            title=f"{int_to_roman(number)}. Podstawowe dabe liczbowe i wskaźniki",
            short_name="Dane liczbowe",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="number",
                            name="numberOfStudents",
                            label="Liczba uczniów (studia stacjonarne)",
                            unit="osoby",
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            name="averageTuitionFee",
                            label="Średnia wysokość czesnego (w rozrachunku rocznym, studia stacjonarne)",
                            unit="PLN",
                            required=True
                        ),
                        self.create_component(
                            component_type="text",
                            mask="fund",
                            name="averageCostOfEducatingStudent",
                            label="Średni koszt kształcenia ucznia (w roku i w tys. zł, studia stacjonarne)",
                            unit="PLN",
                            required=True
                        )
                    ]
                )
            ]
        )
        self.save_part(part)
