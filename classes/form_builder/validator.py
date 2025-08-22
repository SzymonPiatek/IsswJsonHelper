class Validator:
    def __init__(self):
        pass

    @staticmethod
    def length_validator(min_value: int = 0, max_value: int = 0, message: str = None):
        if min_value == 0 and max_value == 0:
            raise ValueError("Musisz podać co najmniej jedną wartość: min_value lub max_value")

        kwargs = {}
        if min_value > 0:
            kwargs["min"] = min_value
        if max_value > 0:
            kwargs["max"] = max_value + 1

        if min_value > 0 and max_value > 0:
            msg = f"Ilość znaków musi zawierać się w przedziale od {min_value} do {max_value}"
        elif min_value > 0:
            msg = f"Ilość znaków musi wynosić co najmniej {min_value}"
        else:
            msg = f"Ilość znaków nie może przekroczyć {max_value}"

        return {
            "name": "LengthValidator",
            "kwargs": kwargs,
            "validationMsg": message if message is not None else msg,
        }

    @staticmethod
    def required_validator():
        return {
            "name": "RequiredValidator"
        }

    @staticmethod
    def related_required_if_equal_validator(field_name: str, value: str):
        return {
            "name": "RelatedRequiredIfEqualValidator",
            "kwargs": {
                "field_name": field_name,
                "value": value
            }
        }

    @staticmethod
    def phone_number_validator():
        return {
            "name": "PhoneNumberValidator",
            "validationMsg": "Wprowadź numer telefonu w formie: +kod kraju oraz pozostałe cyfry numeru. Dla numeru polskiego przykładowo +48123456789"
        }

    @staticmethod
    def email_validator():
        return {
            "name": "EmailValidator",
            "validationMsg": "Podaj prawidłowy adres email."
        }

    @staticmethod
    def pesel_validator():
        return {
            "name": "PeselValidator"
        }

    @staticmethod
    def iban_validator():
        return {
            "name": "IBANValidator"
        }

    @staticmethod
    def swift_validator():
        return {
            "name": "SwiftValidator"
        }

    @staticmethod
    def regon_validator():
        return {
            "name": "RegonValidator",
            "validationMsg": "Niepoprawny numer REGON"
        }

    @staticmethod
    def bank_account_validator():
        return {
            "name": "LengthValidator",
            "kwargs": {
                "min": 26,
                "max": 27
            },
            "validationMsg": "Numer konta bankowego musi liczyć 26 cyfr."
        }

    @staticmethod
    def related_local_sum_validator(field_names: [str]):
        return {
            "name": "RelatedLocalSumValidator",
            "kwargs": {
                "field_names": field_names
            }
        }

    @staticmethod
    def related_sum_validator(field_names: [str]):
        return {
            "name": "RelatedSumValidator",
            "kwargs": {
                "field_names": field_names
            }
        }

    @staticmethod
    def range_validator(min_value: int | float = 0, max_value: int | float = 0, message: str = None):
        if min_value == 0 and max_value == 0:
            raise ValueError("Musisz podać co najmniej jedną wartość: min_value lub max_value")

        kwargs = {}
        if min_value > 0:
            kwargs["min"] = min_value
        if max_value > 0:
            kwargs["max"] = float(max_value) + 0.01

        if min_value > 0 and max_value > 0:
            msg = f"Wartość musi być w zakresie od {min_value}% do {max_value}%"
        elif min_value > 0:
            msg = f"Wartość musi wynosić przynajmniej {min_value}%"
        else:
            msg = f"Wartość nie może przekorczyć {max_value}"

        return {
            "name": "RangeValidator",
            "kwargs": kwargs,
            "validationMsg": message if message is not None else msg,
        }
