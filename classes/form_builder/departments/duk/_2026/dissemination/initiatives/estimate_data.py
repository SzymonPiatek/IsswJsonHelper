from dataclasses import asdict
from classes.form_rules import Validator
from classes.form_estimate_builder.dataclasses_definitions import EstimateSection, CostItem, CostOverride

validators = Validator()


def fraction_cost(title: str, name: str, ratio: float) -> CostItem:
    percent = ratio * 100
    help_text = (
        f"Koszty {title.lower()} nie mogą przekroczyć {percent:.2f}% ogólnej kwoty wnioskowanej. "
        f"W przypadku uzyskania dofinansowania koszty {title.lower()} nie mogą przekroczyć {percent:.2f}% przyznanej dotacji."
    )
    validator = validators.related_fraction_gte_validator(
        field_name="pisfSupportAmount",
        ratio=ratio,
        message=f"Kwota dofinansowania dla tego kosztu nie może przekroczyć {percent:.2f}% kwoty wnioskowanej."
    )
    return CostItem(
        title=f"Koszty {title}",
        name=name,
        helpText=help_text,
        overrides={"RequestedAmount": CostOverride(validators=[validator])},
    )


estimate_sections_pt124 = [
    EstimateSection(
        title="Koszty osobowe i merytoryczne",
        costs=[
            fraction_cost("zarządzania przedsięwzięciem", "projectManagement", 0.15),
            fraction_cost("osobowe", "personal", 0.35),
            CostItem(
                title="Koszty osób współpracujących (np. członków jury, twórców, moderatorów)",
                name="cooperatingPeople",
                helpText="Wyłącznie koszty udokumentowane umowami wraz z odpowiednimi dokumentami księgowymi (faktura lub rachunek).",
            ),
            CostItem(title="Koszty konsultacji eksperckich", name="expertConsultation"),
            CostItem(title="Koszty nagród dla laureatów", name="awards"),
        ],
    ),
    EstimateSection(
        title="Koszty materiałowe i usługowe",
        costs=[
            CostItem(title="Koszty przygotowania kopii filmowych i napisów do filmów", name="copyingAndSubtitling"),
            CostItem(title="Koszty obsługi PR, promocji i reklamy", name="commercials"),
            CostItem(title="Koszty usług graficznych i poligraficznych", name="graphicService"),
            CostItem(title="Koszty nagrań i usług fotograficznych", name="recordingService"),
            CostItem(title="Koszty tłumaczeń", name="translation"),
            CostItem(title="Koszty materiałów biurowych", name="stationery"),
        ],
    ),
    EstimateSection(
        title="Koszty lokalowe i techniczne",
        costs=[
            CostItem(title="Koszty wynajmu powierzchni", name="rentalSurface"),
            CostItem(title="Koszty aranżacji powierzchni", name="arrangementSurface"),
            CostItem(title="Koszty wynajmu sprzętu", name="equipmentRental"),
            CostItem(title="Koszty obsługi technicznej", name="technicalService"),
            CostItem(title="Koszty zabezpieczenia BHP", name="safetyBhp"),
            CostItem(title="Koszty obsługi projektów online", name="onlineProjects"),
        ],
    ),
    EstimateSection(
        title="Koszty logistyczne",
        costs=[
            CostItem(title="Koszty usług transportowych", name="transportServices"),
            CostItem(
                title="Koszty dotyczące podróży",
                name="travel",
                helpText="Wyłącznie koszty udokumentowane fakturami lub biletami (jeśli faktura jest niemożliwa do uzyskania). W przypadku podróży lotniczych – pokrywany jest tylko koszt biletów w klasie ekonomicznej. W przypadku zakupu paliwa – wyłącznie paliwo do samochodów wykorzystywanych do realizacji przedsięwzięcia zgodnie z przepisami (samochód jako środek trwały, leasing, najem). Nie pokrywa się kosztów podróży zagranicznych.",
            ),
            CostItem(
                title="Koszty dotyczące noclegów",
                name="accommodation",
                helpText="Wyłącznie koszty udokumentowane fakturami. Wykluczone: diety, ryczałty, inne koszty nieudokumentowane rachunkiem lub fakturą. Nie pokrywa się kosztów podróży zagranicznych.",
            ),
            fraction_cost("cateringu lub poczęstunku", "catering", 0.15),
        ],
    ),
    EstimateSection(
        title="Koszty prawne i administracyjne",
        costs=[
            CostItem(
                title="Koszty obsługi finansowej",
                name="financialService",
                helpText="Związane z otwarciem i prowadzeniem rachunku bankowego wyłącznie dla operacji finansowych przedsięwzięcia. Koszty prowadzenia księgowości związanej z realizacją przedsięwzięcia. Powinny być udokumentowane rachunkiem lub fakturą z opisem potwierdzającym, że dotyczyły realizacji przedsięwzięcia.",
            ),
            CostItem(title="Koszty licencyjne i najmu kopii", name="licenseRental"),
            CostItem(title="Koszty ubezpieczeń", name="insurance"),
            CostItem(title="Koszty ewaluacji przedsięwzięcia", name="evaluation"),
        ],
    ),
    EstimateSection(
        title="Koszty związane z dostępnością",
        costs=[
            CostItem(title="Dostępność cyfrowa", name="digitalAccessibility", helpText="Dostępne strony internetowe."),
            CostItem(
                title="Dostępność informacyjno–komunikacyjna",
                name="infoAccessibility",
                helpText="Wykonanie audiodeskrypcji, napisów SDH, tłumaczenia PJM.",
            ),
        ],
    ),
]

estimate_sections_pt124 = [asdict(section) for section in estimate_sections_pt124]
estimate_sections_pt3 = []
