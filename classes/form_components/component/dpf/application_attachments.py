from classes.form_factory.form_factory import FormFactory


class ApplicationAttachments(FormFactory):
    def __init__(self):
        super().__init__()

    def description_of_artistic_qualities(self):
        return self.create_component(
            component_type="textarea",
            label="Opis walorów artystycznych i ekonomicznych przedsięwzięcia, tj. uzasadnienie przedsięwzięcia pod kątem kryteriów, o których mowa w art. 22. ust. 3 Ustawy o kinematografii",
            name="descriptionOfArtisticQualities",
            validators=[
                self.validator.length_validator(
                    max_value=5400
                )
            ],
            required=True,
        )

    def expected_results_indicator(self):
        return self.create_component(
            component_type="textarea",
            label="Wskaźniki oczekiwanych rezultatów przedsięwzięcia, tj. w szczególności krótka charakterystyka odbiorców filmu, spodziewana liczba widzów, estymacja rentowności filmu, potencjał festiwalowy",
            name="expectedResultsIndicator",
            validators=[
                self.validator.length_validator(
                    max_value=5400
                )
            ],
            required=True,
        )
