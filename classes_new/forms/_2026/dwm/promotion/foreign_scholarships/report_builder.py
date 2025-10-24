from classes_new.forms._2026.dwm.pisf_structure import ForeignScholarshipsPriority
from classes_new.forms._2026.dwm.promotion.report_builder import PromotionOperationalProgramReportFormBuilder


class ForeignScholarshipsPriorityReportFormBuilder(PromotionOperationalProgramReportFormBuilder):
    def __init__(self):
        super().__init__(
            priority=ForeignScholarshipsPriority()
        )

        self.form_id = self.set_ids(
            local_id=16411,
            uat_id=2824
        )

        self.statements = [
            {
                "label": "Od daty zawarcia umowy nie zmienił się status prawny Stypendysty.",
                "name": "statementLegalStatusUnchanged"
            },
            {
                "label": "Wszystkie podane w niniejszym raporcie informacje są zgodne z aktualnym stanem prawnym i faktycznym.",
                "name": "statementDeclaredInformationUptodate"
            },
            {
                "label": "Przedstawiciele Instytutu dokonujący weryfikacji mogą dokonać poprawy oczywistych omyłek pisarskich i rachunkowych w raporcie końcowym, zawiadamiając o tym Stypendystę.",
                "name": "statementInstituteMayCorrectObviousErrors"
            },
            {
                "label": "Oświadczam, że wszystkie kwoty wymienione w zestawieniu faktur (rachunków) zostały faktycznie poniesione.",
                "name": "statementAllInvoiceAmountsActuallyIncurred"
            },
            {
                "label": "Oświadczam, że wszystkie płatności, w tym podatki i świadczenia od wynagrodzeń zostały uregulowane do dnia zakończenia zadania, o którym mowa w § ………… zawartej umowy z PISF.",
                "name": "statementAllPaymentsSettledByProjectEnd"
            },
            {
                "label": "Oświadczam, że nie toczą się przeciwko mnie żadne postępowania sądowe oraz nie posiadam żadnych tytułów egzekucyjnych wydanych przez komornika.",
                "name": "statementNoLegalProceedingsOrEnforcements"
            }
        ]
        self.grantee_vat_declaration = [
            "Wnioskodawca jest osobą fizyczną, dlatego kwoty zamieszczone w kosztorysie wniosku to KWOTY BRUTTO"
        ]
