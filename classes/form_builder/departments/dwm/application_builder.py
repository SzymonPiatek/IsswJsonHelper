from classes.form_builder.application_builder import ApplicationBuilder
from classes.decorators import not_implemented_func
from classes.form_builder.departments.dwm.department import DWMDepartment
from classes.form_builder.departments.dwm.operation import DWMOperation


class DWMApplicationBuilder(ApplicationBuilder, DWMDepartment, DWMOperation):
    def __init__(self):
        super().__init__()

        self.parts: list = [
            self.create_application_metadata,
            self.create_application_name_data,
            self.create_application_applicant_data,
            self.create_application_applicant_achievements_data,
            self.create_application_description_of_the_project_data,
            self.create_application_logo_data,
            self.create_application_implementation_effects_data,
            self.create_application_other_information_data,
            self.create_application_financial_data,
            self.create_application_statements,
            self.create_application_attachments,
            self.create_application_schedule_data
        ]

    @not_implemented_func
    def create_application_metadata(self, number: int):
        pass

    @not_implemented_func
    def create_application_name_data(self, number: int):
        pass

    @not_implemented_func
    def create_application_applicant_data(self, number: int):
        pass

    @not_implemented_func
    def create_application_applicant_achievements_data(self, number: int):
        pass

    @not_implemented_func
    def create_application_description_of_the_project_data(self, number: int):
        pass

    def create_application_logo_data(self, number: int):
        part = self.create_part(
            title=f"{self.helpers.int_to_roman(number)}. Wskazanie sposobu wykorzystania logotypu PISF / Informacja o dofinansowaniu ze środków PISF w kampanii promocyjnej",
            short_name=f"{self.helpers.int_to_roman(number)}. Logotyp PISF",
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

    @not_implemented_func
    def create_application_other_information_data(self, number: int):
        pass

    @not_implemented_func
    def create_application_financial_data(self, number: int):
        pass

    @not_implemented_func
    def create_application_statements(self, number: int):
        pass

    @not_implemented_func
    def create_application_attachments(self, number: int):
        pass

    @not_implemented_func
    def create_application_schedule_data(self, number: int):
        pass
