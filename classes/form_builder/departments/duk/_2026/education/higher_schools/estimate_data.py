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



estimate_sections = [
    EstimateSection(
        title="Koszty osobowe i merytoryczne",
        costs=[
            fraction_cost("zarządzania przedsięwzięciem", "projectManagement", 0.15),
            fraction_cost("osobowe", "personal", 0.35),
            CostItem(
                title="Koszty osób współpracujących (np. nadzór merytoryczny, opieka dydaktyczna)",
                name="cooperatingPeople",
                helpText="Wyłącznie koszty udokumentowane umowami wraz z odpowiednimi dokumentami księgowymi (faktura lub rachunek).",
            ),
            CostItem(
                title="Koszty konsultacji eksperckich",
                name="expertConsultation",
            ),
        ],
    ),
    EstimateSection(
        title="Koszty materiałowe i usługowe",
        costs=[
            CostItem(title="Wynajem kostiumów, rekwizytów", name="costumesRental"),
            CostItem(title="Materiały biurowe", name="stationery"),
            CostItem(title="Obsługa PR, promocja i reklama", name="commercials"),
            CostItem(title="Usługi graficzne i poligraficzne", name="graphicService"),
            CostItem(title="Nagrania i usługi fotograficzne", name="recordingService"),
            CostItem(title="Tłumaczenia", name="translation"),
        ],
    ),
    EstimateSection(
        title="Koszty lokalowe i techniczne",
        costs=[
            CostItem(title="Wynajem powierzchni", name="rentalSurface"),
            CostItem(title="Aranżacja powierzchni", name="arrangementSurface"),
            CostItem(
                title="Wynajem lub zakup sprzętu",
                name="equipmentRental",
                helpText="Zakup sprzętu wyłącznie na potrzeby realizacji danego przedsięwzięcia.",
            ),
            CostItem(title="Obsługa techniczna", name="technicalService"),
            CostItem(title="Zabezpieczenie BHP", name="safetyBhp"),
            CostItem(title="Obsługa projektów edukacyjnych online", name="onlineEducationProjects"),
        ],
    ),
    EstimateSection(
        title="Koszty logistyczne",
        costs=[
            CostItem(title="Usługi transportowe", name="transportServices"),
            CostItem(
                title="Podróże",
                name="travel",
                helpText=(
                    "Koszty udokumentowane wyłącznie fakturami lub biletami (jeśli brak faktury). "
                    "W przypadku podróży lotniczych – tylko bilety w klasie ekonomicznej. "
                    "W przypadku paliwa – wyłącznie koszty paliwa do samochodów wykorzystywanych "
                    "do realizacji przedsięwzięcia (środek trwały, leasing, najem). "
                    "Z dotacji PISF nie są pokrywane koszty podróży zagranicznych."
                ),
            ),
            CostItem(
                title="Noclegi",
                name="accommodation",
                helpText=(
                    "Koszty udokumentowane wyłącznie fakturami lub rachunkami (z wyłączeniem diet, ryczałtów "
                    "i innych kosztów niewykazanych fakturą/rachunkiem). "
                    "Z dotacji PISF nie są pokrywane koszty podróży zagranicznych, w tym zakwaterowania."
                ),
            ),
            fraction_cost("cateringu lub poczęstunku", "catering", 0.15),
        ],
    ),
    EstimateSection(
        title="Koszty prawne i administracyjne",
        costs=[
            CostItem(
                title="Obsługa finansowa",
                name="financialService",
                helpText=(
                    "Koszty związane z otwarciem i prowadzeniem rachunku bankowego wyłącznie dla operacji finansowych "
                    "związanych z realizacją przedsięwzięcia. Koszty prowadzenia księgowości związanej z realizacją przedsięwzięcia. "
                    "Koszty te powinny być udokumentowane rachunkiem lub fakturą z opisem potwierdzającym związek z przedsięwzięciem."
                ),
            ),
            CostItem(title="Koszty licencyjne i najmu kopii", name="licenseRental"),
            CostItem(title="Ubezpieczenia", name="insurance"),
            CostItem(title="Ewaluacja przedsięwzięcia", name="evaluation"),
        ],
    ),
    EstimateSection(
        title="Koszty związane z dostępnością",
        costs=[
            CostItem(
                title="Dostępność cyfrowa (dostępne strony internetowe)",
                name="digitalAccessibility",
            ),
            CostItem(
                title="Dostępność informacyjno–komunikacyjna (audiodeskrypcja, napisy SDH, tłumaczenia PJM)",
                name="infoAccessibility",
            ),
        ],
    ),
]

estimate_sections = [asdict(section) for section in estimate_sections]
