from classes_new.forms._2026.duk.estimate.dataclasses_definitions import EstimateSection, CostItem
from classes_new.forms._2026.duk.estimate.helpers import fraction_cost
from dataclasses import asdict



estimate_sections_pt = [
    EstimateSection(
        title="Koszty osobowe i merytoryczne",
        costs=[
            fraction_cost(
                title="Zarządzanie przedsięwzięciem",
                name="projectManagement",
                ratio=0.15,
                title_help_text="zarządzania przedsięwzięciem"
            ),
            CostItem(
                title="Opracowanie i redakcja publikacji",
                name="publicationEditing",
                helpText="Autorzy tekstów, redaktorzy, korektorzy."
            ),
            fraction_cost(
                title="Koszty osobowe",
                name="personal",
                ratio=0.35,
                help_text="Wszelkie koszty osobowe nieujęte w pozostałych pozycjach.",
                title_help_text="osobowe"
            ),
            CostItem(
                title="Konsultacje eksperckie",
                name="expertConsultation"
            ),
        ],
    ),
    EstimateSection(
        title="Koszty przygotowania i publikacji",
        costs=[
            CostItem(
                title="Usługi graficzne, fotograficzne i typograficzne",
                name="graphicPhotoTypography"
            ),
            CostItem(
                title="Usługi wydawnicze i poligraficzne",
                name="publishingPrinting"
            ),
            CostItem(
                title="Przygotowanie wersji cyfrowych",
                name="digitalVersions",
                helpText="E-book, audiobook."
            ),
            CostItem(
                title="Opracowanie muzyczne",
                helpText="Nagranie, mastering, digitalizacjia.",
                name="musicalArrangement"
            ),
            CostItem(
                title="Obsługa i utrzymanie serwisu internetowego",
                name="websiteMaintenance"
            ),
            CostItem(
                title="Tłumaczenia",
                name="translation"
            ),
            CostItem(
                title="Obsługa PR, promocja i reklama",
                name="commercials"
            ),
            CostItem(
                title="Dystrybucja",
                name="distribution"
            ),
        ],
    ),
    EstimateSection(
        title="Koszty prawne i organizacyjne",
        costs=[
            CostItem(
                title="Obsługa finansowa",
                name="financialService",
                helpText="W tym koszty związane z otwarciem i prowadzeniem rachunku bankowego wyłącznie dla operacji finansowych związanych z realizacją przedsięwzięcia. Koszty prowadzenia księgowości związanej z realizacją przedsięwzięcia. Wszystkie koszty muszą być udokumentowane rachunkiem lub fakturą z opisem potwierdzającym związek z przedsięwzięciem.",
            ),
            CostItem(
                title="Obsługa prawna",
                name="legalService"
            ),
            CostItem(
                title="Koszty licencyjne i nabycia praw",
                name="rightsAcquisition"
            ),
            CostItem(
                title="Koszty przejazdów i noclegów osób współpracujących przy przedsięwzięciu",
                name="travelAccommodation",
                helpText="Koszty udokumentowane wyłącznie fakturami lub biletami (jeśli brak faktury). W przypadku podróży lotniczych – tylko bilety w klasie ekonomicznej, W przypadku paliwa – wyłącznie koszty paliwa do samochodów wykorzystywanych do realizacji przedsięwzięcia (środek trwały, leasing, najem), Z dotacji PISF nie są pokrywane koszty podróży zagranicznych.",
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
                title="Dostosowanie działań i formy przekazu do osób ze szczególnymi potrzebami, w tym osób z niepełnosprawnościami",
                name="digitalAccessibility"
            ),
        ],
    ),
]

estimate_sections_pt = [asdict(section) for section in estimate_sections_pt]
