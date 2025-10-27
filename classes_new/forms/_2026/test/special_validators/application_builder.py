from classes_new.form_builder.form_builder import ApplicationFormBuilder


class SpecialValidatorsApplicationFormBuilder(ApplicationFormBuilder):
    def __init__(self):
        super().__init__(
            custom_dir_name="test/special_validators",
            custom_file_name="special_validators"
        )

        self.parts = []

        """
        Special validators:
        
        [ ] CheckboxTrueDateLTEToday
        """

