from classes_new.forms._2026.duk.estimate.dataclasses_definitions import EstimateSection, CostItem, CostOverride
from classes_new.forms._2026.duk.estimate.helpers import fraction_cost
from dataclasses import asdict


estimate_sections = [
    EstimateSection(
        title="Koszty osobowe i merytoryczne",
        costs=[
            fraction_cost(
                title="Koszty zarządzania przedsięwzięciem",
                name="projectManagement",
                ratio=0.15,
                title_help_text="zarządzania przedsięwzięciem"
            ),
            fraction_cost(
                title="Koszty osobowe",
                name="personal",
                ratio=0.35,
                help_text="Wszelkie koszty osobowe nieujęte w pozostałych pozycjach.",
                title_help_text="osobowe"
            ),
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
            CostItem(
                title="Promocja i reklama",
                name="promotion"
            ),
            CostItem(
                title="Usługi graficzne i poligraficzne",
                name="graphicServices"
            ),
            CostItem(
                title="Dokumentacja fotograficzna i filmowa",
                name="photoFilmDoc"
            ),
            CostItem(
                title="Tłumaczenia",
                name="translation"
            ),
        ],
    ),
    EstimateSection(
        title="Koszty lokalowe i techniczne",
        costs=[
            CostItem(
                title="Przygotowanie kopii filmowych i napisów do filmów",
                name="copyingAndSubtitling"
            ),
            CostItem(
                title="Wynajem powierzchni",
                name="rentalSurface"
            ),
            CostItem(
                title="Wynajem sprzętu",
                name="equipmentRental"
            ),
            CostItem(
                title="Obsługa techniczna",
                name="technicalService",
                helpText="Dopuszcza się ujęcie obsługi technicznej w kosztach wynajmu sprzętu, jeśli stanowi integralną część usługi dostawcy."
            ),
            CostItem(
                title="Obsługa projektów online",
                name="onlineProjects"
            ),
        ],
    ),
    EstimateSection(
        title="Koszty logistyczne",
        costs=[
            CostItem(
                title="Podróże",
                name="travel",
                helpText=(
                    "Koszty udokumentowane wyłącznie fakturami lub biletami (jeśli niemożliwe jest otrzymanie faktury). "
                    "W przypadku podróży lotniczych pokrywa się z dotacji tylko koszt biletów w klasie ekonomicznej. "
                    "W przypadku zakupu paliwa wyłącznie koszty paliwa do samochodów wykorzystywanych do realizacji przedsięwzięcia zgodnie z obowiązującymi przepisami (tj. jeżeli samochód stanowi środek trwały Wnioskodawcy lub jest przedmiotem leasingu bądź najmu na rzecz Wnioskodawcy)."
                )
            ),
            CostItem(
                title="Noclegi",
                name="accommodation",
                helpText="Koszty udokumentowane wyłącznie fakturami (z wyłączeniem diet, ryczałtów i innych kosztów udokumentowanych w inny sposób, niż rachunkiem lub fakturą)."
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
                title="Obsługa prawna",
                name="legalService"
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
                overrides={
                    "RequestedAmount": CostOverride(
                        readOnly=True,
                    )
                }
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
