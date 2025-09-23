from .priority import PromotionPriority
from ..report_builder import DWMReportBuilder2026


class PromotionReportBuilder(DWMReportBuilder2026, PromotionPriority):
    FORM_ID = 9226

    def __init__(self):
        super().__init__()

    def create_report_base(self):
        self.create_base(
            intro_text=[
                "Raport końcowy",
                "<small>z wykonania przedsięwzięcia realizowanego w ramach Programu Operacyjnego \"Promocja polskiej twórczości filmowej za granicą\"</small> <br> Priorytet I \"Promocja polskiej twórczości filmowej za granicą\""
            ]
        )

    def create_report_basic_data(self):
        part = self.create_part(
            title="I. Dane podstawowe",
            short_name="I. Dane podstawowe",
            chapters=[
                self.section.report_basic_data.project_implementation_period(number="A"),
                self.section.report_basic_data.agreement_and_annex(number="B"),
                self.section.report_basic_data.grantee_name_and_address(number="C")
            ]
        )

        self.save_part(part)

    def create_report_general_data(self):
        part = self.create_part(
            title="II. Informacje ogólne",
            short_name="II. Informacje ogólne",
            chapters=[
                self.create_chapter(
                    class_list=[
                        "grid",
                        "grid-cols-3",
                        "no-title"
                    ],
                    components=[
                        self.create_component(
                            component_type="header",
                            name="taskName",
                            value="1. Nazwa przedsięwzięcia",
                            class_list=[
                                "displayNoneFrontend"
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="1. Nazwa przedsięwzięcia",
                            name="taskName",
                            required=True,
                            validators=[
                                self.validator.length_validator(max_value=600)
                            ],
                            copy_from="applicationTaskName",
                            read_only=True,
                            class_list=[
                                "no-label",
                                "col-span-2",
                                "text-left"
                            ]
                        ),
                        self.create_component(
                            component_type="header",
                            name="taskCompletionInfo",
                            value="2. Stopień realizacji przedsięwzięcia na dzień złożenia raportu",
                            class_list=[
                                "displayNoneFrontend"
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="2. Stopień realizacji przedsięwzięcia na dzień złożenia raportu",
                            name="taskCompletionInfo",
                            validators=[
                                self.validator.length_validator(max_value=10000)
                            ],
                            required=True,
                            class_list=[
                                "no-label",
                                "col-span-2",
                                "text-left"
                            ]
                        ),
                        self.create_component(
                            component_type="header",
                            name="taskImplementationDesc",
                            value="3. Szczegółowy opis wykonania przedsięwzięcia",
                            class_list=[
                                "displayNoneFrontend"
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="3. Szczegółowy opis wykonania przedsięwzięcia",
                            name="taskImplementationDesc",
                            validators=[
                                self.validator.length_validator(max_value=20000)
                            ],
                            required=True,
                            class_list=[
                                "no-label",
                                "col-span-2",
                                "text-left"
                            ]
                        ),
                        self.create_component(
                            component_type="header",
                            name="taskImplementationByPartnersDesc",
                            value="4. Opis działań partnerów w ramach realizacji przedsięwzięcia ze szczególnym uwzględnieniem organów administracji publicznej",
                            class_list=[
                                "displayNoneFrontend"
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            name="taskImplementationByPartnersDesc",
                            label="4. Opis działań partnerów w ramach realizacji przedsięwzięcia ze szczególnym uwzględnieniem organów administracji publicznej",
                            validators=[
                                self.validator.length_validator(max_value=10000)
                            ],
                            required=True,
                            class_list=[
                                "no-label",
                                "col-span-2",
                                "text-left"
                            ]
                        )
                    ]
                )
            ]
        )

        self.save_part(part)

    def create_report_additional_information(self):
        part = self.create_part(
            title="IV. Dodatkowe informacje",
            short_name="IV. Dodatkowe informacje",
            chapters=[
                self.create_chapter(
                    class_list=[
                        "grid",
                        "grid-cols-4",
                    ],
                    components=[
                        self.create_component(
                            component_type="header",
                            value="Dodatkowe informacje",
                            name="additionalGeneralComments",
                            class_list=[
                                "displayNoneFrontend"
                            ]
                        ),
                        self.create_component(
                            component_type="textarea",
                            label="Dodatkowe informacje",
                            name="additionalGeneralComments",
                            validators=[
                                self.validator.length_validator(max_value=10000)
                            ],
                            class_list=[
                                "no-label",
                                "col-span-3",
                                "text-left"
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    components=[
                        self.create_chapter(
                            components=[
                                self.create_component(
                                    component_type="header",
                                    value="Do raportu należy załączyć ewentualny raport medialny, ulotki, plakaty oraz inne materiały promocyjne i informacyjne.",
                                    name="attachmentsDesc"
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Informacja o załącznikach",
                            class_list=[
                                "grid",
                                "grid-cols-4",
                                "no-title"
                            ],
                            components=[
                                self.create_component(
                                    component_type="header",
                                    value="Informacja o załącznikach",
                                    name="attachmentsInfo",
                                    class_list=[
                                        "displayNoneFrontend"
                                    ]
                                ),
                                self.create_component(
                                    component_type="textarea",
                                    name="attachmentsInfo",
                                    validators=[
                                        self.validator.length_validator(max_value=20000)
                                    ],
                                    class_list=[
                                        "col-span-3",
                                        "text-left"
                                    ]
                                )
                            ]
                        ),
                        self.create_chapter(
                            title="Lista załączników",
                            multiple_forms_rules={
                                "minCount": 1,
                                "maxCount": 20
                            },
                            class_list=[
                                "swappable-bg"
                            ],
                            components=[
                                self.create_chapter(
                                    title="Załącznik",
                                    class_list=[
                                        "no-title"
                                    ],
                                    components=[
                                        self.create_component(
                                            component_type="file",
                                            name="reportAttachment"
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                self.create_chapter(
                    title="Oświadczenia",
                    class_list=[
                        "no-title",
                        "grid",
                        "grid-cols-10"
                    ],
                    components=[
                        *[comp
                          for checkbox in [
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
                          for comp in [
                              self.create_component(
                                  component_type="checkbox",
                                  label=checkbox["label"],
                                  name=checkbox["name"],
                                  required=True,
                                  class_list=[
                                      "no-label",
                                      "text-center"
                                  ]
                              ),
                              self.create_component(
                                  component_type="header",
                                  name=checkbox["name"],
                                  class_list=[
                                      "col-span-9",
                                      "text-left",
                                      "displayNoneFrontend"
                                  ]
                              )
                          ]],
                        self.create_component(
                            component_type="text",
                            label="PODPIS BENEFICJENTA:",
                            name="reportSignature",
                            class_list=[
                                "col-start-7",
                                "col-span-4",
                                "text-center",
                                "report-signature",
                                "displayNoneFrontend"
                            ]
                        )
                    ]
                )
            ]
        )

        self.save_part(part)
