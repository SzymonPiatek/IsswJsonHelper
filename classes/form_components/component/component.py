from classes.form_factory.form_factory import FormFactory


class Component(FormFactory):
    def __init__(self):
        super().__init__()

    def voivodeship_select(self, name: str):
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
            required=True
        )

    def project_location(self):
        return self.create_component(
            component_type="text",
            label="Miejscowość",
            name="projectLocation",
            validators=[
                self.validator.length_validator(max_value=1000)
            ],
            required=True
        )
