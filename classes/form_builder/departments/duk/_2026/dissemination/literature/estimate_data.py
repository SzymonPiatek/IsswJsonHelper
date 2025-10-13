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
            CostItem(title="Zarządzanie przedsięwzięciem", name="projectManagement"),
            CostItem(title="Opracowanie i redakcja publikacji (autorzy tekstów, redaktorzy, korektorzy)", name="publicationEditing"),
            fraction_cost("osobowe", "personal", 0.35),
            CostItem(title="Konsultacje eksperckie", name="expertConsultation"),
        ],
    ),
    EstimateSection(
        title="Koszty przygotowania i publikacji",
        costs=[
            CostItem(title="Usługi graficzne, fotograficzne i typograficzne", name="graphicPhotoTypography"),
            CostItem(title="Usługi wydawnicze i poligraficzne", name="publishingPrinting"),
            CostItem(title="Przygotowanie wersji cyfrowych (e-book, audiobook)", name="digitalVersions"),
            CostItem(title="Obsługa i utrzymanie serwisu internetowego", name="websiteMaintenance"),
            CostItem(title="Tłumaczenia", name="translation"),
            CostItem(title="Dystrybucja", name="distribution"),
        ],
    ),
    EstimateSection(
        title="Koszty prawne i organizacyjne",
        costs=[
            CostItem(
                title="Obsługa prawna i finansowa",
                name="legalFinancialService",
                helpText="W tym koszty związane z otwarciem i prowadzeniem rachunku bankowego wyłącznie dla operacji finansowych związanych z realizacją przedsięwzięcia. Koszty prowadzenia księgowości związanej z realizacją przedsięwzięcia. Wszystkie koszty muszą być udokumentowane rachunkiem lub fakturą z opisem potwierdzającym związek z przedsięwzięciem.",
            ),
            CostItem(title="Koszty nabycia praw", name="rightsAcquisition"),
            CostItem(
                title="Koszty przejazdów i noclegów osób współpracujących przy przedsięwzięciu",
                name="travelAccommodation",
                helpText="Koszty udokumentowane wyłącznie fakturami lub biletami (jeśli brak faktury). W przypadku podróży lotniczych – tylko bilety w klasie ekonomicznej, W przypadku paliwa – wyłącznie koszty paliwa do samochodów wykorzystywanych do realizacji przedsięwzięcia (środek trwały, leasing, najem), Z dotacji PISF nie są pokrywane koszty podróży zagranicznych.",
            ),
            CostItem(title="Ewaluacja przedsięwzięcia", name="evaluation"),
        ],
    ),
    EstimateSection(
        title="Koszty związane z dostępnością",
        costs=[
            CostItem(title="Dostępność cyfrowa", name="digitalAccessibility", helpText="Dostępne strony internetowe."),
        ],
    ),
]

estimate_sections = [asdict(section) for section in estimate_sections]
