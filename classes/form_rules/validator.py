from typing import Dict, List, TypedDict, Any, Optional


class RelatedMappedLimitCondition(TypedDict):
    field_name: str
    value: str


class RelatedMappedLimitOption(TypedDict):
    limit: int | float
    conditions: list[RelatedMappedLimitCondition]


class RelatedConditionRatioCondition(TypedDict):
    field_name: str
    value: Any
    max_ratio: Optional[float]
    min_ratio: Optional[float]


class RelatedConditionRangeCondition(TypedDict):
    field_name: str
    value: Any
    max_range: Optional[float]
    min_range: Optional[float]


class Validator:
    def __init__(self):
        self.names = [
            "LengthValidator",
            "RequiredValidator",
            "RelatedRequiredIfEqualValidator",
            "PhoneNumberValidator",
            "EmailValidator",
            "PeselValidator",
            "IBANValidator",
            "SwiftValidator",
            "RegonValidator",
            "RelatedLocalSumValidator",
            "RelatedSumValidator",
            "RangeValidator",
            "ExactValidator",
            "RelatedFractionGTEValidator",
            "RelatedFractionLTEValidator",
            "RelatedShareValidator",
            "RelatedLocalDateLTEValidator",
            "RelatedLocalDateGTEValidator",
            "RelatedAllowedOptionsValidator",
            "RelatedMappedLimitValidator",
            "ZipCodeValidator",
            "RelatedDateLTEValidator",
            "RelatedDateGTEValidator",
            "RelatedMultiplicationValidator",
            "RelatedDateOffsetValidator",
            "CheckboxTrueDateLTEToday",
            "RelatedConditionRatioValidator",
            "RelatedConditionRangeValidator",
            "RelatedLocalDivisionValidator",
            "RelatedEqualityValidator",
            "RelatedLocalEqualityValidator",
            "RelatedNumericEqualityValidator",
            "RelatedDateIncrementValidator"
        ]

    @staticmethod
    def length_validator(min_value: int = None, max_value: int = None, message: str = None):
        """
        Walidator sprawdza długość tekstu (min-max).
        """

        if min_value is None and max_value is None:
            raise ValueError("Musisz podać co najmniej jedną wartość: min_value lub max_value")

        kwargs = {}
        if min_value is not None and min_value > 0:
            kwargs["min"] = min_value
        if max_value is not None and max_value > 0:
            kwargs["max"] = max_value + 1
        if min_value is not None and min_value > 0 and max_value is not None and max_value > 0:
            default_msg = f"Ilość znaków musi zawierać się w przedziale od {min_value} do {max_value}."
        elif min_value is not None and min_value > 0:
            default_msg = f"Ilość znaków musi wynosić co najmniej {min_value}."
        elif max_value is not None and max_value > 0:
            default_msg = f"Ilość znaków nie może przekroczyć {max_value}."
        else:
            default_msg = "Nieprawidłowe ograniczenia długości tekstu."

        return {
            "name": "LengthValidator",
            "kwargs": kwargs,
            "validationMsg": message if message is not None else default_msg,
        }

    @staticmethod
    def required_validator():
        """
        Walidator oznacza komponent jako obowiązkowy.
        """

        return {
            "name": "RequiredValidator"
        }

    @staticmethod
    def related_required_if_equal_validator(field_name: str, value: str):
        """
        Walidator oznacza komponent jako obowiązkowy po spełnieniu warunku.
        """

        return {
            "name": "RelatedRequiredIfEqualValidator",
            "kwargs": {
                "field_name": field_name,
                "value": value
            }
        }

    @staticmethod
    def phone_number_validator():
        """
        Walidator sprawdza poprawność numeru telefonu komórkowego.
        """

        return {
            "name": "PhoneNumberValidator",
            "validationMsg": "Wprowadź numer telefonu w formie: +kod kraju oraz pozostałe cyfry numeru. Dla numeru polskiego przykładowo +48123456789."
        }

    @staticmethod
    def email_validator():
        """
        Walidator sprawdza poprawność adresu mailowego.
        """

        return {
            "name": "EmailValidator",
            "validationMsg": "Podaj prawidłowy adres email."
        }

    @staticmethod
    def pesel_validator():
        """
        Walidator sprawdza poprawność numeru PESEL.
        """

        return {
            "name": "PeselValidator"
        }

    @staticmethod
    def iban_validator():
        """
        Walidator sprawdza poprawność numeru IBAN.
        """

        return {
            "name": "IBANValidator"
        }

    @staticmethod
    def swift_validator():
        """
        Walidator sprawdza poprawność numeru Swift.
        """

        return {
            "name": "SwiftValidator"
        }

    @staticmethod
    def regon_validator():
        """
        Walidator sprawdza poprawność numeru REGON.
        """

        return {
            "name": "RegonValidator",
            "validationMsg": "Niepoprawny numer REGON."
        }

    @staticmethod
    def bank_account_validator():
        """
        Walidator sprawdza poprawność numeru konta bankowego.
        """

        return {
            "name": "LengthValidator",
            "kwargs": {
                "min": 26,
                "max": 27
            },
            "validationMsg": "Numer konta bankowego musi liczyć 26 cyfr."
        }

    @staticmethod
    def nip_validator():
        """
        Walidator sprawdza poprawność numeru NIP.
        """

        return {
            "name": "LengthValidator",
            "kwargs": {
                "min": 9,
                "max": 11
            },
            "validationMsg": "Niepoprawny numer NIP."
        }

    @staticmethod
    def related_local_sum_validator(field_names: List[str]):
        """
        Walidator sprawdza poprawność sumy wartości (lokalnie).
        """

        return {
            "name": "RelatedLocalSumValidator",
            "kwargs": {
                "field_names": field_names
            }
        }

    @staticmethod
    def related_sum_validator(field_names: List[str]):
        """
        Walidator sprawdza poprawność sumy wartości.
        """

        return {
            "name": "RelatedSumValidator",
            "kwargs": {
                "field_names": field_names
            }
        }

    @staticmethod
    def range_validator(min_value: int | float = None, max_value: int | float = None, message: str = None):
        """
        Walidator sprawdza czy wartość jest w danym zakresie (min - max).
        """

        if min_value is None and max_value is None:
            raise ValueError("Musisz podać co najmniej jedną wartość: min_value lub max_value")

        kwargs = {}

        if min_value is not None:
            kwargs["min"] = min_value

        if max_value is not None and max_value > 0:
            kwargs["max"] = float(max_value) + 0.01

        if min_value is not None and max_value is not None and max_value > 0:
            msg = f"Wartość musi być w zakresie od {min_value} do {max_value}."
        elif min_value is not None:
            msg = f"Wartość musi być większa lub równa {min_value}."
        elif max_value is not None and max_value > 0:
            msg = f"Wartość nie może przekroczyć {max_value}."
        else:
            raise ValueError("Błędne wartości")

        return {
            "name": "RangeValidator",
            "kwargs": kwargs,
            "validationMsg": message if message is not None else msg,
        }

    @staticmethod
    def exact_validator(values: List[str], message: str = None):
        """
        Walidator sprawdza, czy wybrana opcja jest jedną z możliwych do wyboru.
        """

        return {
            "name": "ExactValidator",
            "kwargs": {
                "values": values,
            },
            "validationMsg": message
        }

    @staticmethod
    def related_fraction_gte_validator(field_name: str, ratio: float, message: str = None):
        """
        Walidator sprawdza, czy wartość nie przekracza danej wartości procentowej wartości innego pola.
        """

        return {
            "name": "RelatedFractionGTEValidator",
            "kwargs": {
                "field_name": field_name,
                "ratio": ratio
            },
            "validationMsg": message
        }

    @staticmethod
    def related_fraction_lte_validator(field_name: str, ratio: float, message: str = None):
        """
        Walidator sprawdza, czy wartość nie przekracza danej wartości procentowej wartości innego pola.
        """

        return {
            "name": "RelatedFractionLTEValidator",
            "kwargs": {
                "field_name": field_name,
                "ratio": ratio
            },
            "validationMsg": message
        }

    @staticmethod
    def related_share_validator(dividend: str, divisor: str):
        """
        Walidator sprawdza, czy wartość udziału jest poprawna.
        """

        return {
            "name": "RelatedShareValidator",
            "kwargs": {
                "dividend": dividend,
                "divisor": divisor
            }
        }

    @staticmethod
    def related_local_date_lte_validator(field_name: str, message: str = None):
        """
        Walidator sprawdza, czy wartość daty jest mniejsza lub równa wartości daty innego pola.
        """

        return {
            "name": "RelatedLocalDateLTEValidator",
            "kwargs": {
                "field_name": field_name
            },
            "validationMsg": message
        }

    @staticmethod
    def related_local_date_gte_validator(field_name: str, message: str = None):
        """
        Walidator sprawdza, czy wartość daty jest większa lub równa wartości daty innego pola.
        """

        return {
            "name": "RelatedLocalDateGTEValidator",
            "kwargs": {
                "field_name": field_name
            },
            "validationMsg": message
        }

    @staticmethod
    def related_allowed_options_validator(field_name: str, mapping: Dict[str, List[str]]):
        """
        Walidator sprawdza, czy wybrana opcja jest w liście poprawnych opcji dla danej wartości innego pola.
        """

        return {
            "name": "RelatedAllowedOptionsValidator",
            "kwargs": {
                "field_name": field_name,
                "mapping": mapping
            }
        }

    @staticmethod
    def related_mapped_limit_validator(default_limit: int | float, options: list[RelatedMappedLimitOption] = None):
        """
        Walidator sprawdza, czy kwota nie przekracza danej wartości dla wybranej opcji (lub domyślny limit).
        """

        kwargs = {
            "default_limit": default_limit,
        }

        if options:
            kwargs["options"] = options

        return {
            "name": "RelatedMappedLimitValidator",
            "kwargs": kwargs
        }

    @staticmethod
    def related_multiplication_validator(field_names: List[str]):
        """
        Walidator sprawdza, czy poprawnie przemnożono wartości.
        """

        return {
            "name": "RelatedMultiplicationValidator",
            "kwargs": {
                "field_names": field_names
            }
        }

    @staticmethod
    def zip_code_validator():
        """
        Walidator sprawdza poprawność kodu pocztowego
        """

        return {
            "name": "ZipCodeValidator",
            "validationMsg": "Podaj kod pocztowy we właściwym formacie."
        }

    @staticmethod
    def related_date_lte_validator(field_name: str, message: str = None):
        """
        Walidator sprawdza, czy podana data jest wcześniejsza niż data ze wskazanego pola.
        """

        return {
            "name": "RelatedDateLTEValidator",
            "kwargs": {
                "field_name": field_name
            },
            "validationMsg": message
        }

    @staticmethod
    def related_date_gte_validator(field_name: str, message: str = None):
        """
        Walidator sprawdza, czy podana data jest późniejsza niż data ze wskazanego pola.
        """

        return {
            "name": "RelatedDateGTEValidator",
            "kwargs": {
                "field_name": field_name
            },
            "validationMsg": message
        }

    @staticmethod
    def related_date_offset_validator(field_name: str, offset: int, message: str = None):
        return {
            "name": "RelatedDateOffsetValidator",
            "kwargs": {
                "field_name": field_name,
                "offset": offset,
            },
            "validationMsg": message
        }

    @staticmethod
    def checkbox_true_date_lte_today(field_name: str):
        return {
            "name": "CheckboxTrueDateLTEToday",
            "kwargs": {
                "field_name": field_name
            }
        }

    @staticmethod
    def related_condition_ratio_validator(field_name: str, conditions: list[RelatedConditionRatioCondition]):
        """
        Walidator sprawdza, czy wartość jest w danym zakresie wartości pola field_name na podstawie warunków.
        """

        return {
            "name": "RelatedConditionRatioValidator",
            "kwargs": {
                "field_name": field_name,
                "conditions": conditions
            }
        }

    @staticmethod
    def related_condition_range_validator(conditions: list[RelatedConditionRangeCondition]):
        """
        Walidator sprawdza, czy wartość jest w danym zakresie wartości pola field_name na podstawie warunków.
        """

        return {
            "name": "RelatedConditionRangeValidator",
            "kwargs": {
                "conditions": conditions
            }
        }

    @staticmethod
    def related_local_division_validator(dividend: str, divisor: str):
        """
        Walidator sprawdza, czy wartość udziału jest poprawna - lokalnie.
        """

        return {
            "name": "RelatedLocalDivisionValidator",
            "kwargs": {
                "dividend": dividend,
                "divisor": divisor
            }
        }

    @staticmethod
    def related_equality_validator(field_name: str, message: str = None):
        """
        Walidator sprawdza, czy wartość danego pola jest równa wartości innego pola.
        """

        return {
            "name": "RelatedEqualityValidator",
            "kwargs": {"field_name": field_name},
            "validationMsg": message
        }

    @staticmethod
    def related_local_equality_validator(field_name: str, message: str = None):
        """
        Walidator sprawdza, czy wartość danego pola jest równa wartości innego pola - lokalnie.
        """

        return {
            "name": "RelatedLocalEqualityValidator",
            "kwargs": {"field_name": field_name},
            "validationMsg": message
        }

    @staticmethod
    def related_numeric_equality_validator(field_name: str, message: str = None):
        """
        Walidator sprawdza, czy wartość numeryczna danego pola jest równa wartości innego pola - lokalnie.
        """

        return {
            "name": "RelatedNumericEqualityValidator",
            "kwargs": {"field_name": field_name},
            "validationMsg": message
        }

    @staticmethod
    def related_date_increment_validator(field_name: str, amount: int, message: str = None):
        """
        Walidator sprawdza, czy data jest równa dacie z danego pola + amount (liczba dni).
        """

        return {
            "name": "RelatedDateIncrementValidator",
            "kwargs": {
                "field_name": field_name,
                "amount": amount
            },
            "validationMsg": message
        }
