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


class RelatedUniversalRequiredConditionKwargs(TypedDict):
    equal_values: Optional[List[str]]
    min_range: Optional[float]
    max_range: Optional[float]
    is_checked: Optional[bool]


class Validator:
    def __init__(self):
        pass

    @staticmethod
    def length_validator(min_value: int = None, max_value: int = None, message: str = None):
        """
        Walidator sprawdza długość tekstu (min-max).
        """

        result = {
            "name": "LengthValidator",
        }

        if min_value is None and max_value is None:
            raise ValueError("Musisz podać co najmniej jedną wartość: min_value lub max_value")

        kwargs = {}
        if min_value is not None and min_value > 0:
            kwargs["min"] = min_value
        if max_value is not None and max_value > 0:
            kwargs["max"] = max_value

        result["kwargs"] = kwargs

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def required_validator(message: str = None):
        """
        Walidator oznacza komponent jako obowiązkowy.
        """

        result = {
            "name": "RequiredValidator"
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_required_if_equal_validator(field_name: str, value: str, message: str = None):
        """
        Walidator oznacza komponent jako obowiązkowy po spełnieniu warunku.
        """

        result = {
            "name": "RelatedRequiredIfEqualValidator",
            "kwargs": {
                "field_name": field_name,
                "value": value
            }
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def phone_number_validator(message: str = None):
        """
        Walidator sprawdza poprawność numeru telefonu komórkowego.
        """

        result = {
            "name": "PhoneNumberValidator",
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def email_validator(message: str = None):
        """
        Walidator sprawdza poprawność adresu mailowego.
        """

        result = {
            "name": "EmailValidator",
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def pesel_validator(message: str = None):
        """
        Walidator sprawdza poprawność numeru PESEL.
        """

        result = {
            "name": "PeselValidator"
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def iban_validator(message: str = None):
        """
        Walidator sprawdza poprawność numeru IBAN.
        """

        result = {
            "name": "IBANValidator"
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def swift_validator(message: str = None):
        """
        Walidator sprawdza poprawność numeru Swift.
        """

        result = {
            "name": "SwiftValidator"
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def regon_validator(message: str = None):
        """
        Walidator sprawdza poprawność numeru REGON.
        """

        result = {
            "name": "RegonValidator",
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def bank_account_validator(message: str = None):
        """
        Walidator sprawdza poprawność numeru konta bankowego.
        """

        result = {
            "name": "LengthValidator",
            "kwargs": {
                "min": 26,
                "max": 26
            },
            "validationMsg": "Numer konta bankowego musi liczyć 26 cyfr."
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def nip_validator(message: str = None):
        """
        Walidator sprawdza poprawność numeru NIP.
        """

        result = {
            "name": "LengthValidator",
            "kwargs": {
                "min": 10,
                "max": 10
            },
            "validationMsg": "Niepoprawny numer NIP."
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_local_sum_validator(field_names: List[str], message: str = None):
        """
        Walidator sprawdza poprawność sumy wartości (lokalnie).
        """

        result = {
            "name": "RelatedLocalSumValidator",
            "kwargs": {
                "field_names": field_names
            }
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_sum_validator(field_names: List[str], message: str = None):
        """
        Walidator sprawdza poprawność sumy wartości.
        """

        result = {
            "name": "RelatedSumValidator",
            "kwargs": {
                "field_names": field_names
            }
        }

        if message:
            result["validationMsg"] = message

        return result

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

        result = {
            "name": "ExactValidator",
            "kwargs": {
                "values": values,
            },
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_fraction_gte_validator(field_name: str, ratio: float, message: str = None):
        """
        Walidator sprawdza, czy wartość nie przekracza danej wartości procentowej wartości innego pola.
        """

        result = {
            "name": "RelatedFractionGTEValidator",
            "kwargs": {
                "field_name": field_name,
                "ratio": ratio,
            }
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_fraction_lte_validator(field_name: str, ratio: float, message: str = None):
        """
        Walidator sprawdza, czy wartość nie przekracza danej wartości procentowej wartości innego pola.
        """

        result = {
            "name": "RelatedFractionLTEValidator",
            "kwargs": {
                "field_name": field_name,
                "ratio": ratio,
            }
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_share_validator(dividend: str, divisor: str, message: str = None):
        """
        Walidator sprawdza, czy wartość udziału jest poprawna.
        """

        result = {
            "name": "RelatedShareValidator",
            "kwargs": {
                "dividend": dividend,
                "divisor": divisor
            }
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_local_date_lte_validator(field_name: str, message: str = None):
        """
        Walidator sprawdza, czy wartość daty jest mniejsza lub równa wartości daty innego pola.
        """

        result = {
            "name": "RelatedLocalDateLTEValidator",
            "kwargs": {
                "field_name": field_name
            }
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_local_date_gte_validator(field_name: str, message: str = None):
        """
        Walidator sprawdza, czy wartość daty jest większa lub równa wartości daty innego pola.
        """

        result = {
            "name": "RelatedLocalDateGTEValidator",
            "kwargs": {
                "field_name": field_name
            }
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_allowed_options_validator(field_name: str, mapping: Dict[str, List[str]], message: str = None):
        """
        Walidator sprawdza, czy wybrana opcja jest w liście poprawnych opcji dla danej wartości innego pola.
        """

        result = {
            "name": "RelatedAllowedOptionsValidator",
            "kwargs": {
                "field_name": field_name,
                "mapping": mapping
            }
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_mapped_limit_validator(default_limit: int | float, options: list[RelatedMappedLimitOption] = None, message: str = None):
        """
        Walidator sprawdza, czy kwota nie przekracza danej wartości dla wybranej opcji (lub domyślny limit).
        """

        kwargs = {
            "default_limit": default_limit,
        }

        if options:
            kwargs["options"] = options

        result = {
            "name": "RelatedMappedLimitValidator",
            "kwargs": kwargs
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_multiplication_validator(field_names: List[str], message: str = None):
        """
        Walidator sprawdza, czy poprawnie przemnożono wartości.
        """

        result = {
            "name": "RelatedMultiplicationValidator",
            "kwargs": {
                "field_names": field_names
            }
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_local_multiplication_validator(field_names: List[str], message: str = None):
        """
        Walidator sprawdza, czy poprawnie przemnożono wartości.
        """

        result = {
            "name": "RelatedLocalMultiplicationValidator",
            "kwargs": {
                "field_names": field_names
            }
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def zip_code_validator(mesasage: str = None):
        """
        Walidator sprawdza poprawność kodu pocztowego
        """

        result = {
            "name": "ZipCodeValidator",
        }

        if mesasage:
            result["validationMsg"] = mesasage

        return result

    @staticmethod
    def related_date_lte_validator(field_name: str, message: str = None):
        """
        Walidator sprawdza, czy podana data jest wcześniejsza niż data ze wskazanego pola.
        """

        result = {
            "name": "RelatedDateLTEValidator",
            "kwargs": {
                "field_name": field_name
            },
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_date_gte_validator(field_name: str, message: str = None):
        """
        Walidator sprawdza, czy podana data jest późniejsza niż data ze wskazanego pola.
        """

        result = {
            "name": "RelatedDateGTEValidator",
            "kwargs": {
                "field_name": field_name
            },
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_date_offset_validator(field_name: str, offset: int, message: str = None):
        result = {
            "name": "RelatedDateOffsetValidator",
            "kwargs": {
                "field_name": field_name,
                "offset": offset,
            },
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def checkbox_true_date_lte_today(field_name: str, message: str = None):
        result = {
            "name": "CheckboxTrueDateLTEToday",
            "kwargs": {
                "field_name": field_name
            }
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_condition_ratio_validator(field_name: str, conditions: list[RelatedConditionRatioCondition], message: str = None):
        """
        Walidator sprawdza, czy wartość jest w danym zakresie wartości pola field_name na podstawie warunków.
        """

        result = {
            "name": "RelatedConditionRatioValidator",
            "kwargs": {
                "field_name": field_name,
                "conditions": conditions
            }
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_condition_range_validator(conditions: list[RelatedConditionRangeCondition], message: str = None):
        """
        Walidator sprawdza, czy wartość jest w danym zakresie wartości pola field_name na podstawie warunków.
        """

        result = {
            "name": "RelatedConditionRangeValidator",
            "kwargs": {
                "conditions": conditions
            }
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_local_division_validator(dividend: str, divisor: str, message: str = None):
        """
        Walidator sprawdza, czy wartość udziału jest poprawna - lokalnie.
        """

        result = {
            "name": "RelatedLocalDivisionValidator",
            "kwargs": {
                "dividend": dividend,
                "divisor": divisor
            }
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_equality_validator(field_name: str, message: str = None):
        """
        Walidator sprawdza, czy wartość danego pola jest równa wartości innego pola.
        """

        result = {
            "name": "RelatedEqualityValidator",
            "kwargs": {"field_name": field_name},
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_local_equality_validator(field_name: str, message: str = None):
        """
        Walidator sprawdza, czy wartość danego pola jest równa wartości innego pola - lokalnie.
        """

        result = {
            "name": "RelatedLocalEqualityValidator",
            "kwargs": {"field_name": field_name},
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_numeric_equality_validator(field_name: str, message: str = None):
        """
        Walidator sprawdza, czy wartość numeryczna danego pola jest równa wartości innego pola - lokalnie.
        """

        result = {
            "name": "RelatedNumericEqualityValidator",
            "kwargs": {"field_name": field_name},
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_date_increment_validator(field_name: str, amount: int, message: str = None):
        """
        Walidator sprawdza, czy data jest równa dacie z danego pola + amount (liczba dni).
        """

        result = {
            "name": "RelatedDateIncrementValidator",
            "kwargs": {
                "field_name": field_name,
                "amount": amount
            },
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_map_validator(field_name: str, mapping: dict, message: str = None):
        """
        Walidator sprawdza, czy wartość pola odpowiada wartości zdefiniowanej dla wybranej opcji innego pola.
        """

        result = {
            "name": "RelatedMapValidator",
            "kwargs": {
                "field_name": field_name,
                "mapping": mapping,
            },
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_boolean_sum_validator(field_names: list[str], message: str = None):
        """
        Walidator sprawdza, czy co najmniej jedna z badanych wartości jest prawdziwa.
        Jeśli tak, wymaga, aby wartość komponentu również była prawdziwa.
        Jeżeli natomiast żadna z badanych wartości nie jest prawdziwa, walidator wymaga, aby wartość komponentu była fałszywa.
        """

        result = {
            "name": "RelatedBooleanSumValidator",
            "kwargs": {
                "field_names": field_names,
            },
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_sum_of_weights_validator(weights: dict[str, float], message: str = None):
        """
        Walidator sprawdza, czy dana wartość jest równa wartości po spełnieniu wszystkich warunków.
        """

        result = {
            "name": "RelatedSumOfWeightsValidator",
            "kwargs": {
                "weights": weights,
            },
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_last_date_validator(field_name: str, message: str = None):
        """
        Walidator sprawdza, czy data jest większa lub równa najpóźniejszej dacie z danego pola.
        """

        result = {
            "name": "RelatedLastDateValidator",
            "kwargs": {
                "field_name": field_name,
            }
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_equal_if_in_range_validator(field_name: str, required_value: Any, min_value: float = None, max_value: float = None, message: str = None):
        kwargs = {
            "field_name": field_name,
            "required_value": required_value,
        }

        if min_value:
            kwargs["min"] = min_value
        if max_value:
            kwargs["max"] = max_value

        result = {
            "name": "RelatedEqualIfInRangeValidator",
            "kwargs": kwargs,
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_empty_if_validator(field_name: str, message: str = None):
        result = {
            "name": "RelatedEmptyIfValidator",
            "kwargs": {
                "field_name": field_name,
            }
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_fraction_validator(field_name: str, ratio: float, max_value: float = None, message: str = None):
        result = {
            "name": "RelatedFractionValidator",
            "kwargs": {
                "field_name": field_name,
                "ratio": ratio,
            }
        }

        if max_value:
            result["kwargs"]["max"] = max_value

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_any_of_validator(field_names: list[str], message: str = None):
        result = {
            "name": "RelatedAnyOfValidator",
            "kwargs": {
                "field_names": field_names,
            }
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_unique_value_validator(field_name: str, normalize: bool = None, message: str = None):
        """
        Walidator sprawdza, czy wartość w polach o danej nazwie jest unikalna.
        """

        result = {
            "name": "RelatedUniqueValueValidator",
            "kwargs": {
                "field_name": field_name,
            }
        }

        if normalize:
            result["kwargs"]["normalize"] = normalize

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def landline_validator(message: str = None):
        """
        Walidator sprawdza, czy podany numer stacjonarny jest poprawny.
        """

        result = {
            "name": "LandlineValidator",
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def krs_validator(message: str = None):
        """
        Walidator sprwadza, czy podany numer KRS jest poprawny.
        """

        result = {
            "name": "KRSValidator",
        }

        if message:
            result["validationMsg"] = message

        return result

    @staticmethod
    def related_universal_required_validator(field_name: str = None, condition: dict = None, message: str = None):
        result = {
            "name": "RelatedUniversalRequiredValidator",
            "kwargs": {}
        }

        if field_name:
            result["kwargs"]["field_name"] = field_name

        if condition:
            result["kwargs"]["condition"] = condition

        if message:
            result["validationMsg"] = message

        return result
