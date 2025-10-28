from classes_new.forms._2026.duk.estimate.dataclasses_definitions import EstimateSection, CostItem
from classes_new.forms._2026.duk.estimate.helpers import fraction_cost
from dataclasses import asdict


estimate_sections = [
    EstimateSection(
        title="Koszty osobowe i merytoryczne",
        costs=[
            fraction_cost("zarządzania przedsięwzięciem", "projectManagement", 0.15),
            fraction_cost("osobowe", "personal", 0.35),
            CostItem(
                title="Koszty osób współpracujących (np. twórców, prelegentów, moderatorów)",
                name="cooperatingPeople",
                helpText="Wyłącznie koszty udokumentowane umowami wraz z odpowiednimi dokumentami księgowymi (faktura lub rachunek)."
            ),
        ],
    ),
    EstimateSection(
        title="Koszty materiałowe i usługowe",
        costs=[
            CostItem(title="Promocja i reklama", name="promotion"),
            CostItem(title="Usługi graficzne i poligraficzne", name="graphicServices"),
            CostItem(title="Dokumentacja fotograficzna i filmowa", name="photoFilmDoc"),
            CostItem(title="Tłumaczenia", name="translation"),
        ],
    ),
    EstimateSection(
        title="Koszty lokalowe i techniczne",
        costs=[
            CostItem(title="Przygotowanie kopii filmowych i napisów do filmów", name="copyingAndSubtitling"),
            CostItem(title="Wynajem powierzchni", name="rentalSurface"),
            CostItem(title="Wynajem sprzętu", name="equipmentRental"),
            CostItem(title="Obsługa techniczna", name="technicalService"),
            CostItem(title="Obsługa projektów online", name="onlineProjects"),
        ],
    ),
    EstimateSection(
        title="Koszty logistyczne",
        costs=[
            CostItem(
                title="Koszty podróży",
                name="travel",
                helpText=(
                    "Koszty udokumentowane wyłącznie fakturami lub biletami (jeśli brak faktury). "
                    "W przypadku podróży lotniczych – tylko bilety w klasie ekonomicznej. "
                    "W przypadku paliwa – wyłącznie koszty paliwa do samochodów wykorzystywanych do realizacji przedsięwzięcia "
                    "(środek trwały, leasing, najem). Z dotacji PISF nie są pokrywane koszty podróży zagranicznych."
                ),
            ),
            CostItem(
                title="Koszty noclegów",
                name="accommodation",
                helpText=(
                    "Koszty udokumentowane wyłącznie fakturami (z wyłączeniem diet, ryczałtów i innych kosztów niewykazanych fakturą/rachunkiem). "
                    "Z dotacji PISF nie są pokrywane koszty podróży zagranicznych."
                ),
            ),
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
                    "Koszty muszą być udokumentowane rachunkiem lub fakturą z opisem potwierdzającym związek z przedsięwzięciem."
                ),
            ),
            CostItem(
                title="Koszty licencji lub nabycia praw do publicznego pokazu",
                name="publicPerformanceRights",
                helpText="Niezależnie od formuły fakturowania.",
            ),
            CostItem(
                title="Koszty składki Polskiej Federacji Dyskusyjnych Klubów Filmowych",
                name="pfdkfFee",
                helpText="Pokrywana wyłącznie ze środków własnych Wnioskodawcy lub z innych źródeł finansowania.",
            ),
        ],
    ),
    EstimateSection(
        title="Koszty związane z dostępnością",
        costs=[
            CostItem(
                title="Dostępność cyfrowa",
                name="digitalAccessibility",
                helpText="Dostępne strony internetowe.",
            ),
            CostItem(
                title="Dostępność informacyjno–komunikacyjna",
                name="infoAccessibility",
                helpText="Wykonanie napisów SDH, tłumaczenia PJM.",
            ),
        ],
    ),
]

estimate_sections = [asdict(section) for section in estimate_sections]
