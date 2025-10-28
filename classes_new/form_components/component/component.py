from classes_new.form_factory.form_factory import FormFactory


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

