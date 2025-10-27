from classes_new.form_builder.form_builder import ApplicationFormBuilder


class SimpleValidatorsApplicationFormBuilder(ApplicationFormBuilder):
    def __init__(self):
        super().__init__(
            custom_dir_name="test/simple_validators",
            custom_file_name="simple_validators"
        )

        self.parts = []

        """
        Simple validators:
        
        [ ] RequiredValidator
        [ ] ExactValidator
        [ ] LengthValidator
        [ ] RangeValidator
        [ ] ZipCodeValidator
        [ ] PhoneNumberValidator
        [ ] LandlineValidator
        [ ] EmailValidator
        [ ] KRSValidator
        [ ] PeselValidator
        [ ] IBANValidator
        [ ] RegonValidator
        [ ] SwiftValidator
        [ ] RequiredValidator
        [ ] RequiredValidator
        """
