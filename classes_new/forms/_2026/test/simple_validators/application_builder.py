from classes_new.form_builder.form_builder import ApplicationFormBuilder


class SimpleValidatorsApplicationFormBuilder(ApplicationFormBuilder):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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
