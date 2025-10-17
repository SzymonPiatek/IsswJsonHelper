from classes.helpers import int_to_roman
from ..report_builder import DWMReportBuilder2026
from ..priority import ForeignScholarshipPriority


class ForeignScholarshipReportBuilder(DWMReportBuilder2026, ForeignScholarshipPriority):
    FORM_ID = 63

    def __init__(self):
        super().__init__()

        self.intro_text = [
            "Raport końcowy",
            "<small>z wykonania przedsięwzięcia realizowanego w ramach Programu Operacyjnego \"Promocja polskiej twórczości filmowej za granicą\"</small> <br> Priorytet II \"Stypendia Zagraniczne\""
        ]

    def create_report_basic_data(self, number: int):
        part = self.create_part(
            title=f"{int_to_roman(number)}. Dane podstawowe",
            chapters=[
                self.create_chapter(
                    components=[
                        self.create_component(
                            component_type="header",
                            name="instruction",
                            value="<h4 style='color: red';>UWAGA!</h4>Przed wypełnieniem raportu bardzo prosimy o zapoznanie się z <a target='_blank' rel='noopener noreferrer' href='https://isswstorage.blob.core.windows.net/django-files/instrukcja_POVPR2-raport.pdf.pdf' style='font-weight: bold; text-decoration: underline;'>INSTRUKCJĄ</a>",
                            read_only=True,
                            class_list=[
                                "displayNoneFrontend"
                            ]
                        )
                    ]
                ),
                self.section.report_basic_data.project_implementation_period(number="A"),
                self.section.report_basic_data.agreement_and_annex(number="B"),
                self.section.report_basic_data.grantee_name_and_address(number="C")
            ]
        )

        self.save_part(part)
