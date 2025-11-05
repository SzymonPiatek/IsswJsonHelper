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
                title="Koszty osób współpracujących (np. ekspertów, prelegentów, artystów)",
                name="cooperatingPeople",
                helpText=(
                    "Wyłącznie koszty udokumentowane umowami wraz z odpowiednimi dokumentami księgowymi "
                    "(faktura lub rachunek)."
                ),
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
            CostItem(
                title="Opracowanie materiałów dydaktycznych",
                name="educationalMaterials",
            ),
            CostItem(
                title="Przygotowanie kopii filmowych oraz napisów do filmów",
                name="copyingAndSubtitling",
            ),
            CostItem(
                title="Obsługa PR, promocji i reklamy",
                name="commercials",
            ),
            CostItem(
                title="Usługi graficzne i poligraficzne",
                name="graphicService",
            ),
            CostItem(
                title="Nagrania, usługi fotograficzne i montażowe",
                name="recordingService",
            ),
            CostItem(
                title="Usługi informatyczne",
                name="itService"
            ),
            CostItem(
                title="Koszty tłumaczeń",
                name="translation",
            ),
        ],
    ),
    EstimateSection(
        title="Koszty lokalowe i techniczne",
        costs=[
            CostItem(
                title="Wynajem powierzchni",
                name="rentalSurface",
            ),
            CostItem(
                title="Aranżacja powierzchni",
                name="arrangementSurface",
            ),
            CostItem(
                title="Wynajem sprzętu",
                name="equipmentRental",
            ),
            CostItem(
                title="Obsługa techniczna",
                name="technicalService",
                helpText="Dopuszcza się ujęcie obsługi technicznej w kosztach wynajmu sprzętu, jeśli stanowi integralną część usługi dostawcy."
            ),
            CostItem(
                title="Zabezpieczenia BHP",
                name="safetyBhp",
            ),
            CostItem(
                title="Obsługa projektów edukacyjnych online",
                name="onlineEducationProjects",
            ),
        ],
    ),
    EstimateSection(
        title="Koszty logistyczne",
        costs=[
            CostItem(
                title="Usługi transportowe",
                name="transportServices",
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
                    "Koszty udokumentowane wyłącznie fakturami (z wyłączeniem diet, ryczałtów "
                    "i innych kosztów niewykazanych fakturą/rachunkiem). "
                    "Z dotacji PISF nie są pokrywane koszty podróży zagranicznych."
                ),
            ),
            CostItem(
                title="Katering lub poczęstunek",
                name="catering",
                helpText="Koszty cateringu lub poczęstunku nie mogą przekroczyć 15,00% ogólnej kwoty wnioskowanej. W przypadku uzyskania dofinansowania koszty, o których mowa powyżej nie mogą przekroczyć 15,00% przyznanej dotacji."
            )
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
            CostItem(title="Obsługa prawna", name="legalService"),
            CostItem(
                title="Koszty licencji lub nabycia praw do publicznego pokazu wraz z najmem kopii",
                helpText="Niezależnie od formuły fakturowania.",
                name="license",
            ),
            CostItem(
                title="Ubezpieczenia",
                name="insurance",
            ),
            CostItem(
                title="Ewaluacja przedsięwzięcia",
                name="evaluation",
            ),
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
