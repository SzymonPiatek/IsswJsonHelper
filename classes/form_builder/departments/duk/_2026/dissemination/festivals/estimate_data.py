from dataclasses import asdict
from classes.form_estimate_builder.dataclasses_definitions import EstimateSection, CostItem
from classes.form_builder.departments.duk._2026.estimate.helpers import fraction_cost


estimate_sections = [
    EstimateSection(
        title="Koszty osobowe i merytoryczne",
        costs=[
            fraction_cost("zarządzania przedsięwzięciem", "projectManagement", 0.15),
            fraction_cost("osobowe", "personal", 0.35),
            CostItem(
                title="Koszty osób współpracujących (np. członków jury, twórców, moderatorów)",
                name="cooperatingPeople",
                helpText="Wyłącznie koszty udokumentowane umowami wraz z odpowiednimi dokumentami księgowymi (tj. faktura lub rachunek).",
            ),
            CostItem(title="Koszty konsultacji eksperckich", name="expertConsultation"),
            CostItem(title="Koszty nagród dla laureatów", name="awards"),
        ],
    ),
    EstimateSection(
        title="Koszty materiałowe i usługowe",
        costs=[
            CostItem(title="Koszty przygotowania kopii filmowych i napisów do filmów", name="copyingAndSubtitling"),
            CostItem(title="Koszty usług PR, promocji i reklam", name="commercials"),
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
            CostItem(title="Koszty obsługi festiwalu online", name="onlineFestival"),
        ],
    ),
    EstimateSection(
        title="Koszty logistyczne",
        costs=[
            CostItem(title="Koszty usług transportowych", name="transportServices"),
            CostItem(
                title="Koszty dotyczące podróży",
                name="travel",
                helpText=(
                    "Koszty udokumentowane wyłącznie fakturami lub biletami (jeśli niemożliwe jest otrzymanie faktury). "
                    "W przypadku podróży lotniczych pokrywa się z dotacji tylko koszt biletów w klasie ekonomicznej. "
                    "W przypadku zakupu paliwa wyłącznie koszty paliwa do samochodów wykorzystywanych do realizacji przedsięwzięcia "
                    "zgodnie z obowiązującymi przepisami (tj. jeżeli samochód stanowi środek trwały Wnioskodawcy lub jest przedmiotem leasingu bądź najmu). "
                    "Z dotacji PISF nie są pokrywane koszty podróży zagranicznych."
                ),
            ),
            CostItem(
                title="Koszty dotyczące noclegów",
                name="accommodation",
                helpText=(
                    "Koszty udokumentowane wyłącznie fakturami (z wyłączeniem diet, ryczałtów i innych kosztów udokumentowanych "
                    "w inny sposób, niż rachunkiem lub fakturą). Z dotacji PISF nie są pokrywane koszty podróży zagranicznych."
                ),
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
                helpText=(
                    "Koszty związane z otwarciem i prowadzeniem rachunku bankowego wyłącznie dla operacji finansowych "
                    "związanych z realizacją przedsięwzięcia oraz koszty prowadzenia księgowości związanej z realizacją danego przedsięwzięcia. "
                    "Koszty te powinny zostać udokumentowane rachunkiem lub fakturą z opisem potwierdzającym, że dotyczyły realizacji danego przedsięwzięcia."
                ),
            ),
            CostItem(title="Koszty licencyjne i najmu kopii", name="licenseRental"),
            CostItem(title="Koszty ubezpieczeń", name="insurance"),
            CostItem(title="Koszty ewaluacji przedsięwzięcia", name="evaluation"),
        ],
    ),
    EstimateSection(
        title="Koszty związane z dostępnością",
        costs=[
            CostItem(
                title="Koszty związane z dostępnością cyfrową",
                helpText="Dostępne strony internetowe.",
                name="digitalAccessibility",
            ),
            CostItem(
                title="Koszty związane z dostępnością informacyjno–komunikacyjną (audiodeskrypcja, napisy SDH, tłumaczenie PJM)",
                name="infoAccessibility",
            ),
        ],
    ),
]

estimate_sections = [asdict(section) for section in estimate_sections]
