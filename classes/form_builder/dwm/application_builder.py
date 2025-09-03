from classes.form_builder.application_builder import ApplicationBuilder
from classes.form_builder.additional.decorators import not_implemented_func
from classes.form_builder.components.dwm_section import DWMSection


class DWMApplicationBuilder(ApplicationBuilder):
    DEPARTMENT_NAME = 'DWM'
    OPERATION_NAME = 'V. Promocja polskiej twórczości filmowej za granicą'
    OPERATION_NUM = 5

    def __init__(self):
        super().__init__()

        self.section = DWMSection()

    @not_implemented_func
    def create_application_metadata(self):
        pass

    @not_implemented_func
    def create_application_name_data(self):
        pass

    @not_implemented_func
    def create_application_applicant_data(self):
        pass

    @not_implemented_func
    def create_application_applicant_achievements_data(self):
        pass

    @not_implemented_func
    def create_application_description_of_the_project_data(self):
        pass

    def create_application_logo_data(self):
        part = self.create_part(
            title="VI. Wskazanie sposobu wykorzystania logotypu PISF / Informacja o dofinansowaniu ze środków PISF w kampanii promocyjnej",
            short_name="VI. Logotyp PISF",
            chapters=[
                self.create_chapter(
                    title="Opis wykorzystania logotypu lub informacji o dofinansowaniu",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="applicantLogotypePromotionDesc",
                            validators=[
                                self.validator.length_validator(max_value=20000)
                            ],
                            required=True,
                            help_text="Opisz w jaki sposób wykorzystasz logotyp PISF i/lub zamieścisz informację o dofinansowaniu ze środków PISF."
                        )
                    ]
                )
            ]
        )
        self.save_part(part=part)

    def create_application_implementation_effects_data(self):
        part = self.create_part(
            title="VII. Planowane efekty realizacji przedsięwzięcia",
            short_name="VII. Efekty realizacji",
            chapters=[
                self.create_chapter(
                    title="Planowane efekty",
                    components=[
                        self.create_component(
                            component_type="textarea",
                            name="applicantPlannedTaskEffects",
                            validators=[
                                self.validator.length_validator(max_value=20000)
                            ],
                            help_text="Opisz planowane efekty wykonania przedsięwzięcia. Należy podać konkretny efekt np. nawiązanie innej współpracy, zaproszenie na inny festiwal, itp. Po zakończeniu przedsięwzięcia beneficjent jest zobowiązany przedstawić w raporcie efekty przedsięwzięcia.",
                            required=True
                        )
                    ]
                )
            ]
        )
        self.save_part(part=part)

    @not_implemented_func
    def create_application_other_information_data(self):
        pass

    @not_implemented_func
    def create_application_financial_data(self):
        pass

    @not_implemented_func
    def create_application_statements(self):
        pass

    @not_implemented_func
    def create_application_attachments(self):
        pass

    @not_implemented_func
    def create_application_schedule_data(self):
        pass

    def generate(self):
        # Base
        self.create_application_base()

        # 1. Nazwa programu i priorytetu
        self.create_application_metadata()

        # 2. Nazwa przedsięwzięcia
        self.create_application_name_data()

        # 3. Informacja o wnioskodawcy
        self.create_application_applicant_data()

        # 4. Dorobek wnioskodawcy
        self.create_application_applicant_achievements_data()

        # 5. Opis przedsięwzięcia
        self.create_application_description_of_the_project_data()

        # 6. Logotyp PISF
        self.create_application_logo_data()

        # 7. Efekty realizacji
        self.create_application_implementation_effects_data()

        # 8. Inne informacje
        self.create_application_other_information_data()

        # # 9. Koszty przedsięwzięcia
        self.create_application_financial_data()

        # 10. Oświadczenia
        self.create_application_statements()

        # 11. Załączniki
        self.create_application_attachments()

        # 12. Harmonogram
        self.create_application_schedule_data()

        # Zapis
        self.save_output()
