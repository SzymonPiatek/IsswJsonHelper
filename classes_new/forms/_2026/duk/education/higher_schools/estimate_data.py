from classes_new.forms._2026.duk.estimate.dataclasses_definitions import EstimateSection, CostItem
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
                title_help_text="osobowe",
                help_text="Wszelkie koszty osobowe nieujęte w pozostałych pozycjach."
            ),
            CostItem(
                title="Koszty osób współpracujących (np. nadzór merytoryczny, opieka dydaktyczna)",
                name="cooperatingPeople",
                helpText="Wyłącznie koszty udokumentowane umowami wraz z odpowiednimi dokumentami księgowymi (faktura lub rachunek).",
            ),
            CostItem(
                title="Konsultacje eksperckie",
                name="expertConsultation",
            ),
        ],
    ),
    EstimateSection(
        title="Koszty materiałowe i usługowe",
        costs=[
            CostItem(
                title="Wynajem kostiumów, rekwizytów",
                name="costumesRental"
            ),
            CostItem(
                title="Opracowanie materiałów dydaktycznych",
                name="developmentTeachingMaterials"
            ),
            CostItem(
                title="Obsługa PR, promocja i reklama",
                name="commercials"
            ),
            CostItem(
                title="Usługi graficzne i poligraficzne",
                name="graphicService"
            ),
            CostItem(
                title="Nagrania, usługi fotograficzne i montażowe",
                name="recordingService"
            ),
            CostItem(
                title="Usługi informatyczne",
                name="itService"
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
                title="Wynajem powierzchni",
                name="rentalSurface"
            ),
            CostItem(
                title="Aranżacja powierzchni",
                name="arrangementSurface"
            ),
            CostItem(
                title="Wynajem lub zakup sprzętu",
                name="equipmentRental",
                helpText="Zakup sprzętu wyłącznie na potrzeby realizacji danego przedsięwzięcia.",
            ),
            CostItem(
                title="Obsługa techniczna",
                name="technicalService",
                helpText="Dopuszcza się ujęcie obsługi technicznej w kosztach wynajmu sprzętu, jeśli stanowi integralną część usługi dostawcy."
            ),
            CostItem(
                title="Zabezpieczenie BHP",
                name="safetyBhp"
            ),
            CostItem(
                title="Obsługa projektów edukacyjnych online",
                name="onlineEducationProjects"
            ),
        ],
    ),
    EstimateSection(
        title="Koszty logistyczne",
        costs=[
            CostItem(
                title="Usługi transportowe",
                name="transportServices"
            ),
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
            fraction_cost(
                title="Catering lub poczęstunek",
                name="catering",
                ratio=0.15,
                title_help_text="cateringu lub poczęstunku"
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
                    "Koszty te powinny być udokumentowane rachunkiem lub fakturą z opisem potwierdzającym związek z przedsięwzięciem."
                ),
            ),
            CostItem(
                title="Obsługa prawna",
                name="legalService"
            ),
            CostItem(
                title="Koszty licencyjne i najmu kopii",
                name="licenseRental"
            ),
            CostItem(
                title="Ubezpieczenia",
                name="insurance"
            ),
            CostItem(
                title="Ewaluacja przedsięwzięcia",
                name="evaluation"
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
                helpText="Audiodeskrypcja, napisy SDH, tłumaczenia PJM."
            ),
        ],
    ),
]

estimate_sections = [asdict(section) for section in estimate_sections]
