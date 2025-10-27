from classes_new.forms._2026.duk.estimate.dataclasses_definitions import EstimateSection, CostItem
from classes_new.forms._2026.duk.estimate.helpers import fraction_cost
from dataclasses import asdict


estimate_sections_pt124 = [
    EstimateSection(
        title="Koszty osobowe i merytoryczne",
        costs=[
            fraction_cost("zarządzania przedsięwzięciem", "projectManagement", 0.15),
            fraction_cost("osobowe", "personal", 0.35),
            CostItem(
                title="Koszty osób współpracujących (np. członków jury, twórców, moderatorów)",
                name="cooperatingPeople",
                helpText="Wyłącznie koszty udokumentowane umowami wraz z odpowiednimi dokumentami księgowymi (faktura lub rachunek).",
            ),
            CostItem(title="Koszty konsultacji eksperckich", name="expertConsultation"),
            CostItem(title="Koszty nagród dla laureatów", name="awards"),
        ],
    ),
    EstimateSection(
        title="Koszty materiałowe i usługowe",
        costs=[
            CostItem(title="Koszty przygotowania kopii filmowych i napisów do filmów", name="copyingAndSubtitling"),
            CostItem(title="Koszty obsługi PR, promocji i reklamy", name="commercials"),
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
            CostItem(title="Koszty obsługi projektów online", name="onlineProjects"),
        ],
    ),
    EstimateSection(
        title="Koszty logistyczne",
        costs=[
            CostItem(title="Koszty usług transportowych", name="transportServices"),
            CostItem(
                title="Koszty dotyczące podróży",
                name="travel",
                helpText="Wyłącznie koszty udokumentowane fakturami lub biletami (jeśli faktura jest niemożliwa do uzyskania). W przypadku podróży lotniczych – pokrywany jest tylko koszt biletów w klasie ekonomicznej. W przypadku zakupu paliwa – wyłącznie paliwo do samochodów wykorzystywanych do realizacji przedsięwzięcia zgodnie z przepisami (samochód jako środek trwały, leasing, najem). Nie pokrywa się kosztów podróży zagranicznych.",
            ),
            CostItem(
                title="Koszty dotyczące noclegów",
                name="accommodation",
                helpText="Wyłącznie koszty udokumentowane fakturami. Wykluczone: diety, ryczałty, inne koszty nieudokumentowane rachunkiem lub fakturą. Nie pokrywa się kosztów podróży zagranicznych.",
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
                helpText="Związane z otwarciem i prowadzeniem rachunku bankowego wyłącznie dla operacji finansowych przedsięwzięcia. Koszty prowadzenia księgowości związanej z realizacją przedsięwzięcia. Powinny być udokumentowane rachunkiem lub fakturą z opisem potwierdzającym, że dotyczyły realizacji przedsięwzięcia.",
            ),
            CostItem(title="Koszty licencyjne i najmu kopii", name="licenseRental"),
            CostItem(title="Koszty ubezpieczeń", name="insurance"),
            CostItem(title="Koszty ewaluacji przedsięwzięcia", name="evaluation"),
        ],
    ),
    EstimateSection(
        title="Koszty związane z dostępnością",
        costs=[
            CostItem(title="Dostępność cyfrowa", name="digitalAccessibility", helpText="Dostępne strony internetowe."),
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
                title="Koszty honorariów dla artystów, prelegentów i prowadzących wydarzenia",
                name="filmProjectsArtistFees",
            ),
            CostItem(
                title="Koszty podróży i noclegów artystów, prelegentów i prowadzących wydarzenia",
                name="filmProjectsTravelAndAccommodation",
                helpText=(
                    "Koszty udokumentowane wyłącznie fakturami lub biletami (jeśli niemożliwe jest otrzymanie faktury). "
                    "W przypadku podróży lotniczych pokrywa się z dotacji tylko koszt biletów w klasie ekonomicznej."
                ),
            ),
            CostItem(
                title="Koszty licencji lub nabycia praw do publicznego pokazu i najmu kopii",
                name="filmProjectsLicenseFees",
            ),
            CostItem(
                title="Koszty przygotowania kopii filmowych i napisów do filmów",
                name="filmProjectsFilmCopies",
            ),
            CostItem(
                title="Koszty najmu sprzętu",
                name="filmProjectsEquipmentRental",
            ),
            CostItem(
                title="Koszty usług graficznych i poligraficznych",
                name="filmProjectsGraphicServices",
            ),
            CostItem(
                title="Koszty nagrań i usług fotograficznych",
                name="filmProjectsRecordingServices",
            ),
            CostItem(
                title="Koszty promocji i reklamy",
                name="filmProjectsPromotionAdvertising",
            ),
            CostItem(
                title="Koszty tłumaczeń",
                name="filmProjectsTranslations",
            ),
            CostItem(
                title="Koszty obsługi projektów online",
                name="filmProjectsOnlineSupport",
                helpText="Koszty dotyczące utrzymania platformy mojeekino.pl."
            )
        ],
    ),

    EstimateSection(
        title="Wydarzenia branżowe realizowane przez SKS",
        costs=[
            CostItem(
                title="Koszty honorariów dla prelegentów i prowadzących wydarzenia",
                name="industryEventsSpeakerFees",
            ),
            CostItem(
                title="Koszty podróży i noclegów prelegentów i prowadzących wydarzenia",
                name="industryEventsTravelAndAccommodation",
            ),
            CostItem(
                title="Koszty licencji lub nabycia praw do publicznego pokazu i najmu kopii",
                name="industryEventsLicenseFees",
            ),
            CostItem(
                title="Koszty przygotowania kopii filmowych i napisów do filmów",
                name="industryEventsFilmCopies",
            ),
            CostItem(
                title="Koszty najmu sprzętu",
                name="industryEventsEquipmentRental",
            ),
            CostItem(
                title="Koszty usług graficznych i poligraficznych",
                name="industryEventsGraphicServices",
            ),
            CostItem(
                title="Koszty nagrań i usług fotograficznych",
                name="industryEventsRecordingServices",
            ),
            CostItem(
                title="Koszty promocji i reklamy",
                name="industryEventsPromotionAdvertising",
            ),
            CostItem(
                title="Koszty tłumaczeń",
                name="industryEventsTranslations",
            ),
            CostItem(
                title="Koszty cateringu i poczęstunku",
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
                title="Koszty honorariów dla artystów, prelegentów i prowadzących wydarzenia",
                name="cinemaEventsArtistFees",
            ),
            CostItem(
                title="Koszty podróży i noclegów artystów, prelegentów i prowadzących wydarzenia",
                name="cinemaEventsTravelAndAccommodation",
                helpText=(
                    "Koszty udokumentowane wyłącznie fakturami lub biletami (jeśli niemożliwe jest otrzymanie faktury). "
                    "W przypadku podróży lotniczych pokrywa się z dotacji tylko koszt biletów w klasie ekonomicznej."
                ),
            ),
            CostItem(
                title="Koszty licencji lub nabycia praw do publicznego pokazu i najmu kopii",
                name="cinemaEventsLicenseFees",
            ),
            CostItem(
                title="Koszty przygotowania kopii filmowych i napisów do filmów",
                name="cinemaEventsFilmCopies",
            ),
            CostItem(
                title="Koszty najmu sprzętu",
                name="cinemaEventsEquipmentRental",
            ),
            CostItem(
                title="Koszty usług graficznych i poligraficznych",
                name="cinemaEventsGraphicServices",
            ),
            CostItem(
                title="Koszty nagrań i usług fotograficznych",
                name="cinemaEventsRecordingServices",
            ),
            CostItem(
                title="Koszty promocji i reklamy",
                name="cinemaEventsPromotionAdvertising",
            ),
            CostItem(
                title="Koszty tłumaczeń",
                name="cinemaEventsTranslations",
            ),
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
            ),
            CostItem(
                title="Koszty wynagrodzeń ekspertów",
                name="organizationExpertFees",
            ),
            CostItem(
                title="Koszty obsługi finansowej",
                name="organizationFinancialServices",
            ),
            CostItem(
                title="Koszty najmu biura",
                name="organizationOfficeRental",
            ),
            CostItem(
                title="Koszty promocji i reklamy",
                name="organizationPromotionAdvertising",
            ),
            CostItem(
                title="Koszty dotyczące podróży służbowych i noclegów",
                name="organizationBusinessTravel",
                helpText="Wyłącznie koszty dotyczące organizacji Konferencji Kin Studyjnych i Forum Edukacji Filmowej.",
            ),
            CostItem(
                title="Działalność Rady Kin Studyjnych",
                name="organizationActivitiesOfArthouseCinemaCouncil",
                helpText="Pokrywane wyłącznie ze środków Wnioskodawcy."
            )
        ],
    ),

    EstimateSection(
        title="Koszty związane z dostępnością",
        costs=[
            CostItem(
                title="Dostępność cyfrowa (dostępne strony internetowe)",
                name="accessibilityDigital",
            ),
            CostItem(
                title="Dostępność informacyjno–komunikacyjna (wykonanie audiodeskrypcji, napisów SDH, tłumaczenia PJM)",
                name="accessibilityInformationCommunication",
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
