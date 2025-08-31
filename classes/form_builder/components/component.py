from classes.form_builder.form_builder_base import FormBuilderBase


class Component(FormBuilderBase):
    def __init__(self):
        super().__init__()

    def voivodeship_select(self, name: str, required_if_name: str, required_if_value: str):
        return self.create_component(
            component_type="select",
            label="Województwo",
            name=name,
            options=[
                "dolnośląskie",
                "kujawsko-pomorskie",
                "lubelskie",
                "lubuskie",
                "łódzkie",
                "małopolskie",
                "mazowieckie",
                "opolskie",
                "podkarpackie",
                "podlaskie",
                "pomorskie",
                "śląskie",
                "świętokrzyskie",
                "warmińsko-mazurskie",
                "wielkopolskie",
                "zachodniopomorskie"
            ],
            required=True,
            validators=[
                self.validator.related_required_if_equal_validator(
                    field_name=required_if_name,
                    value=required_if_value
                )
            ]
        )

    def project_location(self):
        return self.create_component(
            component_type="text",
            label="Miejscowość",
            name="projectLocation",
            validators=[
                self.validator.length_validator(max_value=100)
            ],
            required=True
        )
