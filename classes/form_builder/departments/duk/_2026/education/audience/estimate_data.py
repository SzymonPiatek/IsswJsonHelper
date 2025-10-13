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
                title="Koszty opracowania materiałów dydaktycznych",
                name="educationalMaterials",
            ),
            CostItem(
                title="Koszty najmu i przygotowania kopii filmowych oraz napisów do filmów",
                name="copyingAndSubtitling",
            ),
            CostItem(
                title="Koszty obsługi PR, promocji i reklamy",
                name="commercials",
            ),
            CostItem(
                title="Koszty usług graficznych i poligraficznych",
                name="graphicService",
            ),
            CostItem(
                title="Koszty nagrań i usług fotograficznych",
                name="recordingService",
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
                title="Koszty wynajmu powierzchni",
                name="rentalSurface",
            ),
            CostItem(
                title="Koszty aranżacji powierzchni",
                name="arrangementSurface",
            ),
            CostItem(
                title="Koszty wynajmu sprzętu",
                name="equipmentRental",
            ),
            CostItem(
                title="Koszty obsługi technicznej",
                name="technicalService",
            ),
            CostItem(
                title="Koszty zabezpieczenia BHP",
                name="safetyBhp",
            ),
            CostItem(
                title="Koszty obsługi projektów edukacyjnych online",
                name="onlineEducationProjects",
            ),
        ],
    ),
    EstimateSection(
        title="Koszty logistyczne",
        costs=[
            CostItem(
                title="Koszty usług transportowych",
                name="transportServices",
            ),
            CostItem(
                title="Koszty dotyczące podróży",
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
                title="Koszty dotyczące noclegów",
                name="accommodation",
                helpText=(
                    "Koszty udokumentowane wyłącznie fakturami (z wyłączeniem diet, ryczałtów "
                    "i innych kosztów niewykazanych fakturą/rachunkiem). "
                    "Z dotacji PISF nie są pokrywane koszty podróży zagranicznych."
                ),
            ),
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
                    "związanych z realizacją przedsięwzięcia. Koszty prowadzenia księgowości związanej z realizacją przedsięwzięcia. "
                    "Koszty te powinny być udokumentowane rachunkiem lub fakturą z opisem potwierdzającym związek z przedsięwzięciem."
                ),
            ),
            CostItem(
                title="Koszty licencyjne",
                name="license",
            ),
            CostItem(
                title="Koszty ubezpieczeń",
                name="insurance",
            ),
            CostItem(
                title="Koszty ewaluacji przedsięwzięcia",
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
