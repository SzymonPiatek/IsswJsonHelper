from classes_new.forms._2026.duk.estimate.dataclasses_definitions import EstimateSection, CostItem, CostOverride
from classes_new.forms._2026.duk.estimate.helpers import fraction_cost
from dataclasses import asdict


estimate_sections_pt124 = [
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
                title="Koszty osób współpracujących (np. członków jury, twórców, moderatorów)",
                name="cooperatingPeople",
                helpText="Wyłącznie koszty udokumentowane umowami wraz z odpowiednimi dokumentami księgowymi (faktura lub rachunek).",
            ),
            CostItem(
                title="Konsultacje eksperckie",
                name="expertConsultation"
            ),
            CostItem(
                title="Nagrody dla laureatów",
                name="awards"
            ),
        ],
    ),
    EstimateSection(
        title="Koszty materiałowe i usługowe",
        costs=[
            CostItem(
                title="Przygotowania kopii filmowych i napisów do filmów",
                name="copyingAndSubtitling"
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
            CostItem(
                title="Materiały biurowe",
                name="stationery"
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
                title="Wynajem sprzętu",
                name="equipmentRental"
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
                title="Obsługa projektów online",
                name="onlineProjects"
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
                helpText="Związane z otwarciem i prowadzeniem rachunku bankowego wyłącznie dla operacji finansowych przedsięwzięcia. Koszty prowadzenia księgowości związanej z realizacją przedsięwzięcia. Powinny być udokumentowane rachunkiem lub fakturą z opisem potwierdzającym, że dotyczyły realizacji przedsięwzięcia.",
            ),
            CostItem(
                title="Obsługa prawna",
                name="legalService"),
            CostItem(
                title="Koszty licencji lub nabycia praw do publicznego pokazu wraz z najmem kopii",
                name="licenseRental",
                helpText="Niezależnie od formuły fakturowania."
            ),
            CostItem(
                title="Ubezpieczenie",
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
                helpText="Dostępne strony internetowe."
            ),
            CostItem(
                title="Dostępność informacyjno–komunikacyjna",
                name="infoAccessibility",
                helpText="Wykonanie audiodeskrypcji, napisów SDH, tłumaczenia PJM.",
            ),
        ],
    ),
]

estimate_sections_pt124 = [asdict(section) for section in estimate_sections_pt124]

estimate_sections_pt3 = [
    EstimateSection(
        title="Projekty filmowe realizowane przez SKS",
        costs=[
            CostItem(
                title="Honoraria dla artystów, prelegentów i prowadzących wydarzenia",
                name="filmProjectsArtistFees",
            ),
            CostItem(
                title="Podróże i noclegi artystów, prelegentów i prowadzących wydarzenia",
                name="filmProjectsTravelAndAccommodation",
                helpText=(
                    "Koszty udokumentowane wyłącznie fakturami lub biletami (jeśli niemożliwe jest otrzymanie faktury). "
                    "W przypadku podróży lotniczych pokrywa się z dotacji tylko koszt biletów w klasie ekonomicznej."
                ),
            ),
            CostItem(
                title="Koszty licencji lub nabycia praw do publicznego pokazu wraz z najmem kopii",
                name="filmProjectsLicenseFees",
                helpText="Niezależnie od formuły fakturowania."
            ),
            CostItem(
                title="Przygotowanie kopii filmowych i napisów do filmów",
                name="filmProjectsFilmCopies",
            ),
            CostItem(
                title="Najem sprzętu",
                name="filmProjectsEquipmentRental",
            ),
            CostItem(
                title="Usługi graficzne i poligraficzne",
                name="filmProjectsGraphicServices",
            ),
            CostItem(
                title="Nagrania, usługi fotograficzne i montażowe",
                name="filmProjectsRecordingServices"
            ),
            CostItem(
                title="Promocja i reklama",
                name="filmProjectsPromotionAdvertising",
            ),
            CostItem(
                title="Tłumaczenia",
                name="filmProjectsTranslations",
            ),
            CostItem(
                title="Obsługa projektów online",
                name="filmProjectsOnlineSupport",
                helpText="Koszty dotyczące utrzymania platformy mojeekino.pl."
            )
        ],
    ),

    EstimateSection(
        title="Wydarzenia branżowe realizowane przez SKS",
        costs=[
            CostItem(
                title="Honoraria dla artystów, prelegentów i prowadzących wydarzenia",
                name="industryEventsSpeakerFees",
            ),
            CostItem(
                title="Podróże i noclegi artystów, prelegentów i prowadzących wydarzenia",
                name="industryEventsTravelAndAccommodation",
            ),
            CostItem(
                title="Koszty licencji lub nabycia praw do publicznego pokazu i najmu kopii",
                name="industryEventsLicenseFees", 
                helpText="Niezależnie od formuły fakturowania."
            ),
            CostItem(
                title="Przygotowanie kopii filmowych i napisów do filmów",
                name="industryEventsFilmCopies",
            ),
            CostItem(
                title="Najem sprzętu",
                name="industryEventsEquipmentRental",
            ),
            CostItem(
                title="Usługi graficzne i poligraficzne",
                name="industryEventsGraphicServices",
            ),
            CostItem(
                title="Nagrania, usługi fotograficzne i montażowe", 
                name="industryEventsRecordingServices"
            ),
            CostItem(
                title="Promocja i reklama",
                name="industryEventsPromotionAdvertising",
            ),
            CostItem(
                title="Tłumaczenia",
                name="industryEventsTranslations",
            ),
            CostItem(
                title="Catering i poczęstunek",
                name="industryEventsCatering",
            ),
            CostItem(
                title="Koszty nagród branżowych",
                name="industryEventsAwards",
            ),
        ],
    ),

    EstimateSection(
        title="Wydarzenia realizowane przez kina studyjne",
        costs=[
            CostItem(
                title="Honoraria dla artystów, prelegentów i prowadzących wydarzenia",
                name="cinemaEventsArtistFees",
            ),
            CostItem(
                title="Podróże i noclegi artystów, prelegentów i prowadzących wydarzenia",
                name="cinemaEventsTravelAndAccommodation",
                helpText=(
                    "Koszty udokumentowane wyłącznie fakturami lub biletami (jeśli niemożliwe jest otrzymanie faktury). "
                    "W przypadku podróży lotniczych pokrywa się z dotacji tylko koszt biletów w klasie ekonomicznej."
                ),
            ),
            CostItem(
                title="Koszty licencji lub nabycia praw do publicznego pokazu wraz z najmem kopii", 
                name="cinemaEventsLicenseFees", 
                helpText="Niezależnie od formuły fakturowania."
            ),
            CostItem(
                title="Przygotowanie kopii filmowych i napisów do filmów",
                name="cinemaEventsFilmCopies",
            ),
            CostItem(
                title="Najem sprzętu",
                name="cinemaEventsEquipmentRental",
            ),
            CostItem(
                title="Usługi graficzne i poligraficzne",
                name="cinemaEventsGraphicServices",
            ),
            CostItem(
                title="Nagrania, usługi fotograficzne i montażowe",
                name="cinemaEventsRecordingServices"
            ),
            CostItem(
                title="Promocja i reklama",
                name="cinemaEventsPromotionAdvertising",
            ),
            CostItem(
                title="Tłumaczenia",
                name="cinemaEventsTranslations",
            ),
            CostItem(
                title="Dostępność informacyjno–komunikacyjna",
                name="informationComunicationAccessiblity",
                helpText="Wykonanie audiodeskrypcji, napisów SDH, tłumaczenia PJM."
            )
        ],
    ),

    EstimateSection(
        title="Koszty organizacji i obsługi SKS",
        costs=[
            CostItem(
                title="Koszty zarządzania przedsięwzięciem",
                name="organizationManagement",
            ),
            CostItem(
                title="Koszty osobowe",
                name="organizationPersonnelCosts",
                helpText="Wszelkie koszty osobowe nieujęte w pozostałych pozycjach."
            ),
            CostItem(
                title="Wynagrodzenia ekspertów",
                name="organizationExpertFees",
            ),
            CostItem(
                title="Obsługa finansowa",
                name="organizationFinancialServices",
            ),
            CostItem(
                title="Koszty najmu biura",
                name="organizationOfficeRental",
            ),
            CostItem(
                title="Promocja i reklama",
                name="organizationPromotionAdvertising",
            ),
            CostItem(
                title="Podróże służbowe i noclegi",
                name="organizationBusinessTravel",
                helpText="Wyłącznie koszty dotyczące organizacji Konferencji Kin Studyjnych, Forum Edukacji Filmowej, szkoleń i działalności eksperckiej.",
            ),
            CostItem(
                title="Działalność Rady Kin Studyjnych",
                name="organizationActivitiesOfArthouseCinemaCouncil",
                helpText="Pokrywane wyłącznie ze środków Wnioskodawcy.",
                overrides={
                    "RequestedAmount": CostOverride(
                        readOnly=True,
                    )
                }
            )
        ],
    ),

    EstimateSection(
        title="Koszty związane z dostępnością",
        costs=[
            CostItem(
                title="Dostępność cyfrowa",
                name="accessibilityDigital",
                helpText="Dostępne strony internetowe.",
            ),
            CostItem(
                title="Dostępność informacyjno–komunikacyjna",
                name="accessibilityInformationCommunication",
                helpText="Wykonanie audiodeskrypcji, napisów SDH, tłumaczenia PJM."
            ),
        ],
    ),

    EstimateSection(
        title="Wsparcie i reprezentacja kin studyjnych",
        costs=[
            CostItem(
                title="Szkolenia i warsztaty dla kin studyjnych",
                name="supportWorkshops",
            ),
            CostItem(
                title="Obsługa i reprezentacja prawna kin studyjnych",
                name="supportLegalRepresentation",
            ),
            CostItem(
                title="Rozpowszechnianie repertuaru studyjnego i dopłaty do seansów",
                name="supportFilmDistribution",
            ),
        ],
    ),
]

estimate_sections_pt3 = [asdict(section) for section in estimate_sections_pt3]
