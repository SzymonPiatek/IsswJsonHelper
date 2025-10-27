from classes_new.forms._2026.duk.estimate.dataclasses_definitions import CostOverride, CostItem
from classes_new.form_rules.validator import Validator

validators = Validator()


def fraction_cost(title: str, name: str, ratio: float) -> CostItem:
    percent = ratio * 100
    help_text = (
        f"Koszty {title.lower()} nie mogą przekroczyć {percent:.0f},00% ogólnej kwoty wnioskowanej. "
        f"W przypadku uzyskania dofinansowania koszty {title.lower()} nie mogą przekroczyć {percent:.0f},00% przyznanej dotacji."
    )
    validator = validators.related_fraction_gte_validator(
        field_name="pisfSupportAmountTotal",
        ratio=ratio,
        message=f"Kwota dofinansowania dla tego kosztu nie może przekroczyć {percent:.0f}% kwoty wnioskowanej."
    )
    return CostItem(
        title=f"Koszty {title}",
        name=name,
        helpText=help_text,
        overrides={"RequestedAmount": CostOverride(validators=[validator])}
    )
