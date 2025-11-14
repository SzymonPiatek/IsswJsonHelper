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
            CostItem(
                title="Koszty osób współpracujących",
                name="cooperatingPeople",
                helpText=(
                    "Zespół badawaczy, eksperci, współpracownicy merytoryczni. "
                    "Wyłącznie koszty udokumentowane umowami wraz z odpowiednimi dokumentami księgowymi (faktura lub rachunek)."
                ),
            ),
            CostItem(
                title="Ekspertyzy, konsultacje specjalistyczne",
                name="expertConsultation",
            ),
        ],
    ),
    EstimateSection(
        title="Koszty realizacji badań i opracowań analitycznych",
        costs=[
            CostItem(
                title="Konstrukcja narzędzi badawczych",
                name="researchTools",
            ),
            CostItem(
                title="Badania terenowe",
                name="fieldResearch",
                helpText="Wywiady, ankiety, grupy fokusowe."
            ),
            CostItem(
                title="Analizy jakościowe",
                name="qualitativeAnalysis",
                helpText="Dane zastane, analiza wywiadów, case study."
            ),
            CostItem(
                title="Analizy ilościowe",
                name="quantitativeAnalysis",
                helpText="Analiza statystyczna."
            ),
            CostItem(
                title="Raport końcowy z badania",
                name="finalReport",
            ),
        ],
    ),
    EstimateSection(
        title="Koszty materiałowe i usługowe",
        costs=[
            CostItem(
                title="Redakcja i korekta tekstów",
                name="editingProofreading",
            ),
            CostItem(
                title="Tłumaczenia",
                name="translation",
            ),
            CostItem(
                title="Usługi graficzne i poligraficzne",
                name="graphicServices",
            ),
        ],
    ),
    EstimateSection(
        title="Koszty logistyczne",
        costs=[
            CostItem(
                title="Podróźe",
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
                    "Koszty te powinny być udokumentowane rachunkiem lub fakturą z opisem potwierdzającym związek z przedsięwzięciem."
                ),
            ),
            CostItem(
                title="Obsługa prawna",
                name="legalService"
            ),
            CostItem(
                title="Koszty licencyjne",
                name="licenseCosts",
            ),
            CostItem(
                title="Koszty ewaluacji przedsięwzięcia",
                name="evaluation",
            ),
        ],
    ),
]

estimate_sections = [asdict(section) for section in estimate_sections]
