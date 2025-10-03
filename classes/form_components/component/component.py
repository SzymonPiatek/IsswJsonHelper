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

    def org_and_legal_structure_select(self, overrides: dict = None):
        overrides = overrides or {}

        return self.create_component(
            component_type="select",
            label=overrides.get('label', False) or '',
            name=overrides.get('name', False) or "orgAndLegalStructure",
            options=[
                "Spółka z ograniczoną odpowiedzialnością",
                "Spółka akcyjna",
                "Spółka jawna",
                "Spółka komandytowa",
                "Spółka komandytowo-akcyjna",
                "Osoba fizyczna prowadząca działalność gospodarczą",
                "Spółka cywilna",
                "Fundacja",
                "Stowarzyszenie",
                "Instytucja kultury",
                "Instytucja filmowa",
                "Publiczna szkoła lub uczelnia artystyczna",
                "Niepubliczna szkoła lub uczelnia artystyczna",
                "Kościół lub związek wyznaniowy",
                "Jednostka samorządu terytorialnego",
                "Placówka dyplomatyczna",
                "Instytut Polski",
                "Inna (np. spółka w organizacji)"
            ],
            required=True,
            help_text="Wybierz formę organizacyjno-prawną wnioskodawcy."
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
