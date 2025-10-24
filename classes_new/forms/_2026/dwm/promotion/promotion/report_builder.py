from classes_new.forms._2026.dwm.pisf_structure import PromotionPriority
from classes_new.forms._2026.dwm.promotion.report_builder import PromotionOperationalProgramReportFormBuilder


class PromotionPriorityReportFormBuilder(PromotionOperationalProgramReportFormBuilder):
    def __init__(self):
        super().__init__(
            priority=PromotionPriority()
        )

        self.form_id = self.set_ids(
            local_id=16408,
            uat_id=2821
        )

        self.is_promotion_priority = True
        self.statements = [
            {
                "label": "Od daty zawarcia umowy nie zmienił się status prawny Beneficjenta.",
                "name": "statementLegalStatusUnchanged"
            },
            {
                "label": "Wszystkie podane w niniejszym raporcie informacje są zgodne z aktualnym stanem prawnym i faktycznym.",
                "name": "statementDeclaredInformationUptodate"
            },
            {
                "label": "Przedstawiciele Instytutu dokonujący weryfikacji mogą dokonać poprawy oczywistych omyłek pisarskich i rachunkowych w raporcie końcowym, zawiadamiając o tym Beneficjenta.",
                "name": "statementInstituteMayCorrectObviousErrors"
            },
            {
                "label": "Oświadczam, że zestawienie faktur (rachunków) obejmuje wyłącznie koszty ujęte w ewidencji księgowej podmiotu realizującego przedsięwzięcie.",
                "name": "statementInvoicesIncludeOnlyRecordedCosts"
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
                "label": "Oświadczam, że w całkowitym koszcie przedsięwzięcia nie został uwzględniony podatek od towarów i usług (VAT) podlegający odzyskaniu lub rozliczeniu w deklaracjach składanych do Urzędu Skarbowego.",
                "name": "statementNoRecoverableVATIncluded"
            },
            {
                "label": "Oświadczam, że nie toczą się przeciwko mnie żadne postępowania sądowe oraz nie posiadam żadnych tytułów egzekucyjnych wydanych przez komornika.",
                "name": "statementNoLegalProceedingsOrEnforcements"
            }
        ]
